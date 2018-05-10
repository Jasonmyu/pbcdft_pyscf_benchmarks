#!/bin/sh
#SBATCH --job-name=kccgf_graphene
#SBATCH --partition=parallel,smallmem,serial
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#SBATCH --mem=120000
#SBATCH -t 96:00:00
#SBATCH --output=new_slurm.out
#SBATCH --error=slurm.err

CURRDIR=$SLURM_SUBMIT_DIR
WORKDIR=$SLURM_SUBMIT_DIR
export TMPDIR=$SLURM_SUBMIT_DIR

echo "tmpdir is set to $TMPDIR"

# loading all necessary modules...
source $HOME/module_load_dev.sh

cd $WORKDIR

export OMP_NUM_THREADS=28

srun -c $OMP_NUM_THREADS python pyscf_c.py
