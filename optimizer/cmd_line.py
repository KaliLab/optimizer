import sys
import Core
import xml.etree.ElementTree as ET


def main(fname):
    try:
        f=open(fname,"r")
    except IOError as ioe:
        sys.exit("File not found!\n"+ioe)
    tree = ET.parse()
    root = tree.getroot()
    if root.tag!="settings":
        sys.exit("Missing \"settings\" tag in xml!")

    core=Core.coreModul()
    #iterate over root to get parameters
    #fill option handler then use get methods to obtain parameters and pass them to core steps
    base_dir=f.readline() # path to base directory
    input_dir=f.readline() # path to input file
    input_size=int(f.readline()) # no_traces
    input_scale=f.readline() # scale of input
    input_length=int(f.readline()) # length of input
    input_freq=int(f.readline()) # sampling freq of input
    input_cont_t=int(f.readline()) # contains time or not
    
    #model file settings
    model_path=f.readline() # path to the model file (.hoc)
    model_spec_dir=f.readline() #path to the channel files
    
    u_fun_string=f.readline()#string of the user defined function waiting for compilation
    
    #stim settings
    stim_type=f.readline() # type of stimulus
    stim_pos=int(f.readline()) # position
    stim_sec=f.readline() # section name
    stim_amp=map(float,f.readline().split(",")) # stimuli amplitude
    stim_del=int(f.readline()) # delay
    stim_dur=int(f.readline()) # duration
    
    #parameters and values
    adjusted_params=f.readline().split(";") # string list of the editable things, section, channel, parameter
    param_vals=float(f.readline().split(",")) # list of values to the parameters
    
    #run controll settings
    run_controll_tstop=int(f.readline()) # tstop
    run_controll_dt=float(f.readline()) # dt
    run_controll_record=f.readline() # parameter to be recorded
    run_controll_sec=f.readline() # section where the recording takes place
    run_controll_pos=float(f.readline()) # position where the recording takes place
    run_controll_vrest=float(f.readline()) # resting voltage
    
    #optimizer settings
    seed=float(f.readline())
    evo_strat=f.readline()
    pop_size=int(f.readline())
    max_evaluation=int(f.readline())
    mutation_rate=float(f.readline())
    num_inputs=int(f.readline())
    boundaries=[map(float,f.readline().split(",")),map(float,f.readline().split(","))]
    
    spike_thres=float(f.readline())
    ffunction=f.readline() #other parameters might be necessary
    feats=f.readline().split(",")
    weights=map(float,f.readline().split(","))
    kwargs={"file" : base_dir,"input" : [base_dir,input_dir,input_size,input_scale,
                                         input_length,input_freq,input_cont_t]}
    core.FirstStep(kwargs)
    
    core.LoadModel({"model" : [model_path,model_spec_dir]})
    
    core.SecondStep({"stim" : [stim_type,stim_pos,stim_sec],"stimparam" : [stim_amp,stim_del,stim_dur]})
    for s,v in zip(adjusted_params,param_vals):
        core.option_handler.SetObjTOOpt(s)
        core.option_handler.SetOptParam(v)
    
    kwargs={"runparam":[run_controll_tstop,
                        run_controll_dt,
                        run_controll_record,
                        run_controll_sec,
                        run_controll_pos,
                        run_controll_vrest],
            "ffun":[spike_thres,ffunction],
            "feat": feats,
            "weights": weights,
            "algo_options":[seed,
                            evo_strat,
                            pop_size,
                            max_evaluation,
                            mutation_rate,
                            num_inputs,
                            boundaries]
                    }
    
    core.ThirdStep(kwargs)
    core.FourthStep()
    print core.optimizer.final_pop[0].candidate[0:len(core.optimizer.final_pop[0].candidate)/2]

    

if __name__=="__main__":
    try:
        parameters=sys.argv[1]
        main(parameters)
    except IndexError:
        sys.exit("Missing filename!")
