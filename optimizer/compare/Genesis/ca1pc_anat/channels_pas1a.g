// genesis

//
// channels.g: voltage-dependent channel definitions.
//

// passive membrane parameters
// float   CM    // Farads/m^2 = 100x ohm/cm^2
// float   RA    // Ohms m     = 0.01x ohm-cm
// float   RM    // Ohms m^2   = 0.0001x ohm-cm^2

// channel equilibrium potentials (V)
// float   EREST_ACT = -0.060
// float   ENA       =  0.055
// float   EK        = -0.090


//========================================================================
//                Make library of prototypes
//========================================================================

// We have to delete the tabchannel tables explicitly when deleting the
// library or the interpol_structs in the tabchans will not get deallocated
// and will cause a memory leak.

function delete_channel_library
    ce /
    delete /library
end


function make_channel_library
    if ({exists /library})
        delete_channel_library
    end

    create neutral /library
    disable /library
    pushe /library
    make_cylind_compartment         /* makes "compartment" */
    pope
end

