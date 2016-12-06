# IQIndex

We have seen that indices of quantum-number conserving tensors have
quantum number <i>sectors</i>. That is, some values the index takes
correspond to a quantum number q1; other values of the index correspond to q2; etc.

Let us revisit our example from the last chapter of a single-site operator acting
on the Hilbert space of a single hard-core boson:

<img class="diagram" width="30%" src="docs/book/images/ablocks.png"/>

We see that for each index, if the index value is 1 then it is in the quantum
number 0 sector. If the index value is 2, the index is in the quantum number 1 sector.
Below we will see that more generally, multiple index values can fall into the same
quantum number sector.

# Constructing an IQIndex

Continuing with the above example, let us construct a tensor index with quantum-number sectors:
an IQIndex.

    auto I = IQIndex("I",
                     Index("I0",1),QN(0),
                     Index("I1",1),QN(1),
                     Out);

In the code above, the name of the IQIndex is "I". It has two sectors, both of size 1. 
The first sector is represented by the Index named "I0" (of size 1) and has quantum number 0.
The second sector is represented by the Index "I1" and has quantum number 1.

The arrow direction of I is specified as Out. The default arrow direction
is Out and we will often omit it below.

The size of this IQIndex is 2, because it has two sectors each of size 1.

<br/>

<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[Block-Sparse Tensors|book/block_sparse]]
</span>

<br/>

