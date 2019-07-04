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
	with open("/home/mohacsi/Desktop/optimizer/Alltest/IBEA/adexpif_external_ca3_pc_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
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
	
minI=[numpy.min(x) for x in zip(*allcummin)]
maxI=[numpy.max(x) for x in zip(*allcummin)]
medI=[numpy.median(x) for x in zip(*allcummin)]



allcummin=[]
for i in range(1,11):
	minl=[]
	maxl=[]
	medl=[]
	cummin=[]
	with open("/home/mohacsi/Desktop/optimizer/Alltest/BP_NSGA/adexpif_external_ca3_pc_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
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
	
minN=[numpy.min(x) for x in zip(*allcummin)]
maxN=[numpy.max(x) for x in zip(*allcummin)]
medN=[numpy.median(x) for x in zip(*allcummin)]




legend=['IBEA_med',
		#'IBEA_med',
		'BP_NSGA_med']#,
		#'BP_NSGA_med']
subdirs=list(next(os.walk('.'))[1])
import matplotlib.cm as cm
colors = cm.nipy_spectral(numpy.linspace(0, 1, len(subdirs)+2))

#plt.plot(numpy.arange(0,101,(101/len(minl))), minI,'-',color=colors[0])
#plt.plot(numpy.arange(0,101,(101/len(maxl))), maxI,'--',color=colors[0])
plt.plot(numpy.arange(0,101,(101/len(medl))), medI,'-.',color=colors[0])
#plt.plot(numpy.arange(0,101,(101/len(minl))), minN,'-',color=colors[1])
#plt.plot(numpy.arange(0,101,(101/len(maxl))), maxN,'--',color=colors[1])
plt.plot(numpy.arange(0,101,(101/len(medl))), medN,'-.',color=colors[1])

for idx,curr_dir in enumerate(subdirs):
	"""with open(str(os.getcwd())+"/"+str(curr_dir)+"/min.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		vals=numpy.minimum.accumulate(vals)
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'-',color=colors[idx+2])
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/max.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'--',color=colors[idx+2])"""
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/median.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[0:-1]
		vals=[float(x) for x in fs]
		vals=numpy.minimum.accumulate(vals)
		plt.plot(numpy.arange(0,101,(101/len(vals))), vals,'-.',color=colors[idx+2])
	
	"""legend.append(str(curr_dir)+'_min')"""
	#legend.append(str(curr_dir)+'_min')
	legend.append(str(curr_dir)+'_med')



plt.yscale('log')
plt.title('IF_All_10run_MSE(ex),SC,1st')
plt.legend(legend, loc='upper right', ncol=4)
plt.xlabel('Gen')
plt.ylabel('Fitness')
plt.grid(True)
plt.savefig("Allrun.png")
plt.show()
