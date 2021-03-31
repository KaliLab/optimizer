TITLE small conductance calcium activated potassium channels

COMMENT
 sKCa - kinetics from Hirschberg (1998), at room temperature
 (22-24degC).

 How the q10 works: There is a q10 for the rates (alpha and beta's)
 called Q10 and a Q10 for the maximum conductance called gmaxQ10.  The
 q10s should have been measured at specific temperatures temp1 and
 temp2 (that are 10degC apart). Ideally, as Q10 is temperature
 dependant, we should know these two temperatures.  We used to
 follow the more formal Arrhenius derived Q10 approach.  The
 temperature at which this channel's kinetics were recorded is tempb
 (base temperature).  What we then need to calculate is the desired
 rate scale for now working at temperature celsius (rate_k).  This was
 given by the empirical Arrhenius equation, using the Q10, but now is 
 using the quick Q10 approximation. 
ENDCOMMENT

NEURON {
	SUFFIX sKCa
	USEION ca READ cai
	USEION k READ ki,ek WRITE ik
	RANGE  gk,isKCa
	GLOBAL sKCatau,activate_Q10,Q10,gmaxQ10,rate_k,gmax_k,temp1,temp2,tempb
}

UNITS {
	(mM) = (milli/liter)
	(mA) = (milliamp)
	F = (faraday) (coulombs)	: Faradays constant 
}

PARAMETER {
        v (mV)
	dt (ms)
	gk = 0.0001 (mho/cm2)
        isKCa = 0.0 (mA/cm2)
	sKCatau = 2.365325544e+01 (ms)
	ek 
	ki
	cai
	celsius
	
	activate_Q10 = 1
	Q10 = 1.5
	gmaxQ10 = 1.5
	temp1 = 19.0 (degC)
	temp2 = 29.0 (degC)
	tempb = 23.0 (degC)
}

ASSIGNED {
	ica (mA/cm2)
        ik (mA/cm2)
        winf 
	wtau (ms)
	rate_k
	gmax_k
}

STATE {
        w
}

BREAKPOINT {
	SOLVE integrate METHOD cnexp
	ik = (gk*gmax_k)*w*(v-ek)
	isKCa = ik
}


UNITSOFF

INITIAL {
	LOCAL ktemp,ktempb,ktemp1,ktemp2
	if (activate_Q10>0) {
	  rate_k = Q10^((celsius-tempb)/10)
          gmax_k = gmaxQ10^((celsius-tempb)/10)
	}else{
	  rate_k = 1.0
	  gmax_k = 1.0
	}
	setinf(cai)
	w = winf
}

DERIVATIVE integrate {
        setinf(cai)
	w' = (winf - w)/wtau
}

PROCEDURE setinf(cai) {
	LOCAL wcai
	: these equations are for micro Molar
	wcai = cai*1000
	winf = 0.81/(1+exp((llog(wcai)+0.3)/ -0.46))
	wtau = sKCatau/rate_k
}

FUNCTION llog(x) {  :returns log of x, but error checks first
        if (x>1e-11) {
                llog = log(x)
	}else{
	        llog=0
        }
}

UNITSON






