: SK-type calcium-activated potassium current
: Reference : Gu et al. 2007 / Borg-Graham 1999

NEURON {
    SUFFIX sk2_hip
    USEION k READ ek WRITE ik
    USEION ca READ cai
    RANGE gk_bar, gk, ik, winf, wtau
    RANGE alpha, beta, tau0
}

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (mM) = (milli/liter)
    (S) = (siemens)
}

PARAMETER {
    v                   (mV)
    gk_bar = .000001    (mho/cm2)
    ek                  (mV)
    cai                 (mM)
    alpha = 5e12        (/ms /mM /mM /mM /mM) :  Borg-Graham 1999: 2e14
    beta = 0.01         (/ms)
    n = 4               (1)
    tau0 = 250          (ms) : Borg-Graham 1999: 100 
}

ASSIGNED {
    winf                (1)
    wtau                (ms)
    tau                 (ms)
    ik                  (mA/cm2)
    gk                  (S/cm2)
}

STATE {
    w       FROM 0 TO 1
}

BREAKPOINT {
    SOLVE states METHOD cnexp
    gk = gk_bar * w * w
    ik = gk * (v - ek)
}

DERIVATIVE states {
    rates(cai)
    w' = (winf - w) / wtau
}

PROCEDURE rates(cai(mM)) {
    tau = 1 / (alpha * cai*cai*cai*cai + beta)
    winf = (alpha * cai*cai*cai*cai) * tau
    wtau = tau + tau0
}

INITIAL {
    rates(cai)
    w = winf
}
