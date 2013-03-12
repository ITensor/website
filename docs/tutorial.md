#Tutorial: Table of Contents#

[[0. Introduction: the ITensor|tutorial]]

[[1. A Simple Measurement|tutorial/simple_measurement]]

</br>

#Introduction: the ITensor#

Before diving into the tutorial, let us introduce the object at the heart of the 
library: the intelligent tensor or ITensor.

As a first example, consider multiplying a 10 x 20 matrix _A_ by a 20 x 30 matrix _B_
to get a 10 x 30 matrix _C_. 
In traditional index notation we would write (summation over `j` implied)

`Cik = Aij Bjk`

To do this using ITensors, first define three Index instances, `i`, `j` and `k`

`Index i("i",10), j("j",20), k("k",30);`

The first argument to each constructor is a string saying how that Index is to be printed.
The second argument is the dimension of the Index, that is, the number of values it can take.

Now declare the actual ITensors:

`ITensor A(i,j), B(j,k), C;`

So far we have only specified the indices of each ITensor; all of their components are set to zero by default.

An ITensor has no ordering of its indices, so `A(2,1)` is not defined;
instead, for example, to set a the (2,1) element of `A` to the value 0.5 we write

`A(i(2),j(1)) = 0.5`

This has the same effect as

`A(j(1),i(2)) = 0.5`

We can set all remaining components of `A` and `B` likewise.

Now the matrix multiplication discussed earlier becomes

`C = A * B`

We can get the same result by computing

`C = B * A`

In either case index `j` is automatically contracted over, so the 
result `C` will have indices `i` and `k`, with no ordering associated
to them. We see that multiplication with ITensors commutes!

(Of course not all operators commute in quantum mechanics, but an ITensor Index carries no
quantum numbers itself. To use quantum numbers, see the documentation on [[IQTensor|classes/iqtensor]].)

Next section, [[a simple measurement|tutorial/simple_measurement]].

[[Back to Main|main]]
