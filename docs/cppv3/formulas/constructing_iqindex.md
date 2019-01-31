# Constructing an IQIndex

IQTensors are block-sparse tensors that respect certain Abelian symmetries (i.e. have well-defined quantum numbers).
An IQTensor infers its block structure from the block structure of its indices, which are objects of type IQIndex.

An IQIndex is a type of Index, but in addition it has 
sectors consisting of Index-QN pairs. Each sector has a fixed size, determined by its Index, and a quantum number
QN object, stating the quantum number associated with that sector (in mathematical terms, labeling the 
representation of the symmetry group action on that sector).

For a concrete example, consider an IQIndex "S" representing a single spin-half degree
of freedom (a single lattice site of a spin 1/2 system).


    IQIndex S("index S",
              Index("S up",1),QN(+1),
              Index("S dn",1),QN(-1));

This IQIndex has two sectors: one associated with spin +1/2 (== QN(+1)) and spin -1/2 (== QN(-1)).
Note that the QN class uses units of spin 1/2.

The total size of this IQIndex is 2 because it has two sectors of size 1.

    Print(S.m());
    //prints: S.m() = 2

We can likewise make a spin one site as follows:

    IQIndex S("index S",
              Index("S up",1),QN(+2),
              Index("S z0",1),QN( 0),
              Index("S dn",1),QN(-2));

A more general IQIndex, such as along the virtual direction of a non-trivial matrix product state,
will have sectors with sizes greater than one

    //General IQIndex
    IQIndex J("index J",
             Index("J+3",6), QN(+3),
             Index("J+1",12),QN(+1),
             Index("J 0",20),QN( 0),
             Index("J-1",6), QN(-1));

Finally, to access the sectors of an IQIndex, use the `.index` and `.qn` accessor methods, which are 1-indexed:

    Print(J.index(2));
    //prints: J.index(2) = ("J+1",12,Link)

    Print(J.qn(3));
    //prints: J.qn(3) = (sz=-1, Nf=0, p=0)

