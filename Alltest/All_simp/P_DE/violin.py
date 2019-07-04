
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

minl=[x[-1] for x in allcummin]
print(minl)
with open(str(os.getcwd())+"/last.txt" , "w") as out_handler:
	for line in minl:
		out_handler.write(str(line)+" \n")
