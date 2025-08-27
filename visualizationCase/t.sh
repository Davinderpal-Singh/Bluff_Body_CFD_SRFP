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
module purge  # Unload everything

module load gcc/12.3.0
module load hwloc/2.7.2
module load openmpi/5.0.8  # or openmpi/5.0.5-gcc-12.3.0-fww5qcd


# Activate your correct conda environment
source activate podEnv

# Source OpenFOAM
export WM_PROJECT_INST_DIR=$HOME
source $HOME/OpenFOAM-9/etc/bashrc

# Go to job directory
cd $SLURM_SUBMIT_DIR

# Run Python script
python new_mode_ag.py

