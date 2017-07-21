// genesis

//
// vclamp_syn.g: functions for running a simulation with voltage clamp
//       and periodic synaptic input
//

function make_ictable
    int time

    create table /idata_c
    call /idata_c TABCREATE 10000 0 0.5

    openfile {real_vdata_file} r
    for(time=0; time<10000; time=time+1)
        setfield /idata_c table->table[{time}] {getarg {readfile {real_vdata_file} } -arg 2}
    end
    closefile {real_vdata_file}
end

function clearfile(filename)
    // clears a disk file
    str       filename
    openfile  {filename} w
    closefile {filename}
end


//
// This function runs the cell simulation with each level of
// current injection in succession.
//

function runvc
    // /Iin is the pulsegen object that generates the currents
    // The output can be viewed with xplot as well as processed
    // to get the spike times or ISIs.

    str file
    clearfile {sim_output_file}

    create table /current_c
    call /current_c TABCREATE 10000 0.0 0.5
    setfield /current_c step_mode 3
    useclock /current_c 1

    addmsg /cell/soma /current_c INPUT inject

    reset
    step {total_duration} -t
    call /out/{sim_output_file} SAVE

    deletemsg /current_c 0 -find /cell/soma INPUT
    call out/{sim_output_file} FLUSH
end

