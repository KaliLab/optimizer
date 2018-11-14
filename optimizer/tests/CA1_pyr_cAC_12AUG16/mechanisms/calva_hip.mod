:Reference:	Magge and Johnston 1995
:Comment:   classic Morris-Lecar description of calcium channel
:Comment:   cell/dendrite - attached recording, junction potential cannot be properly estimated

NEURON	{
	SUFFIX calva_hip
	USEION ca READ eca WRITE ica
	RANGE gca_bar, gca, ica, minf, mtau, hinf, htau, vcorr, vhm, km, tm, vhh, kh, th, tbh, qt10, tbm, celsius_orig
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{

	celsius 		(degC)
	gca_bar = 0.01 (S/cm2)

	vhm = -39.8		(mV)		: v 1/2 for act
	km = 8.3 		(mV)		: act slope
	tm = 1			(ms) 		: max. time constant (guess)
	tbm = 0.1		(ms) 		: baseline time constant (guess)

	vhh = -70		(mV)		: v 1/2 for inact
	kh = -6.5		(mV)		: inact slope
	th = 50			(ms)		: max. time constant (guess)
	tbh = 1			(ms)		: baseline time constant (guess)

	qt10 = 2.3		(1)
	vcorr = 0		(mV)		: voltage shift correction
	celsius_orig = 22 (degC)
}

ASSIGNED	{
	v		(mV)
	eca		(mV)
	ica		(mA/cm2)
	gca		(S/cm2)
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
	gca = gca_bar*m*m*h
	ica = gca*(v-eca)
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
	mtau = ((2*tm) / ( exp((v - (vhm+vcorr)) / (4*km)) + exp((-v + (vhm+vcorr)) / (4*km)) ) + tbm) /qt 	: classic ml

    if(v == (vhh+vcorr)){
    	v = v + 0.0001
    }

	hinf = 1 / (1 + exp(((vhh+vcorr) - v) / kh))
	htau = ((2*th) / ( exp((v - (vhh+vcorr)) / (4*kh)) + exp((-v + (vhh+vcorr)) / (4*kh)) ) + tbh) /qt  : classic ml

	UNITSON
}
