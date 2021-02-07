# <img src="docs/VERSION/classes/icon.png" class="largeicon"> ITensor Library Classes and Methods #

Detailed information about every method and function in the ITensor library.

The documentation may omit minor details that do not change how you use a method,
like describing a particular function as `f(ITensor T)` even though
its actual signature is `f(ITensor const& T)`.

## Utilities

* [[Reading and Writing Objects to Disk|classes/readwrite]]

* [[Support for MPI (Message Passing Interface) Parallelism|classes/parallel]]

* Support for working with lattices:
  - [[LatticeBond Objects|classes/latticebond]]
  - [[Functions for Making Lattices|classes/lattice_functions]]

* [[BondGate|classes/bondgate]] - type for making quantum circuits or time-evolution gates

## Index

* [[Index|classes/index]]. Tensor index.

* Special Index modes:

  - [[QN Index|classes/index_qn]]. Index carrying QN block information.

* [[IndexVal|classes/indexval]]. Index-value pair.

* [[IndexSet|classes/indexset]]. Container for storing indices.

* [[QN|classes/qn]]. Abelian quantum numbers.

## ITensor

* [[ITensor|classes/itensor]]. The elementary tensor type. <br/>

* Sparse ITensors:

    - [[QN ITensor|classes/qnitensor]]
    - [[Single Element ITensor|classes/single_itensor]]
    - [[Combiner|classes/combiner]]
    - [[Delta and Diagonal ITensor|classes/diag_itensor]]


* [[Tensor Decompositions|classes/decomp]]. Singular value decomposition, density matrix diagonalization, etc.

## Matrix product states (MPS) and matrix product operators (MPO)

* [[SiteSet|classes/siteset]]. Collection of site objects, defining a Hilbert space and local operators. <br/>
  - [[SpinHalf and SpinHalfSite|classes/spinhalf]]. S=1/2 spin sites. <br/>
  - [[SpinOne and SpinOneSite|classes/spinone]]. S=1 spin sites. <br/>
  - [[Boson and BosonSite|classes/boson]]. Spinless boson sites with adjustable max occupancy. <br/>
  - [[Fermion and FermionSite|classes/fermion]]. Spinless fermion sites. <br/>
  - [[Electron and ElectronSite|classes/electron]]. Spinful fermion sites. <br/>
  - [[tJ and tJSite|classes/tj]]. t-J model sites. <br/>
  - [[CustomSpin and CustomSpinSite|classes/customspin]]. Spin sites with custom spin S size. <br/>

* [[MPS|classes/mps]]. Matrix product state class. <br/>

* [[MPO|classes/mpo]]. Matrix product operator class. <br/>

* [[Algorithms for MPS and MPO|classes/mps_mpo_algs]]. <br/>

* [[AutoMPO|classes/autompo]]. System for making MPOs from sums of local operators. <br/>

## Density matrix renormalization group (DMRG)

* [[Sweeps|classes/sweeps]]. Class for specifying DMRG accuracy parameters.

* [[DMRG|classes/dmrg]]. Interface for running DMRG calculations.

<!--

* [[Spectrum|classes/spectrum]]. Class for storing & analyzing density matrix eigenvalue spectrum.

* [[InitState|classes/initstate]]. Class for initializing matrix product states.

To Do:
- gateTEvol function
- STOP_DMRG file feature of DMRG codes
- InitState
- Spectrum
- idmrg
- Args
- LocalOp, LocalMPO, etc.
- Observer / DMRGObserver
- DMRGObserver related dmrg functions?
-->

