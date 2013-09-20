
import time
from xml.etree.ElementTree import Element as e, SubElement as se
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(e):
    r_str=ElementTree.tostring(e,'utf-8')
    repsed=minidom.parseString(r_str)
    return repsed.toprettyxml(indent="  ")

# class to handle the settings specified by the user
# there are no separate classes for the different settings, only get-set member functions
# the proper initialization is done via the target classes' constructors (traceReader, modelHandlerNeuron) 
class optionHandler(object):
    def __init__(self):
        prev=dir(self)
        self.start_time_stamp=time.time()
        #exp data settings
        self.base_dir="" # path to base directory
        self.input_dir="" # path to input file
        self.input_size=0 # no_traces
        self.input_scale="" # scale of input
        self.input_length=1 # length of input
        self.input_freq=1 # sampling freq of input
        self.input_cont_t=0 # contains time or not
        self.type=[]
        
        #model file settings
        self.model_path="" # path to the model file (.hoc)
        self.model_spec_dir="" #path to the channel files
        
        self.u_fun_string=""#string of the user defined function waiting for compilation
        
        #stim settings
        self.stim_type="" # type of stimulus
        self.stim_pos=0 # position
        self.stim_sec="" # section name
        self.stim_amp=[] # stimuli amplitude
        self.stim_del=0 # delay
        self.stim_dur=0 # duration
        
        #parameters and values
        self.adjusted_params=[] # string list of the editable things, section, channel, parameter
        self.param_vals=[] # list of values to the parameters
        
        #run controll settings
        self.run_controll_tstop=0 # tstop
        self.run_controll_dt=0 # dt
        self.run_controll_record="" # parameter to be recorded
        self.run_controll_sec="" # section where the recording takes place
        self.run_controll_pos=0 # position where the recording takes place
        self.run_controll_vrest=0 # resting voltage
        
        #optimizer settings
        self.seed=None
        self.evo_strat=None
        
        self.pop_size=None
        self.max_evaluation=None
        self.mutation_rate=None
        
        self.cooling_rate=None
        self.m_gauss=None
        self.std_gauss=None
        self.schedule=None
        self.init_temp=None
        self.final_temp=None
        
        self.acc=None
        self.dwell=None
        
        self.x_tol=None
        self.f_tol=None
        
        self.num_inputs=None
        self.boundaries=[[],[]]
        self.starting_points=None
        
        self.spike_thres=0
        self.spike_window=50
        #self.ffunction=None #other parameters might be necessary
        self.feats=[]
        self.weights=[]
        post=dir(self)
        self.class_content=list(set(post)-set(prev))
        
