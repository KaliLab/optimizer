// cell.p.perfect: "correct" test cell for parameter searches

*cartesian
*asymmetric
*relative

*set_compt_param    RM          0.333
*set_compt_param    RA          1.0
*set_compt_param    CM          0.01
*set_compt_param    EREST_ACT  -0.0543

*compt /library/compartment

// #    name    parent      x   y   z   d     ch dens  ch dens...

soma none  0  0  100  10  

