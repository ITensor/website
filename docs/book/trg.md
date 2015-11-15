# Case Study: TRG Algorithm

The handful of techniques we have covered so far (ITensor contraction and SVD)
are already enough to implement a very powerful algorithm: the _tensor renormalization group_
(TRG).

First proposed by Levin and Nave (cond-mat/0611687), TRG is a strategy for contracting a network
of tensors connected in a two-dimensional lattice pattern by decimating the network
in a heirarchical fashion. The term ["renormalization group"](http://physics.ohio-state.edu/~jay/846/Wilson.pdf) 
in the physics literature refers
to any such process where less important information at small distance scales is 
repeatedly removed until the most important information remains.

## The Problem

TRG can be used to compute certain large, non-trivial sums by exploiting
the fact that they can be recast as the contraction of a lattice of small tensors.

A classic example of such a sum is the "partition function" @@Z@@ of the classical Ising
model at temperature T, defined to be

$$
Z = \sum\_{\sigma\_1 \sigma\_2 \sigma\_3 \ldots} e^{-E(\sigma\_1,\sigma\_2,\sigma\_3,\ldots)/T}
$$

where each Ising "spin" @@\sigma@@ is just a variable taking the values @@\sigma = +1, -1@@ and the energy
@@E(\sigma\_1,\sigma\_2,\sigma\_3,\ldots)@@ is the sum of products @@\sigma\_i \sigma\_j@@ of 
neighboring @@\sigma@@ variables.
In the two-dimensional case described below, there is a "critical" temperature @@T\_c=2.269\ldots@@
at which this Ising system develops an interesting hidden fractal structure.

### One dimension

In one dimension, spins only have two neighbors since they are arranged along a chain.
For a finite-size system of N Ising spins, the usual convention is to use periodic boundary conditions 
meaning that the Nth spin connects back to the first around a circle:
$$
E(\sigma\_1,\sigma\_2,\sigma\_3,\ldots,\sigma\_N) 
 = \sigma\_1 \sigma\_2 + \sigma\_2 \sigma\_3 + \sigma\_3 \sigma\_4 + \ldots + \sigma\_N \sigma\_1 \:.
$$

The classic "transfer matrix" trick for computing @@Z@@ goes as follows:
$$
Z = \sum\_{[\sigma\]} \exp \left(\frac{-1}{T} \sum\_n \sigma\_n \sigma\_{n+1}\right)
 = \sum\_{[\sigma\]} \prod\_{n} e^{-(\sigma\_n \sigma\_{n+1})/ T}
 = \text{Tr} \left(M^N \right)
$$

where @@\text{Tr}@@ means "trace" and the transfer matrix @@M@@ is a 2x2 matrix with elements

$$
M\_{\sigma^{\\!} \sigma^\prime} = e^{-(\sigma^{\\!} \sigma^\prime)/T} \ .
$$

Pictorially, we can view @@\text{Tr}\left(M^N\right)@@ as a chain of tensor contractions around a
circle:

<img class="diagram" width="60%" src="docs/book/images/TRG_1dIsingZ.png"/>

With each 2-index tensor in the above diagram defined to equal the matrix M, is an exact
rewriting of the partition function @@Z@@ as a tensor network.

For this one-dimensional case, the trick to compute @@Z@@ is just to diagonalize @@M@@. 
If @@M@@ has eigenvalues @@\lambda\_1@@ and @@\lambda\_2@@, it follows that 
@@Z = \lambda\_1^N + \lambda\_2^N@@ by the basis invariance of the trace operation.

###  Two dimensions

Now let us consider the main problem of interest. For two dimensions, the energy function
can be written as
$$
E(\sigma\_1, \sigma\_2, \ldots) = \sum\_{\langle i j \rangle} \sigma\_i \sigma\_j
$$
where the notation @@\langle i j \rangle@@ means the sum only includes @@i,j@@ which are
neighboring sites. It helps to visualize the system:

<img class="diagram" width="60%" src="docs/book/images/TRG_2dIsingZ.png"/>

In the figure above, the black arrows are the Ising spins @@\sigma@@ and the 
blue lines represent the local energies @@\sigma\_i \sigma\_j@@.
The total energy @@E@@ of each configuration is the sum of all of these local energies.


Interestingly, it is again possible to rewrite the partition function sum
@@Z@@ as a network of contracted tensors. Define the tensor @@A^{\sigma\_t \sigma\_r \sigma\_b \sigma\_l}@@
to be 
$$
A^{\sigma\_t \sigma\_r \sigma\_b \sigma\_l} = e^{-(\sigma\_t \sigma\_r + \sigma\_r \sigma\_b + \sigma\_b \sigma\_l + \sigma\_l \sigma\_t)/T}
$$

<img class="diagram" width="15%" src="docs/book/images/TRG_Atensor.png"/>

The interpretation of this tensor is that it computes the local energies between the four spins that
live on its indices, and its value is the Boltzmann probability weight @@e^{-E/T}@@ associated with
these energies. Note its similarity to the one-dimensional transfer matrix @@M@@.

With @@A@@ thus defined, the partition function @@Z@@ for the two-dimensional Ising model can
be found by contracting the following network of @@A@@ tensors:

<img class="diagram" width="35%" src="docs/book/images/TRG_2dPeriodic.png"/>

The above drawing is of a lattice of 32 Ising spins (recall that the spins live on
the tensor indices). The indices at the edges of this square wrap around in a periodic
fashion because the energy was defined to use periodic boundary conditions.

## The TRG Algorithm

We can use TRG to compute the above network, which is actually just equal to a single number 
(no uncontracted indices). The philosophy of TRG is that we can replace any tensor
in the network with any other tensor as long as both tensors are equal. 

<br/>


### References

- _The original paper on TRG_:

  Levin and Nave, "Tensor Renormalization Group Approach to Two-Dimensional Classical Lattice Models",
  [PRL 99, 120601](http://dx.doi.org/10.1103/PhysRevLett.99.120601) (2007)  cond-mat/0611687

- _Paper on an improved TRG (TEFR) with very useful figures_:

  Gu and Wen, "Tensor-entanglement-filtering renormalization approach and symmetry-protected topological order"
  [PRB 80, 155131](http://dx.doi.org/10.1103/PhysRevB.80.155131) (2009)  arXiv:0903.1069

- _TNR is an extension of TRG which qualitatively improves TRG's fixed-point behavior
   and can be used to generate MERA tensor networks_:

  Evenbly and Vidal, "Tensor Network Renormalization"
  [PRL 115, 180405](http://dx.doi.org/10.1103/PhysRevB.80.155131) (2015) arxiv:1412.0732

<br/>


<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[Factorizing ITensors|book/itensor_factorizing]]
</span>
