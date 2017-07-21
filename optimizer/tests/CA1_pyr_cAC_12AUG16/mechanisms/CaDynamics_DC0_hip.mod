: Dynamics that track inside calcium concentration
: modified from Destexhe et al. 1994
: Dan Keller and Christian Roessert - removed shell, made dependent on geometry of individual sections via the surface to volume ratio


NEURON	{
	SUFFIX CaDynamics_DC0_hip
	USEION ca READ ica WRITE cai
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

	: kappa_e Calcium binding ratio:
	:	CA1: (Sabatini 2002) 100 for 4um radius, 20 for 0.1um
	: Percent of free calcium (not buffered) gamma = 1/kappa
	gamma = 0.01 (1)

	: rate of removal of calcium:
	: CA1: (Sabatini 2002) 100ms for 4um radius, 12ms for 0.1um
	decay = 100 (ms)

	: baseline calcium
	: CA1: (Sabatini 2002) 65 nM
	minCai = 6.5e-5 (mM)
}

ASSIGNED	{
	ica (mA/cm2)
	diam (um)  : diameter of current segment (automatically available within NMODL, like v)
	surftovol (1/um)
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
}

DERIVATIVE states	{
	cai' = -(10000)*ica*surftovol*gamma/(2*FARADAY) - (cai - minCai)/decay
}
