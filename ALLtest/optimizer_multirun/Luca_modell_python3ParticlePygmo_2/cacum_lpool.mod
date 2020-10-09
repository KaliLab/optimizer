COMMENT
	calcium accumulation into a volume of area*depth next to the
	membrane with a decay (time constant tau) to resting level
	given by the global calcium variable cai0_ca_ion
ENDCOMMENT

NEURON {
	SUFFIX cacum_lpool
	USEION cal READ ical WRITE cali VALENCE 2
	RANGE depth, tau, cali0
}

UNITS {
	(mM) = (milli/liter)
	(mA) = (milliamp)
	F = (faraday) (coulombs)
}

PARAMETER {
	depth = 1 (nm)	: assume volume = area*depth
	tau = 10 (ms)
	cani0 = 50e-6 (mM)	: Requires explicit use in INITIAL
			: block for it to take precedence over cai0_ca_ion
			: Do not forget to initialize in hoc if different
			: from this default.
}

ASSIGNED {
	ical (mA/cm2)
}

STATE {
	cali (mM)
}

INITIAL {
	cali = cali0
}

BREAKPOINT {
	SOLVE integrate METHOD derivimplicit
}

DERIVATIVE integrate {
	cali' = -ical/depth/F/2 * (1e7) + (cali0 - cali)/tau
}
