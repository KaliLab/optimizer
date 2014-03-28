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

include siminit1a.g          // basic simulation definitions
include transfer1a.g   // main simulation function
include match_trace1a.g       // compares voltage response amplitudes
include channels_pas1a.g         // defines the channels
include paramfuncs1a.g       // helper functions for parameter searches
include params1a.g           // sets up parameter table
include cell1a.g             // functions to load in the cell model
include search1a.g           // functions for running parameter searches

do_search

quit
