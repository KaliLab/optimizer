import os
import shutil
import xml.etree.ElementTree as ET
import subprocess
import matplotlib.pyplot as plt

optimizer_path 	= '/home/mohacsi/Desktop/optimizer/optimizer/optimizer.py'
curr_dir  		= os.getcwd()						# base directory
orig_name 		= 'adexpif_external_ca3_pc'						# name of the working directory we want to copy
orig_dir  		= curr_dir + '/'+ 'optimizer_multirun/' + orig_name		# path of this directory
num_runs  		= 1						# how many copies we want
parallel_runs   = 1								# how many optimizations we allow to run in parallel

# define basic things for the xml files
rnd_start  = 1234							# random seed in the first run
max_eval   = 100		# number of iterations
pop_size   = 100				# population size
num_islands = 1
#csv_name   = 'input_data2.dat'	
num_param  = 16
#evo_strat = "Non Dominated Particle Swarm - Pygmo"		 					# number of parameters to optimize (needed as a command line argument)
"""self.Recom=["Evolutionary Algorithm (EA) - Inspyred","Covariance Matrix Adaptation ES (CMAES) - Pygmo",
                "Particle Swarm (PSO) - Inspyred","Indicator Based (IBEA) - Bluepyopt","L-BFGS-B - Scipy"]
        self.Inspyred=["Evolutionary Algorithm (EA) - Inspyred","Particle Swarm (PSO) - Inspyred",
                "Differential Evolution (DE) - Inspyred","Random Search - Inspyred",
                "Nondominated Sorted (NSGAII) - Inspyred","Pareto Archived (PAES) - Inspyred",
                "Simulated Annealing - Inspyred"]
        self.Scipy=["Basinhopping - Scipy","Nelder-Mead - Scipy","L-BFGS-B - Scipy"]
        self.Bluepyopt=["Nondominated Sorted (NSGAII) - Bluepyopt","Indicator Based (IBEA) - Bluepyopt"]
        self.Pygmo=["Differential Evolution (DE) - Pygmo","Self-Adaptive DE (SADE) - Pygmo",
                "Particle Swarm (PSO) - Pygmo","Exponential Evolution Strategies (XNES) - Pygmo",
                "Simple Genetic Algorithm (SGA) - Pygmo","Covariance Matrix Adaptation ES (CMAES) - Pygmo",
                "Single Differential Evolution - Pygmo","Differential Evolution (DE1220) - Pygmo",
                "Bee Colony - Pygmo","FullGrid - Pygmo"]"""

def MakeCopies(evo_name):
	for i in range(1, num_runs+1):
		new_dir = orig_dir + evo_name + '_' + str(i)
	
		if not os.path.exists(new_dir):
			shutil.copytree(orig_dir, new_dir)

def EditXMLs(evo_name,evo_strat):
	for i in range(1,num_runs+1):
		subdir   = orig_dir + evo_name +'_' + str(i)
		xml_name = subdir + '/' + '_settings.xml'

		if os.path.exists(subdir):
			tree = ET.parse(xml_name)
			root = tree.getroot()

			root.find('max_evaluation').text 	= str(float(max_eval))	
			root.find('num_islands').text		= str(float(num_islands))		
			root.find('seed').text 				= str(float(rnd_start + i))
			#root.find('input_dir').text 		= subdir + '/' + csv_name
			root.find('base_dir').text 			= subdir
			root.find('pop_size').text			= str(float(pop_size))
			root.find('evo_strat').text		= str(evo_strat)
			tree.write(xml_name)

		else:
			print(subdir + "doesn't exist")


## generate bash script
## we could do this in one step without the commands list but I it like this way

def GenerateCommands(evo_name):
	# create a list containing the commands we want to run
	commands = []
	for i in range(1, num_runs+1):
		subdir   = orig_dir + evo_name + '_' + str(i)
		xml_name = subdir + '/' + '_settings.xml'

		command = 'python ' + optimizer_path + ' -c ' + xml_name #+ ' -v_level=1'
		
		if i % parallel_runs > 0:
			command += ' &'
		command += '\n'

		commands.append(command)
	#commands.append('wait')		# does not work without this. I don't exactly understand why

	return commands

def CreateBashScript(evo_name):
	# write the commands into a file
	commands = GenerateCommands(evo_name)
	with open('optibash.sh', 'w') as bash_script:
		for line in commands:
			bash_script.write(line)

def RunOptim():
	# run the bash script
	bash_script_name = curr_dir + '/optibash.sh'
	subprocess.call(['sh', bash_script_name])


def main():
	algos = ["Non Dominated Particle Swarm - Pygmo"]
	for evo_strat in algos:
		evo_name=str.split(evo_strat," ")[0]+str.split(evo_strat," ")[-1]
		print(evo_name)
		MakeCopies(evo_name)
		EditXMLs(evo_name,evo_strat)
		CreateBashScript(evo_name)
		RunOptim()


if __name__ == '__main__':
	main()
