#Tutorial: Table of Contents#

[[Introduction|tutorial]]

[[1. A Simple Measurement|tutorial/simple_measurement]]

</br>

#Tutorial Introduction#

Before diving into the tutorial, let us introduce the object at the heart of the 
library: the intelligent tensor or ITensor.

As a first example, consider multiplying a 10 x 20 matrix _A_ by a 20 x 30 matrix _B_
to get a 10 x 30 matrix _C_. 
In traditional index notation we would write (summation over `j` implied)

`Cik = Aij Bjk`

To use ITensors, first define three Index objects, `i`, `j` and `k`

`Index i("i",10), j("j",20),k("k",30);`

The first argument to each constructor is a string saying how that Index is to be printed.
The second argument is the dimension of the Index.

Now declare the actual ITensors:

`ITensor A(i,j),B(j,k),C;`

An ITensor has no ordering of its indices, so `A(2,1)` is not defined;
instead, to set a value of 0.5 for the (2,1) element of `A`, for example,
we write

`A(i(2),j(1)) = 0.5`

which has the same effect as

`A(j(1),i(2)) = 0.5`

Now the multiplication is simply

`C = A * B`

which gives the same result as

`C = B * A`

The index `j` is automatically contracted over, so the 
result `C` has indices `i` and `k`, with no ordering associated
with them. We see that multiplication with ITensors commutes!

Next section, [[a simple measurement|tutorial/simple_measurement]].

[[Back to Main|main]]
