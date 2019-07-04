
import matplotlib.pyplot as plt
import numpy
import os
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
algonames=[]
print(algonames)
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
algossort=dict(sorted(alldict.items(), key=lambda kv: kv[1]))
print(algossort.keys())
parts=plt.violinplot(algossort.values(),showmedians=True)
for idx,pc in enumerate(parts['bodies']):
	if idx in [4,5]:
		pc.set_facecolor('red')
plt.yscale('log')

print(algonames)
plt.xticks(range(1,len(algonames)+1),labels=algossort.keys())
plt.xlabel('Algorithms')
plt.ylabel('Score Value')
plt.title('10xSIMP_100x100ALL_MSE,SC,AP_AMP+W')
plt.show()

