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
		else:
			print("Invalid arguement.\nRecognised arguments:\n\t-h:Help\n\t-g:Graphical interface\n\t-c:Command line interface, specify the settings file in the 2nd argument")
			         
    
    


if __name__=="__main__":
    #print sys.argv
    try:
    	opts, args = getopt.getopt(sys.argv[1:], "c:gh", ["help"])
    except getopt.GetoptError as err:
            sys.exit("Invalid argument! Please run the program with -h argument for help!")
    main(opts)
   

