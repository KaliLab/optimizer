COMMENT

   **************************************************
   File generated by: neuroConstruct v1.5.1 
   **************************************************

   This file holds the implementation in NEURON of the Cell Mechanism:
   Leak_pyr (Type: Channel mechanism, Model: ChannelML based process)

   with parameters: 
   /channelml/@units = Physiological Units 
   /channelml/notes = ChannelML file containing a single Channel description 
   /channelml/channel_type/@name = Leak_pyr 
   /channelml/channel_type/@density = yes 
   /channelml/channel_type/status/@value = stable 
   /channelml/channel_type/notes = Simple example of a leak/passive conductance. Note: for GENESIS cells with a single leak conductance,         it is better to use the Rm and Em variab ... 
   /channelml/channel_type/current_voltage_relation/@cond_law = ohmic 
   /channelml/channel_type/current_voltage_relation/@ion = non_specific 
   /channelml/channel_type/current_voltage_relation/@default_erev = -75 
   /channelml/channel_type/current_voltage_relation/@default_gmax = 3.39905E-4 

// File from which this was generated: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/Leak_pyr/Leak_pyr.xml

// XSL file with mapping to simulator: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/Leak_pyr/ChannelML_v1.8.1_NEURONmod.xsl

ENDCOMMENT


?  This is a NEURON mod file generated from a ChannelML file

?  Unit system of original ChannelML file: Physiological Units

COMMENT
    ChannelML file containing a single Channel description
ENDCOMMENT

TITLE Channel: Leak_pyr

COMMENT
    Simple example of a leak/passive conductance. Note: for GENESIS cells with a single leak conductance,
        it is better to use the Rm and Em variables for a passive current.
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
      

    SUFFIX Leak_pyr
    ? A non specific current is present
    RANGE e
    NONSPECIFIC_CURRENT i
    
    RANGE gmax, gion
    
}

PARAMETER { 
      

    gmax = 0.000000339905 (S/cm2)  ? default value, should be overwritten when conductance placed on cell
    
    e = -75 (mV) ? default value, should be overwritten when conductance placed on cell
    
}



ASSIGNED {
      

    v (mV)
        
    i (mA/cm2)
        
}

BREAKPOINT { 
    i = gmax*(v - e) 
        

}

