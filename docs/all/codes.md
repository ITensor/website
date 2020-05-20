
# ITensor Codes (C++ version 3 compatible)

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


# ITensor Codes (C++ version 2 compatible)

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

