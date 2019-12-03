#!/bin/bash -x  

#SBATCH --nodes=1  

#SBATCH --ntasks=10  
 
#SBATCH --ntasks-per-node=10  

#SBATCH --cpus-per-task=4 

#SBATCH --job-name=optimizer  

#SBATCH --time=0-01:00:00 

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

export PYTHONPATH=/p/home/jusers/mohacsi1/jureca/.local/lib/python3.6/site-packages:$PYTHONPATH 


srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_1/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_2/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_3/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_4/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_NondominatedBluepyopt_5/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_IndicatorBluepyopt_1/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_IndicatorBluepyopt_2/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_IndicatorBluepyopt_3/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_IndicatorBluepyopt_4/_settings.xml &
srun python ~/Desktop/optimizer/optimizer/optimizer.py -c /home/mohacsi/Desktop/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_IndicatorBluepyopt_5/_settings.xml &
