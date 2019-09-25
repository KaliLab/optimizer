import os
import shutil
import xml.etree.ElementTree as ET
import subprocess
import matplotlib.pyplot as plt

optimizer_path 	= '/p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py'
curr_dir  		= os.getcwd()						# base directory
orig_name 		= 'hh_pas_surrogate'						# name of the working directory we want to copy
orig_dir  		= curr_dir + '/'+ 'optimizer_multirun/' + orig_name		# path of this directory
num_runs  		= 2						# how many copies we want
parallel_runs   = 2								# how many optimizations we allow to run in parallel

# define basic things for the xml files
rnd_start  = 1234							# random seed in the first run
max_eval   = 100			# number of iterations
pop_size   = 100				# population size
num_islands = 1
csv_name   = 'input_data2.dat'	
num_param  = 3	
evo_strat = "Particle Swarm (PSO) - Inspyred"		 					# number of parameters to optimize (needed as a command line argument)
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
	commands = ["""#!/bin/bash -x  \n
#SBATCH --nodes=2  \n
#SBATCH --ntasks=2  \n
#SBATCH --ntasks-per-node=1  \n
#SBATCH --cpus-per-task=100  \n
#SBATCH --job-name=optimizer  \n
#SBATCH --time=0-05:10:00 \n
#SBATCH --error=mpi_err.%j \n
#SBATCH --output=mpi_out.%j \n
#SBATCH --account=vsk25 \n
#SBATCH --partition=booster \n

set -e \n
set -x \n

echo ok \n

module --force purge all \n

echo ok1 \n

module use /usr/local/software/jureca/OtherStages \n
module load Architecture/KNL \n
module load Stages/Devel-2019a \n
module load GCC/8.3.0 \n
module load ParaStationMPI/5.2.2-1 \n
module load NEURON/7.6.5-Python-3.6.8 \n
module load Python/3.6.8 \n
module load SciPy-Stack/2019a \n


export PYTHONPATH=/p/home/jusers/mohacsi1/jureca/.local/lib/python3.6/site-packages:$PYTHONPATH \n
echo ok2 \n """]
	for i in range(1, num_runs+1):
		subdir   = orig_dir + '_' + str(i)
		xml_name = subdir + '/' + '_settings.xml'

		command = 'srun -N 1 -n 1 python ' + optimizer_path + ' -c ' + xml_name #+ ' -v_level=1'
		
		if i % parallel_runs > 0:
			command += ' &'
		command += '\n'

		commands.append(command)
	#commands.append('wait')		# does not work without this. I don't exactly understand why

	return commands

def CreateBashScript():
	# write the commands into a file
	commands = GenerateCommands()
	with open('optibash.sbatch', 'w') as bash_script:
		for line in commands:
			bash_script.write(line)

def RunOptim():
	# run the bash script
	bash_script_name = curr_dir + '/optibash.sbatch'
	subprocess.call(['sbatch', bash_script_name])


def main():
	MakeCopies()
	EditXMLs()
	CreateBashScript()
	RunOptim()


if __name__ == '__main__':
	main()
