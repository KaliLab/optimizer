import matplotlib.pyplot as plt
import numpy
import os
allmin=[]

allcummin=[]
for i in range(1,2):
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
lengt=numpy.sqrt(x**2+y**2+z**2)
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlabel('gNA')
ax.set_ylabel('gK')
ax.set_zlabel('gL')
ax.scatter(x,y,z)
ax.plot(x,y,z)
ax.scatter(0.12,0.036,0.0003,'r')
#ax.quiver(x[:-1],y[:-1],z[:-1],x[1:]-x[:-1],y[1:]-y[:-1],z[1:]-z[:-1])
"""
ax.scatter(x[:2],y[:2],z[:2])
ax.quiver(x[0],y[0],z[0],(x[1]-x[0]),(y[1]-y[0]),z[1]-z[0],normalize=True)"""
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlabel('gNA')
ax.set_ylabel('gK')
ax.set_zlabel('gL')
ax.scatter(x[-10:],y[-10:],z[-10:])
ax.plot(x[-10:],y[-10:],z[-10:])
ax.scatter(0.12,0.036,0.0003,'r')
ans=(x[-1]-0.12,y[-1]-0.036,z[-1]-0.0003)
print(ans)
plt.show()

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
