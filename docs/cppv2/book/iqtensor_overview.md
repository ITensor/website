# IQTensor Overview

Physical systems often have symmetries which make computing their properties easier.
Spin-rotation symmetry and particle number conservation (U(1) symmetry) are some key examples.

Here we consider global Abelian symmetries
associated with conserved "quantum numbers". 
Though tensor networks can also respect non-Abelian symmetries, as well
as spatial symmetries, these require additional techniques beyond the scope of our discussion.

Conserving quantum numbers allows tensors to be
block-sparse, with non-zero elements only for certain index ranges.
Many elements will be strictly zero, so we neither have to store these elements in memory or 
iterate over them during computations.

Of course, conserving quantum numbers is important for physics too.
Real experiments often conserve particle number. 
And using quantum numbers can make it easier to compute excited 
state properties.

Using the block-sparse [[IQTensor|classes/iqtensor]] class makes conserving quantum numbers automatic
for any tensor network algorithm. IQTensors have nearly the same interface as ITensors,
so they are straightforward to use in your code. But understanding IQTensors requires some 
background knowledge and an awareness of certain conventions;
these are the focus of the next few chapters.

<br/>
<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[Case Study: TRG Algorithm|book/trg]]
</span>
<span style="float:right;"><img src="docs/arrowright.png" class="icon">
[[Block-Sparse Tensors|book/block_sparse]]
</span>
<br/>
