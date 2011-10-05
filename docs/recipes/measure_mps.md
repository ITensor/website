#Measure the properties of an MPS wavefunction#

Here we'll learn how to measure some properties of the
Heisenberg model wavefunction by adding to the code from the [[previous example|recipes/basic_dmrg]].
Essentially we need three pieces to take an expectation value of some property:  
the operator corresponding to that property, the wavefunction, and a way to do the inner
product of the operator with the wavefunction.

For example, consider trying to measure the z-component of
the spin on some site `j` in the Heisenberg chain.  The operator corresponding to this
measurement is `sz(j)`.  This operator is a method of the `SpinOne::Model model(N);` class
that we defined last time, and can be represented by an ITensor:

<code>
ITensor szj_op = model.sz(j);
</code>

Likewise there are operators for the site `j` spin raising (S+) and lowering operators (S-),
`sp(j)` and `sm(j)`, respectively.
Now there is an efficient way to take the inner product of these local operators with the MPS
wavefunction.  We will make use of the fact that the MPS wavefunction allows us to locally 
represent the wavefunction.  To do this, we must first call the function

<code>
psi.position(j);
</code>

_This step is absolutely vital_.  It tells the MPS wavefunction to put all the information
about the amplitudes of the various spin occupations into the site at `j`.
Without which, measuring `sz(j)` would give errors.  Getting these amplitudes is
then very simple, and they will form the ket part of our Dirac "bra-ket" inner product:

<code>
ITensor ket = psi.AA(j);
</code>

After calling `psi.position(j)`, all the `psi.AA(j+n)` for `n != 0` are effectively basis functions
allowing the wavefunction to represent the site `j+n`.  As basis functions, these `psi.AA(j+n)` do
not have amplitude information; only the `psi.AA(j)` does.  That is why it is vital to call 
`psi.position(j)` before doing a measurement at site `j`.

To get the bra part of the Dirac bra-ket, think about the ket as a column vector, the operator
as a matrix, and the bra as a row vector.  In usual expectation values, the bra is closely related
to the ket.  We can actually get the bra by turning the ket into a row vector and conjugating
any imaginary parts.  The way we do this is simple:

<code>
ITensor bra = conj(primesite(ket));
</code>

The `primesite` function is what turns the ket into a row vector, and `conj` does the conjugation.
(For the Heisenberg model, there isn't a need for the conjugation, though.)
Now we are ready to measure the expectation value of `sz(j)` by using the inner product function `Dot`:

<code>
Real szj = Dot(bra, szj_op*ket);
</code> 






<br>
[[Back to Recipes|recipes]]
