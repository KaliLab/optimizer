import sys
#provides various functions and variables that are used to manipulate different parts of the Python runtime environment
import traceback
#This module provides a standard interface to extract, format and print stack traces of Python programs. It exactly mimics the behavior of the Python interpreter when it prints a stack trace. This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.

import getopt
#like args[] in Java

def main(parameters):
	"""
	The main function, which starts to software according to the given command line arguments.

	:param parameters: the command line parameters:
	* -h help
	* -c command line
	* -g graphic interface

	"""
	for o,a in parameters:
		if o=="-h":
			print("This is the command line help of Optimizer\nRecognised arguments:\n\t-h:Help\n\t-g:Graphical interface\n\t-c:Command line interface, specify the settings file in the 2nd argument")
			sys.exit()
		elif o=="-g":
			import graphic
			try:
				graphic.main(a)
				sys.exit()
			except IndexError as IE:
				print(IE)
				traceback.print_exc()
		elif o=="-c":
			try:
				import cmd_line
			except:
				sys.exit("Cannot find command line file!")
			try:
				cmd_line.main(a)
				sys.exit()
			except IndexError as IE:
				print(IE)
				traceback.print_exc()
				sys.exit("Missing filename!")
			         
    
    


if __name__=="__main__":
    #print sys.argv
    try:
    	opts, args = getopt.getopt(sys.argv[1:], "c:gh", ["help"])
    except getopt.GetoptError as err:
            sys.exit("Invalid argument! Please run the program with -h argument for help!")
    main(opts)
   

