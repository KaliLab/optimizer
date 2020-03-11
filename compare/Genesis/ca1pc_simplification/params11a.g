// genesis

//
// params.g: setting up the parameter table.
//

int NPARAMS = 9  // number of parameters

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
setfield /par stop_after 0
setfield /par restart_every 250
setfield /par scale 1.0
setfield /par simplex_init_noise 0.1


// Set the starting values and ranges of all the parameters.
// usage: initparamSA path param type range center scalemod label
//
// The "scalemod" value represents a typical length scale for the
// parameter.  For multiplicative scale parameters a scalemod value of 1.0
// is usually fine; for the additive minf offset we choose 3 mV out of
// a total of 10 mV range.  The precise value isn't that important,
// but it should be in the right order of magnitude.

initparamSA /par 0  1   10.0    1.0  1.0    "Gbar (Na) scaling"
initparamSA /par 1  1   10.0    1.0  1.0    "Gbar (K_DR) scaling"
initparamSA /par 2  1   10.0    1.0  1.0    "Gbar (K_A) scaling"
initparamSA /par 3  1   10.0    1.0  1.0    "Gbar (Ca_L) scaling"
initparamSA /par 4  1   10.0    1.0  1.0    "Gbar (Ca_N) scaling"
initparamSA /par 5  1   10.0    1.0  1.0    "Gbar (K_M) scaling"
initparamSA /par 6  1   10.0    1.0  1.0    "Gbar (K_C) scaling"
initparamSA /par 7  1   10.0    1.0  1.0    "Gbar (K_AHP) scaling"
initparamSA /par 8  1   10.0    1.0  1.0    "Gbar (H) scaling"

// The following function has to be re-written for each different
// parameter search.  I like to keep all parameters for a given
// channel adjacent to one another.  I also like to keep all channels
// corresponding to a given ion next to one another.  This is only
// really important for the genetic algorithm method, where you
// usually don't want crossovers to split up parameters corresponding
// to the same channel.

function adjust_parameters

    // Adjust voltage-gated conductances
    adjust_Gbar /par  0    /CA1_pyramid/1/Na_soma
    adjust_Gbar /par  1    /CA1_pyramid/1/K_DR
    adjust_Gbar /par  2    /CA1_pyramid/1/K_A_prox
    adjust_Gbar /par  3    /CA1_pyramid/1/CaL
    adjust_Gbar /par  4    /CA1_pyramid/1/CaN
    adjust_Gbar /par  5    /CA1_pyramid/1/K_M
    adjust_Gbar /par  6    /CA1_pyramid/1/K_C
    adjust_Gbar /par  7    /CA1_pyramid/1/K_AHP
    adjust_Gbar /par  8    /CA1_pyramid/1/H_CA1pyr_prox

end

