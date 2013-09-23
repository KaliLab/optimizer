from math import fsum,sqrt
from string import split,strip,replace
from copy import copy







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
        self.fun_dict={"Combinations": self.combineFeatures} 
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
            self.usr_fun_name=self.option.GetUFunString().split("\n")[4][self.option.GetUFunString().split("\n")[4].find(" ")+1:self.option.GetUFunString().split("\n")[4].find("(")]
            self.usr_fun=locals()[self.usr_fun_name]
        except SyntaxError:
            print "Your function contained syntax errors!! Please fix them!"
        except IndexError:
            pass
            
        
        
    def compileUDF(self,section,settings,params):
        
        #print section
        if self.option.GetUFunString()=="":
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


    def ReNormalize(self,l):
        tmp=[]
        for i in range(len(l)):
            tmp.append(l[i]*(self.option.boundaries[1][i]-self.option.boundaries[0][i])+self.option.boundaries[0][i])
        return tmp
    
    
    
        
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
            
        return temp1


        #calculates the gradient at the given time
    def calc_grad_dif(self,mod_t,exp_t,args):
        dt=self.reader.step
        grad_a=0
        grad_b=0
        tmp=[]
        for i in range(1,min(len(mod_t),len(exp_t))-1):
            grad_a=((mod_t[i+1]-mod_t[i-1])/(2*dt))
            grad_b=((exp_t[i+1]-exp_t[i-1])/(2*dt))
            tmp.append((grad_a-grad_b)**2)
        if self.option.output_level=="1":
            print "grad dif"
            print fsum(tmp)/len(tmp)/(pow(max(tmp)-min(tmp),2))
            
            
        return fsum(tmp)/len(tmp)/(pow(max(tmp)-min(tmp),2))  
           
            
        
        #compares the number of spikes in the traces
        #counting only traces which are during the stimulus
    def spike_rate(self,mod_t,exp_t,args):
        temp_fit=0
        stim_dur=self.option.stim_dur
        if stim_dur>=1e9:
            stim_dur=self.option.input_length
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t[int(self.option.stim_del*self.option.input_freq/1000):int(self.option.stim_del*self.option.input_freq/1000+stim_dur*self.option.input_freq/1000)])
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t[int(self.option.stim_del*self.option.input_freq/1000):int(self.option.stim_del*self.option.input_freq/1000+stim_dur*self.option.input_freq/1000)])
        mod_spike=len(spikes[0])
        exp_spike=len(spikes[1])
        if len(spikes[0])<1 or len(spikes[1])<1:
            return 1000
        try:
            #temp_fit+=float(abs(mod_spike-exp_spike))/max( float(exp_spike),float(mod_spike-1) )
            temp_fit+=float(abs(mod_spike-exp_spike))/float(exp_spike+mod_spike+1)
        except ZeroDivisionError:
            temp_fit+=1
        if self.option.output_level=="1":
            print "spike rate:"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print temp_fit
        return temp_fit
        
    
        #compares the two traces based on the 
        #differences in the interspike intervals (isi)
        #normalized
        #returns 2 if model trace has no spikes
    def isi_differ(self,mod_t,exp_t,args):#The value of k was either
