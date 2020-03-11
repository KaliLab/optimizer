:Reference: Hoffman 1997
:comment: 	cell/dendrite - attached recording, junction potential cannot be properly estimated
:			tau not properly determined
:			proximal

NEURON	{
	SUFFIX kap2_hip
	USEION k READ ek WRITE ik
	RANGE gk_bar, gk, ik, minf, mtau, hinf, htau, vcorr, vhm, km, vhh, kh, hmin, qt10, tbm
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{
	celsius 		(degC)
	gk_bar = 0.01 (S/cm2)

	vhm = 11		(mV)		: v 1/2 for act (proximal) (Hoffman 1997)
	km = 18 		(mV)		: act slope (proximal) (Hoffman 1997)
	:vhm = -1		(mV)		: v 1/2 for act (distal) (Hoffman 1997)
	:km = 15 		(mV)		: act slope (distal) (Hoffman 1997)

	tbm = 1			(ms) 		: constant time constant

	vhh = -56		(mV)		: v 1/2 for inact (Hoffman 1997)
	kh = -8			(mV)		: inact slope (Hoffman 1997)
	hmin = 2		(ms)

	vcorr = 0		(mV)		: voltage shift correction
	qt10 = 2.3		(1)
	celsius_orig = 22 (degC)
}

ASSIGNED	{
	v		(mV)
	ek		(mV)
	ik		(mA/cm2)
	gk		(S/cm2)
	minf
	mtau
	hinf
	htau
}

STATE	{
	m
	h
}

BREAKPOINT	{
	SOLVE states METHOD cnexp
	gk = gk_bar*m*h
	ik = gk*(v-ek)
}

DERIVATIVE states	{
	rates()
	m' = (minf-m)/mtau
	h' = (hinf-h)/htau
}

INITIAL{
	rates()
	m = minf
	h = htau
}

PROCEDURE rates(){
  	LOCAL qt
  	qt = qt10^((celsius-celsius_orig)/10)

	UNITSOFF
    if(v == (vhm+vcorr)){
    	v = v+0.0001
    }

	minf = 1 / (1 + exp(((vhm+vcorr) - v) / km))
	mtau = tbm /qt

	hinf = 1 / (1 + exp(((vhh+vcorr) - v) / kh))

	: linear increase
	htau = 0.26*(v+50-vcorr) /qt
	if (htau<hmin/qt) {htau=hmin/qt}

	UNITSON
}
