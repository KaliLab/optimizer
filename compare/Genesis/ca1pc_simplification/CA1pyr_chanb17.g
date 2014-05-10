//genesis

/* FILE INFORMATION
** Channel definitions for hippocampal CA1 pyramidal neuron,
** based on various earlier models plus experimental data
**
** Created by Szabolcs Kali (last modified 10/13/2003)
*/
// kdr, na_y , na_z , k_d atirva!
// CONSTANTS
float EREST_ACT = -0.065 // hippocampal cell resting potential
float ELEAK = -0.075    // leak potential
float ENA = 0.120 + EREST_ACT // 0.055
float EK = -0.015 + EREST_ACT // -0.080
float ECA = 0.145 + EREST_ACT // 0.080
float SOMA_A = 3.320e-9       // soma area in square meters
//K_A, K_DR C-ROSS-hoz kepest 5mV al el, K_M el
//========================================================================
//			Transient Na channels
//========================================================================
function make_Na
        if ({exists Na_soma})
	        return
	end

	float v0,k0,kt,gamma,tau0

        create  tabchannel      Na_soma
                setfield        ^       \
                Ek              {ENA}   \               //      V
                Gbar            { 200 * SOMA_A }    \   //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  3       \
                Ypower  1       \
                Zpower  1

	 create  tabchannel      Na_dend
                setfield        ^       \
                Ek              {ENA}   \               //      V
                Gbar            { 200 * SOMA_A }    \   //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  3       \
                Ypower  1       \
                Zpower  1
		

// X gate (activation)
//ATIRVA
	v0 = -0.03 //-31
	k0 = 0.0045 //0.0045 
	kt = 20000 //20000
	gamma = 0.45 //0.45
	setupalpha Na_soma X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

	//setupalpha Na_dend X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
	//		{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
//distal
	float dv0,dk0,dkt,dgamma,dtau0

	dv0 = -0.031 //-31
	dk0 = 0.0045 //0.0045 
	dkt = 20000 //20000
	dgamma = 0.45 //0.45
	setupalpha Na_dend X {dkt} 0.0 0.0 {-dv0} {-dk0/dgamma}   \
			{dkt}  0.0 0.0 {-dv0} {dk0/(1-dgamma)}
//distal
			
// Y gate (fast inactivation)

        float   xmin = -0.1
        float   xmax = 0.05
        int     xdivs = 49
	v0 = -0.036  //-0.036
	k0 = -0.003 //-0.003
	kt = 1000 //1000
	gamma = 0.9 //0.9 kis ertek a jobb oldali akt. idejet csokkenti
	tau0 = 0.0002 // 0.0003

	//distal channels:
	dv0 = -0.036  //-0.036, 0.044 dend. AP miatt
	dk0 = -0.003 //-0.003
	dkt = 1000 //1000
	dgamma = 0.9 //0.9 kis ertek a jobb oldali akt. idejet csokkenti
	dtau0 = 0.0002 // 0.0003
	//
	
		
	call Na_soma TABCREATE Y {xdivs} {xmin} {xmax}

	call Na_dend TABCREATE Y {xdivs} {xmin} {xmax}

        int i
        float x, dx, y, r, tau, alpha, beta
	//distal channels:
	float dtau, dalpha, dbeta,dy,dtau
	//
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
		alpha = {kt * {exp {gamma * (x - v0) / k0}}}
		beta = {kt * {exp {(gamma - 1)  * (x - v0) / k0}}}
		y = {alpha / (alpha + beta)}
		tau = {1 / (alpha + beta) + tau0}
	//distal
		dalpha = {dkt * {exp {dgamma * (x - v0) / dk0}}}
		dbeta = {dkt * {exp {(dgamma - 1)  * (x - v0) / dk0}}}
		dy = {dalpha / (dalpha + dbeta)}
		dtau = {1 / (dalpha + dbeta) + dtau0}
	//
		
		setfield Na_soma Y_A->table[{i}] {y / tau}
		setfield Na_soma Y_B->table[{i}] {1 / tau}
	//distal
		setfield Na_dend Y_A->table[{i}] {dy / dtau}
		setfield Na_dend Y_B->table[{i}] {1 / dtau}
	//	
		//setfield Na_dend Y_A->table[{i}] {y / tau}
		//setfield Na_dend Y_B->table[{i}] {1 / tau}

	        x = x + dx
        end

	setfield Na_soma Y_A->calc_mode 0   Y_B->calc_mode 0
        call Na_soma TABFILL Y 3000 0
	setfield Na_dend Y_A->calc_mode 0   Y_B->calc_mode 0
        call Na_dend TABFILL Y 3000 0

