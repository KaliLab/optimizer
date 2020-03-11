:Reference: Shah 2008
:comment: 	whole-cell, junction potential not estimated


NEURON	{
	SUFFIX km2_hip
	USEION k READ ek WRITE ik
	RANGE gk_bar, gk, ik, minf, mtau, vcorr, vhm, km, tm, ktm, qt10, tbm
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	celsius 	(degC)
	gk_bar = 0.0001 (S/cm2)
	vhm = -38.7		(mV)		: v 1/2 for act fit (Shah 2008)
	km =  23.9		(mV)		: act slope fit (Shah 2008) 
	tm = 58.4		(ms) 		: max. time constant fit (Shah 2008)
	ktm = 8.7		(mV)		: tau width fit (Shah 2008)
	tbm	= 55.0		(ms)		: tau baseline fit (Shah 2008)

	vcorr = -14.3	(mV)		: voltage shift correction
	qt10 = 2.3		(1)
	celsius_orig = 35 (degC)
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
	mtau = ((2*tm) / ( exp((v - (vhm+vcorr)) / ktm) + exp((-v + (vhm+vcorr)) / ktm) ) + tbm) /qt

	UNITSON
}
