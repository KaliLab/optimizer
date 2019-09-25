
import matplotlib.pyplot as plt
import numpy
import os
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
algonames=[]
print(algonames)
for curr_dir in subdirs:
	try:
		with open(str(os.getcwd())+"/"+str(curr_dir)+"/best_costs.txt" , "r") as out_handler:
			lines=list(out_handler.read().split('\n'))
			gens=[x.replace(" ","") for x in lines]
			gens=list(filter(None,gens))
			vals=[float(x) for x in gens]
			allcummin.append(vals)
			algonames.append(curr_dir.replace("_",""))
	except:
		"ok"


alldict=dict(zip(algonames,allcummin))
algossort=dict(sorted(alldict.items(), key=lambda kv: numpy.median(kv[1])))
print(algossort.keys())
parts=plt.violinplot(algossort.values(),showmedians=True)

plt.yscale('log')

print(algonames)
plt.xticks(range(1,len(algonames)+1),labels=algossort.keys(),fontsize=12)
plt.xlabel('Algorithms',fontsize=14)
plt.ylabel('Error',fontsize=14)
plt.title('10xANAT_100x100ALL_MSE')

my_colors = ['r', 'r', 'g', 'r', 'r', 'g', 'g','r', 'k', 'g','g']
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), my_colors):
    ticklabel.set_color(tickcolor)

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Pygmo',
                          markerfacecolor='r', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Inspyred',
                          markerfacecolor='g', markersize=15)]

plt.legend(['Pygmo','Inspyred'],loc=4, handles=legend_elements)
plt.show()

