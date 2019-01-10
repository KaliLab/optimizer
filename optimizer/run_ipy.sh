#!/bin/bash


ipcluster start  -n 4 --debug &

python optimizer.py -c hh_pas_surrogate_settings.xml