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
	with open("/home/mohacsi/Desktop/optimizer/Alltest/All_simp/IBEA/ca1_pc_simplification_"+str(i)+"/bpopt_stats.txt", "r") as out_handler:
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
	with open("/home/mohacsi/Desktop/optimizer/Alltest/All_simp/BP_NSGA/ca1_pc_simplification_"+str(i)+"/bpopt_stats.txt" , "r") as out_handler:
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



algos=['IBEA','BP_NSGA']
intgs=[]
intgs.append(numpy.trapz(medI,range(100)))
intgs.append(numpy.trapz(medN,range(100)))
subdirs=list(next(os.walk('.'))[1])
import matplotlib.cm as cm
colors = cm.nipy_spectral(numpy.linspace(0, 1, len(subdirs)+2))

for idx,curr_dir in enumerate(subdirs):
	try:
		with open(str(os.getcwd())+"/"+str(curr_dir)+"/median.txt" , "r") as out_handler:
			fs=out_handler.read().split('\n')[0:-1]
			vals=[float(x) for x in fs]
			vals=numpy.minimum.accumulate(vals)
			intgs.append(numpy.trapz(vals,numpy.arange(0,101,(101/len(vals)))))
			algos.append(str(curr_dir))
	except:
		""
	
algdict=dict(zip(algos,intgs))
algossort=dict(sorted(algdict.items(), key=lambda kv: kv[1]))
print(algossort.values())
plt.bar(range(len(algossort.values())),algossort.values(),color=['blue','blue','red','blue','blue','blue','blue','red','red','blue','blue','red','blue'])
plt.xticks(range(len(algossort.values())),algossort.keys(),fontsize=8)
plt.title('Simp_Conv_10run_MSE(ex),SC,1st')
plt.xlabel('Algorithm')
plt.ylabel('Integral')
plt.grid(True)
plt.show()
