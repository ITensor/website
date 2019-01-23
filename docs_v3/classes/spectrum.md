# Spectrum

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

A Spectrum object stores a reduced density matrix eigenvalue spectrum resulting from an SVD or density matrix decomposition.
It is the return value of the `svd` and `denmatDecomp` methods. Spectrum objects can also be constructed from the diagonal
singular-value tensor computed by the `svd` function.

## Synopsis ##

    Spectrum spec = svd(T,U,D,V);

    Print(spec); //view the squares of the singular values of T

    //Thinking of T as a wavefunction, compute its entanglement entropy S
    Real S = 0;
    for(int n = 1; n <= spec.numEigsKept(); ++n)
        {
        S += -spec.eig(n)*log(spec.eig(n));
        }
    printfln("S = %.10f",S);


<!--
## Constructors ##

* `Spectrum()`

  Default constructor, object will contain no eigenvalue information.
  -->
