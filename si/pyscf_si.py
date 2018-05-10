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

cell = gto.Cell()
# .a is a matrix for lattice vectors.
cell.a = '''
5.430697500  0            0
0            5.430697500  0
0            0            5.430697500'''
cell.atom = '''
              Si    0.000000000    0.000000000    0.000000000
              Si    0.000000000    2.715348700    2.715348700
              Si    2.715348700    2.715348700    0.000000000
              Si    2.715348700    0.000000000    2.715348700
              Si    4.073023100    1.357674400    4.073023100
              Si    1.357674400    1.357674400    1.357674400
              Si    1.357674400    4.073023100    4.073023100
              Si    4.073023100    4.073023100    1.357674400
              '''
cell.basis = 'gth-dzvp'
cell.pseudo = 'gth-pade'
cell.verbose = 4
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

