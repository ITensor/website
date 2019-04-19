# Measure the properties of an MPS wavefunction #

Here we will learn how to measure some properties of the
Heisenberg model wavefunction by adding to the code from the [[basic DMRG example|formulas/basic_dmrg]].
Essentially we need three pieces to take an expectation value of some property: the operator 
corresponding to that property, the wavefunction, and a way to do the inner
product of the operator with the wavefunction.

For example, consider trying to measure the z-component of
the spin on some site `j` in the Heisenberg chain. 
This operator can be retrieved from the `sites` object 
that we defined last time, and can be saved as an ITensor:

    ITensor Szjop = sites.op("Sz",j);

Likewise we can obtain operators for the site `j` spin raising (S+) and lowering operators (S-),
by calling `sites.op("Sp",j)` and `sites.op("Sm",j)` respectively.
There is an efficient way to take the inner product of these local operators with the MPS
wavefunction. To do this, we must first call the function

    psi.position(j);

This step is very important.  It "gauges" the MPS tensors to be orthogonal
to the left and to the right of site j.
Without this step, we would have to include all of the MPS tensors in our calculation
to get the right answer. But with this gauging step we can just use the tensor at
site j.

Getting the needed MPS site tensor is very simple:

    ITensor ket = psi(j);

Here we have copied this tensor to a variable called ket to suggest its role as
a Dirac ket in the expectation value we will compute.

To get the bra part of the Dirac bra-ket, we turn ket into a row vector and conjugate
its entries.  The way we do this is simple:

    ITensor bra = dag(prime(ket,Site));

The `prime` function is what turns the ket into a row vector (because it will contract with the 
row index of our operator, which will be an index with a prime level of 1), and `dag` does the hermitian conjugation. 
The argument `Site` passed to prime tells it
to prime Site-type (physical) indices only.

Now we are ready to measure the expectation value of Sz by contracting the bra, operator, and ket. 
The call to `elt(...)` below converts the resulting scalar tensor tensor into a plain real number:

    auto szj = elt(bra*Szjop*ket);

<br/>
<br/>
<br/>

Let's do a slightly more complicated measurement that will involve an operator acting on
on two sites `j` and `j+1`.  The operator @@\vec{S}\_j \cdot \vec{S}\_{j+1}@@ will do just fine.  
A useful way of rewriting this operator is
$$
\vec{S}\_j \cdot \vec{S}\_{j+1} = S^z\_j S^z\_{j+1} + \frac{1}{2} S^+\_j S^-\_{j+1} + \frac{1}{2} S^-\_j S^+\_{j+1}
$$
For example, one of the operators we'll need is

    ITensor spm = 0.5*sites.op("S+",j)*sites.op("S-",j+1);

To represent the wavefunction for two sites, we simply contract together two site tensors:

    ITensor bondket = psi(j)*psi(j+1);

The `bondbra` is made similarly to the `bra` from earlier:

    ITensor bondbra = dag(prime(bondket,Site));

And expectation values are computed in the same way:

    Real spm = elt(bondbra*spm*bondket);

Below is a complete code for measuring properties of the MPS wavefunction.  
The code prints out the measured values of
@@\langle S^z\_j \rangle@@ and @@\langle {S}\_j \cdot \vec{S}\_{j+1} \rangle@@.
<br/>
<br/>
<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/measure_mps.cc">Download the sample code below</a>


    include:docs/VERSION/formulas/measure_mps.cc



