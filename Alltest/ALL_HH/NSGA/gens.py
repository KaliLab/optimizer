
import numpy
import os
import ast
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
for color,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/bpopt_stats.txt" , "r") as out_handler:
		lines=float(out_handler.read().split(',')[-1][:-2])
		allcummin.append(lines)

print(allcummin)
