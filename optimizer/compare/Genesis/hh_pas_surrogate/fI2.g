// genesis

//
// fI.g: functions for initializing tables of currents,
//       and functions to stimulate cell with varying depolarizing
//       currents to give frequency vs. current (f/I) outputs.
//

float fIscale       = 1e-9 // currents in table are in units of 1 nA
int   fItable_index = 0
str   currpath      = "/currtable"

function init_fItable(ncurrs)
    int ncurrs // number of currents
    create table {currpath}
    call {currpath} TABCREATE {ncurrs + 1} 0 0
    // need extra table entry to store delimiter (-9999.0)
end


function add_to_fItable(curr)
    float curr
    setfield {currpath} table->table[{fItable_index}] {curr}
    fItable_index = fItable_index + 1
end


function end_fItable
    setfield {currpath} table->table[{fItable_index}] -9999.0
    // -9999.0 in the table means it's the last entry;
    // -9999.0 is not executed
end


function show_fItable
    int i = 0
    float curr

    while ({getfield {currpath} table->table[{i}]} > -1000.0)
        curr = {getfield {currpath} table->table[{i}]}
        echo Current {i}: {curr}
        i = i + 1
    end
end


function make_fItable
    init_fItable 1
    add_to_fItable 0.2
    end_fItable
end

function make_vmtable
    int time

    create table /vdata_c
    call /vdata_c TABCREATE 6000 0 0.5

    openfile {real_vdata_file} r
    for(time=0; time<6000; time=time+1)
        setfield /vdata_c table->table[{time}] {getarg {readfile {real_vdata_file} } -arg 2}
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

function runfI
    // /Iin is the pulsegen object that generates the currents
    // The output can be viewed with xplot as well as processed
    // to get the spike times or ISIs.

    float current, plotted_current
    int i = 0
    str file
    clearfile {sim_output_file}

    create table /voltage_c
    call /voltage_c TABCREATE 6000 0.0 0.5
    setfield /voltage_c step_mode 3
    useclock /voltage_c 1

    addmsg /cell/soma /voltage_c INPUT Vm

    while ({getfield {currpath} table->table[{i}]} > -1000.0)
        reset
        plotted_current = {getfield {currpath} table->table[{i}]}
        current = plotted_current * fIscale
        setfield /Iin level1 {current}

        step {total_duration} -t
        call /out/{sim_output_file} SAVE

        i = i + 1
    end

    deletemsg /voltage_c 0 -find /cell/soma INPUT
    call out/{sim_output_file} FLUSH
end


