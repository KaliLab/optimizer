TITLE Kd current

COMMENT Equations from 
		  Lyle J Borg-Graham Interpretation of Data and Mechanisms for Hippocampal Pyramidal Cell Models A Chapter in "Cerebral Cortex, Volumne 13: Cortical Models" Edited by P.S.Ulinski, E.G.Jones and A.Peters,New York:plenum Press,1998
		  
		  The Krasnow Institute
		  George Mason University

Copyright	  Maciej Lazarewicz, 2001
		  (mlazarew@gmu.edu)
		  All rights reserved.
ENDCOMMENT

NEURON {
	SUFFIX kdBG_mod
	USEION k WRITE ik
	RANGE  gbar,ik, xtau, ytau, xinf, yinf, vhalfx, vhalfy
	:GLOBAL xtau, ytau, xinf, yinf
}

UNITS {
	(S)	= (siemens)
	(mA)	= (milliamp)
	(mV)	= (millivolt)
	FARADAY	= (faraday) (coulombs)
	R	= (k-mole)  (joule/degC)
}

PARAMETER {
	gbar	=   1.0e-3	(S/cm2)
	Ky	=   2.0e-4	(1/ms)
	gammay	=   0.0		(1)
	zettax	=   3.0		(1)
	zettay	=  -2.5		(1)
	vhalfx	= -63.0		(mV)
	vhalfy	= -90.0		(mV)
	taox	=   1.0		(ms)
	taoy	=   0.0		(ms)
}

ASSIGNED {
	v       (mV)
	ik     	(mA/cm2)
	celsius			(degC)
	xtau    (ms)
	ytau    (ms)
	xinf	(1)
	yinf	(1)
	q10	(1)
	T     	(K)
}

STATE { xs ys }

BREAKPOINT { 
	SOLVE states METHOD cnexp
	ik= gbar * xs^4 * ys^4 * ( v + 95.0 ) 
}

DERIVATIVE states {
	rates()
	xs'= (xinf- xs)/ xtau	
	ys'= (yinf- ys)/ ytau
}

INITIAL {
	T  = celsius + 273.15
	q10= 1.0^( (celsius-35.0) / 10.0(K) )
	rates()
	xs= xinf
	ys= yinf
}

PROCEDURE rates() { LOCAL a, b  
	a = q10*exp( (1.0e-3)*  zettax*(v-vhalfx)*FARADAY/(R*T) )
	b = q10*exp( (1.0e-3)* -zettax*(v-vhalfx)*FARADAY/(R*T) )
	xinf = a / ( a + b )
	xtau = taox

	a = q10*Ky*exp( (1.0e-3)*  zettay*     gammay *(v-vhalfy)*FARADAY/(R*T) )
	b = q10*Ky*exp( (1.0e-3)* -zettay*(1.0-gammay)*(v-vhalfy)*FARADAY/(R*T) )
	yinf = a   / ( a + b )
	ytau = 1.0 / ( a + b ) + taoy
}
