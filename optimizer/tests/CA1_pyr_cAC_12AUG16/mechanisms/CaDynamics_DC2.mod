: Dynamics that track inside calcium concentration
: modified from Destexhe et al. 1994
: Dan Keller and Christian Roessert - removed shell, made dependent on geometry of individual sections via the surface to volume ratio


NEURON	{
	SUFFIX CaDynamics_DC2
	USEION ca READ ica WRITE cai
	RANGE decay, gamma, minCai, ica, surftovol
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
	gamma = 0.01 : percent of free calcium (not buffered): Sabatini 2002: 0.01
	decay = 100 (ms) : rate of removal of calcium: Sabatini 2002: 100ms for 4um radius, 15ms for 1um
	minCai = 5e-5 (mM)
	diamref = 1 (um)
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
	surftovol = 8 / diam
	: printf("%12.9f\n", surftovol)
	cai = minCai
}

DERIVATIVE states	{

	cai' = -(10000)*ica*surftovol*gamma/(2*FARADAY) - (cai - minCai)/decay * diamref * surftovol

    : bigger diameter sections have slower time constants (Oertner and Svoboda 2002)
	: if the surf to vol ratio is in inverse microns,
	: the fit decay applies to the case when the radius of the dendrite is 4 microns (or diam = 8 microns)
	: since SA scales according to 2 pi r and volume scales according to pi r^2
	: the ratio is 2/r
}
