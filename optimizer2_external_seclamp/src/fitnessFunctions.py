from math import fsum,sqrt
from string import split,strip,replace







class spike_frame():
    def __init__(self,start,start_val,peak,peak_val,stop,stop_val):
        self.start_pos=start
        self.stop_pos=stop
        self.peak=peak
        self.peak_val=peak_val
        self.start_val=start_val
        self.stop_val=stop_val
        
class spike(spike_frame):
    def __init(self,start,start_val,peak,peak_val,stop,stop_val,spike):
        spike_frame.__init__(self, start, start_val, peak, peak_val, stop, stop_val)
        self.s=spike#vector, with the spike in it
        

class fF():
    def __init__(self,reader_object,model_object,option_object):
        self.fitnes=[]
        self.thres=option_object.spike_thres
        #self.d_spike=[]
        #self.m_spike=[]
        self.model=model_object
        self.option=option_object
        self.reader=reader_object
        #self.current_pop=0
        self.fun_dict={"Average Squared Error": self.ase,
                       "Spike Count": self.countSpike, 
                       "Combinations": self.combineFeatures, 
                       "Averaged Squared Error II": self.spike_ase,
                       "Feature Extractor I": self.smallFeaturesExtractor,
                       "Derivative Difference": self.derivate_diff}
        self.calc_dict={"Average Squared Error": self.calc_ase,
                        "Spike Count": self.calc_spike, 
                        "Averaged Squared Error II": self.calc_spike_ase,
                        "Spike Rate": self.spike_rate,
                        "ISI Differences": self.isi_differ,
                        "Latency to 1st Spike": self.first_spike,
                        "AP Overshoot": self.AP_overshoot,
                        "AHP Depth": self.AHP_depth,
                        "AP Width": self.AP_width,
                        "Derivative Difference" : self.calc_grad_dif}
        try:
            s=self.option.GetUFunString()
            s=replace(s,"h.","self.model.hoc_obj.")
            exec(compile(replace(s,"h(","self.model.hoc_obj("),'<string>','exec'))
            self.usr_fun_name=self.option.GetUFunString().split("\n")[3][self.option.GetUFunString().split("\n")[3].find(" ")+1:self.option.GetUFunString().split("\n")[3].find("(")]
            self.usr_fun=locals()[self.usr_fun_name]
        except SyntaxError:
            print "Your function contained syntax errors!! Please fix them!"
        except IndexError:
            pass
            
        
        
    def compileUDF(self,section,settings,params):
        
        #print section
        if self.option.GetUFunString()=='':
            for sec in section:
                #print sec
                if len(split(sec," "))==3:
                    self.model.SetChannelParameters(strip(split(sec," ")[0]),strip(split(sec," ")[1]),strip(split(sec," ")[2]),
                                                    params[section.index(sec)])
                
                else:
                    self.model.SetMorphParameters(strip(split(sec," ")[0]),strip(split(sec," ")[1]),params[section.index(sec)])
        else:
            #cal the user def.ed function
            self.usr_fun(self,params)
            
            
        
        
    def modelRunner(self,candidates):
        
        #params=candidates
        from modelHandler import externalHandler
        if isinstance(self.model,externalHandler):
            self.model.record[0]=[]
            out_handler=open("params.param","w")
            for c in candidates:
                out_handler.write(str(c)+"\n")
            out_handler.close()
            from subprocess import call
            call(self.model.GetExec())
            in_handler=open("trace.dat","r")
            for line in in_handler:
                self.model.record[0].append(float(line.split()[1]))
            in_handler.close()
            
        else:
            section=self.option.GetObjTOOpt()
            settings=self.option.GetModelRun()#1. is the integrating step dt
            settings.append(self.reader.data.step)
            self.compileUDF(section, settings, candidates)
            self.model.RunControll(settings)

        #calculates the gradient at the given time
    def calc_grad_dif(self,a,b,args):
        dt=self.reader.step
        grad_a=0
        grad_b=0
        tmp=[]
        for i in range(1,min(len(a),len(b))-1):
            grad_a=((a[i+1]-a[i-1])/(2*dt))
            #print grad_a
            grad_b=((b[i+1]-b[i-1])/(2*dt))
            #print grad_b
            tmp.append((grad_a-grad_b)**2)
            
        return fsum(tmp)/len(tmp)#fsum( map( lambda x: x/max(tmp) ,tmp) )/len(tmp)  
    
    
    
    def derivate_diff(self,candidates,args):
        #temp=[]
        self.fitnes=[]
        temp_fit=0
        #param=self.option.GetModelStimParam()
        #parameter=param
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                
                self.modelRunner(l)
                temp_fit+=self.calc_grad_dif(self.model.record[0],self.reader.data.GetTrace(k),args)#fsum(temp)/len(temp)
                        
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0
            #self.current_pop+=1
        return self.fitnes

        
            
        
        #compare the incoming traces, based on the spike rate, 
        #which is defined as (number of spikes)/trace[first spikes:last spike]
        #it returns a normalized value
        #if the model trace doesn't contain any spikes then the function returns 1000
    def spike_rate(self,a,b,args):
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( a[int(self.option.stim_del*self.option.input_freq/1000):int(self.option.stim_del*self.option.input_freq/1000+self.option.stim_dur*self.option.input_freq/1000)])
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b[int(self.option.stim_del*self.option.input_freq/1000):int(self.option.stim_del*self.option.input_freq/1000+self.option.stim_dur*self.option.input_freq/1000)])
        print "spike rate:"
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        mod_num_o_spikes=len(spikes[0])
        exp_num_o_spikes=len(spikes[1])
        
        mod_rate=float(mod_num_o_spikes)/float(self.option.stim_dur*self.option.input_freq/1000)
        exp_rate=float(exp_num_o_spikes)/float(self.option.stim_dur*self.option.input_freq/1000)
    
        print abs(mod_rate-exp_rate)/max(mod_rate,exp_rate)
        return abs(mod_rate-exp_rate)/max(mod_rate,exp_rate) 
    
        #compares the two traces based on the 
        #differences in the interspike intervals (isi)
        #normalized
        #returns 2 if model trace has no spikes
    def isi_differ(self,a,b,args):#The value of k was either
