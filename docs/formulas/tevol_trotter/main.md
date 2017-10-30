# Time Evolving an MPS with Trotter Gates

A very accurate, efficient, and simple way to time evolve a matrix product state (MPS)
is by using a Trotter decomposition of the time evolution operator. Although the 
discussion below only pertains to the case of a nearest-neighbor one-dimensional
Hamiltonian, the method can be extended to Hamiltonians with arbitrary finite-range
interactions by using swap gates to temporarily exchange sites. (For information
about using swap gates, see <a href="http://iopscience.iop.org/article/10.1088/1367-2630/12/5/055026" target="_blank">New J. Phys. 12, 055026</a>.)

If the Hamiltonian is a sum of local terms
$$
\hat{H} = \sum\_j \hat{h}\_{j,j+1}
$$
where @@\hat{h}\_{j,j+1}@@ only acts non-trivially on sites j and (j+1),
then a Trotter decomposition that is particularly well suited for use
with MPS techniques is
$$
e^{-i \tau H} \approx e^{-i h\_{1,2} \tau/2} e^{-i h\_{2,3} \tau/2} \cdots e^{-i h\_{N-1,N} \tau/2}
e^{-i h\_{N-1,N} \tau/2} e^{-i h\_{N-2,N-1} \tau/2} \cdots e^{-i h\_{1,2} \tau/2} + O(\tau^2)
$$
Note the factors of two in each exponential.
The error in the above decomposition is of order @@\tau^2@@, so this will be the error
accumulated _per time step_. Because of the time-step error, one takes @@\tau@@ to be
small and then applies the above set of operators to an MPS as a single sweep, then
does a number @@(t/\tau)@@ of sweeps to evolve for a total time @@t@@.

The same decomposition can be used for imaginary time evolution by just replacing
@@i \tau \rightarrow \tau@@.

Below is a fully working code that applies the above ideas to time evolve
an MPS which is initially a simple product state with the Heisenberg Hamiltonian:

    include:docs/formulas/tevol_trotter/tevol_trotter.cc

<img class="icon" src="docs/install.png"/>&nbsp;<a href="docs/formulas/tevol_trotter/tevol_trotter.cc">Download the full example code</a>
