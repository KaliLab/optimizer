:Reference: Hoffman 1997
:comment: 	cell/dendrite - attached recording, junction potential cannot be properly estimated
:			tau not properly determined

NEURON	{
	SUFFIX kdr2_hip
	USEION k READ ek WRITE ik
	RANGE gk_bar, gk, ik, minf, mtau, vcorr, vhm, km, tm, qt10, tbm
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	celsius 		(degC)
	gk_bar = 0.003 (S/cm2)
	vhm = 13		(mV)		: v 1/2 for act (proximal) (Hoffman 1997)
	km = 11 		(mV)		: act slope (proximal) (Hoffman 1997)
	
	tm = 20.		(ms) 		: max. time constant (guess)
	tbm = 0.1		(ms) 		: baseline time constant

	vcorr = 0		(mV)		: voltage shift correction
	qt10 = 2.3
	celsius_orig = 22 (degC)
}

ASSIGNED	{
	v		(mV)
	ek		(mV)
	ik		(mA/cm2)
	gk		(S/cm2)
	minf
	mtau
}

STATE	{
	m
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gk = gk_bar*m
	ik = gk*(v-ek)
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
    if(v == (vhm+vcorr)){
    	v = v+0.0001
    }

	minf = 1 / (1 + exp(((vhm+vcorr) - v) / km))
	mtau = ((2*tm) / ( exp((v - (vhm+vcorr)) / (4*km)) + exp((-v + (vhm+vcorr)) / (4*km)) ) + tbm) /qt 	: classic ml

	UNITSON
}
