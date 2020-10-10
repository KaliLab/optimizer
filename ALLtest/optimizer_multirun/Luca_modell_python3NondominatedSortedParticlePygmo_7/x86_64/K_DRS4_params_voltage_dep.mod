TITLE Channel: K_DR

COMMENT
    K delayed rectifier channel for hippocampal CA1 pyramidal neurons
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
      

    SUFFIX K_DRS4_params_voltage_dep
    USEION k READ ek WRITE ik VALENCE 1  ? reversal potential of ion is read, outgoing current is written
           
        
    RANGE gmax, gion
    
    RANGE Xinf, Xtau, X_v0, X_k0, X_tau0, X_gamma, X_kt
    
}

PARAMETER { 
      

    gmax = 0.0090 (S/cm2)  ? default value, should be overwritten when conductance placed on cell
	
	X_tau0 = 2 :Note units of this will be determined by its usage in the generic functions (ms)
	
	X_v0 = -20.0 : Note units of this will be determined by its usage in the generic functions (mV)

    X_k0 = 9 : Note units of this will be determined by its usage in the generic functions (mV)

	X_gamma= 0.9
	
	X_kt=0.05
    
}



ASSIGNED {
      

    v (mV)
    
    celsius (degC)
          

    ? Reversal potential of k
    ek (mV)
    ? The outward flow of ion: k calculated by rate equations...
    ik (mA/cm2)
    
    
    gion (S/cm2)
    Xinf
    Xtau (ms)
    
}

BREAKPOINT { 
                        
    SOLVE states METHOD cnexp
         

    gion = gmax*((X)^4)      

    ik = gion*(v - ek)
            

}



INITIAL {
    
    ek = -80
        
    rates(v)
    X = Xinf
        
    
}
    
STATE {
    X
    
}

DERIVATIVE states {
    rates(v)
    X' = (Xinf - X)/Xtau
    
}

PROCEDURE rates(v(mV)) {  
    
    LOCAL tau, inf, temp_adj_X
        
    TABLE Xinf, Xtau
	DEPEND celsius, X_v0, X_k0, X_tau0, X_gamma, X_kt
	FROM -100 TO 50 WITH 3000
    
    
    UNITSOFF
    temp_adj_X = 1
    
            
                
           

        
    ?      ***  Adding rate equations for gate: X  ***
        
    ? Note: Equation (and all ChannelML file values) in SI Units so need to convert v first...
    
   : v = v * 0.0010   ? temporarily set v to units of equation...
            
    :tau = 0.002

    ? Set correct units of tau for NEURON
    :tau = tau * 1000 
    
	
	tau = 1 / ( (X_kt * (exp (X_gamma * (v - X_v0) / X_k0))) + (X_kt * (exp ((X_gamma - 1)  * (v - X_v0) / X_k0)))) + X_tau0
        
    Xtau = tau/temp_adj_X
     
    inf = 1/(1 + exp (-(v - X_v0)/X_k0))
    
   : v = v * 1000   ? reset v
        
    Xinf = inf
    
    ?     *** Finished rate equations for gate: X ***
         

}


UNITSON


