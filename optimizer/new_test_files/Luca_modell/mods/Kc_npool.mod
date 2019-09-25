: Fast Ca2+ & V-dependent K+ channel
: from Durstewitz & Gabriel (2006), Cerebral Cortex

NEURON {
	SUFFIX Kc_npool
	USEION k READ ki, ko WRITE ik
	USEION can READ cani
        RANGE gk, gKcbar
}

UNITS {
        (mM) = (milli/liter)
	(mA) = (milliamp)
	(mV) = (millivolt)
}

PARAMETER {
	cani		(mM)
	gKcbar= 0.0022	(mho/cm2)
}

ASSIGNED {
	v  (mV)
	ik (mA/cm2)
	cinf 
	ctau (ms)
	gk (mho/cm2)
	ek (mV)
	ki (mM)
	ko (mM)
}

STATE {
	c 
}

INITIAL {
	rate(v)
	c = cinf
}

BREAKPOINT {
	SOLVE states METHOD derivimplicit
	gk = gKcbar*c*c        
	ek = 25*log(ko/ki)
	ik = gk*(v-ek)
}

DERIVATIVE states {
        rate(v)
	c' = (cinf-c)/ctau
}

UNITSOFF

FUNCTION calf(v (mV), cani (mM)) (/ms) { 
	   LOCAL vs, va
           vs=v+40*log10(1000*cani)
	   va=vs+18
	   if (fabs(va)<1e-04){
	   	calf = -0.0064*(-12-va*0.5)
	   }
	   else {	   
		calf = (-0.0064*vs-0.1152)/(-1+exp(-va/12))
	   }
}

FUNCTION cbet(v (mV), cani (mM))(/ms) { 
	   LOCAL vs
	   vs=v+40*log10(cani*1000)+152
	   cbet = 1.7*exp(-vs/30)
}	

PROCEDURE rate(v) {
	   LOCAL  csum, ca, cb
	   ca=calf(v,cani) 
	   cb=cbet(v, cani)
	   csum = ca+cb
	   cinf = ca/csum
	   ctau = 1/csum
	   if (ctau<1.1) { ctau = 1.1 }
}
	
UNITSON
