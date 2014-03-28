// genesis

//
// channels.g: voltage-dependent channel definitions.
//

include compartments

// passive membrane parameters
float   CM    // Farads/m^2 = 100x ohm/cm^2
float   RA    // Ohms m     = 0.01x ohm-cm
float   RM    // Ohms m^2   = 0.0001x ohm-cm^2

// channel equilibrium potentials (V)
float   EREST_ACT = -0.065
float   ENA       =  0.050
float   EK        = -0.077

float SOMA_A = 1e-9

//========================================================================
//                      Tabchan Na channel 
//========================================================================

function make_Na_hh_tchan
        str chanpath = "Na_hh_tchan"
        if ({argc} == 1)
           chanpath = {argv 1}
        end
        if ({exists {chanpath}})
                return
        end

        create tabchannel {chanpath}
                //      V
                //      S
                //      A
                //      S
                setfield ^ Ek {ENA} Gbar {1.2e3*SOMA_A} Ik 0 Gk 0  \
                    Xpower 3 Ypower 1 Zpower 0

        setupalpha {chanpath} X {0.1e6*(0.025 + EREST_ACT)} -0.1e6  \
            -1.0 {-1.0*(0.025 + EREST_ACT)} -0.01  \
            4e3 0.0 0.0 {-1.0*EREST_ACT} 18e-3

        setupalpha {chanpath} Y 70.0 0.0 0.0  \
            {-1.0*EREST_ACT} 0.02 1.0e3 0.0 1.0  \
            {-1.0*(0.030 + EREST_ACT)} -10.0e-3
end

//========================================================================
//                      Tabchan version of K channel
//========================================================================
function make_K_hh_tchan
        str chanpath = "K_hh_tchan"
        if ({argc} == 1)
           chanpath = {argv 1}
        end
        if (({exists {chanpath}}))
                return
        end

        create tabchannel {chanpath}
                //      V
                //      S
                //      A
                //      S
                setfield ^ Ek {EK} Gbar {360.0*SOMA_A} Ik 0 Gk 0  \
                    Xpower 4 Ypower 0 Zpower 0

        setupalpha {chanpath} X {10e3*(0.01 + EREST_ACT)} -10.0e3  \
            -1.0 {-1.0*(0.01 + EREST_ACT)} -0.01 125.0 0.0 0.0  \
            {-1.0*EREST_ACT} 80.0e-3
end


//========================================================================
//                Make library of prototypes
//========================================================================

// We have to delete the tabchannel tables explicitly when deleting the
// library or the interpol_structs in the tabchans will not get deallocated
// and will cause a memory leak.

function delete_channel_library
    ce /library
    call Na_hh_tchan     TABDELETE
    call K_hh_tchan    TABDELETE
    ce /
    delete /library
end


function make_channel_library
    if ({exists /library})
        delete_channel_library
    end

    create neutral /library
    ce /library
    make_cylind_compartment
    make_Na_hh_tchan
    make_K_hh_tchan
    ce /
    disable /library
end

