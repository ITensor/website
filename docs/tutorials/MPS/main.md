<span class='article_title'>Matrix Product States</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 17, 2015</span>

The Hilbert space is large.  Scanning through the entire space would be take longer than is 
reasonable.  Writing down a good guess for the wavefunction can be a great way to get close 
enough to the right ground state. 
A very good guess for the ground state of a gapped system in one dimension is the 
matrix product state (MPS). DMRG and many tensor network methods rely on the MPS ansatz to 
represent ground states and low-lying excited states.

Each bulk tensor of an MPS has three indices, @@A^{\sigma\_i}\_{a\_i a\_{i+1}}@@.  The subscripts convey that indices connecting different bonds may vary in size. The size of a typical index @@a\_i@@ is known as the bond dimension of the MPS, and corresponds to the number of states kept in a DMRG calculation. The index @@\sigma_i@@ is the physical index.  This has two values for a spin@@-1/2@@ chain.

An MPS diagram for a five site system looks like

<p align="center"><img src="docs/tutorials/MPS/MPS.png" alt="MPS" style="height: 150px;"/></p>

We will discuss some characteristics of MPSs and introduce some concepts that are essential for working with MPS in ITensor.

### Using the ITensor MPS Class

To make an MPS, we can use the constructor

    MPS psi;//constructs an uninitialized MPS
    //or
    SpinHalf sites(5);
    auto psi = MPS(sites);//construct a random product state with indices
                          //based on the SiteSet used (here SpinHalf)

which automatically makes a random product-state MPS.

For read-only access to a particular tensor of the MPS, use the ``psi.A(j)`` method.
This method is called "A" because it is very common in the MPS literature to use
the letter A to denote MPS tensors.
For example, if we want to print the fourth tensor of the above MPS, 
we could do

    Print(psi.A(4));

For read and write access to an MPS tensor, use the ``psi.Aref(j)`` method. 
This method is called "Aref" because it returns a reference to the j'th "A" tensor.
Here is an example of using this method to multiply the third MPS tensor by a scalar:

    psi.Aref(3) *= 0.1827;

Another way to modify the tensors of an MPS is to use the ``.setA`` method. 

### Working with MPS Gauges

The gauge of an MPS can be chosen to make computing local properties very efficient. 
The gauge used in standard DMRG calculations chooses
a certain site to be the <i>orthogonality center</i>. 
All sites to the left and right of the orthogonality center will be left and right orthogonal, respectively.

To set site 4 of the 5-site MPS above to be the orthogonality center, call

    psi.position(4);

ITensor will compute a series of [[singular value decompositions|tutorials/SVD]] (in this case, only one) until the orthogonality center reaches site 4. The MPS diagram now looks like:

<p align="center"><img src="docs/tutorials/MPS/MPS_site2.png" alt="Regauged MPS" style="height: 150px;"/></p>

To illustrate one advantage of setting the MPS gauge, consider the diagram below where we have drawn purple squares to be left-normalized while yellow squares are right-normalized.

<p align="center"><img src="docs/tutorials/MPO/onsite.png" alt="MPS Diagram" style="height: 200px;"/></p>

First call ``psi.position(2)`` to center the gauge at site 2 as in the above diagram.

Then to compute the expectation value of the "Sz" operator on site 2, we can use the fact that in the diagram above all of the left-orthogonal and right-orthogonal tensors contract to the identity, so can be left out of the calculation (see [[an article on Correlation functions|tutorials/correlations]] for more details). So the only code needed to obtain the expectation value is:

    auto Mz2 = (dag(prime(psi.A(2),Site))*sites.op("Sz",2)*psi.A(2)).real();

where notice that we only accessed the tensor on site 2 and no other MPS tensors.
We need not bother with the other sites since we know they contract to the identity.

<!--

### Singlet Example

To construct a two-site singlet state in ITensor, we may use

    Index s1("s1",2,Site),
          s2("s2",2,Site);//makes indices for wavefunction tensor
    ITensor psi(s1,s2);//initializes wavefunction
    psi(s1(1),s2(2)) = 1./sqrt(2);//element 1,2 defined
    psi(s1(2),s2(1)) = -1./sqrt(2);//element 2,1 defined

This stores a tensor in the `s1`, `s2` basis and appears in matrix form as

<p align="center"><img src="docs/tutorials/MPS/singlet.png" alt="singlet MPS" style="height: 250px;"/></p>

Following the indices we defined, this is written in matrix form as

$$\Sigma^{\sigma\_i}=\begin{bmatrix}
0&1/\sqrt2\\\\
-1/\sqrt2&0\\\\
\end{bmatrix}$$
   
This is a singlet @@(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)/\sqrt2@@.

### Normalization

To normalize our wavefunction, we can call

    psi.norm();

### A note on bond dimension

-->


