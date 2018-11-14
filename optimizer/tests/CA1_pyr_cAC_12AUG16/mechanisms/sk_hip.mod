: SK-type calcium-activated potassium current
: Reference : Kohler et al. 1996

NEURON {
    SUFFIX sk_hip
    USEION k READ ek WRITE ik
    USEION ca READ cai
    RANGE gk_bar, gk, ik, zinf, ztau
}

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (mM) = (milli/liter)
}

PARAMETER {
    v                   (mV)
    gk_bar = .000001    (mho/cm2)
    ztau = 1            (ms)
    ek                  (mV)
    cai                 (mM)
}

ASSIGNED {
    zinf
    ik                  (mA/cm2)
    gk                  (S/cm2)
}

STATE {
    z       FROM 0 TO 1
}

BREAKPOINT {
    SOLVE states METHOD cnexp
    gk = gk_bar * z
    ik = gk * (v - ek)
}

DERIVATIVE states {
    rates(cai)
    z' = (zinf - z) / ztau
}

PROCEDURE rates(ca(mM)) {
    if(ca < 1e-7){
	    ca = ca + 1e-07
    }
    zinf = 1/(1 + (0.00043 / ca)^4.8)
}

INITIAL {
    rates(cai)
    z = zinf
}
