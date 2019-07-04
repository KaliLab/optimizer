
import numpy
import os
import ast
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
for color,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/island_inds.txt" , "r") as out_handler:
		lines=out_handler.read().split(',')[-3].strip().strip("[]")
		allcummin.append(lines)

print(allcummin)
with open("last.txt" , "w") as out_handler:
	[out_handler.write(x+"\n") for x in allcummin]