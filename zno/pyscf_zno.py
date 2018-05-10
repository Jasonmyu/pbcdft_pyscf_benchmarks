#!/usr/bin/env python

from pyscf.pbc import gto, scf, dft
import numpy
import time
from pyscf.pbc.tools import lattice,pyscf_ase
import ase
from ase.build import bulk

cell = gto.Cell()
ase_atom = bulk('ZnO','wurtzite',a=3.25*1.889725989,c=5.2*1.889725989)
cell.atom=pyscf_ase.ase_atoms_to_pyscf(ase_atom)
cell.a=ase_atom.cell
cell.basis = 'gth-dzvp-molopt'
cell.pseudo = 'gth-pade'
cell.verbose=4
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