// Z gate (slow inactivation)

	call Na_soma TABCREATE Z {xdivs} {xmin} {xmax}

	call Na_dend TABCREATE Z {xdivs} {xmin} {xmax}

        int i
        float zs,zd

        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
		zs = (1+0.8*{exp {(x+0.039)/0.002}})/(1+{exp {(x+0.039)/0.002}})  //58
		r = (1+{exp {450*(x+0.06)}})/(5*{exp {90*(x+0.06)}} + 4*{exp {450*(x+0.045)}})//UJ
//		r = (1+{exp {450*(x+0.06)}})/(5*{exp {90*(x+0.06)}})		
//		r = (1+{exp {450*(x+0.06)}})/(3*{exp {90*(x+0.06)}}) //eredeti
		setfield Na_soma Z_A->table[{i}] {{zs}*{r}}
		setfield Na_soma Z_B->table[{i}] {r}
		
		zd = (1+0.35*{exp {(x+0.058)/0.002}})/(1+{exp {(x+0.058)/0.002}}) //0.35
//		zd = (1+0.5*{exp {(x+0.058)/0.002}})/(1+{exp {(x+0.058)/0.002}}) //eredeti
		setfield Na_dend Z_A->table[{i}] {{zd}*{r}}
		setfield Na_dend Z_B->table[{i}] {r}

	        x = x + dx
        end

	setfield Na_soma Z_A->calc_mode 0   Z_B->calc_mode 0
        call Na_soma TABFILL Z 3000 0

	setfield Na_dend Z_A->calc_mode 0   Z_B->calc_mode 0
        call Na_dend TABFILL Z 3000 0

        addfield Na_soma addmsg1
	setfield Na_soma addmsg1  ".. . CONCEN Vm"

	addfield Na_dend addmsg1
	setfield Na_dend addmsg1  ".. . CONCEN Vm"
		
end

//========================================================================
//			Delayed rectifier K channel
//========================================================================

function make_K_DR
        if ({exists K_DR})
                return
        end

	float v0,k0,kt,gamma

// used to be Xpower = 4, v0 = -0.0103 (or -0.02), k0 = 0.014
// C-ROSS values
        create  tabchannel      K_DR
                setfield        ^       \
                Ek              {EK}	\	           //      V
                Gbar            { 150 * SOMA_A }    \      //      S
                Ik              0       \                  //      A
                Gk              0       \                  //      S
                Xpower  2       \
                Ypower  0       \
                Zpower  0

	v0 = 0.007   // C-ROSS eredeti:0.0016 //86 most, jo 0.0066-al is(5comp ver), a nagy modellbe 0.0096
 	k0 = 0.010    // C-R:0.012, mukodik 0.010-al is
	kt = 50      //most 50,eredeti:250
	gamma = 0.9   //0.9    0.3 el ahp kiraly de vastag AP

	setupalpha K_DR X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end
//K_M:
//	v0 = -0.028   //original: -0,038
//	k0 = 0.006
//	kt = 5
//	gamma = 0.6
//	tau0 = 0.005
//K_DR, ha dominans:
//	v0 = 0.0036   // C-ROSS eredeti:0.0016
//	k0 = 0.01    // 0.0129
//	kt = 200      //250
//	gamma = 0.9   //0.9    0.3 el ahp kiraly de vastag AP


//========================================================================
//			Transient K(A) channels
//========================================================================

