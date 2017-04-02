// genesis
// cell parameter file for the Wallenstein and Hasselmo CA3 pyramidal cell,
// modified from the parameter file for the 1991 Traub CA3 hippocampal cell
// "phi" parameter reduced by e-3
*cartesian
*relative
*symmetric

*set_global RM 294.2	//ohm*m^2  - modified from passive version
*set_global RA 1.0	//ohm*m
*set_global CM 0.0078     //F/m^2
*set_global EREST_ACT	-0.065	// volts

// The format for each compartment parameter line is :
// name  parent  x       y       z       d       ch      dens ...
// For channels, "dens" =  maximum conductance per unit area of compartment

1	none	20	0	0	20	Na_soma	500	K_DR	90	K_A_prox	38			Ca_conc	-5e+13	CaT	0	CaL	19	CaN	20	CaR	0	K_M	50	K_C	39	K_AHP	30	H_CA1pyr_prox	1.1	Ex_channel	-1e-10
2	1	562	0	0	3.16	Na_dend	50	K_DR	40	K_A_prox	11	K_A_dist	132	Ca_conc	-2.7e+13	CaT	14.8	CaL	2.1	CaN	20	CaR	50	K_M	30	K_C	4.2			H_CA1pyr_prox	0.35	H_CA1pyr_dist	4.56	Ex_channel	-1e-10
2a	2	281	0	0	2.5	Na_dend	50	K_DR	40			K_A_dist	200	Ca_conc	-5.4e+13	CaT	14.8	CaL	2.1	CaN	20	CaR	500	K_M	30	K_C	4.2			H_CA1pyr_prox	0.35	H_CA1pyr_dist	4.56	Ex_channel	-1e-10
3	2a	610	0	610	2.0	Na_dend	19	K_DR	40			K_A_dist	246	Ca_conc	-2.3e+13	CaT	24	CaL	0	CaN	20	CaR	200	K_M	30							H_CA1pyr_dist	8.67	Ex_channel	-1e-10
4	2a	460	0	-460	0.63	Na_dend	19	K_DR	40			K_A_dist	250	Ca_conc	-8.8e+13	CaT	25	CaL	0	CaN	20	CaR	200	K_M	30							H_CA1pyr_dist	8.82	Ex_channel	-1e-10
5	1	-927	0	0	2.78	Na_dend	13	K_DR	40	K_A_prox	17	K_A_dist	101	Ca_conc	-1.2e+13	CaT	0	CaL	3.0	CaN	20	CaR	0	K_M	50	K_C	6	K_AHP	30	H_CA1pyr_prox	0.55	H_CA1pyr_dist	3.46	Ex_channel	-1e-10

