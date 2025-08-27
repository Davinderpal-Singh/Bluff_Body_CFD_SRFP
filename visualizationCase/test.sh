#!/bin/bash
#SBATCH --job-name=testEcho
#SBATCH --partition=medium 
#SBATCH --nodelist=cn[08]
#SBATCH --ntasks=1
#SBATCH --time=00:05:00
#SBATCH --output=log.%j.out
#SBATCH --error=log.%j.err

echo "HELLO FROM SLURM"

