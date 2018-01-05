// genesis

//
// cell.g: sets up a simulation which is the basis for the parameter search.
//

// Note that a new cell is defined for each iteration of the parameter
// search.  This is necessary because the tabchannel tables for the KM
// channel are manipulated in destructive ways by the parameter search,
// so it is safest to recreate the cell from scratch each time.  It also
// makes the bookkeeping somewhat simpler, and doesn't consume much
// simulation time.  If the cell model was very large and took a long
// time to load up, this approach might not be feasible.

function newsim(cell, adjust_flag)
    str cell
    int adjust_flag   // if 1, then adjust parameters.

    str ascfile, file

    // Delete objects from previous simulation if any.

    if ({exists /cell})
        delete /Vclamp
	delete /syninput
        delete /cell
	delete /current_c
        delete /out/{sim_output_file}
        delete /out
        reclaim
    end

    // Define new channel library and load in the cell.

    make_channel_library
    readcell {cell} /cell

    // Provide voltage clamp and synaptic input to cell.

// create voltage clamp circuit and attach it to soma
pushe /
make_Vclamp
pope
setfield /Vclamp/PID gain 5e-7
addmsg /cell/soma /Vclamp/PID SNS Vm
addmsg /Vclamp/PID /cell/soma INJECT  output

setfield /Vclamp/lowpass C 1e-8 inject -0.070

// create synaptic input
create pulsegen /syninput
setfield ^ baselevel 0 level1 1 width1 1e-4 delay1 0.1
create spikegen /syninput/spike
setfield ^ thresh 0.5 abs_refract 1e-3 output_amp 1
addmsg /syninput /syninput/spike INPUT output

addmsg /syninput/spike /cell/soma/Ex_channel SPIKE
setfield /cell/soma/Ex_channel synapse[0].weight 1.0
setfield /cell/soma/Ex_channel synapse[0].delay 0.002

    // Save output of simulations to disk.

    clearfile {sim_output_file}

    ce /
    create neutral /out
    create asc_file /out/{sim_output_file}
    setfield ^ leave_open 1 append 1 flush 0 filename {sim_output_file}
    addmsg /cell/soma /out/{sim_output_file} SAVE inject
    useclock /out/{sim_output_file} 1

    if (adjust_flag)
        adjust_parameters
    end
end
