
import matplotlib.pyplot as plt
import numpy
import os
subdirs=list(next(os.walk('.'))[1])
allcummin=[[0.05052349312343095, 0.03827316432930312, 0.02391663684933393, 0.0306452331356941, 0.03998299644451, 0.0402464057116343, 0.0319478972571454, 0.0547830280697398, 0.02506853618338044, 0.0354220769715167],[0.01212965558909578, 0.0195948349201492, 0.01307593021200733, 0.017775767724029, 0.01240266768446323, 0.01275380556169793, 0.01760997430149464, 0.01362338730053385, 0.01667943912747046, 0.01320793034334823]]

algonames=['NSGA*','IBEA']
for curr_dir in subdirs:
	try:
		with open(str(os.getcwd())+"/"+str(curr_dir)+"/last.txt" , "r") as out_handler:
			lines=list(out_handler.read().split('\n'))
			gens=[x.replace(" ","") for x in lines]
			gens=list(filter(None,gens))
			vals=[float(x) for x in gens]
			allcummin.append(vals)
			algonames.append(curr_dir)
	except:
		"ok"

alldict=dict(zip(algonames,allcummin))
algossort=dict(sorted(alldict.items(), key=lambda kv: numpy.median(kv[1])))
print(algossort.keys())
parts=plt.violinplot(algossort.values(),showmedians=True)
for idx,pc in enumerate(parts['bodies']):
	if idx in [1,4,7,8]:
		pc.set_facecolor('red')
plt.yscale('log')

print(algonames)
plt.xticks(range(1,len(algonames)+1),labels=algossort.keys(),fontsize=12)
plt.xlabel('Algorithms',fontsize=14)
plt.ylabel('Error',fontsize=14)
plt.title('10xIF_100x100ALL_MSE,SC,1st')

my_colors = ['r', 'b', 'r', 'r', 'g', 'g', 'g','b', 'g', 'r','r', 'r', 'r','k']
for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), my_colors):
    ticklabel.set_color(tickcolor)

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Pygmo',
                          markerfacecolor='r', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='Inspyred',
                          markerfacecolor='g', markersize=15),
                   Line2D([0], [0], marker='o', color='w', label='BluePyOpt',
                          markerfacecolor='b', markersize=15)]
plt.legend(['Pygmo','Inspyred','BluePyOpt'],loc=4, handles=legend_elements)
plt.show()

