:Reference: Magee 1998
:comment: 	cell/dendrite - attached recording, junction potential cannot be properly estimated

NEURON	{
	SUFFIX h_hip
	NONSPECIFIC_CURRENT ihcn
	RANGE gh_bar, gh, minf, mtau, vcorr, vhm, km, tm, vhtm, ktm, ihcn, qt10, tbm
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	celsius 		(degC)
	gh_bar = 0.00001 (S/cm2)
	ehcn =  -30.0 	(mV)

	vhm = -82		(mV)		: v 1/2 for act (soma) (Magee 1998)
	km = -8.8 		(mV)		: act slope (soma) (Magee 1998)
	:vhm = -90		(mV)		: v 1/2 for act (dendrites) (Magee 1998)
	:km = -8.5 		(mV)		: act slope (dendrites) (Magee 1998)

	tm = 40.1		(ms) 		: max. time constant fit to (Magee 1998)
	vhtm = -81.7	(mV)		: v tau max for act fit to (Magee 1998)
	ktm = 15.7		(mV)		: tau act width fit to (Magee 1998)
	tbm = 8.4		(ms) 		: baseline time constant

	vcorr = 0		(mV)		: voltage shift correction
	qt10 = 4.5		(1)			: measured in (Magee 1998)
	celsius_orig = 33 (degC)
}

ASSIGNED	{
	v		(mV)
	ihcn	(mA/cm2)
	gh		(S/cm2)
	minf
	mtau
}

STATE	{
	m
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gh = gh_bar*m
	ihcn = gh*(v-ehcn)
}

DERIVATIVE states	{
	rates()
	m' = (minf-m)/mtau
}

INITIAL{
	rates()
	m = minf
}

PROCEDURE rates(){
  	LOCAL qt
	qt = qt10^((celsius-celsius_orig)/10)

	UNITSOFF
    if(v == (vhtm+vcorr)){
    	v = v+0.0001
    }

	minf = 1 / (1 + exp(( (vhm+vcorr) - v) / km))
	mtau = ((2*tm) / ( exp((v - (vhtm+vcorr)) / ktm) + exp((-v + (vhtm+vcorr)) / ktm) ) + tbm) /qt

	UNITSON
}
