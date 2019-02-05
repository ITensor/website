# IQIndex

We have seen that indices of quantum-number conserving tensors have
quantum number <i>sectors</i>. That is, some values the index takes
correspond to a quantum number q1; other values of the index correspond to q2; etc.
(These quantum numbers are the small red numbers in the figure below.)

Let us revisit our example from the last chapter of a single-site operator acting
on the Hilbert space of a single hard-core boson:

<img class="diagram" width="30%" src="docs/VERSION/book/images/ablocks.png"/>

We see that for each index, if the index value is 1 then it is in the quantum
number 0 sector. If the index value is 2, the index is in the quantum number 1 sector.
Below we will see that more generally, multiple index values can fall into the same
quantum number sector.

## Constructing a Simple IQIndex

Continuing with the above example, let us construct a tensor index with quantum-number sectors:
an IQIndex.

    auto I = IQIndex("I",
                     Index("I0",1),QN(0),
                     Index("I1",1),QN(1),
                     Out);

An IQIndex contains an ordered collection of Index-QN pairs. The size of the Index determines
the size of that sector and the QN object labels the quantum number of that sector.

In the code above, the name of the IQIndex is "I". It has two sectors, both of size 1. 
The first sector is represented by the Index named "I0" (of size 1) and has quantum number 0.
The second sector is represented by the Index "I1" and has quantum number 1.

The arrow direction of I is specified as Out. The default arrow direction
is Out and we will often omit it below.

The size of this IQIndex is 2, because it has two sectors each of size 1.

## Constructing a General IQIndex

Now lets construct an IQIndex whose sectors correspond to multiple index values.
This can be done by making the sectors out of Index objects whose sizes are
greater than 1.

    auto J = IQIndex("J",
                     Index("j-2",2),QN(-2),
                     Index("j-1",4),QN(-1),
                     Index("j_0",6),QN(0),
                     Index("j+1",4),QN(+1),
                     Index("j+2",2),QN(+2));

This IQIndex has five sectors, labeled by five Index-QN pairs.

The first sector is labeled by the Index named "j-2". It has a size of 3 and an QN (quantum
number) of -2.

The second sector is labeled by the Index "j-1", has a size of 5, and a QN of -1.

Overall we can see that the IQIndex J has 5 sectors of varying sizes and quantum numbers.

The values that J can take (the index values of J) range from 1 up to 18 (=2+4+6+4+2). Values
1 and 2 correspond to the first sector; values 3 through 6 to the second sector; etc.

The above example can be summarized in a chart:

<img class="diagram" width="75%" src="docs/VERSION/book/images/iqindex_chart.png"/>

## Relationship to the Index Class

The IQIndex class is a subtype of the Index class. Thus every IQIndex is also an Index,
and an IQIndex can be automatically converted to an Index.

For the example above of the IQIndex "J", if we convert this IQIndex to an Index, 
the resulting Index will have the same name and total size (=18), but will no longer 
contain information about the sectors (sector sizes, sector Index labels, and QNs).

<br/>

<span style="float:left;"><img src="docs/VERSION/arrowleft.png" class="icon">
[[Block-Sparse Tensors|book/block_sparse]]
</span>

<br/>

