import sys
import Core
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('Agg')
matplotlib.interactive(False)
from pylab import *
ioff()



def main(fname, param=None):
    """
    The main function of the command line version.
    Reads the content of the .xml file into the option object,
    and creates the core object which runs the optimization process based on the .xml file.

    :param fname: the configuration file which contains the settings (should be in xml format)
    :param param: controls the level of output, 0 means minimal, 1 means maximal (the Default is None which is interpreted as 1)

    """
    try:
        f = open(fname, "r")
    except IOError as ioe:
        print ioe
        sys.exit("File not found!\n")
    tree = ET.parse(fname)
    root = tree.getroot()
    if root.tag != "settings":
        sys.exit("Missing \"settings\" tag in xml!")

    core = Core.coreModul()
    if param != None:
        core.option_handler.output_level = param.lstrip("-v_level=")
    core.option_handler.read_all(root)
    core.Print()
    kwargs = {"file" : core.option_handler.GetFileOption(),
            "input": core.option_handler.GetInputOptions()}
    core.FirstStep(kwargs)

    kwargs = {"simulator": core.option_handler.GetSimParam()[0],
            "model" : core.option_handler.GetModelOptions(),
            "sim_command":core.option_handler.GetSimParam()[1]}
    core.LoadModel(kwargs)

    kwargs = {"stim" : core.option_handler.GetModelStim(), "stimparam" : core.option_handler.GetModelStimParam()}
    core.SecondStep(kwargs)


    kwargs = None

    core.ThirdStep(kwargs)
    core.FourthStep()
    #print core.optimizer.final_pop[0].candidate[0:len(core.optimizer.final_pop[0].candidate) / 2]
    print "resulting parameters: ", core.optimal_params
    fig = figure(1, figsize=(7, 6))
    axes = fig.add_subplot(111)
    exp_data = []
    model_data = []
    if core.option_handler.type[-1] != 'features':
        for n in range(core.data_handler.number_of_traces()):
            exp_data.extend(core.data_handler.data.GetTrace(n))
            model_data.extend(core.final_result[n])
        no_traces = core.data_handler.number_of_traces()
    else:
        for n in range(len(core.data_handler.features_data["stim_amp"])):
            model_data.extend(core.final_result[n])
        no_traces = len(core.data_handler.features_data["stim_amp"])
    if core.option_handler.type[-1]  != 'features':
        t = int(ceil(core.option_handler.input_length))
    else:
        t = int(ceil(core.option_handler.run_controll_tstop))
    step = core.option_handler.run_controll_dt
    axes.set_xticks([n for n in range(0, int((t * no_traces) / (step)), int((t * no_traces) / (step) / 5.0)) ])
    axes.set_xticklabels([str(n) for n in range(0, t * no_traces, (t * no_traces) / 5)])
    #print t,step
    #print axes.get_xticks()
    axes.set_xlabel("time [ms]")
    if core.option_handler.type[-1]!= 'features':
        _type = core.data_handler.data.type
    else:
        _type = "Voltage" if core.option_handler.run_controll_record =="v" else "Current" if core.option_handler.run_controll_record == "c" else ""
    axes.set_ylabel(_type + " [" + core.option_handler.input_scale + "]")
    if core.option_handler.type[-1]!= 'features':
        axes.plot(range(0, len(exp_data)), exp_data)
        axes.plot(range(0, len(model_data)), model_data, 'r')
        axes.legend(["target", "model"])
    else:
        axes.plot(range(0, len(model_data)), model_data, 'r')
        axes.legend(["model"])
    fig.savefig("result_trace.png", dpi=None, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches=None, pad_inches=0.1)
    fig.savefig("result_trace.eps", dpi=None, facecolor='w', edgecolor='w')
    fig.savefig("result_trace.svg", dpi=None, facecolor='w', edgecolor='w')



#if __name__=="__main__":
#    print "start"
#    try:
#        print sys.argv
#        parameters=sys.argv[1]
#    except IndexError:
#        sys.exit("Missing filename!")
#    main(parameters)
