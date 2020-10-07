#!/bin/bash -x  

#SBATCH --nodes=10  

#SBATCH --ntasks=10  
 
#SBATCH --ntasks-per-node=1  

#SBATCH --cpus-per-task=100  

#SBATCH --job-name=optimizer  

#SBATCH --time=0-24:00:00 

#SBATCH --error=mpi_err.%j 

#SBATCH --output=mpi_out.%j 

#SBATCH --account=vsk25 

#SBATCH --partition=booster 


set -e 

set -x 


echo ok 


module --force purge all 


echo ok1 


module use /usr/local/software/jureca/OtherStages 

module load Architecture/KNL 

module load Stages/Devel-2019a 

module load GCC/8.3.0 

module load ParaStationMPI/5.2.2-1 

module load NEURON/7.6.5-Python-3.6.8 

module load Python/3.6.8 

module load SciPy-Stack/2019a 


export OMP_NUM_THREADS=100

export PYTHONPATH=/p/home/jusers/mohacsi1/jureca/.local/lib/python3.6/site-packages:$PYTHONPATH 

echo ok2 
 srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_1/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_2/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_3/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_4/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_5/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_6/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_7/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_8/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_9/_settings.xml &
srun -N 1 -n 1 python /p/home/jusers/mohacsi1/jureca/optimizer/optimizer/optimizer.py -c /p/home/jusers/mohacsi1/jureca/optimizer/ALLtest/optimizer_multirun/hh_pas_surrogateNondominatedPygmo_10/_settings.xml
