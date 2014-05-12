The data file has one trace, which is 1000 ms long and the sampling frequency was 40kHz.
The data file also contains the time and was obtained from the corresponding model by using an IClamp (connected to the middle (0.5) of the soma) with the following parameters:
stim.del=200
stim.dur=500
stim.amp=0.2

The following model parameters were set (the others are default):
gnabar_hh=0.1
gkbar_hh=0.03
gl_hh=0.0001

To run the example, you must edit the "hh_pas_settings.xml" file:
set the "model_spec_dir" tag to any existing directory (this model doesn't use additional mod files)
set the "input_dir" tag to the path of the input file (including the file name itself!) (input file: "input_data2.dat")
set the "model_path" tag to the path "hh_pas.hoc" file
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c hh_pas_settings.xml" into the terminal and press enter.

