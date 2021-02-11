# ITensor Codes (Julia Language)

[Looking for the C++ codes? [Click here](http://itensor.org/docs.cgi?page=codes&vers=cppv3).]

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
Matthew Fishman
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

<!--
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
Package for Simulation, Tomography and Analysis of Quantum Computers
</td>
</tr>
-->

</table>
