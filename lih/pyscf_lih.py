#!/usr/bin/env python

'''
Gamma point Hartree-Fock/DFT

The 2-electron integrals are computed using Poisson solver with FFT by default.
In most scenario, it should be used with pseudo potential.
'''

# Note import path which is different to molecule code
from pyscf.pbc import gto, scf, dft
import numpy
import time
from pyscf.pbc.tools import lattice,pyscf_ase
import ase

cell = gto.Cell()
ase_atom = lattice.get_ase_atom('lih')
cell.atom=pyscf_ase.ase_atoms_to_pyscf(ase_atom)
cell.a=ase_atom.cell
cell.basis = 'gth-szv'
cell.pseudo = 'gth-pade'
cell.build()

#mf = scf.RHF(cell)
#ehf = mf.kernel()
#print("HF energy (per unit cell) = %.17g" % ehf)

start = time.time()

mf = dft.RKS(cell)
mf = mf.newton()
mf.xc = 'lda'
mf.direct_scf=True
edft = mf.kernel()
print("DFT energy (per unit cell) = %.17g" % edft)


end = time.time()
print 'DFT compute time', (end-start)
#
# By default, DFT use uniform cubic grids.  It can be replaced by atomic grids.
#
#mf = dft.RKS(cell)
#mf.grids = dft.gen_grid.BeckeGrids(cell)
#mf.xc = 'lda'
#mf.kernel()

#
# Second order SCF solver can be used in the PBC SCF code the same way in the
# molecular calculation
#
#mf = scf.RHF(cell).newton()
#mf.kernel()

