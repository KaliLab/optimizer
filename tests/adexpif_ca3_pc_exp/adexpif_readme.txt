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