#    def dump(self):
#        target=""
#        for m in self.class_content:
#            #error here:TypeError: cannot concatenate 'str' and 'NoneType' objects
#            try:
#                target+=m+" = "+self.__getattribute__(m).__repr__()+"\n"
#            except TypeError:
#                target+=m+" = "+"None"+"\n"
#                
#        return target

    def dump(self):
        root=e("settings")
        for m in self.class_content:
            child=se(root,m)
            try:
                child.text=self.__getattribute__(m).__repr__()
            except TypeError:
                child.text="None"
        return prettify(root)
        

        
        
        
    
    # returns the current settings of the current working directory (referred as base in modelHandler, used in traceReader )    
    def GetFileOption(self):
        return self.base_dir
    
    # sets the current working directory, and other directory specific settings to the given value(s)
    def SetFileOptions(self,options):
        self.base_dir=options
    
    # returns the current input file options     
    def GetInputOptions(self):
        return [[self.input_dir], self.input_size, self.input_scale, self.input_length, self.input_freq, self.input_cont_t]
    
    # sets the input file options to the given values    
    def SetInputOptions(self,options):
        self.input_dir=options[0]
        self.input_size=options[1]
        self.input_scale=options[2]
        self.input_length=options[3]
        self.input_freq=options[4]
        self.input_cont_t=options[5]
        self.type.append(options[6])
        
    # returns the current model options (name, parameters, stimuli, etc)        
    def GetModelOptions(self):
        return [self.model_path,
        self.model_spec_dir]
    
    # sets the values to options (same as above) 
    def SetModelOptions(self,options):
        self.model_path=options[0]
        self.model_spec_dir=options[1]
        
    def GetUFunString(self):
        return self.u_fun_string
    
    def SetUFunString(self,s):
        self.u_fun_string=s
    
    def GetModelStim(self):
        return [self.stim_type,
        self.stim_pos,
        self.stim_sec]
        
    def SetModelStim(self,options):
        self.stim_type=options[0]
        self.stim_pos=options[1]
        self.stim_sec=options[2]
        
    def GetModelStimParam(self):
        return [self.stim_amp,
        self.stim_del,
        self.stim_dur]
        
    def SetModelStimParam(self,options):
        self.stim_amp=options[0]
        self.stim_del=options[1]
        self.stim_dur=options[2]
        
    #only the parameters that are changing    
    def GetObjTOOpt(self):
        return self.adjusted_params
        
    def SetObjTOOpt(self,options):
        if self.adjusted_params.count(options)==0:
            self.adjusted_params.append(options)#string list, one row contains the section, the channel, and the parameter name
        else:
            print "already selected\n"
        #self.adjusted_params=list(set(self.adjusted_params))
            
    def GetOptParam(self):
        return self.param_vals
        
    def SetOptParam(self,options):
        self.param_vals.append(options)#float list, with all the values which selected for optimization
        #self.param_vals=list(set(self.param_vals))
        # 
    def GetModelRun(self):
        return [self.run_controll_tstop,
        self.run_controll_dt,
        self.run_controll_record,
        self.run_controll_sec,
        self.run_controll_pos,
        self.run_controll_vrest]
        
    def SetModelRun(self,options):

        self.run_controll_tstop=options[0]
        self.run_controll_dt=options[1]
        self.run_controll_record=options[2]
        self.run_controll_sec=options[3]
        self.run_controll_pos=options[4]
        self.run_controll_vrest=options[5]
    
    # gets the optimizer settings
    def GetOptimizerOptions(self):
        return {"seed" : self.seed,
                "evo_strat" : self.evo_strat,
                "Size of Population:" : self.pop_size,
                "Number of Generations:" : self.max_evaluation,
                "Mutation Rate:" : self.mutation_rate,
                "Cooling Rate:" : self.cooling_rate,
                "Mean of Gaussian:" : self.m_gauss,
                "Std. Deviation of Gaussian:" : self.std_gauss,
                "Cooling Schedule:" : self.schedule,
                "Initial Temperature:" : self.init_temp,
                "Final Temperature:" : self.final_temp,
                "Accuracy:" : self.acc,
                "Dwell:" : self.dwell,
                "Error Tolerance for x:" : self.x_tol,
                "Error Tolerance for f:" : self.f_tol,
                "num_inputs" : self.num_inputs,
                "boundaries" : self.boundaries,
                "starting_points" : self.starting_points
                }
        
    # sets the optimizer settings (which optimizer, fitness function, generator settings, etc)    
    def SetOptimizerOptions(self,options):
        self.seed=options.get("seed",1234)
        self.evo_strat=options.get("evo_strat")
        
        self.pop_size=options.get("Size of Population:",None)
        self.max_evaluation=options.get("Number of Generations:",None)
        self.mutation_rate=options.get("Mutation Rate:",None)
        
        self.cooling_rate=options.get("Cooling Rate:",None)
        self.m_gauss=options.get("Mean of Gaussian:",None)
        self.std_gauss=options.get("Std. Deviation of Gaussian:",None)
        self.schedule=options.get("Cooling Schedule:",None)
        self.init_temp=options.get("Initial Temperature:",None)
        self.final_temp=options.get("Final Temperature:",None)
        
        self.acc=options.get("Accuracy:",None)
        self.dwell=options.get("Dwell:",None)
        
        self.x_tol=options.get("Error Tolerance for x:",None)
        self.f_tol=options.get("Error Tolerance for f:",None)
        
        self.num_inputs=options.get("num_inputs")
        self.boundaries=options.get("boundaries")
        self.starting_points=options.get("starting_points",None)
        
    def GetFitnessParam(self):
        return [ self.spike_thres,
                self.feats,self.weights ]
        
    def SetFitnesParam(self,options):
        self.spike_thres=options[0][0].get("Spike Detection Thres. (mv)",0.0)
        self.spike_window=options[0][0].get("Spike Window (ms)",50)*self.input_freq/1000.0
        #self.ffunction=options[0][1]
        self.feats=options[0][1]
        self.weights=options[1]
        
    
