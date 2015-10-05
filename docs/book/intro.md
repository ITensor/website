# ITensor Overview

Matrix methods have been a major success in the applied sciences.
*Tensor* methods could offer even greater insight
into complex systems and high dimensional data.
Major developments in physics and chemistry have come from
viewing quantum wavefunctions as tensor networks.
Data scientists are discovering tensor optimization algorithms
which decisively outperform standard techniques.

In real tensor applications, each index of a tensor has
a semantic, or physical meaning. 
Similarly in ITensor, tensor indices are objects with
unique identities. Constructing an index in ITensor looks like:

    Index i("index i",3);

The resulting Index has a size, or bond dimension of 3. Upon creation it gets
indelibly stamped with an internal ID number; all copies of this Index
carry this same ID number. (The string "index i" is the name of this Index only for
printing purposes.)

Having made a few Index objects i, j, k, one can construct ITensors

    ITensor B(i);
    ITensor C(j,i);
    ITensor D(i,j,k);

and set their elements (as shown in the [[ITensor Basics|book/itensor_basics#elements]] chapter).

Since matching indices can be recognized by their ID, ITensor contraction
is simply

    A = B * C * D;

The ITensor contraction
engine recognizes repeated indices and sums 
over them, much like the Einstein summation convention used
in physics. Instead of thinking about the ordering of tensor indices,
users can focus on the structure of tensor networks.
Certain classes of bugs are completely ruled out, such as confusing
different indices of the same size.

Consider the following example involving two matrix-like ITensors 

    ITensor A(i,j),
            B(k,j);
    ITensor C = A*B;

which computes the matrix product @@ C = A B^\mathsf{T} @@.
The Index <code style="border:none;">j</code> appears on both A and B so is automatically summed over,
leaving C to have indices i and k.

In a traditional matrix library, one would need to remember that <code style="border:none;">j</code> is
the second index of B and write something like 

    C = A * transpose(B) //not actual ITensor code!!

to get the correct result. ITensor handles this transposition automatically, 
making user code simple and robust. If B were to be redefined
with transposed index order, the ITensor code `C=A*B` would continue to give the correct result.

ITensor has many other features emphasizing productivity
over programming details:
* Adding ITensors automatically works without the user
needing to permute the index order. 
* ITensor storage automatically switches from real to complex as needed,
such as when setting an element to or multiplying by a complex number.
* ITensors with sparse storage seamlessly interoperate with regular, dense
ITensors.
<br/>
<br/>

Last but not least, ITensor includes many routines for tensor decompositions
and a rich, high-level interface for matrix product state and density matrix 
renormalization group (DMRG) algorithms used in physics applications.
<br/>
<br/>

<span style="float:left;"><img src="docs/book/images/left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Table of Contents|book]]
</span>
<span style="float:right;"><img src="docs/book/images/right_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Index Objects|book/index]]
</span>

