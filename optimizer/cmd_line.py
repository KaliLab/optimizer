import sys
import Core
import xml.etree.ElementTree as ET
from reportlab.lib.colors import coral


def main(fname,param=None):
    """
    The main function of the command line version.
    Reads the content of the .xml file into the option object,
    and creates the core object which runs the optimization process based on the .xml file.
    - *fname* -- the configuration file which contains the settings (should be in xml format)
    - *param* -- controls the level of output, 0 means minimal, 1 means maximal
    (the Default is None which is interpreted as 1) 
    """
    try:
        f=open(fname,"r")
    except IOError as ioe:
        print ioe
        sys.exit("File not found!\n")
    tree = ET.parse(fname)
    root = tree.getroot()
    if root.tag!="settings":
        sys.exit("Missing \"settings\" tag in xml!")

    core=Core.coreModul()
    if param!=None:
        core.option_handler.output_level=param.lstrip("-v_level=") 
    core.option_handler.read_all(root)
    core.Print()
    kwargs={"file" : core.option_handler.GetFileOption(),
            "input": core.option_handler.GetInputOptions()}
    core.FirstStep(kwargs)
    
    kwargs={"simulator": core.option_handler.GetSimParam()[0],
            "model" : core.option_handler.GetModelOptions(),
            "sim_command":core.option_handler.GetSimParam()[1]}
    core.LoadModel(kwargs)
    
    kwargs={"stim" : core.option_handler.GetModelStim(),"stimparam" : core.option_handler.GetModelStimParam()}
    core.SecondStep(kwargs)
    
    
    kwargs=None
    
    core.ThirdStep(kwargs)
    core.FourthStep()
    print core.optimizer.final_pop[0].candidate[0:len(core.optimizer.final_pop[0].candidate)/2]
    print "resulting parameters: ",core.optimal_params

    

#if __name__=="__main__":
#    print "start"
#    try:
#        print sys.argv
#        parameters=sys.argv[1]
#    except IndexError:
#        sys.exit("Missing filename!")
#    main(parameters)
