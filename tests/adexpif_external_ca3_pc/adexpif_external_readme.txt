The input data file (ca3_pc_v2_4.csv) contains 4 voltage traces, corresponding to the responses of a CA3 pyramidal neuron to current steps of different amplitudes. The traces are 1100 ms long, the step starts at 100ms and lasts for 900 ms. The amplitudes are the following:
0.30 nA
0.35 nA
0.40 nA
0.45 nA
The sampling frequency was 5 kHz.

The model to be optimized is an adaptive exponential integrate-and-fire (AdExpIF) neuron. The model is implemented using the Python interface to the NEST simulator (see teststeps_optim5.py), and is handled as a black box by Optimizer. Specifically, the following 10 parameters are the subject of optimization, and are passed to the Python script (along with an extra parameter corresponding to the index of the stimulus) through the file "params.param":
g_L
tau_m
E_L
t_ref
V_reset
V_th
a
b
delta
tau_w

Some additional parameters (C_m and V_peak) of the model are calculated from these parameters in the Python script.

The model script saves the results of the simulation in the files trace.dat (containing the voltage trace) and spike.dat (containg explicit spike times from the same run), which are then used by Optimizer to compute the corresponding cost (fitness) value.

To run the example from the command line, you must edit the "_settings.xml" file:
set the "sim_command" tag to "python /FULL/PATH/TO/MODEL/SCRIPT 10", where /FULL/PATH/TO/MODEL/SCRIPT points to the location of the Python script implementing the model
set the "input_dir" tag to the path of the input file (including the file name itself!)
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c _settings.xml" into the terminal and press enter.
