
import numpy
import os
import ast
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
for color,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/stat_file.txt" , "r") as out_handler:
		lines=out_handler.read().split(',')[-4].strip()
		allcummin.append(lines)

print(allcummin)