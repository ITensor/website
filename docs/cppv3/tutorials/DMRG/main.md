# The Density Matrix Renormalization Group

<span class='article_sig'>Thomas E. Baker and Benedikt Bruognolo&mdash;September 15, 2015</span>

One of the most successful methods to calculate low-energy properties of one-dimensional and two-dimensional quantum systems 
is the density matrix renormalization group (DMRG).  
DMRG uses the [[MPS|tutorials/MPS]] and [[MPO|tutorials/MPO]] representation to calculate the 
ground state of a low dimensional quantum system. The algorithm DMRG is the combination of three other methods that we covered elsewhere:  

  1.  The optimization problem is constructed as a two-site object from the full tensor network
  2.  This reduced operator is solved by an eigensolver such as the [[Lanczos||tutorials/Lanczos]] or [[Davidson algorithm|tutorials/davidson]]
  3.  We apply an [[SVD|tutorials/SVD]] and move to the next two sites

There are various permutations of the above algorithm (for example, single site DMRG is a possibility), but this article will discuss the current implementation in ITensor.

This article will cover the DMRG algorithm.  How to implement the method in ITensor with the [[`dmrg`|book/DMRG]] function and [[why DMRG is successful|tutorials/InfoTheory]] in finding the ground state are in the linked articles.

## How DMRG works

DMRG seeks to reduce the full Hamiltonian, which grows exponentially (for a spin-half chain this grows like @@2^L@@ for @@L@@ spins) in the system size, to a smaller eigenvalue problem to solve for the ground state.  So, we could solve something like

<p align="center"><img src="docs/tutorials/DMRG/schrodinger.png" alt="Schrodinger's equation" style="width: 600px;"/></p>

which is simply Schrodinger's equation,

$$
\mathcal{H}|\psi\rangle=E|\psi\rangle
$$


There are five physical indices that are open on our five site system.  This implies that we are working with a rank five tensor to solve the entire system.  We could solve this with an exact diagonalization calculation (or similar), but for a larger systems, the computational cost grows exponentially with system size (this is bad!) implying that larger systems are inaccessible.  We want to reformulate the problem to search over a reduced number of degrees of freedom. 

We can variationally optimize for some of the components of the MPS instead of all of them at the same time. The equation to search for two components in the MPS is

<p align="center"><img src="docs/tutorials/DMRG/dmrg_eig0.png" alt="DMRG eigenvalue equation" style="width: 600px;"/></p>

The MPS has now been gauged so its orthogonality center is located on the tensor we wish to minimize. Note that we have chosen to vary two tensors in the network.  This allows for full control of the bond dimension in the SVD. There are single site updates, but ITensor currently uses a two site update.  No matter how many tensors are chosen to variationally minimize, truncating the network like this incurs a large savings in that the network. 

The tensor multiplying @@E@@ can be contracted down to a single tensor:

<p align="center"><img src="docs/tutorials/DMRG/dmrg_eig.png" alt="DMRG eigenvalue equation" style="width: 600px;"/></p>

Mathematically varying tensor is equivalent to taking the partial derivative of the expectation value of the normalized Hamiltonian,

$$
\frac{\partial}{\partial A_i^*}\frac{\langle\psi|\mathcal{H}|\psi\rangle}{\langle\psi|\psi\rangle}\overset!=0
$$ 

Varying both (as shown above) is

$$
\frac{\partial}{\partial [A\_{i}^\ast{}A\_{i+1}^{\ast}]}\frac{\langle\psi|\mathcal{H}|\psi\rangle}{\langle\psi|\psi\rangle}\overset!=0
$$ 

and require the solution to find the variational minimum in energy.  We will always place the orthogonality center on the tensor we want to obtain.  This form of the eigenvalue problem is handling a tensor that is rank four (which is reduced to rank two if we combine each pair of physical and link indices with a tensor product).  In order to find the tensor, we may use a sparse eigenvalue solver like the Lanczos or Davidson algorithms in the reduced Hilbert space and solve the equation 

$$
\mathcal{H}[A^{\sigma\_i}\_{a\_ia\_{i+1}}A^{\sigma\_{i+1}}\_{a\_{i+1}a\_{i+2}}]-E[A^{\sigma\_i}\_{a\_ia\_{i+1}}A^{\sigma\_{i+1}}\_{a\_{i+1}a\_{i+2}}]\overset!=0
$$

While the mathematical expression for this eigenvalue problem on the local tensor is cumbersome (we have hidden a complicated sum by simply writing @@\mathcal{H}@@ in the above), the ITensor code is not.  We will cover how the [[Lanczos and Davidson|tutorials/Lanczos]] algorithms work in the library in another article; however,  ITensor provides a function `davidson` that will evaluate this for us. The output of the `davidson` algorithm undergoes a SVD in order to restore the form of the MPS (see [[SVD|tutorials/SVD]] for code examples).

There is one more step that must be taken to ensure the algorithm is fast and can solve larger systems than exact diagonalization.  Keeping all states in the SVD is not necessary to obtain the correct ground state at an acceptable accuracy. Truncating the MPS in the SVD keeps only the most relevant degrees of freedom for the ground state and eliminates extraneous degrees of freedom.  Controlling the number of many body states kept with the `maxm` and `minm` functions in ITensor does this.  Repositioning the orthogonality center to the next pair of sites and sweeping back and forth in the system eventually approaches the ground state.

One way to see that our calculation has converged is to check the truncation error which is a measure of discarded singular values in the SVD. A lower value is better.   

The [[Mini-Course|course]] contains a DMRG tutorails and shows how the ITensor codes works in full.

