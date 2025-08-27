#!/bin/bash
#SBATCH --job-name=openfoam_test
#SBATCH --partition=medium
#SBATCH --nodelist=cn[07]
#SBATCH --ntasks=40
#SBATCH --time=5-00:00:00
#SBATCH --output=log.%j.out
#SBATCH --error=log.%j.err


# Load OpenFOAM environment
module purge
#module load gcc/12.3.0-gcc-12.3.0-b3lfzmk
module load gcc/10.2.0-gcc-12.3.0-4miv5iz
#module load openfoam/v9
#module load openmpi4/4.1.6
#module load openmpi/4.1.6-gcc-12.3.0-7ymeek3

#module load glibc/2.28-gcc-12.3.0-cfr5e6b 
#module load gnu12/12.3.0
export PATH=$HOME/openmpi-4.1.6-gcc10/bin:$PATH
export LD_LIBRARY_PATH=$HOME/openmpi-4.1.6-gcc10/lib:$LD_LIBRARY_PATH 
#source /iitgn/apps/spack/opt/spack/linux-rocky8-skylake_avx512/gcc-12.3.0/openfoam-org-9-*/etc/bashrc
export WM_PROJECT_INST_DIR=$HOME
source $HOME/OpenFOAM-9/etc/bashrc

# Move to case directory
cd $SLURM_SUBMIT_DIR

# Optional: Clean old results
# foamCleanTutorials

#Meshing
#blockMesh
rm -r pro*
checkMesh
# Decompose domain for parallel run
decomposePar -force

# Run the solver in parallel
mpirun -np 40 pimpleFoam -parallel
#pimpleFoam
#pisoFoam
# Reconstruct final fields
reconstructPar

