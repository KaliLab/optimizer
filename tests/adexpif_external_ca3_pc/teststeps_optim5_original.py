# -*- coding: iso-8859-1 -*-
"""
PyNN model
Simulation of a step current injection into an AdExpIF neuron

Szabolcs Kali, IEM HAS
Dec 2013
"""

from pyNN.utility import get_script_args
import numpy

simulator_name = get_script_args(1)[0]  
exec("from pyNN.%s import *" % simulator_name)

params = numpy.genfromtxt("params.param")

setup()

gL_Bas 		= params[0]   #5.0e-3 #7.14293e-3
tauMem_Bas 	= params[1]   #14.0
Cm_Bas 		= tauMem_Bas * gL_Bas
Vrest_Bas 	= params[2]   #-70.0
reset_Bas 	= params[3]   #-56.0 #-55.0
theta_Bas 	= params[4]   #-50.0
tref_Bas 	= params[5]   #0.1

E_Exc = 0.0
E_Inh = -70.0

tauSyn_BasExc = 3.0
tauSyn_BasInh = 1.5

a = params[6]   #0.0 #8.0 #5.0 #3.2 #-0.8 #4.0         #nS	Subthreshold adaptation conductance
#a = 0.
# moves threshold up

b = params[7]   #0.0 #0.2 #0.055 #0.001 #0.1 #0.065 #0.0805      #nA	Spike-triggered adaptation
#b = 0.
# -> decreases the slope of the f-I curve
# 0.3 - slope = 3-4 Hz/100 pA
# 0.15 - slope = 6-7 Hz/100 pA
# 0.065 -slope = 15 Hz/100 pA

delta_T = params[8]   #2.0 #0.5 #0.8	#mV	Slope factor
tau_w = params[9]   #20 #100#144.0   #ms	Adaptation time constant
# changes shape of f-I curve
# 44 steeper, 160 flatter

v_spike = theta_Bas + 10 * delta_T	#mV	Spike detection threshold

cell_params_Bas = {"cm":        Cm_Bas,
                   "tau_m":		tauMem_Bas,
                   "v_rest":    Vrest_Bas,
                   "e_rev_E":   E_Exc,
                   "e_rev_I":   E_Inh,
                   "tau_syn_E": tauSyn_BasExc,
                   "tau_syn_I": tauSyn_BasInh,
                   "tau_refrac":tref_Bas,
                   "v_reset":   reset_Bas,
                   "v_thresh":  theta_Bas,
                   "a":    		a,
                   "b":    		b,
                   "delta_T": 	delta_T,
                   "tau_w":    	tau_w,
                   "v_spike":  	v_spike}


# cells = Population(27,EIF_cond_exp_isfa_ista, cell_params_Bas)
cells = Population(1,EIF_cond_exp_isfa_ista, cell_params_Bas)
cells.initialize(v=-60.0)

# current = [0.010000,  -0.010000 ,  0.020000 , -0.020000,   0.030000 , -0.030000, 0.040000,   -0.040000 ,  0.050000,  -0.050000,   0.060000,  -0.060000,   0.070000 , -0.070000, 0.080000 , -0.080000 ,  0.090000 , -0.090000 ,  0.100000 , -0.100000,   0.150000, 0.200000 ,  0.250000 ,  0.300000 ,  0.350000 ,  0.400000  , 0.450000]
# current = [current[x] + 0.05 for x in range(len(current))]
current_list = [0.15, 0.2, 0.3, 0.6]

trace_num = int(round(params[10]))
current = current_list[trace_num]
print current

for cell in cells:
    
    current_source = StepCurrentSource(times=[100.0, 900.0], amplitudes=[current, 0.0])
    cell.inject(current_source)


cells.record(['spikes', 'v'])

run(1099.91)

# uj syntaxa van ennek is
vm_array	= cells.get_data('v')
spike_array	= cells.get_data('spikes')


# mintak alapjan a kiiras
# eloszor a potencialokat es ertekeket irjuk ki file-ba
# for seg in vm_array.segments:
# 	vm = seg.analogsignalarrays[0]

# 	potentials = numpy.squeeze(vm)
# 	times = vm.times

# 	printable = numpy.array([times, potentials]).T

# 	numpy.savetxt('trace2.dat', printable[::2,:], fmt='%.2f')

# # spike traint irjuk ki file-ba
# for seg in spike_array.segments:
# 	st = seg.spiketrains[0]
# 	numpy.savetxt('spike2.dat', st, fmt='%.2f')


# mivel 1 db segment van es abban 1 analogsignalarray illetve spiketrain
# ez a suritett megoldas a kiirasra ugyanazt csinalja
vm 			= vm_array.segments[0].analogsignalarrays[0]
print_vm 	= numpy.array([vm.times , numpy.squeeze(vm)]).T
numpy.savetxt('trace.dat', print_vm[::2,:], fmt='%.2f')


printable_spiketrain = spike_array.segments[0].spiketrains[0]
numpy.savetxt('spike.dat', printable_spiketrain, fmt='%.2f')

#import matplotlib.pyplot as plt
#plt.plot(print_vm[:,1])
#plt.show()

end()
