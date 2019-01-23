## Matrix Product States (MPS)

In particular, diagrams can be used to represent matrix product states (MPS); the site by site decomposition of the wavefunction.  This makes relating concepts and principles in DMRG and tensor networks much easier on paper.

It turns out that choosing the MPS basis for the wavefunction is a good ansatz for finding the actual ground state and enables methods like DMRG to function well.  We can use a diagram to represent an MPS:

<p align="center"><img src="docs/articles/MPS.png" alt="MPS Diagram" style="width: 500px;"/></p>

$$=A^{\sigma_1}A^{\sigma_2}A^{\sigma_3}A^{\sigma_4}A^{\sigma_5}$$

DMRG automatically finds the coefficients for each of the tensors by simply knowing the MPO.  In fact, the goal of many tensor networks is to find the elements of these tensors for a given system.  

### Gauges

Gauging an MPS can help speed up computations dramatically.  To see why, note that there is an orthogonality condition where @@\sum_{\sigma}A^{\sigma}A^{\sigma\dagger}=1@@ if both @@A^{\sigma_1}@@ and @@A^{\sigma_1'}@@ are in the same gauge (i.e., both right- or both left-normalized).

In the MPS example used in this section, the orthogonality center (red) has been placed at the last site, so each of the purple squares are left-normalized (denoted by @@A@@ where @@B@@ is the right-normalized). Technically we may only place the orthogonality center on a bond, but the `position` function will always place the orthogonality center to the right of the called index.  To center the gauge on a particular site, we can use the ITensor code:

    auto N = 5;
    MPS psi;
    psi.position(N);

To reposition the orthogonality center (red square):

    psi.position(N-1);

which gives the modified diagram:

<p align="center"><img src="docs/articles/gauge.png" alt="Re-gauged MPS" style="width: 500px;"/></p>

$$=A^{\sigma_1}A^{\sigma_2}A^{\sigma_3}A^{\sigma_4}B^{\sigma_5}$$

and has written the first four sites as left-normalized and the last site as right-normalized (yellow).  The becomes important in efficiently contracting a tensor network in [[an article on Contractions|articles/contractions]].

Some diagrams also have arrows, but we'll talk about those in [[an article on quantum numbers.|]]

The last two diagrams have had their physical indices pointing upward.  Reorienting them so that they point downwards (and can interface with the physical indices pointing upwards on the MPOs below) can be specified with `dag`:

    ITensor cpsi = dag(psi);
    auto cpsi * psi;//calculates the overlap

But note that multiplying `cpsi` by `psi` gives the overlap between @@\langle\psi|\psi\rangle@@ simply.


###Links

So far, we have noted several times physical indices (vertical lines).  The horizontal lines have a different name: links.  Everywhere, ITensor makes a distinction between physical indices and links and will not contract the two by default. (Miles:  How do I set links on an operator, anyway?  automatically?)

Links can also be primed just as physical indices:

    auto ir = commonIndex(psi.A(i),psi.A(i+1),Link);//primes the link 
                                                    //between sites i and 
                                                    //i+1 of psi
    prime(psi,ir);

See [[an article on Contractions|articles/contractions]] to see how priming a link can be used in an ITensor code.



## Matrix Product Operators (MPO)

<p align="center"><img src="docs/articles/MPO.png" alt="MPO Diagram" style="width: 500px;"/></p>

$$=M^{\sigma_1'\sigma_1}M^{\sigma_2'\sigma_2}M^{\sigma_3'\sigma_3}M^{\sigma_4'\sigma_4}M^{\sigma_5'\sigma_5}$$

MPOs are the counterparts to the MPS.  They are operators rewritten in the same site by site basis as the MPS.  Note that each of these operators has two free indices on each tensor.  This allows the MPO to link with both a bra and a ket vector.  Vertical lines are called physical indices while the horizontal lines are called links.

### Prime Indices

ITensor uses a novel priming system to avoid renaming all the physical indices pointing up.  If we didn't name the indices that point up something different, then we would contract the top and bottom lines when using `*` by default--something we don't want to do, generally!

In order to avoid this, we assign a prime level to each index.  By default, this is zero.  This example shows that the `prime` function will change the prime level, incrementing it by one.

    Index s("s",5);//Five site example
    ITensor psi(s);
    ITensor cpsi = dag(prime(psi,Site));//primes the physical index
                                        //and reverses arrows

We've also included the `dag` function that changes the direction of the physical indices in the diagram.  `cpsi` forms the entire bra vector:

<p align="center"><img src="docs/articles/bra.png" alt="Primed and Daggered MPS" style="width: 500px;"/></p>

$$=A^{\sigma_1'\dagger}A^{\sigma_2'\dagger}A^{\sigma_3'\dagger}A^{\sigma_4'\dagger}A^{\sigma_5'\dagger}$$

ITensor is able to generate MPOs with a unique feature:  [[AutoMPO|]].

### Contracting MPOs and MPSs in ITensor

If we specify all of our indicies in the right way, then contracting two ITensors is trivial.  Let's see an example using the `commaInit` function to initialize the @@S_z@@ operator over all the sites `s`.

    commaInit(Sz,s,prime(s)) = 0.5, 0.0,
                               0.0,-0.5;//define Sz operator
    ITensor C = cpsi * Sz * psi

ITensor automatically contracts all like indices (same prime level, same site number, etc.).  Tutorial 1 details more on this subject.  Now, this isn't always the best way to contract the tensor network.  We'll talk about how to do this efficiently in [[an article on Contractions|articles/contractions]].
