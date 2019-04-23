# Exactly Compute Ground State of a Small Hamiltonian

As a test for more scalable codes, it is often useful to work
in the full Hilbert space and exactly find the ground state of
the Hamiltonian of a small system.

Below is a code that initializes a random wavefunction as a 
single ITensor, then applies @@e^{-\tau\, H}@@ a few times
to this ITensor wavefunction to obtain the ground state.


    include:docs/cppv3/formulas/simple_ed/simple_ed.cc

