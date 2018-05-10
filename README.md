# pbcdft_pyscf_benchmarks
PBC/DFT benchmark files of various crystals for Pyscf

Pyscf dev version: 712e40e23e7a7c928f2e0c27498b3fa5f122454b

Parameters used:

cell.basis = 'gth-dzvp'

cell.pseudo = 'gth-pade'
mf = mf.newton()

mf.xc = 'lda'

mf.direct_scf=True

Note that basis sets for several atoms used in this benchmark pack may need to be added to:

/home/jyu5/pyscf/pyscf/pbc/gto/basis

By default, several gth-dzvp-molopt.dat basis sets were added for use in this pack.
