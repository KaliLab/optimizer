import matplotlib.pyplot as plt
import numpy
import os
allcummin=[]
subdirs=list(next(os.walk('.'))[1])
for idx,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/stat_file.txt" , "r") as out_handler:
		fs=out_handler.read().split('\n')[:-1]
		vals=[float(numpy.dot(eval(x)[3],[1/3]*12)) for x in fs]
		vals=numpy.minimum.accumulate(vals)
		allcummin.append(vals)

minl=[numpy.min(x) for x in zip(*allcummin)]
maxl=[numpy.max(x) for x in zip(*allcummin)]
medl=[numpy.median(x) for x in zip(*allcummin)]

	
with open("min.txt" , "w") as out_handler:
	for line in minl:
		out_handler.write(str(line)+"\n")
with open("max.txt" , "w") as out_handler:
	for line in maxl:
		out_handler.write(str(line)+"\n")
with open("median.txt" , "w") as out_handler:
	for line in medl:
		out_handler.write(str(line)+"\n")
			
