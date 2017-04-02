// genesis

//
// SAorig.g
//

//
// This script is used to regenerate the original target data files
// for use by the parameter search.
//

int orig = 1

include siminit3.g          // basic simulation definitions
include vclamp
include vclamp_syn.g               // sets up table of currents
include channels_syn.g         // defines the channels
include paramfuncs_syn.g       // helper functions for parameter searches
include params.g           // sets up parameter table
include cell3.g             // functions to load in the cell model
include search3.g           // functions for running parameter searches

make_orig

quit
