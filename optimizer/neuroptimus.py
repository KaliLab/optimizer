import sys
import traceback
import getopt

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
		elif o=="-g":
			import graphic
			try:
				graphic.main(a)
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
			except IndexError as IE:
				print(IE)
				traceback.print_exc()
				sys.exit("Missing filename!")
	sys.exit("Unknown arguments!\nPlease run the program with either -h, -g,-c arguments!")         
    
    


if __name__=="__main__":
    #print sys.argv
    #try:
        opts, args = getopt.getopt(sys.argv[1:], "c:gh", ["help"])
        main(opts)
    #except IndexError:
        #sys.exit("Missing arguments!\n Please run the program with either -h, -g,-c arguments!")
