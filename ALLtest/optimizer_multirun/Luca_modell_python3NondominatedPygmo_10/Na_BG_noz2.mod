TITLE Channel: Na_BG_noz2

COMMENT
    Generic HH-type Na channel model in Borg-Graham format
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
    
    SUFFIX Na_BG_noz2
    USEION na READ ena WRITE ina VALENCE 1  ? reversal potential of ion is read, outgoing current is written
           
        
    RANGE gmax, gion
    
    RANGE Xinf, Xtau
    RANGE Yinf, Ytau
        
    RANGE X_v0, X_k0, X_kt, X_gamma, X_tau0
    RANGE Y_v0, Y_k0, Y_kt, Y_gamma, Y_tau0

}

PARAMETER { 
    
    gmax = 0.0050 (S/cm2)  ? default value, should be overwritten when conductance placed on cell
    
    X_v0 = -24.0 : Note units of this will be determined by its usage in the generic functions (mV)

    X_k0 = 11.5 : Note units of this will be determined by its usage in the generic functions (mV)

    X_kt = 4 : Note units of this will be determined by its usage in the generic functions (1/ms)

    X_gamma = 0.3 : Note units of this will be determined by its usage in the generic functions

    X_tau0 = 0.0 : Note units of this will be determined by its usage in the generic functions (ms)
    
    Y_v0 = -58.3 : Note units of this will be determined by its usage in the generic functions (mV)

    Y_k0 = -6.7 : Note units of this will be determined by its usage in the generic functions (mV)

    Y_kt = 0.025 : Note units of this will be determined by its usage in the generic functions (1/ms)

    Y_gamma = 0.5 : Note units of this will be determined by its usage in the generic functions

    Y_tau0 = 0.0 : Note units of this will be determined by its usage in the generic functions (ms)

}



ASSIGNED {
    
    v (mV)
    
    celsius (degC)
          

    ? Reversal potential of na
    ena (mV)
    ? The outward flow of ion: na calculated by rate equations...
    ina (mA/cm2)
    
    
    gion (S/cm2)
    Xinf
    Xtau (ms)
    Yinf
    Ytau (ms)
    
}

BREAKPOINT { 
                        
    SOLVE states METHOD cnexp
         

    gion = gmax*((X)^3)*((Y)^1)

    ina = gion*(v - ena)
            

}



INITIAL {
    
    ena = 55
        
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


