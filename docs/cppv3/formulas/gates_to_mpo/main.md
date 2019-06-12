# Transforming a Set of Gates into an MPO

Here we describe how to transform a set of gates into an MPO.

Imagine we have a Hamiltonian that is a sum of local terms
$$
H = \sum\_j h\_{j,j+1}
$$
where @@h\_{j,j+1}@@ only acts non-trivially on sites j and (j+1),
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

The same decomposition can be used for imaginary time evolution just by replacing
@@i \tau \rightarrow \tau@@.

Below is a fully working code that applies the above ideas to time evolve
an MPS which is initially a simple product state with the Heisenberg Hamiltonian.

The `BondGate` class has a constructor that accepts a local Hamiltonian term as a
tensor, and automatically exponentiates it to make a Trotter gate with the specified
time step. The `gateTEvol` function is a helper function that handles the logic of
applying a container of gates to an MPS the right number of times and with the 
appropriate truncation of the MPS after each step.

    include:docs/VERSION/formulas/gates_to_mpo/gates_to_mpo.cc

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/tevol_trotter/tevol_trotter.cc">Download the full example code</a>
