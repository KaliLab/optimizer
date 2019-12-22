#!/bin/bash -x  

#SBATCH --nodes=1  

#SBATCH --ntasks=1  
 
#SBATCH --ntasks-per-node=1  

#SBATCH --cpus-per-task=48 

#SBATCH --job-name=optimizer  

#SBATCH --time=0-24:00:00 

#SBATCH --error=mpi_err.%j 

#SBATCH --output=mpi_out.%j 

#SBATCH --account=vsk25 

#SBATCH --partition=batch 


set -e
set -x

module --force purge all


module use /usr/local/software/jureca/OtherStages
module load Stages/Devel-2019a
module load GCC/8.3.0
module load ParaStationMPI/5.2.2-1
module load NEURON/7.6.5-Python-3.6.8
module load SciPy-Stack/2019a-Python-3.6.8
module load Jupyter/2019a-Python-3.6.8-damian


export PYTHONPATH=/p/home/jusers/mohacsi1/jureca/.local/lib/python3.6/site-packages:$PYTHONPATH 
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_1/_settings.xml 
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_2/_settings.xml
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_3/_settings.xml
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_4/_settings.xml
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_5/_settings.xml

