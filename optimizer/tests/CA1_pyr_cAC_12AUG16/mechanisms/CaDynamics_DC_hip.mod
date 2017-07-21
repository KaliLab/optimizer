: Dynamics that track inside calcium concentration
: modified from Destexhe et al. 1994
: Dan Keller and Christian Roessert - removed shell, made dependent on geometry of individual sections via the surface to volume ratio


NEURON	{
	SUFFIX CaDynamics_DC_hip
	USEION ca READ ica WRITE cai
	RANGE decay :, decay_slope, decay_off
	RANGE kappa :, k_slope, k_off, min_diam
	RANGE minCai, ica, surftovol
}

UNITS	{
	(mV) = (millivolt)
	(mA) = (milliamp)
	FARADAY = (faraday) (coulombs)
	PI      = (pi)       (1)
	(molar) = (1/liter)
	(mM) = (millimolar)
	(um)	= (micron)
}

PARAMETER	{
	: k Calcium binding ratio:
	:	CA1: (Sabatini 2002) 100 for 4um radius, 20 for 0.1um
	: L5: (Helmchen 1996) 100 @ 7um diam
	k_slope = 15
	k_off = -40

	: rate of removal of calcium:
	: CA1: (Sabatini 2002) 100ms for 4um radius, 12ms for 0.1um
	: L5: (Helmchen 1996) 70ms @ 7um diam
	decay_slope = 21.25 (ms)
	decay_off = -70 (ms)

	min_diam = 4
	max_diam = 10
	minCai = 6.5e-5 (mM) 	: CA1: (Sabatini 2002) 65 nM
}

ASSIGNED	{
	ica (mA/cm2)
	diam (um)  : diameter of current segment (automatically available within NMODL, like v)
	surftovol (1/um)
	kappa (1)
	decay (ms)
	}

STATE	{
	cai (mM)
	}

BREAKPOINT	{ SOLVE states METHOD cnexp }

INITIAL {
	: surface = 2*PI*(diam/2)*L
	: volume = PI*(diam/2)*(diam/2)*L
	surftovol = 4 / diam
	cai = minCai

	: bigger diameter sections have slower time constants (Oertner and Svoboda 2002)
	: and higher kappa (binding ratio, inverse of percent of free calcium (not buffered)),
	: adjust to reference diameter in recordings

	if (diam < min_diam) {
		kappa = 1/ (k_slope * min_diam + k_off)
		decay = decay_slope * min_diam + decay_off

	}else if (diam > max_diam){
		kappa = 1/ (k_slope * max_diam + k_off)
		decay = decay_slope * max_diam + decay_off

	} else {
		kappa = 1/ (k_slope * diam + k_off)
		decay = decay_slope * diam + decay_off
	}
}

DERIVATIVE states	{
	cai' = -(10000)*ica*surftovol/kappa/(2*FARADAY) - (cai - minCai)/decay
}
