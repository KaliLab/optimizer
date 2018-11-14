The data trace was obtained from a biophisicly accurate reconstruction of a CA1 layer piramidal cell, by stimulating the somatic section with a 200 pA current stimuli. The experiment lasted for 1000 ms and the stimuli started at 200 ms and lasted for 600 ms (ended at 800 ms). The sampling frequency was 5kHz.
WARNING: the data is given in V not in mV

The model was created by clusterizing the branches of the detailed model into 6 compartments, the parameter values of the channels were obtained by averaging the values in the detailed model.
The somatic parameters are the subjects of optimization.

The additional mechanisms required by the model are in the mod_files folder. You must run the nrnivmodl command to optain the necessary files (you should select the folder containing the files obtained by nrnivmodl as the special folder in the program)

To run the example, you must edit the "ca1pc_model_settings.xml" file:
set the "model_spec_dir" tag to the directory, where you store the files obtained by the nrnivmodl command
set the "input_dir" tag to the path of the input file (including the file name itself!) (input file:Vinj48_2c_1.dat)
set the "model_path" tag to the path "ca1pc_model.hoc" file
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c ca1pc_model_settings.xml" into the terminal and press enter.


For step-by-step instructions to run the example from the Optimizer GUI please refer to 'ca1_pc_simplification_GUI.pdf'.
