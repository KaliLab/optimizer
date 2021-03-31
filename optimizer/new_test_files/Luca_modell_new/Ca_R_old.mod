
TITLE Channel: Ca_BG_MN2

COMMENT
    Generic HH-type Ca channel model in Borg-Graham format
ENDCOMMENT


UNITS {
    (mA) = (milliamp)
    (mV) = (millivolt)
    (S) = (siemens)
    (um) = (micrometer)
    (molar) = (1/liter)
    (mM) = (millimolar)
    (l) = (liter)
}


NEURON {
    
    SUFFIX Ca_R_old
    USEION ca WRITE ica VALENCE 2  ? reversal potential of ion is read, outgoing current is written
           
        
    RANGE gmax, gion
    
    RANGE Xinf, Xtau
    RANGE Yinf, Ytau
        
    RANGE X_v0, X_k0, X_kt, X_gamma, X_tau0
    RANGE Y_v0, Y_k0, Y_kt, Y_gamma, Y_tau0

}

PARAMETER { 
    
	eca = 80 (mV)

    gmax = 0.020 (S/cm2)  ? default value, should be overwritten when conductance placed on cell
    
    X_v0 = -2 : Note units of this will be determined by its usage in the generic functions (mV)

    X_k0 = 10 : Note units of this will be determined by its usage in the generic functions (mV)

    X_kt = 0.1 : Note units of this will be determined by its usage in the generic functions (1/ms)

    X_gamma = 0.5 : Note units of this will be determined by its usage in the generic functions

    X_tau0 = 0 : Note units of this will be determined by its usage in the generic functions (ms)
    
    Y_v0 = -53 : Note units of this will be determined by its usage in the generic functions (mV)

    Y_k0 = -9 : Note units of this will be determined by its usage in the generic functions (mV)

    Y_kt = 0.010 : Note units of this will be determined by its usage in the generic functions (1/ms)

    Y_gamma = 0.5 : Note units of this will be determined by its usage in the generic functions

    Y_tau0 = 20.0 : Note units of this will be determined by its usage in the generic functions (ms)

}



ASSIGNED {
    
    v (mV)
    
    celsius (degC)
          

    ? Reversal potential of ca
    ? eca (mV)
    ? The outward flow of ion: ca calculated by rate equations...
    ica (mA/cm2)
    
    
    gion (S/cm2)
    Xinf
    Xtau (ms)
    Yinf
    Ytau (ms)
    
}

BREAKPOINT { 
                        
    SOLVE states METHOD cnexp
         

    gion = gmax*((X)^2)*((Y)^1)

    ica = gion*(v - eca)
            

}



INITIAL {
    
    eca = 80
        
    rates(v)
    X = Xinf
    Y = Yinf
    
}
    
STATE {
    X
    Y
}

DERIVATIVE states {
    rates(v)
    X' = (Xinf - X)/Xtau
    Y' = (Yinf - Y)/Ytau
}

PROCEDURE rates(v(mV)) {  
    
    LOCAL tau, inf, temp_adj_X, temp_adj_Y
        
    TABLE Xinf, Xtau,Yinf, Ytau
    DEPEND celsius, X_v0, X_k0, X_kt, X_gamma, X_tau0, Y_v0, Y_k0, Y_kt, Y_gamma, Y_tau0
    FROM -100 TO 50 WITH 3000
    
    
    UNITSOFF

    temp_adj_X = 1
    temp_adj_Y = 1

        
    ?      ***  Adding rate equations for gate: X  ***
            
    tau = 1 / ( (X_kt * (exp (X_gamma * (v - X_v0) / X_k0))) + (X_kt * (exp ((X_gamma - 1)  * (v - X_v0) / X_k0)))) + X_tau0
        
    Xtau = tau/temp_adj_X
    
    
    inf = 1 / ( 1 + exp (-(v - X_v0) / X_k0)) 
        
    Xinf = inf
    
    ?     *** Finished rate equations for gate: X ***
    
    
    ?      ***  Adding rate equations for gate: Y  ***
    
    tau = 1 / ( (Y_kt * (exp (Y_gamma * (v - Y_v0) / Y_k0))) + (Y_kt * (exp ((Y_gamma - 1)  * (v - Y_v0) / Y_k0)))) + Y_tau0
    
    Ytau = tau/temp_adj_Y
    
    
    inf = 1 / ( 1 + exp (-(v - Y_v0) / Y_k0)) 
    
    Yinf = inf
    
    ?     *** Finished rate equations for gate: Y ***
    

}


UNITSON


