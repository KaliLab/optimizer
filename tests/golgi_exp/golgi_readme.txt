The data file contains one trace obtained from a golgi cell by using current clamp. The file contains the time as well.
The cell was excited by a short(0.5ms,250pA) and by a long(500ms,12pA) pulse injected into the soma, so you have to use the provided stimuli file (for this, select the "Custom Waveform" option from the dropdown menu on the stimuli layer and then load the file).
The data trace is 1200ms long and the sampling frequency was 20kHz.
The provided model is a passive one and it"s based on a precise reconstruction, and we are interested in the cm, Ra, g_pas parameters.
Because we had to set the e_pas parameter to 0 and we wanted to optimize the previous parameters in every section, we created a function to do this for us (see udeffun_ca_ra_pyr.txt), you can load this on the model selection layer.
