
import numpy
import os
import ast
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
for color,curr_dir in enumerate(subdirs):
	minl=[100]
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/island_inds.txt" , "r") as out_handler:
		lines=out_handler.readlines()
		for line in lines:
			if not line[0].isspace():
				
				lina=line.split(", ")
				lin=lina[2]
				currmin=float(lin[1:-1])
				if currmin>minl[-1]:
					minl.append(minl[-1])
				else:
					minl.append(currmin)
	allcummin.append(minl[1:])

minl=[numpy.min(x) for x in zip(*allcummin)]
maxl=[numpy.max(x) for x in zip(*allcummin)]
medl=[numpy.median(x) for x in zip(*allcummin)]
print(minl)
with open(str(os.getcwd())+"/min.txt" , "w") as out_handler:
	for line in minl:
		out_handler.write(str(line)+" \n")
with open(str(os.getcwd())+"/max.txt" , "w") as out_handler:
	for line in maxl:
		out_handler.write(str(line)+" \n")
with open(str(os.getcwd())+"/median.txt" , "w") as out_handler:
	for line in medl:
		out_handler.write(str(line)+" \n")
with open(str(os.getcwd())+"/all_stat.txt" , "w") as out_handler:
	for line in allcummin:
		out_handler.write(str(line)+" \n")