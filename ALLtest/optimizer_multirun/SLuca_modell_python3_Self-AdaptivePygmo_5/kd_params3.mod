COMMENT
Conceptual model:  D current for a model of a fast-spiking cortical interneuron.

Authors and citation:
  Golomb D, Donner K, Shacham L, Shlosberg D, Amitai Y, Hansel D (2007).
  Mechanisms of Firing Patterns in Fast-Spiking Cortical Interneurons. 
  PLoS Comput Biol 3:e156.

Original implementation and programming language/simulation environment:
  by Golomb et al. for XPP
  Available from http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=97747

This implementation is by N.T. Carnevale and V. Yamini for NEURON.
ENDCOMMENT

NEURON {
  SUFFIX kd_params3
  USEION k READ ek WRITE ik
  RANGE gkd, g, ainfi, binfi, theta_a, theta_b, sigma_a, sigma_b, tau_a, tau_b, ik, b_kt
}

UNITS {
  (S) = (siemens)
  (mV) = (millivolt)
  (mA) = (milliamp)
}

PARAMETER {
  gkd = 0.00039 (S/cm2)
  theta_a = -60 (mV)
  sigma_a = 10 (mV)
  theta_b = -90 (mV)
  sigma_b = -10 (mV)
  tau_a = 2 (ms)
  tau0_b = 1 (ms)
  b_gamma = 0.5
  b_kt = 0.006
}

ASSIGNED {
  v (mV)
  ek (mV)
  ik (mA/cm2)
  g (S/cm2)
}

STATE {a b}

BREAKPOINT {
  SOLVE states METHOD cnexp
  g = gkd * a^3 * b
  ik = g * (v-ek)
}

INITIAL {
  a = ainfi(v)
  b = binfi(v)
}

DERIVATIVE states {
  a' = (ainfi(v)-a)/tau_a
  b' = (binfi(v)-b)/tau_b(v)
}

FUNCTION ainfi(v (mV)) {
  UNITSOFF
  ainfi=1/(1 + exp(-(v-theta_a)/sigma_a))
  UNITSON
}

FUNCTION binfi(v (mV)) {
  UNITSOFF
  binfi=1/(1 + exp(-(v-theta_b)/sigma_b))
  UNITSON
}

FUNCTION tau_b (v (mV)){
	UNITSOFF
	tau_b = 1 / ( (b_kt * (exp (b_gamma * (v - theta_b) / sigma_b))) + (b_kt * (exp ((b_gamma - 1) * (v - theta_b) / sigma_b)))) + tau0_b
	UNITSON
}
