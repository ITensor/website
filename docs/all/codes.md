
# Sections

* [Julia ITensor Codes](#julia_codes)
* [C++ ITensor Version 3 Codes](#cppv3_codes)
* [C++ ITensor Version 2 Codes](#cppv2_codes)

<a name="julia_codes"></a>
# Julia ITensor Codes

Open-source codes based on ITensor for a variety projects and tasks.
If you have a high-quality code you'd like listed here, please
<a href="about.html">contact us</a>. Codes extending core ITensor
features may become candidates for inclusion in ITensor at a later date.

(Codes listed as maintained by "ITensor" are officially maintained by the developers
of the ITensor library and will be tested against and updated along with the ITensor library.
Other codes are maintained separately from ITensor by the maintainers
shown next to each code. Please contact them directly if you have any issues 
with or questions about the codes.)

<br/>
<br/>

<table id="codes" style="border-collapse: collapse; border-spacing: 10px;">

<tr>
<td class="name">
Name
</td>
<td class="contrib">
<b>Maintainers</b>
</td>
<td class="descrip">
<b>Description</b>
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/joselado/dmrgpy" target="_blank"> 
DMRGPy
</a> 
</td>
<td class="contrib">
Jose Lado
</td>
<td class="descrip">
DMRGPy is a Python library to compute quasi-one-dimensional spin chains and fermionic systems using matrix product states with DMRG as implemented in ITensor. Most of the computations can be performed both with DMRG and exact diagonalization for small systems, which allows one to benchmark the results.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/mtfishman/GaussianMatrixProductStates.jl" target="_blank"> 
Gaussian Matrix Product States
</a> 
</td>
<td class="contrib">
<a href="https://www.simonsfoundation.org/team/matthew-fishman/">Matt Fishman</a>
</td>
<td class="descrip">
A package for creating the matrix product state (MPS) of a free fermion (Gaussian) state.
This package uses a technique based on PRB 92, 075132 (arxiv:1504.07701)
which deterministically computes a nearly optimal MPS approximation of a given
free fermion or Gaussian state.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/ITensor/ITensorsGPU.jl" target="_blank"> 
ITensorsGPU
</a> 
</td>
<td class="contrib">
Katharine Hyatt
</td>
<td class="descrip">
ITensorsGPU extends the ITensor library by allowing ITensors to have GPU storage. These ITensors are allocated in GPU memory and use fast, parallelized CUDA GPU routines for operations such as tensor contraction and factorization, which can result in very large speedups.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/ITensor/ITensorsVisualization.jl" target="_blank"> 
ITensors Visualization
</a> 
</td>
<td class="contrib">
<a href="https://www.simonsfoundation.org/team/matthew-fishman/">Matt Fishman</a>
</td>
<td class="descrip">
Visualize tensor contractions performed with the ITensor library. The visualizations
are interactive (tensor positions are draggable) and useful information about indices is shown: 
line widths correspond to
dimensions and quantum number is shown when applicable.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/YiqingZhouKelly/LinQu.jl" target="_blank"> 
LinQu
</a> 
</td>
<td class="contrib">
<a href="https://github.com/YiqingZhouKelly">Yiqing Zhou</a>
</td>
<td class="descrip">
Julia library for quantum circuit simulation using tensor networks
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/GTorlai/PastaQ.jl" target="_blank"> 
PastaQ
</a> 
</td>
<td class="contrib">
<a href="https://www.simonsfoundation.org/team/giacomo-torlai/">Giacomo Torlai</a><br/>
<a href="https://www.simonsfoundation.org/team/matthew-fishman/">Matt Fishman</a>
</td>
<td class="descrip">
Package for Simulation, Tomography and Analysis of Quantum Computers. Features include
simulation of quantum circuits, scalable quantum state tomography (pure and mixed), and 
scalable quantum process tomography.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/orialb/TimeEvoMPS.jl" target="_blank"> 
TimeEvoMPS
</a> 
</td>
<td class="contrib">
Ori Alberton
</td>
<td class="descrip">
The goal of this package is to provide implementations of time-evolution algorithms for matrix-product states using ITensors.jl. Algorithms currently implemented include TEBD (with 2nd and 4th order Trotter decomposition) and TDVP (two-site variant).
</td>
</tr>

</table>

<a name="cppv3_codes"></a>
# ITensor C++ Version 3 Codes

Open-source codes based on ITensor for a variety projects and tasks.
If you have a high-quality code you'd like listed here, please
<a href="about.html">contact us</a>. Codes extending core ITensor
features may become candidates for inclusion in ITensor at a later date.

(Codes listed as maintained by "ITensor" are officially maintained by the developers
of the ITensor library and will be tested against and updated along with the ITensor library.
Other codes are maintained separately from ITensor by the maintainers
shown next to each code. Please contact them directly if you have any issues 
with or questions about the codes.)

<br/>
<br/>

<table id="codes" style="border-collapse: collapse; border-spacing: 10px;">

<tr>
<td class="name">
Name
</td>
<td class="contrib">
<b>Maintainers</b>
</td>
<td class="descrip">
<b>Description</b>
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/Tatsuto-Yamamoto/CTMRG-by-ITensor" target="_blank">
CTMRG
</a>
</td>
<td class="contrib">
Tatsuto Yamamoto
</td>
<td class="descrip">
The corner transfer matrix renormalization group (CTMRG) algorithm of Nishino and Okunishi for contracting fully symmetric infinite 2D tensor networks.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/ITensor/iDMRG" target="_blank">iDMRG</a>
</td>
<td class="contrib">
Miles Stoudenmire
</td>
<td class="descrip">
A single header file for idmrg calculations based on the ITensor library,
with example driver codes.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/yantaow/iTDVP/tree/master" target="_blank">iTDVP</a>
</td>
<td class="contrib">
<a href="https://github.com/yantaow">Yantao Wu</a>
</td>
<td class="descrip">
A realization of an infinite matrix product state, supporting the infinite time-dependent
variational principle (iTDVP) algorithm. Includes sample codes.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/emstoudenmire/parallelDMRG" target="_blank">Parallel DMRG</a>
</td>
<td class="contrib">
Miles Stoudenmire
</td>
<td class="descrip">
Real-space parallel DMRG code. Works for both single MPO Hamiltonians and
Hamiltonians that are a sum of separate MPOs. Uses MPI to communicate DMRG
boundary tensors across nodes.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/ITensor/TDVP" target="_blank">TDVP</a>
</td>
<td class="contrib">
<a href="https://github.com/mingruyang">Mingru Yang</a>
</td>
<td class="descrip">
Implementation of the time-dependent variational principle (TDVP) 
method for time evolving MPS for any Hamiltonian which can
be represented as an MPO. Supports both the 1-site and 2-site
algorithms.
</td>
</tr>

</table>


<a name="cppv2_codes"></a>
# ITensor C++ Version 2 Codes

(Codes listed here are maintained separately from ITensor by the maintainers
shown next to each code. Please contact them directly if you have any issues 
with or questions about the codes.)

_If you would like help upgrading your code to version 3 of ITensor,
please <a href="about.html">contact us</a>._

<br/>
<br/>

<table id="codes" style="border-collapse: collapse; border-spacing: 10px;">

<tr>
<td class="name">
Name
</td>
<td class="contrib">
<b>Maintainers</b>
</td>
<td class="descrip">
<b>Description</b>
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/joselado/dmrgpy" target="_blank">DMRGPy</a>
</td>
<td class="contrib">
<a href="https://sites.google.com/site/joseluislado/home" target="_blank">Jose Lado</a>
</td>
<td class="descrip">
DMRGPy is a Python library to compute quasi-one-dimensional spin chains and fermionic systems using matrix product states with DMRG as implemented in ITensor. Most of the computations can be performed both with DMRG and exact diagonalization for small systems, which allows one to benchmark the results.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/emstoudenmire/finiteTMPS" target="_blank">Finite T MPS</a>
</td>
<td class="contrib">
Benedikt Bruognolo <br/>
Miles Stoudenmire
</td>
<td class="descrip">
Codes for finite temperature calculations with MPS techniques, including the minimally
entangled typical thermal states (METTS) algorithm applied to 2D systems.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/hoihui/itebd" target="_blank">iTEBD</a>
</td>
<td class="contrib">
Hoi Hui
</td>
<td class="descrip">
A single header file for itebd calculations based on the ITensor library,
with example driver codes.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/emstoudenmire/parallelDMRG/tree/v2" target="_blank">Parallel DMRG</a>
</td>
<td class="contrib">
Miles Stoudenmire
</td>
<td class="descrip">
(To get the ITensor version 2 compatible version of this code, use git to 
check out the "v2" branch.)

Real-space parallel DMRG code. Works for both single MPO Hamiltonians and
Hamiltonians that are a sum of separate MPOs. Uses MPI to communicate DMRG
boundary tensors across nodes.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/jurajHasik/pi-peps" target="_blank">Pi-PEPS</a>
</td>
<td class="contrib">
<a href="https://cm.sissa.it/people/members.php?ID=236" target="_blank">Juraj Hasik</a>
</td>
<td class="descrip">
C++ library built on top of ITensor for running iPEPS simulations of two dimensional spin systems. Wavefunctions are optimized through Simple Update or Full Update. Expectation values and environments are computed by directional CTMRG algorithm.
</td>
</tr>

<tr>
<td class="name">
<a href="https://github.com/emstoudenmire/TNML" target="_blank">
Tensor Network Machine Learning
</a>
</td>
<td class="contrib">
Miles Stoudenmire
</td>
<td class="descrip">
Handwriting recognition using matrix product states (MPS) to parameterize
the weights of the model, and a DMRG-like algorithm to optimize.
</td>
</tr>

</table>

