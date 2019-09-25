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
	with open("/home/mohacsi/Desktop/optimizer/Alltest/ALL_HH/IBEA/hh_pas_surrogate_"+str(i)+"/bpopt_stats.txt", "r") as out_handler:
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
	with open("/home/mohacsi/Desktop/optimizer/Alltest/ALL_HH/NSGA/hh_pas_surrogate_"+str(i)+"/bpopt_stats.txt", "r") as out_handler:
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



algos=['IBEA','NSGA']
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
plt.bar(range(len(algossort.values())),algossort.values(),color=['blue','blue','red','blue','blue','red','blue','blue','blue','red','red','blue','blue','blue','blue'])
plt.xticks(range(len(algossort.values())),algossort.keys(),fontsize=12)
plt.title('HH_Conv_10run_MSE(ex),SC,AP_AMP,WIDTH')
plt.xlabel('Algorithm',fontsize=12)
plt.ylabel('Area under error curve',fontsize=12)
plt.ylim([0,1])
plt.grid(True)
my_colors = ['g', 'g', 'b', 'r', 'r', 'b', 'g','r', 'r', 'g','g', 'r', 'k','g','g']
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), my_colors):
    ticklabel.set_color(tickcolor)

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Pygmo',
                          markerfacecolor='r', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Inspyred',
                          markerfacecolor='g', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='BluePyOpt',
                          markerfacecolor='b', markersize=15)]
plt.legend(['Pygmo','Inspyred','BluePyOpt'],loc=2, handles=legend_elements)
plt.show()
