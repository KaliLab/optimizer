// genesis

//
// siminit.g: basic definitions for simulation.
//

setrand -sprng
randseed
floatformat %g

int restore       = 0  // flag for whether to restore old parameter values

//
// Check to see if the simulation is in progress.
// The "sim_status" file consists of a single integer:
//
// 0 means the parameter search has not yet begun,
// 1 means the search is in progress, and
// 2 means the search is over.
//
// We use this file so that a shell script can control genesis.
// Periodically stopping, saving and restarting genesis is important
// because this is the only way to guarantee that memory leaks don't
// eventually accumulate and crash the simulation.
//

int status

openfile sim_status r
status = {readfile sim_status}
closefile sim_status

if (status == 1)
    restore = 1
elif (status == 2)
    echo
    echo Search is finished!
    quit
end

// simulation timings:

float tmax = 1.5                // simulation time in sec
float dt = 0.000025             // simulation time step in sec
setclock  0  {dt}               // set the simulation clock
setclock 1 5e-5

float DEL1 = 0.2
float WIDTH1 = 0.003
float AMP1 = 5e-10
float DEL2 = 0.303
float WIDTH2 = 0.6
float AMP2 = 1e-11

// file names:

str cellfile          = "131117-C2.p"
// str origcellfile      = "CA3wh_pas.p"
str sim_output_file   = "Vm"
// str sim_spk_file      = {sim_output_file} @ ".spk.sim"
str bestfile          = {sim_output_file} @ ".best"
// str sim_spk_file_best = {sim_spk_file} @ ".best"
str matchfile         = "match.values"
str restore_file      = "param.save"

// Where the best values of the parameters are stored:
str best_param_file   = "best.params"

// This is what we want our parameter search to match.  It consists of
// spike times from the "real" cell.  In fact, other forms of data,
// such as membrane potential traces, can also be used, but they
// require changes to the matching function.

str real_vdata_file      = "data/131117-C2_IC1500.dat"
// str real_spk_file      = "data/Vinj48_2c.spk.data"

