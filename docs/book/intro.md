# Introduction to ITensor

Matrix methods have been a major success in the applied sciences.
*Tensor* methods could be even more powerful
for understanding complex systems and high dimensional data.
Exciting developments in physics and chemistry have come from
expressing quantum wavefunctions as *tensor networks*.
Data scientists are discovering tensor-based optimization algorithms
which decisively outperform more common techniques.

In real-world tensor applications, each index of a tensor has
a semantic, or physical meaning. 
In ITensor, tensor indices are likewise a specific type of object with
a unique identity. Constructing an index in ITensor looks like:

    Index s1("site 1",2);

The resulting Index s1 has a bond dimension or extent of 2; it is also 
stamped indelibly with a unique internal ID number and all copies of s1
will carry this same ID number. (The string "site 1" is for
printing purposes.)

Since matching indices can be recognized by their ID, tensor contraction in ITensor
looks like

    A = B * C * D;

The ITensor contraction
engine recognizes repeated indices and sums 
over them, much like the Einstein summation convention used
in physics. Instead of worrying about the order of tensor indices,
ITensor lets users focus on the topology of
tensor contraction diagrams.
Certain classes of bugs can no longer happen, such as confusing two indices of
the same size.

Consider the following example involving two matrix-like ITensors 

    ITensor A(i,j),
            B(k,j);
    ITensor C = A*B;

which computes the matrix multiplication @@ C = A B^\mathsf{T} @@.

In a traditional matrix library, we would need to remember that j is
the second index of B and write something like 

    C = A * transpose(B) //not actual ITensor code

to get the correct result.

ITensor has many other features to let you solve problems
rather than worry about programming details:
* Adding ITensors with identical index structure always succeeds without 
having to permute the index order. 
* ITensor storage automatically switches from real to complex as needed.
* ITensors  with sparse storage interoperate seamlessly with regular, dense
ITensors.
<br/>
<br/>

Finally, ITensor includes many routines for standard tensor decompositions
and a rich, high-level interface for
matrix product state and density matrix renormalization group (DMRG) algorithms.

<img src="../../left_arrow.png" width="20px" style="vertical-align:middle;"/> [[Table of Contents|book]]
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
<img src="../../right_arrow.png" width="20px" style="vertical-align:middle;"/> [[Index Objects|book/index]]

