TITLE D1_LTP_time_window
COMMENT
	automatically generated from an SBtab file
	date: Fri Apr 03 16:29:37 2020
ENDCOMMENT
NEURON {
	SUFFIX D1_LTP_time_window_Luca_cai_initials : OR perhaps POINT_PROCESS ?
	RANGE DA_start, DA_max : input
	RANGE pSubstrate_out, PP1_out, CaM_out, D32_out, total_CaMKII_activated_out : output
	RANGE ATP_expression : assigned
	RANGE Ca_expression : assigned
	RANGE DA_expression : assigned
	RANGE AMP : assigned
	RANGE ATP : assigned
	RANGE Ca : assigned
	RANGE DA : assigned
	RANGE AC5 : compound
	RANGE AC5_ATP : compound
	RANGE AC5_Ca : compound
	RANGE AC5_Ca_ATP : compound
	RANGE AC5_Ca_GaolfGTP : compound
	RANGE AC5_Ca_GaolfGTP_ATP : compound
	RANGE AC5_GaolfGTP : compound
	RANGE AC5_GaolfGTP_ATP : compound
	RANGE B56PP2A : compound
	RANGE B56PP2A_D32p75 : compound
	RANGE B56PP2A_pARPP21 : compound
	RANGE B56PP2Ap : compound
	RANGE B56PP2Ap_D32p75 : compound
	RANGE B56PP2Ap_pARPP21 : compound
	RANGE B72PP2A : compound
	RANGE B72PP2A_D32p34 : compound
	RANGE B72PP2A_D32p75 : compound
	RANGE B72PP2A_pARPP21 : compound
	RANGE B72PP2A_Ca_D32p34 : compound
	RANGE B72PP2A_Ca_D32p75 : compound
	RANGE B72PP2A_Ca : compound
	RANGE B72PP2A_Ca_pARPP21 : compound
	RANGE CaM : compound
	RANGE CaM_Ca2 : compound
	RANGE CaM_Ca4 : compound
	RANGE CaM_Ca4_pARPP21 : compound
	RANGE CaMKII : compound
	RANGE CaMKII_CaM_Ca4 : compound
	RANGE CaMKII_CaM : compound
	RANGE CaMKII_CaM_Ca2 : compound
	RANGE CaMKII_CaM_Ca2_psd : compound
	RANGE CaMKII_CaM_psd : compound
	RANGE CaMKII_CaM_Ca4_psd : compound
	RANGE CaMKII_psd : compound
	RANGE cAMP : compound
	RANGE Substrate : compound
	RANGE CDK5 : compound
	RANGE CDK5_D32 : compound
	RANGE D1R : compound
	RANGE D1R_DA : compound
	RANGE D1R_Golf_DA : compound
	RANGE D1R_Golf : compound
	RANGE D32p34 : compound
	RANGE D32p75 : compound
	RANGE D32 : compound
	RANGE GaolfGDP : compound
	RANGE GaolfGTP : compound
	RANGE Gbgolf : compound
	RANGE Golf : compound
	RANGE pCaMKII : compound
	RANGE pCaMKII_CaM_Ca4 : compound
	RANGE pCaMKII_CaM : compound
	RANGE pCaMKII_CaM_Ca2 : compound
	RANGE pCaMKII_CaM_Ca2_psd : compound
	RANGE pCaMKII_CaM_psd : compound
	RANGE pCaMKII_CaM_Ca4_psd : compound
	RANGE pCaMKII_psd : compound
	RANGE pSubstrate : compound
	RANGE PDE4 : compound
	RANGE PDE4_cAMP : compound
	RANGE PDE10r : compound
	RANGE PDE10r_cAMP : compound
	RANGE PDE10c : compound
	RANGE PDE10c_cAMP : compound
	RANGE PKA : compound
	RANGE PKAc : compound
	RANGE PKAc_B56PP2A : compound
	RANGE PKAc_D32 : compound
	RANGE PKAc_ARPP21 : compound
	RANGE PKA_Ca2MP : compound
	RANGE PKA_Ca4MP : compound
	RANGE PKAc_D32p75 : compound
	RANGE PKAreg : compound
	RANGE PP1 : compound
	RANGE PP1_pCaMKII_psd : compound
	RANGE PP1_pSubstrate : compound
	RANGE PP1_D32p34 : compound
	RANGE CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : compound
	RANGE pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : compound
	RANGE CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : compound
	RANGE pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : compound
	RANGE PP2B : compound
	RANGE PP2Bc : compound
	RANGE PP2Bc_D32p34 : compound
	RANGE PP2B_CaM : compound
	RANGE PP2B_CaM_Ca2 : compound
	RANGE pARPP21 : compound
	RANGE ARPP21 : compound
	RANGE pCaMKII_psd_Substrate : compound
	RANGE pCaMKII_CaM_psd_Substrate : compound
	RANGE pCaMKII_CaM_Ca2_psd_Substrate : compound
	RANGE pCaMKII_CaM_Ca4_psd_Substrate : compound
	RANGE CaMKII_CaM_psd_Substrate : compound
	RANGE CaMKII_CaM_Ca2_psd_Substrate : compound
	RANGE CaMKII_CaM_Ca4_psd_Substrate : compound
	RANGE total_CaMKII_activated : compound
        USEION ca READ cai VALENCE 2 : sth. like this may be needed for ions you have in your model
}
CONSTANT {
	tau_DA1 = 34.979 (millisecond) : a constant
	tau_DA2 = 420 (millisecond) : a constant
	DA_basal = 20 (nanomole/liter) : a constant
	Ca_basal = 60 (nanomole/liter) : a constant
}
PARAMETER {
	kf_R0 = 0.0299985 (/millisecond): a kinetic parameter
	kf_R1 = 0.0150003 (/millisecond): a kinetic parameter
	kf_R2 = 5.00035e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R2 = 0.25 (/millisecond): a kinetic parameter
	kf_R3 = 5.00035e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R3 = 0.25 (/millisecond): a kinetic parameter
	kf_R4 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R4 = 0.001 (/millisecond): a kinetic parameter
	kf_R5 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R5 = 0.0199986 (/millisecond): a kinetic parameter
	kf_R6 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R6 = 2.99999 (/millisecond): a kinetic parameter
	kf_R7 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R7 = 2.99985e-06 (/millisecond): a kinetic parameter
	kf_R8 = 1e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R8 = 0.2 (/millisecond): a kinetic parameter
	kf_R9 = 0.01 (/millisecond): a kinetic parameter
	kf_R10 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R10 = 0.000299985 (/millisecond): a kinetic parameter
	kf_R11 = 0.000199986 (/millisecond): a kinetic parameter
	kf_R12 = 0.001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R12 = 0.00150003 (/millisecond): a kinetic parameter
	kf_R13 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R13 = 0.1 (/millisecond): a kinetic parameter
	kf_R14 = 0.01 (/millisecond): a kinetic parameter
	kf_R15 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R15 = 0.1 (/millisecond): a kinetic parameter
	kf_R16 = 1e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R16 = 0.01 (/millisecond): a kinetic parameter
	kf_R17 = 1.50003e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R17 = 0.1 (/millisecond): a kinetic parameter
	kf_R18 = 8.00018e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R18 = 0.1 (/millisecond): a kinetic parameter
	kf_R19 = 1.50003e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R19 = 0.1 (/millisecond): a kinetic parameter
	kf_R20 = 0.00800018 (/millisecond): a kinetic parameter
	kf_R21 = 0.00150003 (/millisecond): a kinetic parameter
	kf_R22 = 0.00800018 (/millisecond): a kinetic parameter
	kf_R23 = 0.00129987 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R23 = 0.0001 (/millisecond): a kinetic parameter
	kf_R24 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R24 = 1 (/millisecond): a kinetic parameter
	kf_R25 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R25 = 1.99986e-07 (/millisecond): a kinetic parameter
	kf_R26 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R26 = 0.1 (/millisecond): a kinetic parameter
	kf_R27 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R27 = 2.99985e-05 (/millisecond): a kinetic parameter
	kf_R28 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R28 = 0.01 (/millisecond): a kinetic parameter
	kf_R29 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R29 = 0.001 (/millisecond): a kinetic parameter
	kf_R30 = 8.00018e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R30 = 0.1 (/millisecond): a kinetic parameter
	kf_R31 = 0.00150003 (/millisecond): a kinetic parameter
	kf_R32 = 0.00299985 (/millisecond): a kinetic parameter
	kf_R33 = 0.00299985 (/millisecond): a kinetic parameter
	kf_R34 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R34 = 0.001 (/millisecond): a kinetic parameter
	kf_R35 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R35 = 0.001 (/millisecond): a kinetic parameter
	kf_R36 = 0.00120005 (/millisecond): a kinetic parameter
	kf_R37 = 8.00018e-06 (/millisecond): a kinetic parameter
	kf_R38 = 2.60016e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R38 = 0.350002 (/millisecond): a kinetic parameter
	kf_R39 = 3.46019e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R39 = 0.0500035 (/millisecond): a kinetic parameter
	kf_R40 = 0.0500035 (/millisecond): a kinetic parameter
	kr_R40 = 2.99985e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R41 = 2.99985e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R41 = 0.001 (/millisecond): a kinetic parameter
	kf_R42 = 0.00249977 (/millisecond): a kinetic parameter
	kf_R43 = 1e-09 (/nanomole/liter^2-millisecond): a kinetic parameter
	kr_R43 = 0.001 (/millisecond): a kinetic parameter
	kf_R44 = 0.00299985 (/millisecond): a kinetic parameter
	kf_R45 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R45 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R46 = 0.01 (/millisecond): a kinetic parameter
	kf_R47 = 0.1 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R48 = 2.54976e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R48 = 0.001 (/millisecond): a kinetic parameter
	kf_R49 = 1e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R49 = 0.001 (/millisecond): a kinetic parameter
	kf_R50 = 7.50067e-08 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R50 = 0.001 (/millisecond): a kinetic parameter
	kf_R51 = 1.29987e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R51 = 0.001 (/millisecond): a kinetic parameter
	kf_R52 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R52 = 0.001 (/millisecond): a kinetic parameter
	kf_R53 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R53 = 0.001 (/millisecond): a kinetic parameter
	kf_R54 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R54 = 0.01 (/millisecond): a kinetic parameter
	kf_R55 = 0.0500035 (/millisecond): a kinetic parameter
	kf_R56 = 0.00254976 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R57 = 0.001 (/millisecond): a kinetic parameter
	kf_R58 = 1.99986e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R59 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R60 = 7.50067e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R61 = 0.0249977 (/millisecond): a kinetic parameter
	kf_R62 = 0.00064998 (/nanomole/liter-millisecond): a kinetic parameter
	kf_R63 = 0.001 (/millisecond): a kinetic parameter
	kf_R64 = 0.001 (/millisecond): a kinetic parameter
	kf_R65 = 0.001 (/millisecond): a kinetic parameter
	kf_R66 = 0.001 (/millisecond): a kinetic parameter
	kf_R67 = 6.00067e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R67 = 0.25 (/millisecond): a kinetic parameter
	kf_R68 = 6.00067e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R68 = 0.25 (/millisecond): a kinetic parameter
	kf_R69 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R69 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R70 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R70 = 0.0400037 (/millisecond): a kinetic parameter
	kf_R71 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R71 = 0.4 (/millisecond): a kinetic parameter
	kf_R72 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R72 = 4 (/millisecond): a kinetic parameter
	kf_R73 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R73 = 0.1 (/millisecond): a kinetic parameter
	kf_R74 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R74 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R75 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R75 = 0.01 (/millisecond): a kinetic parameter
	kf_R76 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R76 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R77 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R77 = 0.000400037 (/millisecond): a kinetic parameter
	kf_R78 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R78 = 0.0400037 (/millisecond): a kinetic parameter
	kf_R79 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R79 = 0.4 (/millisecond): a kinetic parameter
	kf_R80 = 4.49987e-05 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R80 = 0.2 (/millisecond): a kinetic parameter
	kf_R81 = 0.01 (/millisecond): a kinetic parameter
	kf_R82 = 0.000500035 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R82 = 0.01 (/millisecond): a kinetic parameter
	kf_R83 = 0.01 (/millisecond): a kinetic parameter
	kf_R84 = 7.00003e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R84 = 0.1 (/millisecond): a kinetic parameter
	kf_R85 = 0.001 (/millisecond): a kinetic parameter
	kf_R86 = 4.00037e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R86 = 0.1 (/millisecond): a kinetic parameter
	kf_R87 = 0.01 (/millisecond): a kinetic parameter
	kf_R88 = 7.00003e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R88 = 0.1 (/millisecond): a kinetic parameter
	kf_R89 = 0.001 (/millisecond): a kinetic parameter
	kf_R90 = 4.00037e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R90 = 0.1 (/millisecond): a kinetic parameter
	kf_R91 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R91 = 0.001 (/millisecond): a kinetic parameter
	kf_R92 = 0.01 (/millisecond): a kinetic parameter
	kf_R93 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R93 = 0.01 (/millisecond): a kinetic parameter
	kf_R94 = 0.01 (/millisecond): a kinetic parameter
	kf_R95 = 0.0001 (/millisecond): a kinetic parameter
	kf_R96 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R96 = 0.01 (/millisecond): a kinetic parameter
	kf_R97 = 0.01 (/millisecond): a kinetic parameter
	kf_R98 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R98 = 0.01 (/millisecond): a kinetic parameter
	kf_R99 = 0.01 (/millisecond): a kinetic parameter
	kf_R100 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R100 = 0.01 (/millisecond): a kinetic parameter
	kf_R101 = 0.01 (/millisecond): a kinetic parameter
	kf_R102 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R102 = 0.01 (/millisecond): a kinetic parameter
	kf_R103 = 0.01 (/millisecond): a kinetic parameter
	kf_R104 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R104 = 0.01 (/millisecond): a kinetic parameter
	kf_R105 = 0.01 (/millisecond): a kinetic parameter
	kf_R106 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R106 = 0.01 (/millisecond): a kinetic parameter
	kf_R107 = 0.01 (/millisecond): a kinetic parameter
	kf_R108 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R108 = 1e-06 (/millisecond): a kinetic parameter
	kf_R109 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R109 = 1e-06 (/millisecond): a kinetic parameter
	kf_R110 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R110 = 1e-06 (/millisecond): a kinetic parameter
	kf_R111 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R111 = 1e-06 (/millisecond): a kinetic parameter
	kf_R112 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R112 = 0.000400037 (/millisecond): a kinetic parameter
	kf_R113 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R113 = 0.0400037 (/millisecond): a kinetic parameter
	kf_R114 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R114 = 0.4 (/millisecond): a kinetic parameter
	kf_R115 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R115 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R116 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R116 = 0.01 (/millisecond): a kinetic parameter
	kf_R117 = 8.00018e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R117 = 0.001 (/millisecond): a kinetic parameter
	kf_R118 = 0.001 (/millisecond): a kinetic parameter
	kf_R119 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R120 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R120 = 0.0400037 (/millisecond): a kinetic parameter
	kf_R121 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R121 = 0.4 (/millisecond): a kinetic parameter
	kf_R122 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R122 = 4 (/millisecond): a kinetic parameter
	kf_R123 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R123 = 0.1 (/millisecond): a kinetic parameter
	kf_R124 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R124 = 0.00199986 (/millisecond): a kinetic parameter
	kf_R125 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R125 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R126 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R126 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R127 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R127 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R128 = 0.000500035 (/millisecond): a kinetic parameter
	kr_R128 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R129 = 1e-06 (/millisecond): a kinetic parameter
	kr_R129 = 0.000500035 (/millisecond): a kinetic parameter
	kf_R130 = 3.59998e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R130 = 0.0229985 (/millisecond): a kinetic parameter
	kf_R131 = 0.00390032 (/millisecond): a kinetic parameter
	kf_R132 = 1.10002e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R132 = 0.00540008 (/millisecond): a kinetic parameter
	kf_R133 = 10 (/millisecond): a kinetic parameter
	kf_R134 = 3.59998e-07 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R134 = 0.0229985 (/millisecond): a kinetic parameter
	kf_R135 = 0.00390032 (/millisecond): a kinetic parameter
	kf_R136 = 1.10002e-06 (/nanomole/liter-millisecond): a kinetic parameter
	kr_R136 = 0.00540008 (/millisecond): a kinetic parameter
	kf_R137 = 10 (/millisecond): a kinetic parameter
	DA_start  = 100 (millisecond) : an input
	DA_max  = 1480 (nanomole/liter) : an input
}
ASSIGNED {
	cai (millimolarity): Ca concentration from NMDA channels 
	time (millisecond) : alias for t
	ATP_expression : a pre-defined algebraic expression
	Ca_expression : a pre-defined algebraic expression
	DA_expression : a pre-defined algebraic expression
	AMP : a pre-defined algebraic expression
	ATP : a pre-defined algebraic expression
	Ca : a pre-defined algebraic expression
	DA : a pre-defined algebraic expression
	ReactionFlux0 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux1 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux2 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux3 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux4 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux5 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux6 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux7 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux8 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux9 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux10 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux11 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux12 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux13 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux14 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux15 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux16 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux17 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux18 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux19 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux20 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux21 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux22 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux23 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux24 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux25 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux26 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux27 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux28 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux29 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux30 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux31 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux32 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux33 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux34 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux35 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux36 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux37 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux38 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux39 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux40 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux41 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux42 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux43 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux44 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux45 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux46 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux47 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux48 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux49 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux50 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux51 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux52 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux53 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux54 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux55 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux56 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux57 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux58 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux59 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux60 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux61 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux62 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux63 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux64 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux65 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux66 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux67 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux68 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux69 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux70 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux71 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux72 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux73 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux74 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux75 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux76 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux77 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux78 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux79 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux80 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux81 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux82 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux83 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux84 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux85 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux86 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux87 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux88 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux89 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux90 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux91 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux92 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux93 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux94 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux95 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux96 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux97 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux98 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux99 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux100 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux101 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux102 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux103 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux104 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux105 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux106 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux107 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux108 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux109 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux110 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux111 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux112 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux113 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux114 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux115 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux116 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux117 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux118 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux119 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux120 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux121 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux122 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux123 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux124 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux125 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux126 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux127 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux128 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux129 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux130 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux131 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux132 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux133 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux134 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux135 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux136 : a flux, for use in DERIVATIVE mechanism
	ReactionFlux137 : a flux, for use in DERIVATIVE mechanism
	pSubstrate_out : an observable
	PP1_out : an observable
	CaM_out : an observable
	D32_out : an observable
	total_CaMKII_activated_out : an observable
}
PROCEDURE assign_calculated_values() {
	time = t : an alias for the time variable, if needed.
	ATP_expression = 5000000 : assignment for expression EX0
	Ca_expression = 0 : assignment for expression EX1
	DA_expression = DA_basal+(1/(1+exp((-10E+10)*(time-DA_start)))*(DA_max/(exp(-tau_DA1*tau_DA2/(tau_DA2-tau_DA1)*log(tau_DA2/tau_DA1)/tau_DA1)-exp(-tau_DA1*tau_DA2/(tau_DA2-tau_DA1)*log(tau_DA2/tau_DA1)/tau_DA2))*(exp(-(time-DA_start)/tau_DA1)-exp(-(time-DA_start)/tau_DA2)))) : assignment for expression EX2
	AMP = 0 : assignment for expression S8
	ATP = 5e+06 : assignment for expression S9
	Ca = cai*(1e6) : assignment for expression S24
	DA = DA_expression : assignment for expression S47
	ReactionFlux0 = kf_R0*GaolfGTP : flux expression R0
	ReactionFlux1 = kf_R1*D1R_Golf_DA : flux expression R1
	ReactionFlux2 = kf_R2*D1R_Golf*DA-kr_R2*D1R_Golf_DA : flux expression R2
	ReactionFlux3 = kf_R3*D1R*DA-kr_R3*D1R_DA : flux expression R3
	ReactionFlux4 = kf_R4*AC5*GaolfGTP-kr_R4*AC5_GaolfGTP : flux expression R4
	ReactionFlux5 = kf_R5*CaM*Ca-kr_R5*CaM_Ca2 : flux expression R5
	ReactionFlux6 = kf_R6*PP2B*CaM-kr_R6*PP2B_CaM : flux expression R6
	ReactionFlux7 = kf_R7*CaM_Ca4*PP2B-kr_R7*PP2Bc : flux expression R7
	ReactionFlux8 = kf_R8*PKAc*D32-kr_R8*PKAc_D32 : flux expression R8
	ReactionFlux9 = kf_R9*PKAc_D32 : flux expression R9
	ReactionFlux10 = kf_R10*PKAc*B56PP2A-kr_R10*PKAc_B56PP2A : flux expression R10
	ReactionFlux11 = kf_R11*PKAc_B56PP2A : flux expression R11
	ReactionFlux12 = kf_R12*D32p34*PP1-kr_R12*PP1_D32p34 : flux expression R12
	ReactionFlux13 = kf_R13*CDK5*D32-kr_R13*CDK5_D32 : flux expression R13
	ReactionFlux14 = kf_R14*CDK5_D32 : flux expression R14
	ReactionFlux15 = kf_R15*D32p75*PKAc-kr_R15*PKAc_D32p75 : flux expression R15
	ReactionFlux16 = kf_R16*B72PP2A*Ca-kr_R16*B72PP2A_Ca : flux expression R16
	ReactionFlux17 = kf_R17*B56PP2Ap*D32p75-kr_R17*B56PP2Ap_D32p75 : flux expression R17
	ReactionFlux18 = kf_R18*B72PP2A*D32p75-kr_R18*B72PP2A_D32p75 : flux expression R18
	ReactionFlux19 = kf_R19*D32p75*B72PP2A_Ca-kr_R19*B72PP2A_Ca_D32p75 : flux expression R19
	ReactionFlux20 = kf_R20*B56PP2Ap_D32p75 : flux expression R20
	ReactionFlux21 = kf_R21*B72PP2A_D32p75 : flux expression R21
	ReactionFlux22 = kf_R22*B72PP2A_Ca_D32p75 : flux expression R22
	ReactionFlux23 = kf_R23*D32p34*PP2Bc-kr_R23*PP2Bc_D32p34 : flux expression R23
	ReactionFlux24 = kf_R24*CaM_Ca2*Ca-kr_R24*CaM_Ca4 : flux expression R24
	ReactionFlux25 = kf_R25*Ca*PP2B_CaM-kr_R25*PP2B_CaM_Ca2 : flux expression R25
	ReactionFlux26 = kf_R26*Ca*PP2B_CaM_Ca2-kr_R26*PP2Bc : flux expression R26
	ReactionFlux27 = kf_R27*CaM_Ca2*PP2B-kr_R27*PP2B_CaM_Ca2 : flux expression R27
	ReactionFlux28 = kf_R28*AC5*Ca-kr_R28*AC5_Ca : flux expression R28
	ReactionFlux29 = kf_R29*AC5_Ca*GaolfGTP-kr_R29*AC5_Ca_GaolfGTP : flux expression R29
	ReactionFlux30 = kf_R30*D32p75*B56PP2A-kr_R30*B56PP2A_D32p75 : flux expression R30
	ReactionFlux31 = kf_R31*B56PP2A_D32p75 : flux expression R31
	ReactionFlux32 = kf_R32*B72PP2A_Ca_D32p34 : flux expression R32
	ReactionFlux33 = kf_R33*B72PP2A_D32p34 : flux expression R33
	ReactionFlux34 = kf_R34*D32p34*B72PP2A_Ca-kr_R34*B72PP2A_Ca_D32p34 : flux expression R34
	ReactionFlux35 = kf_R35*D32p34*B72PP2A-kr_R35*B72PP2A_D32p34 : flux expression R35
	ReactionFlux36 = kf_R36*PP2Bc_D32p34 : flux expression R36
	ReactionFlux37 = kf_R37*B56PP2Ap : flux expression R37
	ReactionFlux38 = kf_R38*cAMP*PKA-kr_R38*PKA_Ca2MP : flux expression R38
	ReactionFlux39 = kf_R39*cAMP*PKA_Ca2MP-kr_R39*PKA_Ca4MP : flux expression R39
	ReactionFlux40 = kf_R40*PKA_Ca4MP-kr_R40*PKAc*PKAreg : flux expression R40
	ReactionFlux41 = kf_R41*cAMP*PDE4-kr_R41*PDE4_cAMP : flux expression R41
	ReactionFlux42 = kf_R42*PDE4_cAMP : flux expression R42
	ReactionFlux43 = kf_R43*PDE10r*cAMP^2-kr_R43*PDE10c : flux expression R43
	ReactionFlux44 = kf_R44*PDE10r_cAMP : flux expression R44
	ReactionFlux45 = kf_R45*cAMP*PDE10r-kr_R45*PDE10r_cAMP : flux expression R45
	ReactionFlux46 = kf_R46*PDE10c_cAMP : flux expression R46
	ReactionFlux47 = kf_R47*GaolfGDP*Gbgolf : flux expression R47
	ReactionFlux48 = kf_R48*AC5_GaolfGTP*ATP-kr_R48*AC5_GaolfGTP_ATP : flux expression R48
	ReactionFlux49 = kf_R49*AC5*ATP-kr_R49*AC5_ATP : flux expression R49
	ReactionFlux50 = kf_R50*AC5_Ca*ATP-kr_R50*AC5_Ca_ATP : flux expression R50
	ReactionFlux51 = kf_R51*AC5_Ca_GaolfGTP*ATP-kr_R51*AC5_Ca_GaolfGTP_ATP : flux expression R51
	ReactionFlux52 = kf_R52*GaolfGTP*AC5_ATP-kr_R52*AC5_GaolfGTP_ATP : flux expression R52
	ReactionFlux53 = kf_R53*GaolfGTP*AC5_Ca_ATP-kr_R53*AC5_Ca_GaolfGTP_ATP : flux expression R53
	ReactionFlux54 = kf_R54*Ca*AC5_ATP-kr_R54*AC5_Ca_ATP : flux expression R54
	ReactionFlux55 = kf_R55*AC5_GaolfGTP_ATP : flux expression R55
	ReactionFlux56 = kf_R56*cAMP*AC5_GaolfGTP : flux expression R56
	ReactionFlux57 = kf_R57*AC5_ATP : flux expression R57
	ReactionFlux58 = kf_R58*cAMP*AC5 : flux expression R58
	ReactionFlux59 = kf_R59*AC5_Ca_ATP : flux expression R59
	ReactionFlux60 = kf_R60*cAMP*AC5_Ca : flux expression R60
	ReactionFlux61 = kf_R61*AC5_Ca_GaolfGTP_ATP : flux expression R61
	ReactionFlux62 = kf_R62*cAMP*AC5_Ca_GaolfGTP : flux expression R62
	ReactionFlux63 = kf_R63*AC5_GaolfGTP : flux expression R63
	ReactionFlux64 = kf_R64*AC5_Ca_GaolfGTP : flux expression R64
	ReactionFlux65 = kf_R65*AC5_GaolfGTP_ATP : flux expression R65
	ReactionFlux66 = kf_R66*AC5_Ca_GaolfGTP_ATP : flux expression R66
	ReactionFlux67 = kf_R67*D1R*Golf-kr_R67*D1R_Golf : flux expression R67
	ReactionFlux68 = kf_R68*Golf*D1R_DA-kr_R68*D1R_Golf_DA : flux expression R68
	ReactionFlux69 = kf_R69*cAMP*PDE10c-kr_R69*PDE10c_cAMP : flux expression R69
	ReactionFlux70 = kf_R70*CaMKII*CaM_Ca4-kr_R70*CaMKII_CaM_Ca4 : flux expression R70
	ReactionFlux71 = kf_R71*CaM_Ca2*CaMKII-kr_R71*CaMKII_CaM_Ca2 : flux expression R71
	ReactionFlux72 = kf_R72*CaM*CaMKII-kr_R72*CaMKII_CaM : flux expression R72
	ReactionFlux73 = kf_R73*CaMKII_CaM_Ca2*Ca-kr_R73*CaMKII_CaM_Ca4 : flux expression R73
	ReactionFlux74 = kf_R74*CaMKII_CaM*Ca-kr_R74*CaMKII_CaM_Ca2 : flux expression R74
	ReactionFlux75 = kf_R75*pCaMKII_CaM_Ca2*Ca-kr_R75*pCaMKII_CaM_Ca4 : flux expression R75
	ReactionFlux76 = kf_R76*pCaMKII_CaM*Ca-kr_R76*pCaMKII_CaM_Ca2 : flux expression R76
	ReactionFlux77 = kf_R77*pCaMKII*CaM_Ca4-kr_R77*pCaMKII_CaM_Ca4 : flux expression R77
	ReactionFlux78 = kf_R78*pCaMKII*CaM_Ca2-kr_R78*pCaMKII_CaM_Ca2 : flux expression R78
	ReactionFlux79 = kf_R79*pCaMKII*CaM-kr_R79*pCaMKII_CaM : flux expression R79
	ReactionFlux80 = kf_R80*ARPP21*PKAc-kr_R80*PKAc_ARPP21 : flux expression R80
	ReactionFlux81 = kf_R81*PKAc_ARPP21 : flux expression R81
	ReactionFlux82 = kf_R82*pARPP21*CaM_Ca4-kr_R82*CaM_Ca4_pARPP21 : flux expression R82
	ReactionFlux83 = kf_R83*B72PP2A_Ca_pARPP21 : flux expression R83
	ReactionFlux84 = kf_R84*pARPP21*B72PP2A_Ca-kr_R84*B72PP2A_Ca_pARPP21 : flux expression R84
	ReactionFlux85 = kf_R85*B72PP2A_pARPP21 : flux expression R85
	ReactionFlux86 = kf_R86*pARPP21*B72PP2A-kr_R86*B72PP2A_pARPP21 : flux expression R86
	ReactionFlux87 = kf_R87*B56PP2Ap_pARPP21 : flux expression R87
	ReactionFlux88 = kf_R88*pARPP21*B56PP2Ap-kr_R88*B56PP2Ap_pARPP21 : flux expression R88
	ReactionFlux89 = kf_R89*B56PP2A_pARPP21 : flux expression R89
	ReactionFlux90 = kf_R90*pARPP21*B56PP2A-kr_R90*B56PP2A_pARPP21 : flux expression R90
	ReactionFlux91 = kf_R91*pSubstrate*PP1-kr_R91*PP1_pSubstrate : flux expression R91
	ReactionFlux92 = kf_R92*PP1_pSubstrate : flux expression R92
	ReactionFlux93 = kf_R93*Substrate*pCaMKII_psd-kr_R93*pCaMKII_psd_Substrate : flux expression R93
	ReactionFlux94 = kf_R94*pCaMKII_psd_Substrate : flux expression R94
	ReactionFlux95 = kf_R95*pCaMKII : flux expression R95
	ReactionFlux96 = kf_R96*Substrate*pCaMKII_CaM_psd-kr_R96*pCaMKII_CaM_psd_Substrate : flux expression R96
	ReactionFlux97 = kf_R97*pCaMKII_CaM_psd_Substrate : flux expression R97
	ReactionFlux98 = kf_R98*Substrate*pCaMKII_CaM_Ca2_psd-kr_R98*pCaMKII_CaM_Ca2_psd_Substrate : flux expression R98
	ReactionFlux99 = kf_R99*pCaMKII_CaM_Ca2_psd_Substrate : flux expression R99
	ReactionFlux100 = kf_R100*Substrate*pCaMKII_CaM_Ca4_psd-kr_R100*pCaMKII_CaM_Ca4_psd_Substrate : flux expression R100
	ReactionFlux101 = kf_R101*pCaMKII_CaM_Ca4_psd_Substrate : flux expression R101
	ReactionFlux102 = kf_R102*Substrate*CaMKII_CaM_psd-kr_R102*CaMKII_CaM_psd_Substrate : flux expression R102
	ReactionFlux103 = kf_R103*CaMKII_CaM_psd_Substrate : flux expression R103
	ReactionFlux104 = kf_R104*Substrate*CaMKII_CaM_Ca2_psd-kr_R104*CaMKII_CaM_Ca2_psd_Substrate : flux expression R104
	ReactionFlux105 = kf_R105*CaMKII_CaM_Ca2_psd_Substrate : flux expression R105
	ReactionFlux106 = kf_R106*Substrate*CaMKII_CaM_Ca4_psd-kr_R106*CaMKII_CaM_Ca4_psd_Substrate : flux expression R106
	ReactionFlux107 = kf_R107*CaMKII_CaM_Ca4_psd_Substrate : flux expression R107
	ReactionFlux108 = kf_R108*pCaMKII_CaM_Ca4-kr_R108*pCaMKII_CaM_Ca4_psd : flux expression R108
	ReactionFlux109 = kf_R109*pCaMKII_CaM_Ca2-kr_R109*pCaMKII_CaM_Ca2_psd : flux expression R109
	ReactionFlux110 = kf_R110*pCaMKII_CaM-kr_R110*pCaMKII_CaM_psd : flux expression R110
	ReactionFlux111 = kf_R111*pCaMKII-kr_R111*pCaMKII_psd : flux expression R111
	ReactionFlux112 = kf_R112*CaM_Ca4*pCaMKII_psd-kr_R112*pCaMKII_CaM_Ca4_psd : flux expression R112
	ReactionFlux113 = kf_R113*pCaMKII_psd*CaM_Ca2-kr_R113*pCaMKII_CaM_Ca2_psd : flux expression R113
	ReactionFlux114 = kf_R114*CaM*pCaMKII_psd-kr_R114*pCaMKII_CaM_psd : flux expression R114
	ReactionFlux115 = kf_R115*pCaMKII_CaM_psd*Ca-kr_R115*pCaMKII_CaM_Ca2_psd : flux expression R115
	ReactionFlux116 = kf_R116*pCaMKII_CaM_Ca2_psd*Ca-kr_R116*pCaMKII_CaM_Ca4_psd : flux expression R116
	ReactionFlux117 = kf_R117*pCaMKII_psd*PP1-kr_R117*PP1_pCaMKII_psd : flux expression R117
	ReactionFlux118 = kf_R118*PP1_pCaMKII_psd : flux expression R118
	ReactionFlux119 = kf_R119*CaMKII_psd : flux expression R119
	ReactionFlux120 = kf_R120*CaM_Ca4*CaMKII_psd-kr_R120*CaMKII_CaM_Ca4_psd : flux expression R120
	ReactionFlux121 = kf_R121*CaM_Ca2*CaMKII_psd-kr_R121*CaMKII_CaM_Ca2_psd : flux expression R121
	ReactionFlux122 = kf_R122*CaM*CaMKII_psd-kr_R122*CaMKII_CaM_psd : flux expression R122
	ReactionFlux123 = kf_R123*CaMKII_CaM_Ca2_psd*Ca-kr_R123*CaMKII_CaM_Ca4_psd : flux expression R123
	ReactionFlux124 = kf_R124*CaMKII_CaM_psd*Ca-kr_R124*CaMKII_CaM_Ca2_psd : flux expression R124
	ReactionFlux125 = kf_R125*CaMKII_CaM-kr_R125*CaMKII_CaM_psd : flux expression R125
	ReactionFlux126 = kf_R126*CaMKII_CaM_Ca2-kr_R126*CaMKII_CaM_Ca2_psd : flux expression R126
	ReactionFlux127 = kf_R127*CaMKII_CaM_Ca4-kr_R127*CaMKII_CaM_Ca4_psd : flux expression R127
	ReactionFlux128 = kf_R128*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd-kr_R128*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R128
	ReactionFlux129 = kf_R129*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd-kr_R129*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R129
	ReactionFlux130 = kf_R130*CaMKII_CaM_Ca4*CaMKII_CaM_Ca4-kr_R130*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R130
	ReactionFlux131 = kf_R131*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R131
	ReactionFlux132 = kf_R132*pCaMKII_CaM_Ca4*CaMKII_CaM_Ca4-kr_R132*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R132
	ReactionFlux133 = kf_R133*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R133
	ReactionFlux134 = kf_R134*CaMKII_CaM_Ca4_psd*CaMKII_CaM_Ca4_psd-kr_R134*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R134
	ReactionFlux135 = kf_R135*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R135
	ReactionFlux136 = kf_R136*pCaMKII_CaM_Ca4_psd*CaMKII_CaM_Ca4_psd-kr_R136*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R136
	ReactionFlux137 = kf_R137*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R137
	total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate

}
STATE {
	AC5 (nanomole/liter) : a state variable
	AC5_ATP (nanomole/liter) : a state variable
	AC5_Ca (nanomole/liter) : a state variable
	AC5_Ca_ATP (nanomole/liter) : a state variable
	AC5_Ca_GaolfGTP (nanomole/liter) : a state variable
	AC5_Ca_GaolfGTP_ATP (nanomole/liter) : a state variable
	AC5_GaolfGTP (nanomole/liter) : a state variable
	AC5_GaolfGTP_ATP (nanomole/liter) : a state variable
	B56PP2A (nanomole/liter) : a state variable
	B56PP2A_D32p75 (nanomole/liter) : a state variable
	B56PP2A_pARPP21 (nanomole/liter) : a state variable
	B56PP2Ap (nanomole/liter) : a state variable
	B56PP2Ap_D32p75 (nanomole/liter) : a state variable
	B56PP2Ap_pARPP21 (nanomole/liter) : a state variable
	B72PP2A (nanomole/liter) : a state variable
	B72PP2A_D32p34 (nanomole/liter) : a state variable
	B72PP2A_D32p75 (nanomole/liter) : a state variable
	B72PP2A_pARPP21 (nanomole/liter) : a state variable
	B72PP2A_Ca_D32p34 (nanomole/liter) : a state variable
	B72PP2A_Ca_D32p75 (nanomole/liter) : a state variable
	B72PP2A_Ca (nanomole/liter) : a state variable
	B72PP2A_Ca_pARPP21 (nanomole/liter) : a state variable
	CaM (nanomole/liter) : a state variable
	CaM_Ca2 (nanomole/liter) : a state variable
	CaM_Ca4 (nanomole/liter) : a state variable
	CaM_Ca4_pARPP21 (nanomole/liter) : a state variable
	CaMKII (nanomole/liter) : a state variable
	CaMKII_CaM_Ca4 (nanomole/liter) : a state variable
	CaMKII_CaM (nanomole/liter) : a state variable
	CaMKII_CaM_Ca2 (nanomole/liter) : a state variable
	CaMKII_CaM_Ca2_psd (nanomole/liter) : a state variable
	CaMKII_CaM_psd (nanomole/liter) : a state variable
	CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable
	CaMKII_psd (nanomole/liter) : a state variable
	cAMP (nanomole/liter) : a state variable
	Substrate (nanomole/liter) : a state variable
	CDK5 (nanomole/liter) : a state variable
	CDK5_D32 (nanomole/liter) : a state variable
	D1R (nanomole/liter) : a state variable
	D1R_DA (nanomole/liter) : a state variable
	D1R_Golf_DA (nanomole/liter) : a state variable
	D1R_Golf (nanomole/liter) : a state variable
	D32p34 (nanomole/liter) : a state variable
	D32p75 (nanomole/liter) : a state variable
	D32 (nanomole/liter) : a state variable
	GaolfGDP (nanomole/liter) : a state variable
	GaolfGTP (nanomole/liter) : a state variable
	Gbgolf (nanomole/liter) : a state variable
	Golf (nanomole/liter) : a state variable
	pCaMKII (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca4 (nanomole/liter) : a state variable
	pCaMKII_CaM (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca2 (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca2_psd (nanomole/liter) : a state variable
	pCaMKII_CaM_psd (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable
	pCaMKII_psd (nanomole/liter) : a state variable
	pSubstrate (nanomole/liter) : a state variable
	PDE4 (nanomole/liter) : a state variable
	PDE4_cAMP (nanomole/liter) : a state variable
	PDE10r (nanomole/liter) : a state variable
	PDE10r_cAMP (nanomole/liter) : a state variable
	PDE10c (nanomole/liter) : a state variable
	PDE10c_cAMP (nanomole/liter) : a state variable
	PKA (nanomole/liter) : a state variable
	PKAc (nanomole/liter) : a state variable
	PKAc_B56PP2A (nanomole/liter) : a state variable
	PKAc_D32 (nanomole/liter) : a state variable
	PKAc_ARPP21 (nanomole/liter) : a state variable
	PKA_Ca2MP (nanomole/liter) : a state variable
	PKA_Ca4MP (nanomole/liter) : a state variable
	PKAc_D32p75 (nanomole/liter) : a state variable
	PKAreg (nanomole/liter) : a state variable
	PP1 (nanomole/liter) : a state variable
	PP1_pCaMKII_psd (nanomole/liter) : a state variable
	PP1_pSubstrate (nanomole/liter) : a state variable
	PP1_D32p34 (nanomole/liter) : a state variable
	CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable
	CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 (nanomole/liter) : a state variable
	PP2B (nanomole/liter) : a state variable
	PP2Bc (nanomole/liter) : a state variable
	PP2Bc_D32p34 (nanomole/liter) : a state variable
	PP2B_CaM (nanomole/liter) : a state variable
	PP2B_CaM_Ca2 (nanomole/liter) : a state variable
	pARPP21 (nanomole/liter) : a state variable
	ARPP21 (nanomole/liter) : a state variable
	pCaMKII_psd_Substrate (nanomole/liter) : a state variable
	pCaMKII_CaM_psd_Substrate (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca2_psd_Substrate (nanomole/liter) : a state variable
	pCaMKII_CaM_Ca4_psd_Substrate (nanomole/liter) : a state variable
	CaMKII_CaM_psd_Substrate (nanomole/liter) : a state variable
	CaMKII_CaM_Ca2_psd_Substrate (nanomole/liter) : a state variable
	CaMKII_CaM_Ca4_psd_Substrate (nanomole/liter) : a state variable
	total_CaMKII_activated (nanomole/liter) : a state variable
}
INITIAL {
     AC5 = 2.6579740648536387
 	 AC5_ATP = 664.5955722158345
	 AC5_Ca = 0.011455491216440293
	 AC5_Ca_ATP = 2.8642831776146602 
	 AC5_Ca_GaolfGTP = 0.0005087730491145609 
	 AC5_Ca_GaolfGTP_ATP = 0.1276760000022537
	 AC5_GaolfGTP = 0.11762328938669141 
	 AC5_GaolfGTP_ATP = 29.624906977591287 
	 B56PP2A = 891.3882782297828 
	 B56PP2A_D32p75 = 773.8986890359638 
	 B56PP2A_pARPP21 = 22.004569833130333 
	 B56PP2Ap = 119.83225503696232
	 B56PP2Ap_D32p75 = 183.32968907852563 
	 B56PP2Ap_pARPP21 = 4.752784515174912
	 B72PP2A = 998.1762288155527
	 B72PP2A_D32p34 = 0.029586434857564403
	 B72PP2A_D32p75 = 866.6114349644631
	 B72PP2A_pARPP21 = 24.640708285240002
	 B72PP2A_Ca_D32p34 = 0.001275120308719799
	 B72PP2A_Ca_D32p75 = 65.81498998111533
	 B72PP2A_Ca = 43.01953875726838
	 B72PP2A_Ca_pARPP21 = 1.706240090303376
	 CaM = 3271.1613030579483
	 CaM_Ca2 = 42.30197029468885
	 CaM_Ca4 = 0.18232282358259608 
	 CaM_Ca4_pARPP21 = 5.682096670017442
	 CaMKII = 16861.31022167976
	 CaMKII_CaM_Ca4 = 7.653695787280561
	 CaMKII_CaM = 1378.7438408069913 
	 CaMKII_CaM_Ca2 = 178.1085180682959
	 CaMKII_CaM_Ca2_psd = 15.344587294726768
	 CaMKII_CaM_psd = 117.20636345254225 
	 CaMKII_CaM_Ca4_psd = 0.6836514096472648 
	 CaMKII_psd = 1431.2784425994976
	 cAMP = 38.077478703814286
	 Substrate = 2898.4324981645364
	 CDK5 = 1354.5983328435307 
	 CDK5_D32 = 445.4016679783238
	 D1R = 1476.965276006024
	 D1R_DA = 5.959513286613785
	 D1R_Golf_DA = 2.0091697499991463
	 D1R_Golf = 515.0660409549953
	 D32p34 = 0.23709844962796384
	 D32p75 = 11014.977244009184
	 D32 = 36168.79062206558
	 GaolfGDP = 0.010083118413574194
	 GaolfGTP = 0.008914911110695258
	 Gbgolf = 29.889710469343125
	 Golf = 1453.0350762349071
	 pCaMKII = 0.0026152322826163694
	 pCaMKII_CaM_Ca4 = 0.00041326366874510956
	 pCaMKII_CaM = 0.0021363473128570283
	 pCaMKII_CaM_Ca2 = 0.0003364074902532764
	 pCaMKII_CaM_Ca2_psd = 0.00029964701372417826
	 pCaMKII_CaM_psd = 0.00223880855203415 
	 pCaMKII_CaM_Ca4_psd = 0.00015640795348060934
	 pCaMKII_psd = 0.002734310759402372
	 pSubstrate = 82.25679040587481 
	 PDE4 = 1507.8595078954654
	 PDE4_cAMP = 492.1404908824553
	 PDE10r = 396.93707251699345 
	 PDE10r_cAMP = 302.30479218857784
 	 PDE10c = 0.5755168324209912 
	 PDE10c_cAMP = 0.1826207133266763
	 PKA = 1143.825553233938
	 PKAc = 2.6887584775003255 
	 PKAc_B56PP2A = 4.793733616212578 
	 PKAc_D32 = 4.630911543143565
	 PKAc_ARPP21 = 11.123552417073366
	 PKA_Ca2MP = 3.235620105419139 
	 PKA_Ca4MP = 0.08525605875534487
	 PKAc_D32p75 = 29.616613444303574 
	 PKAreg = 52.85356959978496 
	 PP1 = 2582.1938739416964 
	 PP1_pCaMKII_psd = 0.0028242717416327636
	 PP1_pSubstrate = 9.655356749304744
	 PP1_D32p34 = 408.14794647416636
	 CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 2.019451923560302e-05
	 pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 1.1773379671332063e-11 
	 CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 0.0007700483148596818
	 pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 3.4773054620114007e-10
	 PP2B = 26.730674733834796
	 PP2Bc = 162.45364687157698
	 PP2Bc_D32p34 = 38.512174821299965
	 PP2B_CaM = 2.9146880204369956
	 PP2B_CaM_Ca2 = 3769.3888179670294
	 pARPP21 = 623.2570162577764
	 ARPP21 = 19306.833014960313
	 pCaMKII_psd_Substrate = 0.00019814424825483155
	 pCaMKII_CaM_psd_Substrate = 0.00016223724242164732
	 pCaMKII_CaM_Ca2_psd_Substrate = 2.1714185950523916e-05
	 pCaMKII_CaM_Ca4_psd_Substrate = 1.133424072480528e-05
	 CaMKII_CaM_psd_Substrate = 8.493462821347531 
	 CaMKII_CaM_Ca2_psd_Substrate = 1.11195909383754
	 CaMKII_CaM_Ca4_psd_Substrate = 0.04954140423400814
	 total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate

}
BREAKPOINT {
	SOLVE ode METHOD cnexp
	assign_calculated_values() : procedure
}
DERIVATIVE ode {
	AC5' = -ReactionFlux4-ReactionFlux28-ReactionFlux49+ReactionFlux57-ReactionFlux58+ReactionFlux63 : affects compound with ID S0
	AC5_ATP' = ReactionFlux49-ReactionFlux52-ReactionFlux54-ReactionFlux57+ReactionFlux58+ReactionFlux65 : affects compound with ID S1
	AC5_Ca' = ReactionFlux28-ReactionFlux29-ReactionFlux50+ReactionFlux59-ReactionFlux60+ReactionFlux64 : affects compound with ID S2
	AC5_Ca_ATP' = ReactionFlux50-ReactionFlux53+ReactionFlux54-ReactionFlux59+ReactionFlux60+ReactionFlux66 : affects compound with ID S3
	AC5_Ca_GaolfGTP' = ReactionFlux29-ReactionFlux51+ReactionFlux61-ReactionFlux62-ReactionFlux64 : affects compound with ID S4
	AC5_Ca_GaolfGTP_ATP' = ReactionFlux51+ReactionFlux53-ReactionFlux61+ReactionFlux62-ReactionFlux66 : affects compound with ID S5
	AC5_GaolfGTP' = ReactionFlux4-ReactionFlux48+ReactionFlux55-ReactionFlux56-ReactionFlux63 : affects compound with ID S6
	AC5_GaolfGTP_ATP' = ReactionFlux48+ReactionFlux52-ReactionFlux55+ReactionFlux56-ReactionFlux65 : affects compound with ID S7
	B56PP2A' = -ReactionFlux10-ReactionFlux30+ReactionFlux31+ReactionFlux37+ReactionFlux89-ReactionFlux90 : affects compound with ID S10
	B56PP2A_D32p75' = ReactionFlux30-ReactionFlux31 : affects compound with ID S11
	B56PP2A_pARPP21' = -ReactionFlux89+ReactionFlux90 : affects compound with ID S12
	B56PP2Ap' = ReactionFlux11-ReactionFlux17+ReactionFlux20-ReactionFlux37+ReactionFlux87-ReactionFlux88 : affects compound with ID S13
	B56PP2Ap_D32p75' = ReactionFlux17-ReactionFlux20 : affects compound with ID S14
	B56PP2Ap_pARPP21' = -ReactionFlux87+ReactionFlux88 : affects compound with ID S15
	B72PP2A' = -ReactionFlux16-ReactionFlux18+ReactionFlux21+ReactionFlux33-ReactionFlux35+ReactionFlux85-ReactionFlux86 : affects compound with ID S16
	B72PP2A_D32p34' = -ReactionFlux33+ReactionFlux35 : affects compound with ID S17
	B72PP2A_D32p75' = ReactionFlux18-ReactionFlux21 : affects compound with ID S18
	B72PP2A_pARPP21' = -ReactionFlux85+ReactionFlux86 : affects compound with ID S19
	B72PP2A_Ca_D32p34' = -ReactionFlux32+ReactionFlux34 : affects compound with ID S20
	B72PP2A_Ca_D32p75' = ReactionFlux19-ReactionFlux22 : affects compound with ID S21
	B72PP2A_Ca' = ReactionFlux16-ReactionFlux19+ReactionFlux22+ReactionFlux32-ReactionFlux34+ReactionFlux83-ReactionFlux84 : affects compound with ID S22
	B72PP2A_Ca_pARPP21' = -ReactionFlux83+ReactionFlux84 : affects compound with ID S23
	CaM' = -ReactionFlux5-ReactionFlux6-ReactionFlux72-ReactionFlux79-ReactionFlux114-ReactionFlux122 : affects compound with ID S25
	CaM_Ca2' = ReactionFlux5-ReactionFlux24-ReactionFlux27-ReactionFlux71-ReactionFlux78-ReactionFlux113-ReactionFlux121 : affects compound with ID S26
	CaM_Ca4' = -ReactionFlux7+ReactionFlux24-ReactionFlux70-ReactionFlux77-ReactionFlux82-ReactionFlux112-ReactionFlux120 : affects compound with ID S27
	CaM_Ca4_pARPP21' = ReactionFlux82 : affects compound with ID S28
	CaMKII' = -ReactionFlux70-ReactionFlux71-ReactionFlux72+ReactionFlux95+ReactionFlux119 : affects compound with ID S29
	CaMKII_CaM_Ca4' = ReactionFlux70+ReactionFlux73-ReactionFlux127-ReactionFlux130-ReactionFlux130+ReactionFlux131-ReactionFlux132 : affects compound with ID S30
	CaMKII_CaM' = ReactionFlux72-ReactionFlux74-ReactionFlux125 : affects compound with ID S31
	CaMKII_CaM_Ca2' = ReactionFlux71-ReactionFlux73+ReactionFlux74-ReactionFlux126 : affects compound with ID S32
	CaMKII_CaM_Ca2_psd' = -ReactionFlux104+ReactionFlux105+ReactionFlux121-ReactionFlux123+ReactionFlux124+ReactionFlux126 : affects compound with ID S33
	CaMKII_CaM_psd' = -ReactionFlux102+ReactionFlux103+ReactionFlux122-ReactionFlux124+ReactionFlux125 : affects compound with ID S34
	CaMKII_CaM_Ca4_psd' = -ReactionFlux106+ReactionFlux107+ReactionFlux120+ReactionFlux123+ReactionFlux127-ReactionFlux134-ReactionFlux134+ReactionFlux135-ReactionFlux136 : affects compound with ID S35
	CaMKII_psd' = ReactionFlux118-ReactionFlux119-ReactionFlux120-ReactionFlux121-ReactionFlux122 : affects compound with ID S36
	cAMP' = -ReactionFlux38-ReactionFlux39-ReactionFlux41-2*ReactionFlux43-ReactionFlux45+ReactionFlux55-ReactionFlux56+ReactionFlux57-ReactionFlux58+ReactionFlux59-ReactionFlux60+ReactionFlux61-ReactionFlux62-ReactionFlux69 : affects compound with ID S37
	Substrate' = ReactionFlux92-ReactionFlux93-ReactionFlux96-ReactionFlux98-ReactionFlux100-ReactionFlux102-ReactionFlux104-ReactionFlux106 : affects compound with ID S38
	CDK5' = -ReactionFlux13+ReactionFlux14 : affects compound with ID S39
	CDK5_D32' = ReactionFlux13-ReactionFlux14 : affects compound with ID S40
	D1R' = -ReactionFlux3-ReactionFlux67 : affects compound with ID S41
	D1R_DA' = ReactionFlux1+ReactionFlux3-ReactionFlux68 : affects compound with ID S42
	D1R_Golf_DA' = -ReactionFlux1+ReactionFlux2+ReactionFlux68 : affects compound with ID S43
	D1R_Golf' = -ReactionFlux2+ReactionFlux67 : affects compound with ID S44
	D32p34' = ReactionFlux9-ReactionFlux12-ReactionFlux23-ReactionFlux34-ReactionFlux35 : affects compound with ID S45
	D32p75' = ReactionFlux14-ReactionFlux15-ReactionFlux17-ReactionFlux18-ReactionFlux19-ReactionFlux30 : affects compound with ID S46
	D32' = -ReactionFlux8-ReactionFlux13+ReactionFlux20+ReactionFlux21+ReactionFlux22+ReactionFlux31+ReactionFlux32+ReactionFlux33+ReactionFlux36 : affects compound with ID S48
	GaolfGDP' = ReactionFlux0-ReactionFlux47+ReactionFlux63+ReactionFlux64+ReactionFlux65+ReactionFlux66 : affects compound with ID S49
	GaolfGTP' = -ReactionFlux0+ReactionFlux1-ReactionFlux4-ReactionFlux29-ReactionFlux52-ReactionFlux53 : affects compound with ID S50
	Gbgolf' = ReactionFlux1-ReactionFlux47 : affects compound with ID S51
	Golf' = ReactionFlux47-ReactionFlux67-ReactionFlux68 : affects compound with ID S52
	pCaMKII' = -ReactionFlux77-ReactionFlux78-ReactionFlux79-ReactionFlux95-ReactionFlux111 : affects compound with ID S53
	pCaMKII_CaM_Ca4' = ReactionFlux75+ReactionFlux77-ReactionFlux108+ReactionFlux131-ReactionFlux132+ReactionFlux133+ReactionFlux133 : affects compound with ID S54
	pCaMKII_CaM' = -ReactionFlux76+ReactionFlux79-ReactionFlux110 : affects compound with ID S55
	pCaMKII_CaM_Ca2' = -ReactionFlux75+ReactionFlux76+ReactionFlux78-ReactionFlux109 : affects compound with ID S56
	pCaMKII_CaM_Ca2_psd' = -ReactionFlux98+ReactionFlux99+ReactionFlux109+ReactionFlux113+ReactionFlux115-ReactionFlux116 : affects compound with ID S57
	pCaMKII_CaM_psd' = -ReactionFlux96+ReactionFlux97+ReactionFlux110+ReactionFlux114-ReactionFlux115 : affects compound with ID S58
	pCaMKII_CaM_Ca4_psd' = -ReactionFlux100+ReactionFlux101+ReactionFlux108+ReactionFlux112+ReactionFlux116+ReactionFlux135-ReactionFlux136+ReactionFlux137+ReactionFlux137 : affects compound with ID S59
	pCaMKII_psd' = -ReactionFlux93+ReactionFlux94+ReactionFlux111-ReactionFlux112-ReactionFlux113-ReactionFlux114-ReactionFlux117 : affects compound with ID S60
	pSubstrate' = -ReactionFlux91+ReactionFlux94+ReactionFlux97+ReactionFlux99+ReactionFlux101+ReactionFlux103+ReactionFlux105+ReactionFlux107 : affects compound with ID S61
	PDE4' = -ReactionFlux41+ReactionFlux42 : affects compound with ID S62
	PDE4_cAMP' = ReactionFlux41-ReactionFlux42 : affects compound with ID S63
	PDE10r' = -ReactionFlux43+ReactionFlux44-ReactionFlux45 : affects compound with ID S64
	PDE10r_cAMP' = -ReactionFlux44+ReactionFlux45 : affects compound with ID S65
	PDE10c' = ReactionFlux43+ReactionFlux46-ReactionFlux69 : affects compound with ID S66
	PDE10c_cAMP' = -ReactionFlux46+ReactionFlux69 : affects compound with ID S67
	PKA' = -ReactionFlux38 : affects compound with ID S68
	PKAc' = -ReactionFlux8+ReactionFlux9-ReactionFlux10+ReactionFlux11-ReactionFlux15+ReactionFlux40-ReactionFlux80+ReactionFlux81 : affects compound with ID S69
	PKAc_B56PP2A' = ReactionFlux10-ReactionFlux11 : affects compound with ID S70
	PKAc_D32' = ReactionFlux8-ReactionFlux9 : affects compound with ID S71
	PKAc_ARPP21' = ReactionFlux80-ReactionFlux81 : affects compound with ID S72
	PKA_Ca2MP' = ReactionFlux38-ReactionFlux39 : affects compound with ID S73
	PKA_Ca4MP' = ReactionFlux39-ReactionFlux40 : affects compound with ID S74
	PKAc_D32p75' = ReactionFlux15 : affects compound with ID S75
	PKAreg' = ReactionFlux40 : affects compound with ID S76
	PP1' = -ReactionFlux12-ReactionFlux91+ReactionFlux92-ReactionFlux117+ReactionFlux118 : affects compound with ID S77
	PP1_pCaMKII_psd' = ReactionFlux117-ReactionFlux118 : affects compound with ID S78
	PP1_pSubstrate' = ReactionFlux91-ReactionFlux92 : affects compound with ID S79
	PP1_D32p34' = ReactionFlux12 : affects compound with ID S80
	CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd' = -ReactionFlux128+ReactionFlux134-ReactionFlux135 : affects compound with ID S81
	pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd' = -ReactionFlux129+ReactionFlux136-ReactionFlux137 : affects compound with ID S82
	CaMKII_CaM_Ca4_CaMKII_CaM_Ca4' = ReactionFlux128+ReactionFlux130-ReactionFlux131 : affects compound with ID S83
	pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4' = ReactionFlux129+ReactionFlux132-ReactionFlux133 : affects compound with ID S84
	PP2B' = -ReactionFlux6-ReactionFlux7-ReactionFlux27 : affects compound with ID S85
	PP2Bc' = ReactionFlux7-ReactionFlux23+ReactionFlux26+ReactionFlux36 : affects compound with ID S86
	PP2Bc_D32p34' = ReactionFlux23-ReactionFlux36 : affects compound with ID S87
	PP2B_CaM' = ReactionFlux6-ReactionFlux25 : affects compound with ID S88
	PP2B_CaM_Ca2' = ReactionFlux25-ReactionFlux26+ReactionFlux27 : affects compound with ID S89
	pARPP21' = ReactionFlux81-ReactionFlux82-ReactionFlux84-ReactionFlux86-ReactionFlux88-ReactionFlux90 : affects compound with ID S90
	ARPP21' = -ReactionFlux80+ReactionFlux83+ReactionFlux85+ReactionFlux87+ReactionFlux89 : affects compound with ID S91
	pCaMKII_psd_Substrate' = ReactionFlux93-ReactionFlux94 : affects compound with ID S92
	pCaMKII_CaM_psd_Substrate' = ReactionFlux96-ReactionFlux97 : affects compound with ID S93
	pCaMKII_CaM_Ca2_psd_Substrate' = ReactionFlux98-ReactionFlux99 : affects compound with ID S94
	pCaMKII_CaM_Ca4_psd_Substrate' = ReactionFlux100-ReactionFlux101 : affects compound with ID S95
	CaMKII_CaM_psd_Substrate' = ReactionFlux102-ReactionFlux103 : affects compound with ID S96
	CaMKII_CaM_Ca2_psd_Substrate' = ReactionFlux104-ReactionFlux105 : affects compound with ID S97
	CaMKII_CaM_Ca4_psd_Substrate' = ReactionFlux106-ReactionFlux107 : affects compound with ID S98
	total_CaMKII_activated' = pCaMKII_CaM_Ca4_psd' + pCaMKII_CaM_Ca2_psd' + pCaMKII_CaM_psd' + pCaMKII_psd' + CaMKII_CaM_Ca4_psd' + CaMKII_CaM_Ca2_psd' + CaMKII_CaM_Ca4_psd_Substrate' + CaMKII_CaM_psd_Substrate' + CaMKII_CaM_Ca2_psd_Substrate' + pCaMKII_psd_Substrate' + pCaMKII_CaM_psd_Substrate' + pCaMKII_CaM_Ca2_psd_Substrate' + pCaMKII_CaM_Ca4_psd_Substrate'

}
PROCEDURE observables_func() {
	pSubstrate_out = pSubstrate : Output ID Y0
	PP1_out = PP1 : Output ID Y1
	CaM_out = CaM : Output ID Y2
	D32_out = D32 : Output ID Y3
	total_CaMKII_activated_out = total_CaMKII_activated
	
}