#four ISIs or one-fifth of the total number of ISIs, whichever was the smaller
#of the two
        add_data=args.get("add_data",None)
        print "isi difference:"
        spikes=[0,0]
        spikes[0]=self.detectSpike( a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b)
        tmp=[]
        tmp.append(abs(len(spikes[0])-len(spikes[1]))/max( float(len(spikes[0])),float(len(spikes[1])-1) ))
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<2 or len(spikes[1])<2:
            return 1000
        k=0
        limit=min(4,len(spikes[1])//2)
        for s1,s2 in zip(range(len(spikes[0])),range(len(spikes[1]))):
            try:
                k+=1
                if k>limit:
                    tmp.append(abs((spikes[0][s1+1].peak-spikes[0][s1].peak)/max(a)
                        -(spikes[1][s2+1].peak-spikes[1][s2].peak)/max(b)))
                
            except IndexError:
                pass
        print fsum(tmp)/len(tmp)
        return fsum(tmp)/len(tmp)
    
    
        #compares the two traces based on the latency of the first spikes
        #abs(spikes[0][0].start_pos/len(a)-spikes[1][0].start_pos/len(b))normalized
    def first_spike(self,a,b,args):
        add_data=args.get("add_data",None)
        print "first spike"
        spikes=[0,0]
        spikes[0]=self.detectSpike( a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b)
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        print abs(spikes[0][0].start_pos/len(a)-spikes[1][0].start_pos/len(b))
        return abs(spikes[0][0].start_pos/len(a)-spikes[1][0].start_pos/len(b))
    
    
        #compares the traces based on the spike heights (heights calculated as the following:
        #abs(peak avlue-spike threshold) )
        #normalized
    def AP_overshoot(self,a,b,args):
        add_data=args.get("add_data",None)
        print "AP oveshoot:"
        spikes=[0,0]
        spikes[0]=self.detectSpike( a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b)
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        tmp=[abs((s1.peak_val-self.thres)-(s2.peak_val-self.thres)) for s1,s2 in zip(spikes[0],spikes[1])]
        try:
            print fsum(tmp)/max(tmp)
            return  fsum(tmp)/max(tmp)
        except OverflowError:
            return 1000
    
    
        #compares the two traces based on the after-hyperpolarization depth
        #basically finds the minimum value between spikes and compares them
        #normalized
    def AHP_depth(self,a,b,args):
        add_data=args.get("add_data",None)
        print "AHP depth:"
        spikes=[0,0]
        spikes[0]=self.detectSpike( a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b)
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        tmp=0
        for s1,s2 in zip(range(len(spikes[0])),range(len(spikes[1]))):
            try:
                tmp+=abs((min(a[spikes[0][s1].stop_pos:spikes[0][s2+1].start_pos]))/min(a)-(min(b[spikes[1][s2].stop_pos:spikes[1][s2+1].start_pos]))/min(b))
            except IndexError:
                tmp+=abs((min(a[spikes[0][s1].stop_pos-1:-1]))-(min(b[spikes[1][s2].stop_pos-1:-1])))

                
        print tmp
        return tmp
    
    
        #compares the traces based on the width of the action potentials
        #the width is computed at the base of the spike and at the middle of the spike
        #not normalized 
    def AP_width(self,a,b,args):#atlagos spike szelesseget, vagy utolso/elso vagy csak az elso
        add_data=args.get("add_data",None)
        print "AP width:"
        spikes=[0,0]
        spikes[0]=self.detectSpike( a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( b)
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        avg1=0.0
        avg2=0.0
        for s1,s2 in zip(spikes[0],spikes[1]):
            avg1+=s1.peak+len(a[s1.peak:s1.stop_pos])/2-s1.start_pos+len(a[s1.start_pos:s1.peak])/2
            avg2+=s2.peak+len(b[s2.peak:s2.stop_pos])/2-s2.start_pos+len(b[s2.start_pos:s2.peak])/2
#            avg1=s1.start_pos+len(a[s1.start_pos:s1.peak])/2
#            avg2=s1.peak+len(a[s1.peak:s1.stop_pos])/2
#            avg3=s2.start_pos+len(b[s2.start_pos:s2.peak])/2
#            avg4=s2.peak+len(b[s2.peak:s2.stop_pos])/2
#            tmp+=abs((s1.stop_pos-s1.start_pos)-(s2.stop_pos-s2.start_pos))+abs((a[avg1]-a[avg2])-(a[avg3]-a[avg4]))
        avg1=float(avg1)/float(len(spikes[0]))
        avg2=float(avg2)/float(len(spikes[1]))
        print abs(avg1-avg2)
        return abs(avg1-avg2)

    
        #calculates the averaged squared error's of the close proximity of spikes
    def calc_spike_ase(self,a,b,args):
        window=self.option.spike_window
        add_data=args.get("add_data",None)
        tmp=[]
        spikes=[0,0]
        spikes[0]=self.detectSpike(a)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike(b)
        print "mod: ", len(spikes[0])
        print "exp: ", len(spikes[1])
        if len(spikes[1])<1 or len(spikes[0])<1:
            return self.calc_ase(a, b)
        tmp.append(self.calc_ase(a[0:spikes[1][0].start_pos],b[0:spikes[1][0].start_pos]))
        for i,s in enumerate(spikes[1]):
            try:
                tmp.append(self.calc_ase(a[s.stop_pos:spikes[1][i+1].start_pos],b[s.stop_pos:spikes[1][i+1].start_pos] ))
            except IndexError:
                tmp.append(self.calc_ase(a[spikes[1][i].stop_pos:],b[spikes[1][i].stop_pos] ))
        print fsum(tmp)
        return fsum(tmp)
        
        # averaged squared error 
    def calc_ase(self,model,exp,args):
        #print "ase:"
        temp=[]
        for n in range(min([len(exp),len(model)])):
            if model[n]>100 or model[n]<-100:
                return 100
            try:
                temp.append(pow(exp[n]-model[n],2))
            except OverflowError:
                return 100
            except TypeError:
                return 2
        
        #take the sqrt of the whole
        #calc the square of the max-min
        #fsum( map( lambda x: x/max(tmp) ,tmp) ) 
        return fsum(temp)/len(temp)/max(temp)#(sqrt(fsum(temp)/len(temp)))/(max(max(exp,model))-min(min(exp,model)))
    
    def ReNormalize(self,l):
        tmp=[]
        for i in range(len(l)):
            tmp.append(l[i]*(self.option.boundaries[1][i]-self.option.boundaries[0][i])+self.option.boundaries[0][i])
        return tmp
    
    def ase(self,candidates,args):
        #temp=[]
        self.fitnes=[]
        temp_fit=0
        #param=self.option.GetModelStimParam()
        #parameter=param
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                add_data=None
                args["add_data"]=add_data
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                
                self.modelRunner(l)
                #for n in range(len(self.reader.data)):
                #    temp.append(pow(self.reader.GetTrace(k)[n]-self.model.record[k][n],2))
                temp_fit+=self.calc_ase(self.model.record[0],self.reader.data.GetTrace(k),args)#fsum(temp)/len(temp)
                        
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0
            #self.current_pop+=1
        return self.fitnes


    def spike_ase(self,candidates,args):
        #temp=[]
        self.fitnes=[]
        temp_fit=0
        #param=self.option.GetModelStimParam()
        #parameter=param
        window=self.option.spike_window
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                try:
                    add_data=[spike_frame(n-window,0,n,1,n+50,0) for n in self.reader.additional_data.get(k)]
                except AttributeError:
                    add_data=None
                args["add_data"]=add_data
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                self.modelRunner(l)                
                temp_fit+=self.calc_spike_ase(self.model.record[0],self.reader.data.GetTrace(k),args)#fsum(temp)/len(temp)
                        
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0
            #self.current_pop+=1
        return self.fitnes


        
    # spike detection
    def detectSpike(self,vect):
        start_pos=0
        stop_pos=0
        start=0
        temp1=[]
        for n in range(len(vect)):
            if vect[n]>self.thres and start==0:
                start_pos=n
                start=1
            elif vect[n]<self.thres and start==1:
                stop_pos=n
                start=0
                s=spike_frame(start_pos,vect[start_pos],vect.index(max(vect[start_pos:stop_pos])),max(vect[start_pos:stop_pos]),stop_pos,vect[stop_pos])
                temp1.append(s)
#        start_pos=0
#        stop_pos=0
#        start=0
#        for n in range(len(vect2)):
#            if vect2[n]>self.thres and start==0:
#                start_pos=n
#                start=1
#            if vect2[n]<self.thres and start==1:
#                stop_pos=n
#                start=0
#                s=spike_frame(start_pos,vect2[start_pos],vect2.index(max(vect2[start_pos:stop_pos])),max(vect2[start_pos:stop_pos]),stop_pos,vect2[stop_pos])
#                temp2.append(s)
#        
#        spikes.append(temp1)#model
#        spikes.append(temp2)#exp
#        
            
        return temp1
    
    def calc_spike(self,a,b,args):
        add_data=args.get("add_data",None)
        temp_fit=0
        spikes=[0,0]
        print a[0:50]
        spikes[0]=self.detectSpike(a)
        print spikes[0]
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike(b)
        mod_spike=len(spikes[0])
        exp_spike=len(spikes[1])
        print "mod: ", mod_spike
        print "exp: ", exp_spike            
        try:
            temp_fit+=float(abs(mod_spike-exp_spike))/max( float(exp_spike),float(mod_spike-1) )
        except ZeroDivisionError:
            print "error"
            temp_fit+=1
        print temp_fit
        return temp_fit

    
    
    def countSpike(self,candidates,args):
        temp_fit=0
        self.fitnes=[]
        #spikes=[]
        #param=self.option.GetModelStimParam()
        #parameter=param
        window=self.option.spike_window
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                print self.reader.additional_data==None
                try:
                    add_data=[spike_frame(n-window,0,n,1,n+50,0) for n in self.reader.additional_data.get(k)]
                    print len(add_data)
                except AttributeError:
                    add_data=None
                args["add_data"]=add_data
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                self.modelRunner(l)
                temp_fit+=self.calc_spike(self.model.record[0],self.reader.data.GetTrace(k),args)
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0         
            
            #self.current_pop+=1
        return self.fitnes
    
    def combineFeatures(self,candidates,args):
        print "combine"
        self.fitnes=[]
        features=self.option.feats
        weigths=self.option.weights
        temp_fit=0
        window=self.option.spike_window
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                try:
                    add_data=[spike_frame(n-window,0,n,1,n+50,0) for n in self.reader.additional_data.get(k)]
                except AttributeError:
                    add_data=None
                args={}
                args["add_data"]=add_data
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                self.modelRunner(l)
                print features,weigths
                for f,w in zip(features,weigths):
                    print w
                    temp_fit+=w*(f( self.model.record[0],
                                                    self.reader.data.GetTrace(k),args ))
                            
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0
        return self.fitnes
    
    
    def smallFeaturesExtractor(self,candidates,args):
        #temp=[]
        self.fitnes=[]
        temp_fit=0
        #param=self.option.GetModelStimParam()
        #parameter=param
        window=self.option.spike_window
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            print l
            l=self.ReNormalize(l)
            print l
            for k in range(self.reader.number_of_traces()):
                try:
                    add_data=[spike_frame(n-window,0,n,1,n+50,0) for n in self.reader.additional_data.get(k)]
                except AttributeError:
                    add_data=None
                args["add_data"]=add_data
                param=self.option.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model.SetCustStimuli(parameter)
                else:
                    self.model.SetStimuli(parameter)
                self.modelRunner(l)
                #for n in range(len(self.reader.data)):
                #    temp.append(pow(self.reader.GetTrace(k)[n]-self.model.record[k][n],2))
                for f in [self.spike_rate,self.isi_differ,self.first_spike,self.AP_overshoot,self.AHP_depth,self.AP_width]:
                    temp_fit+=f(self.model.record[0],self.reader.data.GetTrace(k),args)
                        
            self.fitnes.append(temp_fit)
            print temp_fit
            temp_fit=0
            #self.current_pop+=1
        return self.fitnes
       
 