function make_K_A_dist
	if ({exists K_A_dist})
                return
	end

	float v0,k0,kt,gamma

	create  tabchannel      K_A_dist
	setfield        ^       \
		Ek              {EK}    \
		Gbar            { 50 * SOMA_A }     \
		Ik              0       \
		Gk              0       \
		Xpower  2       \
		Ypower  1       \
		Zpower  0
	
	v0 = -0.0165 //C-ROSS eredeti: -0.0165, 135-re allitva, h dendritikus injekcio eseten a denriten alakuljon k1 1. spike
	k0 = 0.012 // C-ROSS: 0.0176 , 0.12 OK
	kt = 450 //450 volt, 455 c modellhez atallitva most 650 ha KM magas
	gamma = 0.5

	setupalpha K_A_dist X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

	float   xmin = -0.1
	float   xmax = 0.05
	int     xdivs = 49
	call K_A_dist TABCREATE Y {xdivs} {xmin} {xmax}

	int i
	float x,dx,y
	float tau,minf
	dx = (xmax - xmin)/xdivs
	x = xmin
	for (i = 0 ; i <= {xdivs} ; i = i + 1)
		minf = 1 / {1 + {exp {125*(x + 0.051)}}} //0.016 most x + 0.056 C-ROSS, (125*(..
		if (x > -0.030)
			tau = 0.26*(x + 0.030) + 0.005
		else
			tau = 0.005
		end
		setfield K_A_dist Y_A->table[{i}] {{minf} / {tau}}
		setfield K_A_dist Y_B->table[{i}] {1 / {tau}}
		x = x + dx
	end

	setfield K_A_dist Y_A->calc_mode 0   Y_B->calc_mode 0
	call K_A_dist TABFILL Y 3000 0
end
//C-ROSS values
function make_K_A_prox
	if ({exists K_A_prox})
                return
	end

	float v0,k0,kt,gamma

	create  tabchannel      K_A_prox
	setfield        ^       \
		Ek              {EK}    \
		Gbar            { 50 * SOMA_A }     \
		Ik              0       \
		Gk              0       \
		Xpower  2       \
		Ypower  1       \
		Zpower  0
	
	v0 = -0.0054  // C-ROSS: -0.0054
	k0 = 0.012  // 0.021 C-ROSS , atirva 0.03 ra hogy KA okozza -50mV-on a minimumat
	kt = 450 //450 OK, 650, ha KM magas
	gamma = 0.5

	setupalpha K_A_prox X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

	float   xmin = -0.1
	float   xmax = 0.05
	int     xdivs = 49
	call K_A_prox TABCREATE Y {xdivs} {xmin} {xmax}

	int i
	float x,dx,y
	float tau,minf
	dx = (xmax - xmin)/xdivs
	x = xmin
	for (i = 0 ; i <= {xdivs} ; i = i + 1)
		minf = 1 / {1 + {exp {125*(x + 0.051)}}}// + 0.056 eredetileg, 125*
		if (x > -0.030)
			tau = 0.26*(x + 0.030) + 0.005
		else
			tau = 0.005
		end
		setfield K_A_prox Y_A->table[{i}] {{minf} / {tau}}
		setfield K_A_prox Y_B->table[{i}] {1 / {tau}}
		x = x + dx
	end

	setfield K_A_prox Y_A->calc_mode 0   Y_B->calc_mode 0
	call K_A_prox TABFILL Y 3000 0
end

//========================================================================
//			Persistent Na channel
//========================================================================
function make_NaP
        if ({exists NaP})
	        return
	end

	float v0,k0,kt,gamma

        create  tabchannel      NaP
                setfield        ^       \
                Ek              {ENA}   \               //      V
                Gbar            { 2 * SOMA_A }    \   //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  1       \
                Ypower  0       \
                Zpower  0

	v0 = -0.0001 //-0.050
	k0 = 0.006
	kt = 1000
	gamma = 0.5

	setupalpha NaP X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end

//========================================================================
//                      Low-threshold Ca(T) Channel
//========================================================================
function make_CaT
        if ({exists CaT})
                return
        end

	float v0,k0,kt,gamma

        create  tabchannel      CaT
                setfield        ^       \
                Ek              {ECA}   \               //      V
                Gbar            { 5 * SOMA_A }      \   //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  2       \
                Ypower  1       \
                Zpower  0

// X gate (activation) -- according to Randall and Tsien (1997)

	v0 = -0.017 //-0.017
	k0 = 0.0117 //0.0117
	kt = 30 //30 most
	gamma = 0.5

	setupalpha CaT X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

