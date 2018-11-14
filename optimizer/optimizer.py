import sys
import traceback


def main(parameters):
    """
    The main function, which starts to software according to the given command line arguments.
    
    :param parameters: the command line parameters:
        * -h help
        * -c command line
        * -g graphic interface
        
    """
    if parameters[0]=="-h":
        print("This is the command line help of Optimizer\nRecognised arguments:\n\t-h:Help\n\t-g:Graphical interface\n\t-c:Command line interface, specify the settings file in the 2nd argument")
    elif parameters[0]=="-g":
        #os.system(os.getcwd()+"/graphic.py")
        import graphic
        try:
            graphic.main(parameters[1])
        except IndexError:
            graphic.main()
    elif parameters[0]=="-c":
        try:
            import cmd_line
            try:
                cmd_line.main(parameters[1],parameters[2])
            except IndexError:
                cmd_line.main(parameters[1])
            
        except IndexError as IE:
            print IE
            traceback.print_exc()
            sys.exit("Missing filename!")
    else:
        sys.exit("Unknown arguments!\nPlease run the program with either -h, -g,-c arguments!")         
    
    


if __name__=="__main__":
    #print sys.argv
    try:
        parameters=sys.argv[1:]
        main(parameters)
    except IndexError:
        sys.exit("Missing arguments!\n Please run the program with either -h, -g,-c arguments!")
