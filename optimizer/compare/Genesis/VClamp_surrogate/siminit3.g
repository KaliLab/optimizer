// genesis

//
// siminit.g: basic definitions for simulation.
//

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

int generations_so_far

openfile sim_status r
generations_so_far = {readfile sim_status}
closefile sim_status

if (generations_so_far > 0)
    restore = 1
end

// simulation timings:

setclock    0    0.00001        // sec
setclock    1    0.00005        // output interval

float total_duration    = 0.500

// file names:

str cellfile          = "cell.p"
str sim_output_file   = "ic"
str bestfile          = {sim_output_file} @ ".best"
str matchfile         = "match.values"
str restore_file      = "param.save"

// Where the best values of the parameters are stored:
str best_param_file   = "best.params"

// This is what we want our parameter search to match.  It consists of
// spike times from the "real" cell.  In fact, other forms of data,
// such as membrane potential traces, can also be used, but they
// require changes to the matching function.

str real_vdata_file = "iclamp.data"
