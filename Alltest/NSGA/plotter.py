import matplotlib.pyplot as plt
import numpy
import os
allmin=[]
allmax=[]
allmed=[]
allcummin=[]
for i in range(1,11):
	minl=[]
	maxl=[]
	medl=[]
	cummin=[]
	with open(str(os.getcwd())+"/hh_pas_surrogate_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
		out_handler.readline()
		lines=out_handler.readlines()
		for line in lines:
			lina=line.split(",")
			minl.append(float(lina[1]))
			maxl.append(float(lina[2]))
			medl.append(float(lina[3]))
			cummin.append(float(lina[4]))
	allmin.append(minl)
	allmax.append(maxl)
	allmed.append(medl)
	allcummin.append(cummin)
	
minl=[numpy.min(x) for x in zip(*allmin)]
maxl=[numpy.max(x) for x in zip(*allmax)]
medl=[numpy.mean(x) for x in zip(*allmed)]
cummin=[numpy.min(x) for x in zip(*allcummin)]

plt.plot(range(0,len(minl)), minl)
plt.plot(range(0,len(maxl)), maxl)
plt.plot(range(0,len(medl)), medl)
plt.plot(range(0,len(cummin)), cummin)
plt.yscale('log')
plt.title('HH_BPNSGA_10run_MSE(ex),SC,AMP,W')
plt.legend(['min','max','med','cumul'])
plt.xlabel('Gen')
plt.ylabel('Fitness')
plt.grid(True)
plt.savefig("test.png")
plt.show()
