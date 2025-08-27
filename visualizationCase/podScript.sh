#!/bin/bash
#SBATCH --job-name=podJob
#SBATCH --partition=large
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --time=5-00:00:00
#SBATCH --output=log.%j.out
#SBATCH --error=log.%j.err

# Load required modules
module purge
module load gcc/12.3.0
module load miniconda3/24.7.1-gcc-12.3.0-jyvq4fr
module load openmpi/4.1.6-gcc-12.3.0-7ymeek3

# Activate your correct conda environment
source activate podEnv

# Source OpenFOAM
export WM_PROJECT_INST_DIR=$HOME
source $HOME/OpenFOAM-9/etc/bashrc

# Go to job directory
cd $SLURM_SUBMIT_DIR

# Run Python script
python vis2.py

