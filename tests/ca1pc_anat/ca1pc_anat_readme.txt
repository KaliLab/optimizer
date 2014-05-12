The input data file ("131117-C2_short.dat") contains one trace obtained from a ca1 layer piramidal cell by using current clamp.
The cell was excited by a short 500pA and by a long 10pA pulse injected into the soma, so you have to use the provided stimuli file (for this, select the "Custom Waveform" option from the dropdown menu on the stimuli layer and then load the file: "cell2_stim.dat").
The data trace is 1500ms long and the sampling frequency was 20kHz.
The provided model is a passive one and it"s based on a precise reconstruction, and we are interested in the cm, Ra, g_pas parameters.
Because we had to set the e_pas parameter to 0 and we wanted to optimize the previous parameters in every section, we created a function to do this for us (see "udeffun_pyr_3param.txt"), you can load this on the model selection layer.

To run the example, you must edit the "morphology_131117-C2_settings.xml" file:
set the "model_spec_dir" tag to a valid directory (this can be any existing directory since this model doesn't require additional mod files)
set the "stim_amp" tag to the path of the stimuli file ("cell2_stim.dat") in the following fashion: "[path_to_file/cell2_stim.dat]"
set the "input_dir" tag to the path of the input file (including the file name itself!)
set the "model_path" tag to the path "morphology_131117-C2.hoc" file
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c morphology_131117-C2_settings.xml" into the terminal and press enter.
