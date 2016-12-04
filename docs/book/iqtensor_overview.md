# IQTensor Overview

Physical systems can have symmetries which make it easier to understand their
structure and to compute their properties. Key examples are spin-rotation
symmetry or particle number conservation.

Here we consider only global Abelian symmetries
associated with conserved "quantum numbers". 
Though tensor networks can exploit spatial and non-Abelian symmetries,
these require additional techniques.

Conserving quantum numbers will make our tensors
block-sparse, with non-zero elements only for certain index ranges.
Many elements will be strictly zero, so we neither have to store them in memory or 
loop over them in computations.

Of course, conserving quantum numbers is important for physics too.
Real experiments often conserve particle number. 
Using quantum numbers can also make it easier to compute excited 
state properties.

Using the block-sparse [[IQTensor|classes/iqtensor]] class makes conserving quantum numbers automatic
for any tensor network algorithm. IQTensors have nearly the same interface as ITensors,
so they are easy to use.

<br/>
<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[Case Study: TRG Algorithm|book/trg]]
</span>
<span style="float:right;"><img src="docs/arrowright.png" class="icon">
[[Block-Sparse Tensors|book/block_sparse]]
</span>
<br/>
