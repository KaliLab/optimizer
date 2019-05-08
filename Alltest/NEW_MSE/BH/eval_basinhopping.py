import numpy as np
import matplotlib.pyplot as plt
from string import count, split, strip

path = '/home/tmp/Documents/Tesztek/KOKI/OPTIMIZATION/HH_NEW_PLUS/BH/0.3'
num_runs = 10
num_iter = 100
num_repet = 1

every_fit = np.ndarray(shape = (num_runs, num_iter))

for i in range(1,num_runs+1):
	print (i)
	file_name = path + '/hh_pas_surrogate_%r/basinhopping.log' % i
	file = open(file_name)


	s="starting point"
	scores=[]
	best_scores=[]
	for line in file:
	    if count (line, s) != 1 and len(line.split('\t'))==3:
		score=float(line.split('\t')[1])
		scores.append(score)
	every_fit[i-2,:] = np.array(scores)
	scores=[]
#print every_fit


fig1 = plt.figure()

for idx in range(num_runs):
	for i in range(num_iter):
		every_fit[idx,i] = np.min(every_fit[idx,:(i+1)])

	plt.plot(every_fit[idx,:], label=str(idx+1))

plt.legend()
plt.xlabel('iteration')
plt.ylabel('minimal fitness score')
plt.yscale('log')
plt.ylim([0, 1])

mean_t = []
std_t  = []
min_t =	[]
max_t = []
median_t = []
for i in range(num_iter):
		for j in range(num_repet):
			mean_t.append(np.mean(every_fit[:,i]))
			std_t.append(np.std(every_fit[:,i]))
			min_t.append(np.amin(every_fit[:,i]))
			max_t.append(np.amax(every_fit[:,i]))
			median_t.append(np.median(every_fit[:,i]))


mean_minus_std = np.array(mean_t) - np.array(std_t)
mean_plus_std  = np.array(mean_t) + np.array(std_t)

fig2 = plt.figure()
plt.plot(mean_t, label='Mean score')
plt.plot(mean_minus_std, label='Mean - std')
plt.plot(mean_plus_std, label='Mean + std')
plt.xlabel('iteration')
plt.ylabel('score value')
plt.yscale('log')
plt.ylim([0, 1])
plt.legend()


print 'mean of the results:\t%r' % mean_t[-1]
print 'standard deviation\t%r' % std_t[-1]


np.savetxt(path + '/mean.txt', mean_t)
np.savetxt(path + '/mean_minus_std.txt', mean_minus_std)
np.savetxt(path + '/mean_plus_std.txt', mean_plus_std)
np.savetxt(path + '/min.txt', min_t)
np.savetxt(path + '/max.txt', max_t)
np.savetxt(path + '/median.txt', median_t)


#plt.show()
