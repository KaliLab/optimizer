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
	with open("/home/mohacsi/Desktop/IBEAtest/optimizer_multirun/hh_pas_surrogate_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
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
	
minl=[x[-1] for x in zip(*allcummin)]

plt.plot(numpy.arange(0,101,(101/len(medl))), medl,'r-.')

for i in range(1,11):
	minl=[]
	maxl=[]
	medl=[]
	cummin=[]
	with open("/home/mohacsi/Desktop/IBEAtest/ibea-multirun/hh_pas_surrogate_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
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

minl=[x[-1] for x in zip(*allcummin)]

plt.plot(numpy.arange(0,101,(101/len(minl))), minl,'b-')


legend=['BP_NSGA_min','BP_NSGA_max','BP_NSGA_med','IBEA_min','IBEA_max','IBEA_med']
subdirs=list(next(os.walk('.'))[1])
for color,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/min.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'C'+str(color)+'-')
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/max.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'C'+str(color)+'--')
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/median.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'C'+str(color)+'-.')
	
	legend.append(str(curr_dir)+'_min')
	legend.append(str(curr_dir)+'_max')
	legend.append(str(curr_dir)+'_med')



plt.yscale('log')
plt.title('HH_BP+INSP_10run_MSE(ex),SC,AMP,W')
plt.legend(legend, loc='upper right', ncol=4)
plt.xlabel('Gen')
plt.ylabel('Fitness')
plt.grid(True)
plt.savefig("Allrun.png")
plt.show()
