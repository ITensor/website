# QN ITensor Introduction

Physical systems often respect certain symmetries which can make computing 
their properties more efficient numerically.
Key examples are spin-rotation symmetry and particle number conservation (U(1) symmetry).

Here we consider global symmetries associated with conserved "quantum numbers". 
We only consider the case of Abelian symmetries. Though tensor networks can in principle
respect non-Abelian symmetries too, these are not yet supported by ITensor.

From a computational perspective, conservation of quantum numbers allows 
tensors to be block-sparse, with non-zero elements only for certain index ranges.
Many elements will be strictly zero, so we neither have to store these 
elements in memory or iterate over them during computations.

Of course, conserving quantum numbers is quite important for physical reasons.
Experiments involving trapped atoms often (ideally) conserve particle number, for example.
And using quantum numbers can make it easier to compute excited state properties.

Using block-sparse ITensors makes conserving quantum numbers automatic
for any tensor network algorithm. These ITensors have exactly the same interface as 
dense ITensors, just a different storage type, so they are straightforward to use in your code. 
But understanding QN ITensors requires some 
background knowledge and an awareness of certain conventions which are enforced;
these are the focus of the next few chapters.

<br/>
<span style="float:left;"><img src="docs/VERSION/arrowleft.png" class="icon">
[[Case Study: TRG Algorithm|book/trg]]
</span>
<span style="float:right;"><img src="docs/VERSION/arrowright.png" class="icon">
[[Block-Sparse Tensors|book/block_sparse]]
</span>
<br/>
