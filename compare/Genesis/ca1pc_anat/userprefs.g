//genesis

echo Using local user preferences!

include compartments 

/************************************************************************
**  2	Invoking functions to make prototypes in the /library element
************************************************************************/

/*   To ensure that all subsequent elements are made in the library    */
	pushe /library

	/* Make the standard types of compartments  */

	make_cylind_compartment		/* makes "compartment" */
	make_sphere_compartment		/* makes "compartment_sphere" */
	make_cylind_symcompartment	/* makes "symcompartment" */
	make_sphere_symcompartment	/* makes "symcompartment_sphere" */

	/* Assign some constants to override those used in traub91proto.g */
	EREST_ACT = -0.065       // resting membrane potential (volts)
	float ELEAK = -0.065    // leak potential

	/* returning to the root element */
	pope

/*************************************************************** *******
**
**	3	Setting preferences for user-variables.
**
**********************************************************************/

/* See defaults.g for default values of these. Put your preferred
   values for these in your copy of userprefs in the directory from
   which you are running your simulations. */

//user_symcomps = 1 // symmetric
user_intmethod = 11

user_syntype1 = ""
user_syntype2 = ""
user_help = "README"
user_name = "Szabolcs Kali"
user_cell = "/ca1pc"
user_pfile = "131117-C2.p"

float user_wx = 6.47e-4  // wx, wy, cx, cy, cz for the draw widget
float user_wy = 6.47e-4
float user_cx = 1.25e-4
float user_cy = 0.0
float user_cz = 0.2e-3

// Set the scales for the graphs in the two cell windows
user_ymin1 = -0.1
user_ymax1 = 0.15
user_xmax1 = 0.5
user_xmax2 = 0.5
user_ymin2 = 0.0
user_ymax2 = 5e-7
user_yoffset2 = 0.0

