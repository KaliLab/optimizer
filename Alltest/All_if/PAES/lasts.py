
import numpy
import os
import ast
subdirs=list(next(os.walk('.'))[1])
allcummin=[]
for color,curr_dir in enumerate(subdirs):
	with open(str(os.getcwd())+"/"+str(curr_dir)+"/stat_file.txt" , "r") as out_handler:
		lines=out_handler.read().split('\n')[-2]
		print(curr_dir)
		best=lines[lines.rfind("(")+1:lines.rfind(")")].split(',')
		fltbest=[float(x) for x in best]
		allcummin.append(numpy.mean(fltbest))

print(allcummin)
with open("last.txt" , "w") as out_handler:
	[out_handler.write(str(x)+"\n") for x in allcummin]
