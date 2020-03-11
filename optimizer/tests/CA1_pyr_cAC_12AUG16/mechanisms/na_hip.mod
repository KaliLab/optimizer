:Reference: Magee and Johnston 1995
:Comment: 	cell/dendrite - attached recording, junction potential cannot be properly estimated
:Comment:	tau not properly determined

NEURON	{
	SUFFIX na_hip
	USEION na READ ena WRITE ina
	RANGE gna_bar, gna, ina, minf, mtau, hinf, htau, vcorr, vhm, km, ktm, tm, vhh, kh, kth, th, tbh, qt10, tbm, celsius_orig
}

UNITS	{
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER	{

	celsius 		(degC)
	gna_bar = 0.01   (S/cm2)

	vhm = -40.8		(mV)		: v 1/2 for act (fit)
	km = 8.6 		(mV)		: act slope (fit)
	
	ktm = 3.0		(mV)		: act tau slope (guess)
	tm = 0.3		(ms) 		: max. time constant (guess)
	tbm = 0.05		(ms) 		: baseline time constant (guess)

	vhh = -61.8 	(mV)		: v 1/2 for inact (fit), same value in htau
	kh = -7.3		(mV)		: inact slope (fit)

	kth = 4.5		(mV)		: inact time width (fit)
	th = 10.1		(ms)		: max. time constant (fit)
	tbh = 0.3		(ms)		: htau base (fit)

	qt10 = 2.3		(1)
	vcorr = 0		(mV)		: voltage shift correction
	celsius_orig = 22 (degC)
}

ASSIGNED	{
	v		(mV)
	ena		(mV)
	ina		(mA/cm2)
	gna		(S/cm2)
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
	gna = gna_bar*m*m*m*h
	ina = gna*(v-ena)
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
	mtau = ((2*tm) / ( exp((v - (vhm+vcorr)) / (4*ktm)) + exp((-v + (vhm+vcorr)) / (4*ktm)) ) + tbm) /qt 	: classic ml

    if(v == (vhh+vcorr)){
    	v = v + 0.0001
    }

	hinf = 1 / (1 + exp(((vhh+vcorr) - v) / kh))
	htau = ((2*th) / ( exp((v - (vhh+vcorr)) / (4*kth)) + exp((-v + (vhh+vcorr)) / (4*kth)) ) + tbh) /qt  : classic ml

	UNITSON
}
