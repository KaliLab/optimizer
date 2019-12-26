#!/bin/bash -x  

#SBATCH --nodes=10  

#SBATCH --ntasks=10  
 
#SBATCH --ntasks-per-node=1  

#SBATCH --cpus-per-task=48 

#SBATCH --job-name=optimizer  

#SBATCH --time=0-10:00:00 

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
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_1/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_2/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_3/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_4/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_5/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_6/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_7/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_8/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_9/_settings.xml &
srun python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/Luca_modell_python3_RandomInspyred_10/_settings.xml 
