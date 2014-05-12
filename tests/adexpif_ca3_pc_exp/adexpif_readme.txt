The input data file contains 4 traces each with different step amplitudes. The traces are 1100 ms long, the step starts at 100ms and lasts for 900 ms.The amplitudes are the following:
0.30 nA
0.35 nA
0.40 nA
0.45 nA
The sampling frequency was 5 kHz.

Some of the parameters of the model were changed (based on other simualtions), and the following ones are the subject of optimization:
vthres
vreset
trefrac
a
b
delta
tauw
cm
EL
GL
e_pas(=EL)
g_pas(obtained from GL)
This model has some special requirements to work (i.e be stable), so the optimization process must use a function (see the provided one). As the passive parameters are derived from the EL and GL parameters this optimization has 10 parameters.

To run the example, you must edit the "int&fire_settings.xml" file:
set the "model_spec_dir" tag to a directory, which contains the adexp.mod file
set the "input_dir" tag to the path of the input file (including the file name itself!) (input file:ca3_sort.txt.csv)
set the "model_path" tag to the path "int&fire.hoc" file
set the "base_dir" tag to a directory where you want the results to be stored
After these modifications type "python optimizer.py -c int&fire_settings.xml" into the terminal and press enter.
