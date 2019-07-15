import matplotlib.pyplot as plt
import numpy
import os
allmin=[]

allcummin=[]
for i in range(1,11):
	cummin=[]
	params=[]
	with open(str(os.getcwd())+"/hh_pas_surrogate_"+str(i)+"/bpopt_pop.txt" , "r") as out_handler:
		out_handler.readline()
		lines=out_handler.readlines()
		for line in lines:
			line1=line[line.find('(')+1:line.find(')')]
			lina=line1.split(",")
			line2=line[line.find('[')+1:line.find(']')]
			linb=line2.split(",")
			cummin.append(sum([float(x) for x in lina]))
			params.append([float(x) for x in linb])
	minsa=[]
	paras=[]
	for x in range(1,101):
		minsa.append(cummin[100*(x-1):100*x])
		paras.append(params[100*(x-1):100*x])
	bpr=[]
	for mns,prs in zip(minsa,paras):
		bpr.append(prs[mns.index(min(mns))])

	x=numpy.array([i[0] for i in bpr])
	y=numpy.array([i[1] for i in bpr])
	z=numpy.array([i[2] for i in bpr])
	xif=x-0.12
	yif=y-0.036
	zif=z-0.0003
	lengt=numpy.sqrt(xif**2+yif**2+zif**2)
	allcummin.append(lengt)
allmed=[numpy.median(x) for x in zip(*allcummin)]
allmin=[numpy.min(x) for x in zip(*allcummin)]
allmax=[numpy.max(x) for x in zip(*allcummin)]
plt.plot(allmed)
plt.plot(allmin)
plt.plot(allmax)
plt.show()
#ax.scatter(0.12,0.036,0.0003,'r')
#ax.quiver(x[:-1],y[:-1],z[:-1],x[1:]-x[:-1],y[1:]-y[:-1],z[1:]-z[:-1])
"""


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
plt.show()"""
