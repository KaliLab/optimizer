TITLE T-type calcium current (Cav3.1)

UNITS {
    (mV) = (millivolt)
    (mA) = (milliamp)
    (S) = (siemens)
    (molar) = (1/liter)
    (mM) = (millimolar)
    FARADAY = (faraday) (coulomb)
    R = (k-mole) (joule/degC)
}

NEURON {
    SUFFIX cat31
    USEION ca READ cai, cao WRITE ica VALENCE 2
    RANGE pbar, ica
}

PARAMETER {
    pbar = 0.0 (cm/s)
    :q = 1	: room temperature 21 C
    q = 3	: body temperature 35 C

    X_v1 = -63.57
    X_k1 = 8.687
    X_tau0 = 1.275
    X_taumax = 13.54
    X_tauvhalf = -59.3
    valamimeredekseg = 6.8

    Y_v0 = -72
    Y_k0 = -6.9
    Y_tau0 = 20.0
    Y_taumax = 106.73
    Y_tauvhalf = - 56.37
    valamimeredekseg2  = 7.4
} 

ASSIGNED { 
    v (mV)
    ica (mA/cm2)
    eca (mV)
    celsius (degC)
    cai (mM)
    cao (mM)
    Xinf
    Xtau (ms)
    Yinf
    Ytau (ms)
}

STATE { m h }

BREAKPOINT {
    SOLVE states METHOD cnexp
    ica = pbar*m*m*m*h*ghk(v, cai, cao)
}

INITIAL {
    rates()
    m = Xinf
    h = Yinf
}

DERIVATIVE states { 
    rates()
    m' = (Xinf-m)/Xtau*q
    h' = (Yinf-h)/Ytau*q
}

PROCEDURE rates() {
    UNITSOFF

    Xinf = 1 / ( 1 + exp (-(v - X_v1) / X_k1))
    Xtau= X_tau0+ X_taumax/(1+exp((v-(X_tauvhalf))/ valamimeredekseg))
    Yinf = 1 / ( 1 + exp (-(v - Y_v0) / Y_k0))
    Ytau= Y_tau0+ Y_taumax/(1+exp((v-(Y_tauvhalf))/ valamimeredekseg2))
    UNITSON
}

FUNCTION ghk(v (mV), ci (mM), co (mM)) (.001 coul/cm3) {
    LOCAL z, eci, eco
    z = (1e-3)*2*FARADAY*v/(R*(celsius+273.15))
    if(z == 0) {
        z = z+1e-6
    }
    eco = co*(z)/(exp(z)-1)
    eci = ci*(-z)/(exp(-z)-1)
    ghk = (1e-3)*2*FARADAY*(eci-eco)
}

COMMENT

Rat Cav3.2 channels were isolated and transfection of human embryonic
kidney cells was performed [1].  Electrophysiological recordings were
done in 21 C.

NEURON model by Alexander Kozlov <akozlov@kth.se>. Kinetics of m3h
type was used [2-4]. Activation time constant was scaled up accordingly.

[1] Iftinca M, McKay BE, Snutch TP, McRory JE, Turner RW, Zamponi
GW (2006) Temperature dependence of T-type calcium channel
gating. Neuroscience 142(4):1031-42.

[2] Crunelli V, Toth TI, Cope DW, Blethyn K, Hughes SW (2005) The
'window' T-type calcium current in brain dynamics of different behavioural
states. J Physiol 562(Pt 1):121-9.

[3] Wolf JA, Moyer JT, Lazarewicz MT, Contreras D, Benoit-Marand M,
O'Donnell P, Finkel LH (2005) NMDA/AMPA ratio impacts state transitions
and entrainment to oscillations in a computational model of the nucleus
accumbens medium spiny projection neuron. J Neurosci 25(40):9080-95.

[4] Evans RC, Maniar YM, Blackwell KT (2013) Dynamic modulation of
spike timing-dependent calcium influx during corticostriatal upstates. J
Neurophysiol 110(7):1631-45.

Modified from Lindroos 2008. cat32.mod by Luca Tar 2021

ENDCOMMENT
