In this example we estimate some basic synaptic parameters based on a simulated voltage clamp experiment with synaptic input.
The target data (iclamp.dat) consist of the recorded clamp current (in units of nA) from a virtual voltage clamp electrode inserted into a single-compartment model, which contains Hodgkin-Huxley-type Na+ and K+ conductances, plus a conductance-based synapse with a double exponential time course (rise time: 0.3 ms, decay time: 3 ms, maximal conductance: 10 nS, delay: 0 ms). The data file also contains time.
The model neuron receives through the synapse a spike train input, which consists of 4 spikes at regular 100 ms intervals starting at 100 ms. The full length of the recording is 500 ms, the sampling rate is 40 kHz.
The model file (simple_hh_syn_vclamp_toopt.hoc) contains the neuronal model (including the synapse), the spike generator (NetStim) object which generates the input, and a NetCon object which connects the input to the cell.
As we need to set the parameters of the synapse and those of the NetCon, and Optimizer cannot discover these parameters automatically, we use a simple user function (ufun.txt) to adjust the parameters (maximal conductance (in microsiemens), synaptic delay, rise time constant, decay time constant (all in milliseconds)).
We need voltage clamp at a constant level (-70 mV); one way to accomplish this is to use a step protocol in voltage clamp with a single amplitude of -70 mV (and arbitrary delay and duration), and an initial voltage of -70 mV.
The optimization should be done using the mean square error cost function. Evolutionary optimization for 100 generations with a population of 100 restores the original parameters with high precision.

To run the example, you must edit the "simple_hh_syn_vclamp_toopt2_settings.xml" file:
set the "model_spec_dir" tag to any existing directory
set the "input_dir" tag to the path of the input file (including the file name itself!) (input file:"iclamp_new.dat")
set the "model_path" tag to the path "simple_hh_syn_vclamp_toopt2.hoc" file
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c simple_hh_syn_vclamp_toopt2_settings.xml" into the terminal and press enter.
