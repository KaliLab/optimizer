// genesis

//
// params.g: setting up the parameter table.
//

int NPARAMS = 3     // number of parameters

// This is the main parameter search object:
create paramtableSA /par

call /par TABCREATE {NPARAMS}

// The following annealing schedule is a simple proportional decrease
// in temperature as the search proceeds.

setfield /par iterations_per_temp 1  inittemp 1.0 \
          annealing_method 2 annealing_rate 0.999

// Automatically set the "done" flag if the matches are very
// close to each other at a low temperature.  Also call the RESTART
// action every 250 iterations.

setfield /par testtemp 0.0001 tolerance 0.000001
setfield /par restart_every 250
setfield /par scale 1.0
setfield /par simplex_init_noise 0.1


// Set the starting values and ranges of all the parameters.
// usage: initparamGA path param type range center label

initparamSA /par 0  1   10.0    1.0	1.0  "Na Gbar scaling"
initparamSA /par 1  1   10.0    1.0	1.0  "Kdr Gbar scaling"
initparamSA /par 2  1   10.0    1.0	1.0  "RM scaling"


// The following function has to be re-written for each different
// parameter search.  I like to keep all parameters for a given
// channel adjacent to one another.  I also like to keep all channels
// corresponding to a given ion next to one another.  This is only
// really important for the genetic algorithm method, where you
// usually don't want crossovers to split up parameters corresponding
// to the same channel.

function adjust_parameters(table)

    // Adjust Gbars of ion channels:
    adjust_Gbar /par 0     /cell/soma/Na_hh_tchan
    adjust_Gbar /par 1     /cell/soma/K_hh_tchan
    adjust_Rm /par 2     /cell/soma
end


