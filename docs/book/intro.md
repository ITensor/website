# ITensor Library Overview

Matrix methods have been a major success in the applied sciences.
*Tensor* methods promise even greater insights and more powerful
algorithms.
Major advances in physics and chemistry have come from
tensor network wavefunctions.
Data scientists are discovering tensor algorithms
which decisively outperform standard techniques.

When a problem is cast into the language of tensors,
each tensor index can typically be assigned
a semantic, or physical meaning. 
Similarly in ITensor, tensor indices are objects with
unique identities. Constructing an index in ITensor looks like:

    auto i = Index("index i",3);

The resulting Index has a size, or dimension of 3. Upon creation it is 
indelibly stamped with an internal ID number so all copies of this Index
can recognize each other.

Having made a few Index objects i, j, k, one can construct ITensors

    auto A = ITensor(i);
    auto B = ITensor(j,i);
    auto C = ITensor(i,j,k);

and set their elements (as shown in the [[ITensor Basics|book/itensor_basics#elements]] chapter).

Since matching indices can recognize each other, ITensor contraction
is simply

    D = A * B * C;

The ITensor contraction engine recognizes repeated indices and sums 
over them, like the Einstein summation convention used
in physics. Instead of bookkeeping the order of tensor indices,
users can focus on the structure of tensor networks.
Certain bugs are ruled out, such as mistaking one index for
another of the same size.

Let's take a closer look at an example involving two matrix-like ITensors 

    auto A = ITensor(i,j);
    auto B = ITensor(k,j);
    auto C = A * B;

Here the contraction `A * B` computes the matrix product @@ C = A B^\mathsf{T} @@.
The Index <code style="border:none;">j</code> appears on both A and B so is automatically summed over,
leaving C to have indices i and k.

In a standard matrix library, one would need to remember that <code style="border:none;">j</code> is
the second index of B and write something like 

    C = A * transpose(B) //not actual ITensor code!!

to get the correct result. ITensor handles this transposition automatically, 
making user code simple and robust. If B were to be redefined
with transposed index order, the ITensor operation `A * B` would continue to give the correct result.

Say we didn't want to contract over the index j &mdash; we could do the following

    auto D = prime(A,j) * B;

The call to `prime(A,j)` puts a single, lightweight prime on A's copy of index j. It no longer
matches the copy of j on B so these will not be contracted and D will end up with four indices i,j',j,k. 
We have computed an outer product of two matrices with very little effort.


ITensor has many other features emphasizing productivity
over programming details:
* Adding ITensors simply works without 
the user having to permute the index order. 
* ITensor data storage automatically switches from real to complex as needed,
such as when multiplying by a complex number.
* Sparse ITensors seamlessly interoperate with regular, dense
ITensors.
* Quantum-number conserving (block sparse) tensors have the same interface as dense tensors.


Last but not least, ITensor includes routines for tensor decompositions
and a rich, high-level layer for matrix product state and density matrix 
renormalization group (DMRG) algorithms used in physics and chemistry.
<br/>
<br/>

<span style="float:left;"><img src="docs/arrowleft.png" class="icon"> 
[[Table of Contents|book]]
</span>
<span style="float:right;"><img src="docs/arrowright.png" class="icon"> 
[[Index Objects|book/index]]
</span>

