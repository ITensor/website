#Tutorial: A Simple Measurement

First let's model a single spin 1/2 degree of freedom. 
We will need an Index to define the Hilbert space of the spin:

`Index s("s",2,Site);`

Index objects come in two varieties, `Site` or `Link`. It is helpful to use 
`Site` indices for lattice site, or physical, degrees of freedom and `Link` for indices internal
to our tensor network.


## Wavefunction ##

We can represent a single-site wavefunction as a rank 1 ITensor:

<img src="docs/tutorial/ket.png" style=""/>

`ITensor ket(s);`


Let us choose the initial state to be at a 45-degree angle between the +z and +x axes:

<code>
Real theta = Pi/4;
ket(s(1)) = cos(theta/2);
ket(s(2)) = sin(theta/2);
</code>

(The factors of 2 in the `cos` and `sin` are present because our wavefunction represents a spin 1/2.)

## Operators ##

To measure the spin's properties we will need operators: 

<code>
ITensor Sz(s,primed(s)),
        Sx(s,primed(s));
</code>

Here `primed(s)` makes an Index &nbsp;`s'` which is identical to the Index &nbsp;`s` but
has a prime level of 1. The library treats indices with different prime levels
as distinct, even if they match otherwise.
We can convert a primed Index to its original form later by just setting its prime level back to zero.

This is the convention we use throughout the library:
single-site operators are rank 2 tensors with indices S and S',
where S is a `Site` Index.

Now set the elements of `Sz` and `Sx`:

<code>
commaInit(Sz,s,primed(s)) << 0.5, 0
                             0, -0.5;

commaInit(Sx,s,primed(s)) << 0, 0.5
                             0.5, 0;
</code>

## Measurements ##

Now, for our measurements we would like to take
the expectation value of `Sz` and `Sx`. 
First make the Dirac "bra" conjugate of the wavefunction:

<img src="docs/tutorial/bra.png" style=""/>

`ITensor bra = conj(primed(ket));`



The `primed` function increases the prime level of all indices
by 1.

Finally, we compute the expectation value as the diagram

<img src="docs/tutorial/expect.png" style=""/>

which becomes in code:

<code>
Real zz = (bra \* Sz \* ket).toReal();
Real xx = (bra \* Sx \* ket).toReal();

cout << "<Sz> = " << zz << endl;
cout << "<Sx> = " << xx << endl;
</code>


The `toReal()` method is needed to convert the
rank 0 ITensors resulting from the contraction
into real numbers.

If all goes well, we should see the printout

<code>
<Sz> = 0.35355
<Sx> = 0.35355
</code>

which are indeed the components of a magnitude
1/2 vector at a 45 degree angle between +z and +x.

</br>

Up to the [[table of contents|tutorial]].

[[Back to Main|main]]
