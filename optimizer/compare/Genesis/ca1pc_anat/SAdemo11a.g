// genesis

//
// SAdemo.g
//

//
// This demo runs a parameter search on a simple cell model using the
// simulated annealing (SA) parameter search method.  The cell is a
// simple one-compartment cell with three ionic conductances.  A series
// of six current injections ranging from 0.1 nA to 1.0 nA is delivered
// to the cell.  The spike times are extracted from the outputs and
// compared with the spike times for the target data set.  The free
// parameters of the simulation are adjusted to make the simulated cell
// reproduce the target output as closely as possible.
//

int orig = 0  // Used to regenerate the original data files.

// Create a library of prototype elements to be used by the cell reader
include compartments
include CA1pyr_chanb17
include CA1_synchan0  // excitatory and inhibitory synaptic channels in CA1

include siminit11a.g          // basic simulation definitions
include transfer11a.g   // main simulation function
include match_trace11a.g       // compares voltage response amplitudes
include channels3.g         // defines the channels
include paramfuncs.g       // helper functions for parameter searches
include params11a.g           // sets up parameter table
include cell11a.g             // functions to load in the cell model
include search11arid.g           // functions for running parameter searches

do_search

quit
