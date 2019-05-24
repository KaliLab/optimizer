import os
import shutil
import xml.etree.ElementTree as ET
import subprocess
import matplotlib.pyplot as plt

optimizer_path 	= '/home/mohacsi/work/optimizer/optimizer/optimizer.py'
curr_dir  		= os.getcwd()						# base directory
orig_name 		= 'adexpif_external_ca3_pc'						# name of the working directory we want to copy
orig_dir  		= curr_dir + '/'+ 'optimizer_multirun6/' + orig_name		# path of this directory
num_runs  		= 10						# how many copies we want
parallel_runs   = 5								# how many optimizations we allow to run in parallel

# define basic things for the xml files
rnd_start  = 1234							# random seed in the first run
max_eval   = 100				# number of iterations
pop_size   = 100				# population size
num_islands = 1

csv_name   = 'ca3_pc_v2_4.csv'				# the csv we want to use
sim_script = 'teststeps_optim5.py'			# the script for the external simulator
num_param  = 10	
evo_strat = "Basinhopping - Scipy"		 					# number of parameters to optimize (needed as a command line argument)


def MakeCopies():
	for i in range(1, num_runs+1):
		new_dir = orig_dir + '_' + str(i)
	
		if not os.path.exists(new_dir):
			shutil.copytree(orig_dir, new_dir)

def EditXMLs():
	for i in range(1,num_runs+1):
		subdir   = orig_dir + '_' + str(i)
		xml_name = subdir + '/' + '_settings.xml'

		if os.path.exists(subdir):
			tree = ET.parse(xml_name)
			root = tree.getroot()

			root.find('max_evaluation').text 	= str(float(max_eval))	
			root.find('num_islands').text		= str(float(num_islands))		
			root.find('seed').text 				= str(float(rnd_start + i))
			root.find('sim_command').text 		= 'python ' + subdir + '/' + sim_script + ' ' + str(int(num_param))
			root.find('input_dir').text 		= subdir + '/' + csv_name
			root.find('base_dir').text 			= subdir
			root.find('pop_size').text			= str(float(pop_size))
			root.find('evo_strat').text		= str(evo_strat)
			tree.write(xml_name)

		else:
			print(subdir + "doesn't exist")


## generate bash script
## we could do this in one step without the commands list but I it like this way

def GenerateCommands():
	# create a list containing the commands we want to run
	commands = []
	for i in range(1, num_runs+1):
		subdir   = orig_dir + '_' + str(i)
		xml_name = subdir + '/' + '_settings.xml'

		command = 'python ' + optimizer_path + ' -c ' + xml_name #+ ' -v_level=1'
		
		if i % parallel_runs > 0:
			command += ' &'
		command += '\n'

		commands.append(command)
	commands.append('wait')		# does not work without this. I don't exactly understand why

	return commands

def CreateBashScript():
	# write the commands into a file
	commands = GenerateCommands()
	with open('run_simulations.sh', 'w') as bash_script:
		for line in commands:
			bash_script.write(line)

def RunOptim():
	# run the bash script
	bash_script_name = curr_dir + '/run_simulations.sh'
	subprocess.call(['sh', bash_script_name])


def main():
	MakeCopies()
	EditXMLs()
	CreateBashScript()
	RunOptim()


if __name__ == '__main__':
	main()
