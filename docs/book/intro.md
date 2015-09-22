# ITensor Overview

Matrix methods have been a major success in the applied sciences.
*Tensor* methods promise even greater insight
into complex systems and high dimensional data.
Major developments in physics and chemistry have come from
viewing quantum wavefunctions as tensor networks.
Data scientists are discovering tensor optimization algorithms
which decisively outperform standard techniques.

In real tensor applications, each index of a tensor has
a semantic, or physical meaning. 
Similarly in ITensor, tensor indices are objects with
unique identities. Constructing an index in ITensor looks like:

    Index s1("site 1",2);

The resulting Index <code style="border:none;">s1</code> has a size, or bond dimension of 2. Upon creation it gets
indelibly stamped with an internal ID number; all copies of <code style="border:none;">s1</code>
carry this same ID number. (The string "site 1" is the name of this Index only for
printing purposes.)

Since matching indices can be recognized by their ID, tensor contraction in ITensor
is simply

    A = B * C * D;

The ITensor contraction
engine recognizes repeated indices and sums 
over them, much like the Einstein summation convention used
in physics. Instead of worrying about the order of tensor indices,
users can focus on the structure of tensor networks.
Certain classes of bugs are completely ruled out, such as confusing
different indices of the same size.

Consider the following example involving two matrix-like ITensors 

    ITensor A(i,j),
            B(k,j);
    ITensor C = A*B;

which computes the matrix product @@ C = A B^\mathsf{T} @@.
The Index <code style="border:none;">j</code> appears on both A and B so is automatically summed over.

In a traditional matrix library, one would need to remember that <code style="border:none;">j</code> is
the second index of B and write something like 

    C = A * transpose(B) //not actual ITensor code

to get the correct result. ITensor handles this transposition automatically, 
making user code simple and robust. If B were to be redefined
with transposed index order, the ITensor code `C=A*B` would continue to give the correct result.

ITensor has many other features emphasizing productivity
over programming details:
* Adding ITensors with the same indices automatically works without 
needing to permute the index order. 
* ITensor storage automatically switches from real to complex as needed,
such as when setting an element to or multiplying by a complex number.
* ITensors with sparse storage seamlessly interoperate with regular, dense
ITensors.
<br/>
<br/>

Finally, ITensor includes many routines for standard tensor decompositions
and a rich, high-level interface for
matrix product state and density matrix renormalization group (DMRG) algorithms.
<br/>
<br/>

<span style="float:left;"><img src="../../left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Table of Contents|book]]
</span>
<span style="float:right;"><img src="../../right_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Index Objects|book/index]]
</span>

