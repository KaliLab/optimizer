//genesis  -  transferwh_pas.g - GENESIS Version 2.2
// Created by Szabolcs Kali

/*======================================================================
  Activates an excitatory synapse in each compartment of a simple
  5-compartment passive model neuron, and records the maximum voltage
  transient in all compartments for each case.
  ======================================================================*/

//===============================
//      Function Definitions
//===============================

function step_tmax
    step {tmax} -time
end
    
function make_vmtable
int time

create table /vdata_c
call /vdata_c TABCREATE 30000 0 0.5

openfile {real_vdata_file} r
	for(time=0; time<30000; time=time+1)
	    setfield /vdata_c table->table[{time}] { {getarg {readfile {real_vdata_file} } -arg 2} / 1000}
	end
	closefile {real_vdata_file}

end
	
//===============================
//   Main function: run_transfer 
//===============================

function run_transfer
int i

check

create table /voltage_c
call /voltage_c TABCREATE 30000 0.0 0.5
setfield /voltage_c step_mode 3
useclock /voltage_c 1

//	addmsg /CA1_pyramid/{compt} /voltage{compt} INPUT Vm
//	showfield /CA1_pyramid/{compt} Rm Cm Ra  // for debugging

	openfile {sim_output_file} w
	closefile {sim_output_file}

// j = 0
	addmsg /input /CA1_pyramid/Soma INJECT output
//	setfield /input level1 2e-10
//	setfield /CA1_pyramid/{compt}/Ex_channel \
//	      synapse[0].weight 1.0 synapse[0].delay 0.0
	addmsg /CA1_pyramid/Soma /voltage_c INPUT Vm

	openfile  {sim_output_file} a
        writefile {sim_output_file} "/newplot"
	writefile {sim_output_file} "/plotname 0.2"
        closefile {sim_output_file}

	reset
	step {tmax} -time

	call /out/{sim_output_file} SAVE

	deletemsg /CA1_pyramid/Soma 0 -find /input INJECT
	deletemsg /voltage_c 0 -find /CA1_pyramid/Soma INPUT

	call out/{sim_output_file} FLUSH

//		call /voltage{i} TABOP M
//		writefile Vmax {getfield /voltage{i} output}
//		setfield /vmax_current table->table[{j}] {getfield /voltage{i} output}
//		j = j + 1
//	end

// closefile Vmax
end

