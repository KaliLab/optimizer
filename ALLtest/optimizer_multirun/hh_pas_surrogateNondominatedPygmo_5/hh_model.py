import numpy as np
from neuron import h, gui

params = np.genfromtxt('params.param')

soma = h.Section(name='soma')
soma.insert('hh')

soma.gnabar_hh = params[0]  # Sodium conductance in S/cm2
soma.gkbar_hh = params[1]  # Potassium conductance in S/cm2
soma.gl_hh = params[2]    # Leak conductance in S/cm2

stim = h.IClamp(soma(0.5))
stim.delay = 50
stim.dur = 300
stim.amp = 0.3

v_vec = h.Vector()        # Membrane potential vector
t_vec = h.Vector()        # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)
simdur = 1000

h.tstop = simdur
h.run()

times = t_vec.to_python()
voltages = v_vec.to_python()

np.savetxt('trace.dat', np.array([times, voltages]).T, fmt='%.3f')
