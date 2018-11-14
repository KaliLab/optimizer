
# coding: utf-8

# In[158]:

import nest
import numpy as np

nest.ResetKernel()


# In[159]:

params = np.genfromtxt("params.param")

gL_Bas      = params[0]*1000   #5.0e-3 #7.14293e-3
tauMem_Bas 	= params[1]   #14.0
Cm_Bas      = tauMem_Bas * gL_Bas
Vrest_Bas 	= params[2]   #-70.0
reset_Bas 	= params[4]-params[3] #params[3]   #-56.0 #-55.0
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
tau_w   = params[9]   #20 #100#144.0   #ms	Adaptation time constant
# changes shape of f-I curve
# 44 steeper, 160 flatter

v_spike = theta_Bas + 10 * delta_T	#mV	Spike detection threshold


# In[160]:

# this is how we create a neuron
neuron = nest.Create('aeif_cond_exp')

cell_params_Bas = {"C_m":         Cm_Bas,
                   #"tau_m":       tauMem_Bas,      # tau_m in pynn
                   "g_L":         gL_Bas,
                   "E_L":         Vrest_Bas,
                   "E_ex":        E_Exc,
                   "E_in":        E_Inh,
                   "tau_syn_ex":  tauSyn_BasExc,
                   "tau_syn_in":  tauSyn_BasInh,
                   "t_ref":       tref_Bas,
                   "V_reset":     reset_Bas,
                   "V_th":        theta_Bas,
                   "a":           a,             
                   "b":           b*1000,
                   "Delta_T":     delta_T,
                   "tau_w":       tau_w,
                   "V_peak":      v_spike}

nest.SetStatus(neuron, cell_params_Bas)
nest.SetStatus(neuron, {'V_m':-60.0})


# In[161]:

current_list = [150., 200., 300., 600.]

trace_num = int(round(params[10]))
current   = current_list[trace_num]


# In[162]:

current_gen = nest.Create('step_current_generator')
nest.SetStatus(current_gen, {'amplitude_times': [100., 900.], 'amplitude_values': [current, 0.0]})


# In[163]:

voltmeter     = nest.Create('voltmeter', params={'interval':0.2})
spikedetector = nest.Create('spike_detector')


# In[164]:

nest.Connect(current_gen, neuron)
nest.Connect(voltmeter,   neuron)
nest.Connect(neuron,      spikedetector)


# In[165]:

nest.Simulate(1100.1)


# In[166]:

times    = nest.GetStatus(voltmeter)[0]['events']['times']      # they start from 1.0
times    = np.insert(times, 0, 0.)
voltages = nest.GetStatus(voltmeter)[0]['events']['V_m']
voltages = np.insert(voltages, 0, -60.)
spikes   = nest.GetStatus(spikedetector)[0]['events']['times']

#import matplotlib.pyplot as plt
#plt.plot(times, voltages)
#plt.show()

# In[167]:

np.savetxt('spike.dat', spikes, fmt='%.2f')
np.savetxt('trace.dat', np.array([times, voltages]).T, fmt='%.2f')