// Y gate (inactivation) -- according to Thompson and Wong (1991)

	v0 = -0.071 //-0.076
	k0 = -0.0068
	kt = 10
	gamma = 0.5

	setupalpha CaT Y {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end

//========================================================================
//                      High-threshold Ca(L) Channel
//========================================================================

function make_CaL
        if ({exists CaL})
                return
        end

	float v0,k0,kt,gamma

        create  tabchannel      CaL
                setfield        ^       \
                Ek              {ECA}   \               //      V
                Gbar            { 20 * SOMA_A }      \  //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  2       \
                Ypower  0       \
                Zpower  0

// data from Bell et al. (2001)

	v0 = 0.0065 //most -0.0055
	k0 = 0.0085 //0.0085
	kt = 300
	gamma = 0.5

	setupalpha CaL X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end

//========================================================================
//                      High-threshold Ca(N) Channel
//========================================================================

function make_CaN
        if ({exists CaN})
                return
        end

	float v0,k0,kt,gamma

        create  tabchannel      CaN
                setfield        ^       \
                Ek              {ECA}   \               //      V
                Gbar            { 20 * SOMA_A }      \  //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  2       \
                Ypower  1       \
                Zpower  0

// X gate (activation)

	v0 = -0.0005 //-0.01
	k0 = 0.006
	kt = 150
	gamma = 0.5

	setupalpha CaN X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

// Y gate (inactivation)

	v0 = -0.070 //-0.075
	k0 = -0.0065
	kt = 5
	gamma = 0.5

	setupalpha CaN Y {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end

//========================================================================
//                      High-threshold Ca(R) Channel
//========================================================================

function make_CaR
        if ({exists CaR})
                return
        end

	float v0,k0,kt,gamma

        create  tabchannel      CaR
                setfield        ^       \
                Ek              {ECA}   \               //      V
                Gbar            { 20 * SOMA_A }      \  //      S
                Ik              0       \               //      A
                Gk              0       \               //      S
                Xpower  2       \
                Ypower  1       \
                Zpower  0

// X gate (activation) -- according to Randall and Tsien (1997)

	v0 = -0.002  // most -0.002 orig:-0.008, emiatt nem viszi tulzasba a depolarizaciot
	k0 = 0.010   // orig: 0.008
	kt = 100   // eredeti:100, na spiketrain elkerulese miatt atirva
	gamma = 0.5

	setupalpha CaR X {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}

// Y gate (inactivation)
// Ca spike hossza ettol fugg
	v0 = -0.053  // changed from -0.068, eredeti -0.055 most -0.05
	k0 = -0.009	//eredeti: -0.011
	kt = 1.5	//eredeti: 2
	gamma = 0.5

	setupalpha CaR Y {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
end

//========================================================================
//                      Ca conc
//========================================================================

function make_Ca_conc
        if ({exists Ca_conc})
                return
        end
        create Ca_concen Ca_conc
        setfield Ca_conc \
                tau     0.01333   \      // sec
                B       17.402e12 \      // Curr to conc for soma
                Ca_base 0.0
        addfield Ca_conc addmsg1
	addfield Ca_conc addmsg2
        addfield Ca_conc addmsg3
	addfield Ca_conc addmsg4
        setfield Ca_conc \
                addmsg1 "../CaT . I_Ca Ik" \
		addmsg2	"../CaL . I_Ca Ik" \
		addmsg3 "../CaN . I_Ca Ik" \
		addmsg4	"../CaR . I_Ca Ik"
end

//========================================================================
//                   Ca-dependent K(AHP) Channel
//========================================================================

function make_K_AHP
        if ({exists K_AHP})
                return
        end

        create  tabchannel      K_AHP
                setfield        ^       \
                Ek              {EK}   \               //      V
                Gbar            { 8 * SOMA_A }    \    //      S
                Ik              0       \              //      A
                Gk              0       \              //      S
                Xpower  0       \
                Ypower  0       \
                Zpower  1

        float   xmin = 0.0
        float   xmax = 1000.0
        int     xdivs = 50

        call K_AHP TABCREATE Z {xdivs} {xmin} {xmax}
        int i
        float x,dx,y
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
            if (x < 500.0)
                y = 0.02*x
            else
                y = 10.0
            end
            setfield K_AHP Z_A->table[{i}] {y}
            setfield K_AHP Z_B->table[{i}] {y + 1.0}
            x = x + dx
        end

//        setfield K_AHP Z_A->calc_mode 0   Z_B->calc_mode 0  // 1 instead of 0
        call K_AHP TABFILL Z 3000 0

        addfield K_AHP addmsg1
        setfield K_AHP \
                addmsg1        "../Ca_conc . CONCEN Ca"
end

//========================================================================
//                   Ca-dependent K(C) Channel
//========================================================================

function make_K_C
        if ({exists K_C})
                return
        end

        create  tabchannel    K_C
                setfield        ^       \
                Ek              {EK}    \                       //      V
                Gbar            { 100.0 * SOMA_A }      \       //      S
                Ik              0       \                       //      A
                Gk              0                               //      S

        float   xmin = -0.1
        float   xmax = 0.05
        int     xdivs = 49
        call K_C TABCREATE X {xdivs} {xmin} {xmax}
        int i
        float x,dx,alpha,beta
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
            if (x < EREST_ACT + 0.05)
                alpha = {exp {53.872*(x - EREST_ACT) - 0.66835}}/0.018975
		beta = 2000*{exp {(EREST_ACT + 0.0065 - x)/0.027}} - alpha
            else
		alpha = 2000*{exp {(EREST_ACT + 0.0065 - x)/0.027}}
		beta = 0.0
            end
            setfield K_C X_A->table[{i}] {alpha}
            setfield K_C X_B->table[{i}] {alpha+beta}
            x = x + dx
        end

	setfield K_C X_A->calc_mode 0 X_B->calc_mode 0
	setfield K_C Xpower 1
	call K_C TABFILL X 3000 0

        float   xmin = 0.0
        float   xmax = 1000.0
        int     xdivs = 50

        call K_C TABCREATE Z {xdivs} {xmin} {xmax}
        int i
        float x,dx,y
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
            if (x < 250.0)
                y = x/250.0
            else
                y = 1.0
            end
	    /* activation will be computed as Z_A/Z_B */
            setfield K_C Z_A->table[{i}] {y}
            setfield K_C Z_B->table[{i}] 1.0
            x = x + dx
        end

	setfield K_C Z_A->calc_mode 0 Z_B->calc_mode 0
	setfield K_C Zpower 1

	setfield K_C instant {INSTANTZ}
	call K_C TABFILL Z 3000 0

        addfield K_C addmsg1
        setfield K_C addmsg1  "../Ca_conc  . CONCEN Ca" 
end

//========================================================================
//         Hyperpolarization-activated Mixed Cation (H) Channels
//========================================================================

function make_H_CA1pyr_prox
        if (({exists H_CA1pyr_prox}))
                return
        end

float EH = -0.030		// reversal potential for mixed cation current

        create tabchannel H_CA1pyr_prox
        setfield H_CA1pyr_prox Ek {EH} Gbar {50.0*SOMA_A} Gk 0 Ik 0  \
            Xpower 1 Ypower 0 Zpower 0

	float   xmin = -0.1
	float   xmax = 0.05
	int     xdivs = 49
	call H_CA1pyr_prox TABCREATE X {xdivs} {xmin} {xmax}

	int i
	float x,dx
	float tau,minf
	dx = (xmax - xmin)/xdivs
	x = xmin
	for (i = 0 ; i <= {xdivs} ; i = i + 1)
		minf = 1 / {1 + {exp {300*(x + 0.083)}}}  // changed from 151, worked with 300
		tau = {exp {33.0 * (x + 0.075)}} / {11.0 * (1 + {exp {83.0* (x + 0.075)}})}
		setfield H_CA1pyr_prox X_A->table[{i}] {{minf} / {tau}}
		setfield H_CA1pyr_prox X_B->table[{i}] {1 / {tau}}
		x = x + dx
	end
	setfield H_CA1pyr_prox X_A->calc_mode 0 X_B->calc_mode 0
	call H_CA1pyr_prox TABFILL X 3000 0
end

function make_H_CA1pyr_dist
        if (({exists H_CA1pyr_dist}))
                return
        end

float EH = -0.030

        create tabchannel H_CA1pyr_dist
        setfield H_CA1pyr_dist Ek {EH} Gbar {50.0*SOMA_A} Gk 0 Ik 0  \
            Xpower 1 Ypower 0 Zpower 0

	float   xmin = -0.1
	float   xmax = 0.05
	int     xdivs = 49
	call H_CA1pyr_dist TABCREATE X {xdivs} {xmin} {xmax}

	int i
	float x,dx
	float tau,minf
	dx = (xmax - xmin)/xdivs
	x = xmin
	for (i = 0 ; i <= {xdivs} ; i = i + 1)
		minf = 1 / {1 + {exp {300*(x + 0.089)}}}  // changed from 167, worked with 300
		tau = {exp {33.0 * (x + 0.075)}} / {11.0 * (1 + {exp {83.0* (x + 0.075)}})}
		setfield H_CA1pyr_dist X_A->table[{i}] {{minf} / {tau}}
		setfield H_CA1pyr_dist X_B->table[{i}] {1 / {tau}}
		x = x + dx
	end
	setfield H_CA1pyr_dist X_A->calc_mode 0 X_B->calc_mode 0
	call H_CA1pyr_dist TABFILL X 3000 0
end

//========================================================================
//			Muscarine-sensitive K channel
//========================================================================
//MODIFIED
function make_K_M
        if ({exists K_M})
                return
        end

        float   xmin = -0.1
        float   xmax = 0.05
        int     xdivs = 49

	float v0,k0,kt,gamma,tau0

        create  tabchannel      K_M
                setfield        ^       \
                Ek              {EK}	\	           //      V
                Gbar            { 150 * SOMA_A }    \      //      S
                Ik              0       \                  //      A
                Gk              0       \                  //      S
                Xpower  2      \
                Ypower  0       \
                Zpower  0

// model from Borg-Graham (1998)

	v0 = -0.018   //now: -0,033 for 455 comp adjusted -0.028, erre erzekeny
	k0 = 0.003	//0.006
	kt = 5
 	gamma = 0.8	//orig: 0,6, minel nagyobb annal ritkabban tuzel most 0.8
	tau0 = 0.02	//0.005

	call K_M TABCREATE X {xdivs} {xmin} {xmax}

        int i
        float x, dx, y, r, tau, alpha, beta
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
		alpha = {kt * {exp {gamma * (x - v0) / k0}}}
		beta = {kt * {exp {(gamma - 1)  * (x - v0) / k0}}}
		y = {alpha / (alpha + beta)}
		tau = {1 / (alpha + beta) + tau0}

		setfield K_M X_A->table[{i}] {y / tau}
		setfield K_M X_B->table[{i}] {1 / tau}

	        x = x + dx
        end

end




//========================================================================
//			Delayed K channel
//========================================================================

function make_K_D
        if ({exists K_D})
                return
        end

        float   xmin = -0.1
        float   xmax = 0.05
        int     xdivs = 49

	float v0,k0,kt,gamma,tau0

        create  tabchannel      K_D
                setfield        ^       \
                Ek              {EK}	\	           //      V
                Gbar            { 150 * SOMA_A }    \      //      S
                Ik              0       \                  //      A
                Gk              0       \                  //      S
                Xpower  2       \
                Ypower  1       \
                Zpower  0

// model from Borg-Graham (1998)

// X gate
	
	v0 = -0.063	// = V0.5 =-0.063 (Borg), -0.0088 a cikkben
	k0 = 0.0087	// 0.0087 = R*T/(z*F) z = 3
	kt = 500	// K (nincs megadva) legyen kb 2500
	gamma = 0.5	// nincs megadva mert 1/Kt << tau0,vagyis feszultsegfuggetlen ezert ures gamma is
	tau0 = 0.0001	// 0.001 = Tau0 csak ebben a formaban lehet tau0-t beletenni
	
	
	call K_D TABCREATE X {xdivs} {xmin} {xmax}

        int i
        float x, dx, y, r, tau, alpha, beta
        dx = (xmax - xmin)/xdivs
        x = xmin
        for (i = 0 ; i <= {xdivs} ; i = i + 1)
		alpha = {kt * {exp {gamma * (x - v0) / k0}}}
		beta = {kt * {exp {(gamma - 1)  * (x - v0) / k0}}}
		y = {alpha / (alpha + beta)}
		tau = {1 / (alpha + beta) + tau0}
//		tau = {tau0}
		setfield K_D X_A->table[{i}] {y / tau}
		setfield K_D X_B->table[{i}] {1 / tau}

	        x = x + dx
        end

// Y gate 

	v0 = -0.073	//Borg
	k0 = -0.005	//= -0.01 ha kiseb mint 0 van inaktivacio!, -0.0069 nél OK, minel kisebb, annal meredekebb minf(itt inakt.)
	kt = 0.73	// 0.2= K, 0.73-al jobb.
	gamma = 0	//0 de akkor 0-val való osztás, amit vmiert elfogad

	setupalpha K_D Y {kt} 0.0 0.0 {-v0} {-k0/gamma}   \
			{kt}  0.0 0.0 {-v0} {k0/(1-gamma)}
		

end

