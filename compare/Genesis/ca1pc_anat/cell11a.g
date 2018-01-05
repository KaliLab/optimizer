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
    int compt,i
    str ascfile, file

    // Delete objects from previous simulation if any.

    if ({exists /CA1_pyramid})
        delete /CA1_pyramid
	delete /input
	delete /voltage_c
        delete /out/{sim_output_file}
        delete /out
        reclaim
    end

    // Define new channel library and load in the cell.

    make_channel_library
    readcell {cell} /CA1_pyramid

    // create spike input
    create pulsegen /input
    setfield ^ baselevel 0 width1 {WIDTH} delay1 {DEL1} delay2 {DEL2}
//    create spikegen /input/spike
//    setfield ^ thresh 0.5 abs_refract 1e-3 output_amp 1
//    addmsg /input /input/spike INPUT output
    
    // Save output of simulations to disk.

    openfile {sim_output_file} w
    closefile {sim_output_file}

    ce /
    create neutral /out
    create asc_file /out/{sim_output_file}
    setfield ^ leave_open 1 append 1 flush 0 filename {sim_output_file}
    addmsg /CA1_pyramid/1 /out/{sim_output_file} SAVE Vm
    useclock /out/{sim_output_file} 1

    if (adjust_flag)
        adjust_parameters
    end
end
