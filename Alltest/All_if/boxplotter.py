
import matplotlib.pyplot as plt
import numpy
import os
subdirs=list(next(os.walk('.'))[1])
allcummin=[[0.05052349312343095, 0.03827316432930312, 0.02391663684933393, 0.0306452331356941, 0.03998299644451, 0.0402464057116343, 0.0319478972571454, 0.0547830280697398, 0.02506853618338044, 0.0354220769715167],[0.01212965558909578, 0.0195948349201492, 0.01307593021200733, 0.017775767724029, 0.01240266768446323, 0.01275380556169793, 0.01760997430149464, 0.01362338730053385, 0.01667943912747046, 0.01320793034334823]]

algonames=['BP_NSGA','IBEA']
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

plt.violinplot(allcummin,showmedians=True)
plt.yscale('log')

print(algonames)
plt.xticks(range(1,len(algonames)+1),labels=algonames)
plt.xlabel('Algorithms')
plt.ylabel('Score Value')
plt.title('10xIF_100x100ALL_MSE,SC,1st')
plt.show()

