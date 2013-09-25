from traceHandler import *
from modelHandler import *
from fitnessFunctions import *
from optimizerHandler import *
from optionHandler import optionHandler
from string import find,count
from scipy.interpolate import interp1d
from scipy import linspace
import time


def meanstdv(x):
    from math import sqrt
    n, mean, std = len(x), 0, 0
    for a in x:
        mean = mean + a
    mean = mean / float(n)
    for a in x:
        std = std + (a - mean)**2
    std = sqrt(std / float(n-1))
    return mean, std

class coreModul():
    """
    This class is responsible to carry out the main steps of the optimization process by
    interacting with the other modules. The main attributes are the following:
    .. data:: data_handler: performs input operations and handles input data
    .. data:: option_handler: stores the settings
    .. data:: model_handler: handles the model and runs the simulations and carries out other model related tasks
    .. data:: optimizer: carries out the optimization process
    .. data:: optimal_params: contains the resulting parameters
    .. data:: ffun_calc_list: contains the list of available fitness functions in a dictionary
    """
    def __init__(self):
        self.data_handler=DATA()
        self.option_handler=optionHandler()
        self.model_handler=None
        self.optimizer=None
        f_m={"Average Squared Error": "calc_ase",
                        "Spike Count": "calc_spike", 
                        "Averaged Squared Error II": "calc_spike_ase",
                        "Spike Rate": "spike_rate",
                        "ISI Differences": "isi_differ",
                        "Latency to 1st Spike": "first_spike",
                        "AP Overshoot": "AP_overshoot",
                        "AHP Depth": "AHP_depth",
                        "AP Width": "AP_width",
                        "Derivative Difference" : "calc_grad_dif"}
        self.ffun_mapper=dict((v,k) for k,v in f_m.iteritems())
        self.ffun_calc_list=["Average Squared Error",
                             "Spike Count", 
                             "Averaged Squared Error II",
                             "Spike Rate",
                             "ISI Differences",
                             "Latency to 1st Spike",
                             "AP Overshoot",
                             "AHP Depth",
                             "AP Width",
                             "Derivative Difference"]
        self.grid_result=None
        
    def htmlStrBold(self,inp):
        return "<b>"+str(inp)+"</b>"
    
    def htmlStr(self,inp):
        return "<p>"+str(inp)+"</p>"
    
    def htmlUnderline(self):
        return "text-decoration:underline"
    
    def htmlResize(self,size):
        return "font-size:"+str(int(size))+"%"  
    
    def htmlAlign(self,align_to):
        if align_to not in ["left","right","center"]:
            raise ValueError
        return  "text-align:"+align_to  
    
    def htmlStyle(self,inp,*args):
        tmp_str="<span style=\""
        for n in args:
            tmp_str+=n+";"
        tmp_str+="\">"+str(inp)+"</span>"
        return tmp_str
    
    def htmlTable(self,header_list,data):
        tmp_str="<table border=\"1\" align=\"center\">"
        for h in header_list:
            tmp_str+="\n<th>"+str(h)+"</th>"
            
        for r in data:
            tmp_str+="\n<tr>"
            for c in r:
                tmp_str+="\n<td>"+str(c)+"</td>"
            tmp_str+="\n</tr>"
            
        tmp_str+="\n</table>"
        return tmp_str
    
    def htmlPciture(self,inp):
        return "<img style=\"border:none;\" src=\""+inp+"\" align=\"center\">"
    
    
    def Print(self):
        print [self.option_handler.GetFileOption(),
               self.option_handler.GetInputOptions(),
               self.option_handler.GetModelOptions(),
               self.option_handler.GetModelStim(),
               self.option_handler.GetModelStimParam(),
               self.option_handler.GetObjTOOpt(),
               self.option_handler.GetOptParam(),
               self.option_handler.GetFitnessParam(),
               self.option_handler.GetOptimizerOptions()]
        print "\n"
        
    def FirstStep(self,args):
        """
        Stores the location of the input, and the base directory in the ``option_handler`` object
        and reads the data from the file into the ``data_handler`` object.
        :param args: dictionary with keys "file" and "input"
        """
        self.option_handler.SetFileOptions(args.get("file"))
        self.option_handler.SetInputOptions(args.get("input"))

        self.data_handler.Read([self.option_handler.input_dir],self.option_handler.input_size,self.option_handler.input_scale,self.option_handler.input_length,self.option_handler.input_freq,self.option_handler.type[-1])

    def LoadModel(self,args):
        """
        Stores the type of the simulator as well as the optional parameters passed to it.
        Creates the ``model_handler`` objects which can be either ``modelHandlerNeuron`` or ``externalHandler``.
        If the ``externalHandler`` is selected then the number of parameters subject to optimization is also set.
        :param args: dictionary with keys "simulator" and "sim_command"
        """
        self.option_handler.SetSimParam([args.get("simulator","Neuron"),args.get("sim_command"),None])
        if self.option_handler.GetSimParam()[0]=="Neuron":
            self.option_handler.SetModelOptions(args.get("model"))
            self.model_handler=modelHandlerNeuron(self.option_handler.model_path,self.option_handler.model_spec_dir,self.option_handler.base_dir)
        else:
            self.model_handler=externalHandler(self.option_handler.GetSimParam()[1])
            self.model_handler.SetNParams(self.option_handler)
            self.option_handler.SetModelStimParam([[0]*self.data_handler.number_of_traces(),0,0])
    def ReturnSections(self):
        """
        :return: the sections found in the model including "None" in a ``string`` ``list``.
        """
        temp=self.model_handler.GetParameters()
        sections=[]
        for n in temp:
            sections.append(n[0])
        sections=list(set(sections))
        sections.append("None")
        return sections
           
    def ReturnMorphology(self):
        """
        :return: the morphological parameters found in the model including "None" in a ``string`` ``list``.
        """
        temp=self.model_handler.GetParameters()
        morphs=(string.split(temp[0][1], ", "))
        morphs=list(set(morphs))
        morphs.append("None")
        return morphs
        
    def ReturnChannels(self,section):
        """
        Collects the channels from the given section.
        :param section: the name of the section 
        :return: the channels in the given section including "None" in a ``string`` ``list``.
        """
        temp=self.model_handler.GetParameters()
        channels=[]
        for n in temp:
            if n[0]==section:
                for k in split(n[2]," "):
                        if k!="":
                            for s in split(n[3]," "):
                                if count(k,s)==1 and s!="":
                                    channels.append(s)
            

        channels=list(set(channels))
        channels.append("None")
        return channels

    def ReturnChParams(self,channel):
        """
        Collects channel parameters from the given channel
        :param channel: the name of the channel mechanism
        :return: the channel parameters in the given channel including "None" in a ``string`` ``list``.
        .. note::
            This function returns everything from the channel object not only the parameters.
        """    
        temp=self.model_handler.GetParameters()
        ch_param=[]
        for n in temp:
            if find(n[3],channel)!=-1:
                for p in n[2].split():
                    if find(p,channel)!=-1:
                        ch_param.append(p)
        ch_param=list(set(ch_param))
        ch_param.append("None")
        return ch_param
    
    #not in use
    def SetModel(self,args):
        
        if args.get("channel")!="None":
            self.model_handler.SetChannelParameters(args.get("section"), args.get("channel"), args.get("params"), args.get("values"))
        else:
            self.model_handler.SetMorphParameters(args.get("section"), args.get("morph"), args.get("values"))      

    def SetModel2(self,args):
        """
        Stores the selected parameter as subject to optimization in the ``option_handler`` object.
        For future use it offers a way to store initial value (not in use at the moment).
        :param args: must be a string-string dictionary containing the following keys:
            * section
            * channel
            * params
            * value
            or:
            * section
            * morph
            * values
        """
        if args.get("channel")!="None":
            self.option_handler.SetObjTOOpt(args.get("section").encode("utf-8")+" "+args.get("channel").encode("utf-8")+" "+args.get("params").encode("utf-8"))
            self.option_handler.SetOptParam(args.get("values"))
        else:
            self.option_handler.SetObjTOOpt(args.get("section").encode("utf-8")+" "+args.get("morph").encode("utf-8"))
            self.option_handler.SetOptParam(args.get("values"))

    def SecondStep(self,args):
        """
        Stores the stimulation settings in the option object.
        :param args: must be a dictionary with the following keys:
            * stim
                must hold a ``list`` as value, which contains:
                * stimulus type as ``string``, must be either "IClamp" or "VClamp"
                * position of stimulus inside the section as of real value (0-1)
                * name of stimulated section as ``string``
            * stimparam
                must hold a ``list`` as value which contains:
                * stimulus amplitudes as a ``list`` of real values
                * delay of stimulus as real value
                * duration of stimulus as real value
                
        """    
        self.option_handler.SetModelStim(args.get("stim"))
        self.option_handler.SetModelStimParam(args.get("stimparam"))
        
        
    def ThirdStep(self,args):
        """
        Stores the parameters in the ``option_handler`` object regarding the optimization process.
        If the sampling rate of the simulation is higher than the sampling rate of the input trace,
        then it re-samples the input using linear interpolation to create more points.
        Currently running a simulation with lower sampling rate than the input trace is not supported!
        After storing the necessary settings the ``optimizer`` object is initialized and the optimization is performed.
        The raw results are stored in the ``final_pop`` variable in the ``optimizer`` object.
        :param args: a dictionary containing the following keys: 
            * runparam
                must be a list containing the following values:
                * length of simulation as real value
                * integration step as real value
                * parameter to record as ``string``
                * name of the section where the recording takes place as ``string``
                * position inside the section as real value (0-1)
                * initial voltage as a real value
            * feat
                must be a ``list`` with the names of the selected fitness functions
            * weights
                must be a list of real values
            * algo_options
                must be a dictionary containing options related to the optimization algorithm
                mandatory parameters:
                    * seed
                    * evo_strat
                    * pop_size
                    * num_inputs
                    * boundaries
                optional parameters belonging to the different algorithms (see the optimizerHandler module for more)
                    * max_evaluation
                    * mutation_rate
                    * cooling_rate
                    * m_gauss
                    * std_gauss
                    * schedule
                    * init_temp
                    * final_temp
                    * acc
                    * dwell
                    * x_tol
                    * f_tol
                optional parameter shared by every algorithm
                    * starting_points
        """        
        if args!=None:
            self.option_handler.SetModelRun(args.get("runparam"))
            fit_par=[]
            #fit_par.append(args.get("ffun",[]))
            fit_par.append(args.get("feat",[]))
            fit_par.append(args.get("weights",[]))
            print fit_par
            self.option_handler.SetFitnesParam(fit_par)
            tmp=args.get("algo_options")
            #tmp.append(args.get("starting_points"))
            self.option_handler.SetOptimizerOptions(tmp)
            
        if self.option_handler.run_controll_dt<self.data_handler.data.step:
            #we have to resample the input trace so it would match the model output
            #will use lin interpolation
            x=linspace(0,self.option_handler.run_controll_tstop,self.option_handler.run_controll_tstop*(1/self.data_handler.data.step))#x axis of data points
            
            tmp=[]
            for i in range(self.data_handler.number_of_traces()):
                y=self.data_handler.data.GetTrace(i)#y axis, the values from the input traces, corresponding to x
                f=interp1d(x,y)
                #we have the continuous trace, we could re-sample it now
                new_x=linspace(0,self.option_handler.run_controll_tstop,self.option_handler.run_controll_tstop/self.option_handler.run_controll_dt)
                #self.trace_reader.SetColumn(i,f(new_x)) the resampled vector replaces the original in the trace reader object
                tmp.append(f(new_x))
            self.data_handler.data.t_length=len(tmp[0])
            self.data_handler.data.freq=self.option_handler.run_controll_tstop/self.option_handler.run_controll_dt
            self.data_handler.data.step=self.option_handler.run_controll_dt
            transp=map(list,zip(*tmp))
            self.data_handler.data.data=[]
            for n in transp:
                self.data_handler.data.SetTrace(n)
        #running simulation with smaller resolution is not supported
        if self.option_handler.run_controll_dt>self.data_handler.data.step:
            self.option_handler.run_controll_dt=self.data_handler.data.step
            
                
                
        if self.option_handler.evo_strat=="Classical EO":
            self.optimizer=simpleEO(self.data_handler,self.model_handler,self.option_handler)
        if self.option_handler.evo_strat=="Simulated Annealing":
            self.optimizer=annealing(self.data_handler,self.model_handler,self.option_handler)        
        if self.option_handler.evo_strat=="SA Scipy":
            self.optimizer=scipy_anneal(self.data_handler,self.model_handler,self.option_handler)
        if self.option_handler.evo_strat=="Nelder-Mead":
            self.optimizer=fmin(self.data_handler,self.model_handler,self.option_handler)
        if self.option_handler.evo_strat=="L-BFGS-B":
            self.optimizer=L_BFGS_B(self.data_handler,self.model_handler,self.option_handler)

        start_time=time.time()
        self.optimizer.Optimize()
        stop_time=time.time()
        self.optimizer.final_pop.sort(reverse=True)
        print self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)],"fitness: ",self.optimizer.final_pop[0].fitness
        print "Optimization lasted for ", stop_time-start_time, " s"
    
    def FourthStep(self,args={}):
        """
        Renormalizes the output of the ``optimizer`` (see optimizerHandler module for more), and runs
        a simulation with the optimal parameters to receive an optimal trace.
        The components of the fitness value is calculated on this optimal trace.
        Settings of the entire work flow are saved into a configuration file named "model name"_settings.xml.
        A report of the results is generated in the form of a html document.
        :param args: currently not in use
        """   
        self.final_result=[]
        self.optimal_params=self.optimizer.fit_obj.ReNormalize(self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)])
        if self.option_handler.GetUFunString()=='':
            out_handler=open("params.param","w")
            for n,k in zip(self.option_handler.GetObjTOOpt(),self.optimizer.fit_obj.ReNormalize(self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)])):
                tmp=n.split(" ")
                if isinstance(self.model_handler, externalHandler):
                    out_handler.write(str(k)+"\n")
                else:
                    if len(tmp)==3:
                        self.model_handler.SetChannelParameters(tmp[0], tmp[1], tmp[2], k)
                    else:
                        self.model_handler.SetMorphParameters(tmp[0], tmp[1], k)
            out_handler.close()
        else:
            try:
                s=self.option_handler.GetUFunString()
                s=replace(s,"h.","self.model_handler.hoc_obj.")
                exec(compile(replace(s,"h(","self.model_handler.hoc_obj("),'<string>','exec'))
            except SyntaxError:
                print "Your function contained syntax errors!! Please fix them!"
            
            self.usr_fun_name=self.option_handler.GetUFunString().split("\n")[4][self.option_handler.GetUFunString().split("\n")[4].find(" ")+1:self.option_handler.GetUFunString().split("\n")[4].find("(")]
            self.usr_fun=locals()[self.usr_fun_name]
            self.usr_fun(self,self.optimizer.fit_obj.ReNormalize(self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)]))
        #the first cell is a vector with all the stimuli in the simulation
        #the first cell is the current stimulus
        for k in range(self.data_handler.number_of_traces()):
                param=self.option_handler.GetModelStimParam()
                parameter=param
                parameter[0]=param[0][k]
                if isinstance(parameter[0], unicode):
                    self.model_handler.SetCustStimuli(parameter)
                else:
                    extra_param=self.option_handler.GetModelRun()
                    self.model_handler.SetStimuli(parameter,extra_param)
                if isinstance(self.model_handler, externalHandler):
                    from subprocess import call
                    call(self.model_handler.GetExec())
                    in_handler=open("trace.dat","r")
                    for line in in_handler:
                        self.model_handler.record[0].append(float(line.split()[1]))
                    in_handler.close()
                else:
                    s=self.option_handler.GetModelRun()
                    s.append(self.data_handler.data.step)
                    self.model_handler.RunControll(s)
                #calculate the error components
                self.error_comps=self.optimizer.fit_obj.getErrorComponents(k, self.model_handler.record[0])
                self.final_result.extend(self.model_handler.record)
                
        f_handler=open(self.option_handler.model_path.split("/")[-1].split(".")[0]+"_settings.xml","w")
        f_handler.write(self.option_handler.dump(self.ffun_mapper))
        f_handler.close()
        
        name=self.option_handler.model_path.split("/")[-1].split(".")[0]
        f_handler=open(name+"_results.html","w")
        tmp_str="<!DOCTYPE html>\n<html>\n<body>\n"
        tmp_str+=self.htmlStr(str(time.asctime( time.localtime(time.time()) )))+"\n"
        tmp_str+="<p>"+self.htmlStyle("Optimization of <b>"+name+".hoc</b> based on: "+self.option_handler.input_dir,self.htmlAlign("center"))+"</p>\n"
        tmp_list=[]
        tmp_fit=self.optimizer.fit_obj.ReNormalize(self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)])
        for name,mmin,mmax,f in zip(self.option_handler.GetObjTOOpt(),self.option_handler.boundaries[0],self.option_handler.boundaries[1],tmp_fit):
            tmp_list.append([str(name),str(mmin),str(mmax),str(f)])
        tmp_str+="<center><p>"+self.htmlStyle("Results",self.htmlUnderline(),self.htmlResize(200))+"</p></center>\n"
        tmp_str+=self.htmlTable(["Parameter Name","Minimum","Maximum","Optimum"], tmp_list)+"\n"
        tmp_str+="<center><p>"+self.htmlStrBold("Fitnes: ")
        tmp_str+=self.htmlStrBold(str(self.optimizer.final_pop[0].fitness))+"</p></center>\n"
        tmp_str+=self.htmlPciture("result_trace.png")+"\n"
        for k in self.option_handler.GetOptimizerOptions().keys():
            tmp_str+="<p><b>"+k+" =</b> "+str(self.option_handler.GetOptimizerOptions()[k])+"</p>\n"
            
        tmp_str+="<p><b>feats =</b> "+ str(self.option_handler.feats)+"</p>\n"
        tmp_str+="<p><b>weights =</b> "+ str(self.option_handler.weights)+"</p>\n"
        tmp_str+="<p><b>user function =</b> "+ str(self.option_handler.u_fun_string)+"</p>\n"
        tmp_str+="</body>\n</html>\n"
        f_handler.write(tmp_str)
        f_handler.close()
        
                
    def callGrid(self):
        """
        Calculates fitness values on a defined grid (see optimizerHandler module for more).
        This tool is purely for analyzing results, and we do not recommend to use it to obtain parameter values.
        """
        self.optimizer=grid(self.data_handler,self.model_handler,self.option_handler)
        self.optimizer.Optimize(self.optimal_params)
        self.grid_result=self.optimizer.final_pop
        

             
        
                  
               
               
               
               
               
               
        
        
        