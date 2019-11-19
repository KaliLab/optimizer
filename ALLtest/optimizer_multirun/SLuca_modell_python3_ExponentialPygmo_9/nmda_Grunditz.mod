TITLE NMDA receptor--one of the two input stimulation of our model

: This mechanism is taken from the Neuron data base "exp2syn.mod" 
: The original comment are below between "COMMENT" and "ENDCOMMENT".
: 
: Our modifications:
: 
: 1.We added a single receptor conductance factor: "g_max=0.000045 (uS)".
:   An event of weight 1 generates a peak conductance of 1*g_max.
:   The weight is equal to the number of ampa receptors open at peak conductance
:
: 2.The NMDA receptors are simulated using a slow rise time constant 
:   and a double-expontial decay time constant

: The kinetic rate constants and channel conductance are taken from Franks KM, Bartol TM and Sejnowski TJ 
: A Monte Carlo model reveals independent signaling at central glutamatergic synapses 
: J Biophys (2002) 83(5):2333-48
: and Spruston N, Jonas P and Sakmann B
: Dendritic glutamate receptor channels in rat hippocampal CA3 and CA1 neurons
: J Physiol (1995) 482(2): 325-352
: correctd for physiological tempterature with Q10 from Hestrin S, Sah P and Nicoll RA  
: Mechanisms generating the time course of dual component excitatory synaptic currents 
: recorded in hippocampal slices
: Neuron (1990) 5: 247-253
:
: Written by Lei Tian on 04/12/06 



COMMENT
Two state kinetic scheme synapse described by rise time tau1,
and decay time constant tau2. The normalized peak condunductance is 1.
Decay time MUST be greater than rise time.

The solution of A->G->bath with rate constants 1/tau1 and 1/tau2 is
 A = a*exp(-t/tau1) and
 G = a*tau2/(tau2-tau1)*(-exp(-t/tau1) + exp(-t/tau2))
	where tau1 < tau2

If tau2-tau1 -> 0 then we have a alphasynapse.
and if tau1 -> 0 then we have just single exponential decay.

The factor is evaluated in the
initial block such that an event of weight 1 generates a
peak conductance of 1.

Because the solution is a sum of exponentials, the
coupled equations can be solved as a pair of independent equations
by the more efficient cnexp method.

ENDCOMMENT


NEURON {
	POINT_PROCESS nmda_Grunditz
	RANGE tau1, tau2, tau3, e, i, g_max, g, A, B, C	,k
	NONSPECIFIC_CURRENT i
	GLOBAL total
}

UNITS {
	(nA) = (nanoamp)
	(mA) = (milliamp)
	(mV) = (millivolt)
	(uS) = (microsiemens)
}

PARAMETER {
	tau1 = 3.18     (ms) <1e-9,1e9>     :rise time constant
	tau2 = 57.14      (ms) <1e-9,1e9>	:decay time constant
	tau3 = 2000     (ms) <1e-9,1e9>	    :decay time constant
	
	g_max= 0.000045 (uS)			: single channel conductance
	e    = 0 (mV)
	mg   = 1 (mM)

	k = 1e-06 (mA/nA)
}

ASSIGNED {
	v (mV)
	i (nA)
	factor
	total (uS)
	g (uS)
	
}

STATE {
	A (uS)
	B (uS)
	C (uS)
}

INITIAL {
	LOCAL t_peak
	total = 0
	if (tau1/tau2 > .9999) {
		tau1 = .9999*tau2
	}
	A = 0
	B = 0
	C = 0
	
	factor=0.8279	:from matlab to make the peak of the conductance curve shape to be 1*weight (then multiply with g_max)
	factor = 1/factor
	
}

BREAKPOINT {
	SOLVE state METHOD cnexp
	
	g = g_max*(B*0.8+C*0.2-A)
	i = g*(v - e)*1/(1+(exp(0.08(/mV) * -v)*(mg / 0.69)))	
	
}

DERIVATIVE state {
	A' = -A/tau1
	B' = -B/tau2
	C' = -C/tau3
}

NET_RECEIVE(weight (uS)) {
	A=A+weight*factor
	B=B+ weight*factor
	C=C+weight*factor
	total = total+weight
	
}

