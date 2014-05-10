//genesis

/* FILE INFORMATION
** CA1 excitatory (AMPA-type glutamatergic) and inhibitory (GABA-A)
** synaptically activated channels  (based on mitsyn.g by Upi Bhalla)
** 
** Data from Maccaferri et al. (2000)
**
** Implemented by Szabolcs Kali (based on generic channels by D. Beeman)
*/

// CONSTANTS
float EGlu = 0.0  // changed from 0.045
float EGABA = -0.070 // changed from -0.082
float SOMA_A = 1e-9
float GGlu = SOMA_A * 50
float GGABA = SOMA_A * 50
float G_NMDA = SOMA_A * 6     // maximum conductance
// float E_NMDA = 0.0          // reversal potential
float tau1_NMDA = 6.5e-3   // open time constant
float tau2_NMDA = 300.0e-3   // close time constant
float CMg = 2.0     // Magnesium concentration for magnesium block
float eta = 0.33
float gamma = 60


//===================================================================
//                     SYNAPTIC CHANNELS 
//===================================================================


function make_Ex_channel
	if ({exists Ex_channel})
		return
	end

	create		synchan	Ex_channel
    	setfield	        Ex_channel \
		Ek			{EGlu} \
		tau1		{ 2.0e-4 } \	// sec
		tau2		{ 3.0e-3 } \ 	// sec
		gmax		{GGlu} // Siemens
end

function make_NMDA
        if ({exists NMDA})
                return
        end

        create          synchan NMDA
        setfield                NMDA \
                Ek                      {EGlu} \
                tau1            { tau1_NMDA } \    // sec
                tau2            { tau2_NMDA } \    // sec
                gmax            {GGlu} // Siemens
end

function make_slow_Inh_channel
	if ({exists sInh_channel})
		return
	end

	create		synchan	sInh_channel
    	setfield	        sInh_channel \
	Ek			{ EGABA } \
	tau1		{ 6.0e-3 } \	// sec
	tau2		{ 30.0e-3 } \	// sec
	gmax		{GGABA}		// Siemens
end

function make_fast_Inh_channel
        if ({exists fInh_channel})
                return
        end

        create          synchan fInh_channel
        setfield	fInh_channel \
        Ek                      { EGABA - 0.010 } \ // shift introduced for testing
        tau1            { 2.0e-3 } \ 
        tau2            { 14.0e-3 } \ 
        gmax            {GGABA}         // Siemens
end

