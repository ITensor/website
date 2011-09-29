#Tutorial Introduction#

As a first example, consider multiplying a 10 x 20 matrix A by a 20 x 30 matrix B
to get a 10 x 30 matrix C. In traditional index notation we would write (summation over `j` implied)

`Cik = Aij Bjk`

To use ITensors, first we define three Index objects, `i`, `j` and `k`

`Index i("i",10), j("j",20),k("k",30);`

(The indices in quotes tell how the Index objects are to be printed.)
Then we define the ITensors

`ITensor A(i,j),B(j,k),C;`

ITensor `A` has no ordering of its indices, so `A(2,1)` is not defined;
instead, to fill in a value of, say, 0.5 for the (2,1) element of `A`
we write

`A(j(1),i(2)) = 0.5`

which would be identical to

`A(i(2),j(1)) = 0.5`

Now the multiplication is simply

`C = A * B`

which would be identical to 

`C = B * A`

The index `j` is automatically contracted over, so the 
result `C` has indices `i` and `k`, with no ordering associated
with them. We see that multiplication with ITensors commutes!




[[Back to Main|main]]
