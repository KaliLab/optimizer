import numpy as np
import matplotlib.pyplot as plt

########################*************DISCLAIMER*************########################
########################************SLOPPY CODE!************########################
####################****WORKS WITH EVEN NUMBER OF RUNS ONLY!****####################

#the main directories of the runs
dirs = ['/home/nest/Documents/TESTS/ANAT/PYGMO/SINGLE/CMAES',
	'/home/nest/Documents/TESTS/ANAT/PYGMO/SINGLE/DE',
	'/home/nest/Documents/TESTS/ANAT/PYGMO/SINGLE/PSO',
	'/home/nest/Documents/TESTS/ANAT/PYGMO/SINGLE/SADE',
	'/home/nest/Documents/TESTS/ANAT/PYGMO/SINGLE/XNES']

#labels of the runs
labels = [dir.split('/')[-1] for dir in dirs]


#colors of the runs on the plots
colors = ['C0', 'C1', 'C2', 'C3', 'C5', 'C6', 'C8', 'C9', 'C4', 'C7']

plt.figure(figsize=(6,6))
plt.suptitle("SINGLE PYGMO ALGOS ON ANAT")


def gen_multiplier(arr):
	temp = []
	gens = 100
	for elem in arr:
		for i in range(gens):
			temp.append(elem)
	return temp


x_length = 0
#plotting
for i in range(len(dirs)):
	median 			= np.genfromtxt(dirs[i] + '/results/median.txt')
	minim 			= np.genfromtxt(dirs[i] + '/results/min.txt')
	maxim 			= np.genfromtxt(dirs[i] + '/results/max.txt')
	plt.plot(gen_multiplier(maxim), colors[i]+ '-.',label=labels[i] + ' max', linewidth=1.5 )
	plt.plot(gen_multiplier(median), colors[i],label=labels[i] + ' med', linewidth=1.5 )
	plt.plot(gen_multiplier(minim), colors[i]+ '--',label=labels[i] + ' min', linewidth=1.5 )
	x_length = 10000

plt.legend(fontsize=10, ncol=2)
plt.xlim(0,x_length)

plt.yscale('log')

#additional options as axes labels, scales, fontsize etc.

plt.show()