#four ISIs or one-fifth of the total number of ISIs, whichever was the smaller
#of the two
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t)
        tmp=[]
        #tmp.append(abs(len(spikes[0])-len(spikes[1]))/max( float(len(spikes[0])),float(len(spikes[1])-1) ))
        if len(spikes[0])<1 and len(spikes[1])<1:
            return 0
        if len(spikes[0])<1 != len(spikes[1])<1:
            return 1
        k=0
        limit=min(4,len(spikes[1])//2)
        for s1,s2 in zip(range(len(spikes[0])),range(len(spikes[1]))):
            try:
                k+=1
                if k>limit:
                    tmp.append(pow((spikes[0][s1+1].peak-spikes[0][s1].peak)
                        -(spikes[1][s2+1].peak-spikes[1][s2].peak)),2)
                
            except IndexError:
                pass
        if self.option.output_level=="1":
            print "isi difference:"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print fsum(tmp)/len(exp_t)
        return fsum(tmp)/len(exp_t)
    
    
        #compares the two traces based on the latency of the first spikes
    def first_spike(self,mod_t,exp_t,args):
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t)
        if len(spikes[0])<1 and len(spikes[1])<1:
            return 0
        if len(spikes[0])<1 != len(spikes[1])<1:
            return 1
        if self.option.output_level=="1":            
            print "first spike"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print pow(spikes[0][0].start_pos-spikes[1][0].start_pos,2)/len(exp_t)
        return pow(spikes[0][0].start_pos-spikes[1][0].start_pos,2)/len(exp_t)
    
    
        #compares the traces based on the spike heights (heights calculated as the following:
        #abs(peak avlue-spike threshold) )
        #normalized
    def AP_overshoot(self,mod_t,exp_t,args):
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t)
        max_amp=max(map(lambda x: max(x.peak_val),exp_t))
        if len(spikes[0])<1 and len(spikes[1])<1:
            return 0
        if len(spikes[0])<1 != len(spikes[1])<1:
            return 1
        tmp=[pow((s1.peak_val-self.thres)-(s2.peak_val-self.thres),2) for s1,s2 in zip(spikes[0],spikes[1])]
        try:
            if self.option.output_level=="1":
                print "AP oveshoot:"
                print "mod: ", len(spikes[0])
                print "exp: ", len(spikes[1])
                print fsum(tmp)/len(tmp)/max_amp
            return  fsum(tmp)/len(tmp)/max_amp
        except OverflowError:
            print "overflow"
            return 10
    
    
        #compares the two traces based on the after-hyperpolarization depth
        #basically finds the minimum value between spikes and compares them
        #normalized
    def AHP_depth(self,mod_t,exp_t,args):
        #calculate average value of the minimum voltage between two APs for both traces,
        #take absolute (or squared) difference,
        #normalize by (square of) the range of all exp voltage values
        #(subthreshold range would be even better, but may be more difficult).
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t)
        if len(spikes[0])<1 and len(spikes[1])<1:
            return 0
        if len(spikes[0])<1 != len(spikes[1])<1:
            return 1
        e=[]
        m=[]
        for s1,s2 in zip(range(len(spikes[0])),range(len(spikes[1]))):
            try:
                m.append(min(mod_t[spikes[0][s1].stop_pos:spikes[0][s2+1].start_pos]))
                e.append(min(exp_t[spikes[1][s2].stop_pos:spikes[1][s2+1].start_pos]))
            except IndexError:
                m.append(min(mod_t[spikes[0][s1].stop_pos:]))
                e.append(min(exp_t[spikes[1][s2].stop_pos:]))

        avg_e=fsum(e)/len(e)
        avg_m=fsum(m)/len(m)
        sub_t_e=filter(lambda x: x<self.thres, exp_t)
        if self.option.output_level=="1":
            print "AHP depth:"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print pow(avg_e-avg_m,2)/pow(max(sub_t_e)-min(sub_t_e),2)
        tmp=pow(avg_e-avg_m,2)/pow(max(sub_t_e)-min(sub_t_e),2) 
        return tmp
    
    
        #compares the traces based on the width of the action potentials
        #the width is computed at the base of the spike and at the middle of the spike
        #not normalized 
    def AP_width(self,mod_t,exp_t,args):#atlagos spike szelesseget, vagy utolso/elso vagy csak az elso
        add_data=args.get("add_data",None)
        spikes=[0,0]
        spikes[0]=self.detectSpike( mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike( exp_t)
        if len(spikes[0])<1 and len(spikes[1])<1:
            return 0
        if len(spikes[0])<1 != len(spikes[1])<1:
            return 1
        avg1=[]
        avg2=[]
        for s1,s2 in zip(spikes[0],spikes[1]):
            avg1.append((s1.stop_pos-s1.start_pos)/2)
            avg2.append((s2.stop_pos-s2.start_pos)/2)

        if self.option.output_level=="1":
            print "AP width:"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print pow((fsum(avg2)/len(avg2)-fsum(avg1)/len(avg1))/(fsum(avg2)/len(avg2)),2)
        return pow((fsum(avg2)/len(avg2)-fsum(avg1)/len(avg1))/(fsum(avg2)/len(avg2)),2)

    
        #calculates the averaged squared error's of the close proximity of spikes
    def calc_spike_ase(self,mod_t,exp_t,args):
        window=self.option.spike_window
        add_data=args.get("add_data",None)
        tmp=[]
        spikes=[0,0]
        spikes[0]=self.detectSpike(mod_t)
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike(exp_t)
        e=copy(mod_t)
        m=copy(exp_t)
        if len(spikes[1])<1 and len(spikes[0])<1:
            return self.calc_ase(mod_t, exp_t,args)
        for s_e,s_m in zip(spikes[1],spikes[0]):
            e[s_e.start_pos-window:s_e.stop_pos+window]=0
            m[s_m.start_pos-window:s_m.stop_pos+window]=0
#        tmp.append(self.calc_ase(a[0:spikes[1][0].start_pos-window],
#                                 b[0:spikes[1][0].start_pos-window],args))
#        for i,s in enumerate(spikes[1]):
#            try:
#                tmp.append(self.calc_ase(a[s.stop_pos+window:spikes[1][i+1].start_pos-window],
#                                         b[s.stop_pos+window:spikes[1][i+1].start_pos-window],args ))
#            except IndexError:
#                tmp.append(self.calc_ase(a[spikes[1][i].stop_pos+window:],b[spikes[1][i].stop_pos+window:],args ))
#        print fsum(tmp)/len(tmp)
        if self.option.output_level=="1":
            print "spike_ase"
            print "mod: ", len(spikes[0])
            print "exp: ", len(spikes[1])
            print self.calc_ase(m, e, args)
        return self.calc_ase(m, e, args)
        
        # averaged squared error 
    def calc_ase(self,mod_t,exp_t,args):
        #print "ase:"
        temp=[]
        for n in range(min([len(exp_t),len(mod_t)])):
            if mod_t[n]>100 or mod_t[n]<-100:
                return 100
            try:
                temp.append(pow(exp_t[n]-mod_t[n],2))
            except OverflowError:
                return 100
            except TypeError:
                return 2
        if self.option.output_level=="1":
            print "ase"
            print fsum(temp)/len(temp)/( pow( max(exp_t)-min(exp_t),2 ) )
        return fsum(temp)/len(temp)/( pow( max(exp_t)-min(exp_t),2 ) )#(sqrt(fsum(temp)/len(temp)))/(max(max(exp,model))-min(min(exp,model)))
    
    
    def calc_spike(self,mod_t,exp_t,args):
        add_data=args.get("add_data",None)
        temp_fit=0
        spikes=[0,0]
        spikes[0]=self.detectSpike(mod_t)
        print spikes[0]
        if add_data!=None:
            spikes[1]=add_data
        else:
            spikes[1]=self.detectSpike(exp_t)
        mod_spike=len(spikes[0])
        exp_spike=len(spikes[1])
        try:
            #temp_fit+=float(abs(mod_spike-exp_spike))/max( float(exp_spike),float(mod_spike-1) )
            temp_fit+=float(abs(mod_spike-exp_spike))/float(exp_spike+mod_spike+1)
        except ZeroDivisionError:
            temp_fit+=1
        if self.option.output_level=="1":
            print "spike count"
            print "mod: ", mod_spike
            print "exp: ", exp_spike
            print temp_fit
        return temp_fit

    
    
    
    
    def combineFeatures(self,candidates,args):
        self.fitnes=[]
        features=self.option.feats
        weigths=self.option.weights
        temp_fit=0
        window=self.option.spike_window
        self.model.CreateStimuli(self.option.GetModelStim())
        for l in candidates:
            if self.option.output_level=="1":
                print l
            l=self.ReNormalize(l)
            if self.option.output_level=="1":
                print l
            for k in range(self.reader.number_of_traces()):
                try:
                    add_data=[spike_frame(n-window,self.thres,n,1,n+window,self.thres) for n in self.reader.additional_data.get(k)]
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
                    extra_param=self.option.GetModelRun()
                    self.model.SetStimuli(parameter,extra_param)
                self.modelRunner(l)
                if self.option.output_level=="1":
                    print features,weigths
                for f,w in zip(features,weigths):
                    temp_fit+=w*(f( self.model.record[0],
                                                    self.reader.data.GetTrace(k),args ))
                            
            self.fitnes.append(temp_fit)
            if self.option.output_level=="1":
                print temp_fit
            temp_fit=0
        return self.fitnes
    
    def getErrorComponents(self,index_of_trace,model_output):
        features=self.option.feats
        weigths=self.option.weights
        fit_list=[]
        window=self.option.spike_window
        try:
            add_data=[spike_frame(n-window,0,n,1,n+50,0) for n in self.reader.additional_data.get(index_of_trace)]
        except AttributeError:
            add_data=None
        args={}
        args["add_data"]=add_data
        for f,w in zip(features,weigths):
            fit_list.append([w,f,(f( model_output,self.reader.data.GetTrace(index_of_trace),args ))])
        return fit_list
    
    