
An ITensor has indices like a normal tensor--for instance, an ITensor having two indices is a matrix. Each Index has a unique ID number and remembers its dimension. This allows indices to be correctly matched during tensor operations.


To construct an ITensor, first construct indices for it to use.

`Index a("a",2), b("b",2), c("c",2);`

Each Index is declared with two arguments: its name and its dimension. In this case, all of the Indices have dimension 2.

Now declare two ITensors and set their components.


`ITensor M(a,b), X(b,c);`

<code>
M(a(1),b(1)) = 11; M(a(1),b(2)) = 12;
&nbsp;M(a(2),b(1)) = 21; M(a(2),b(2)) = 22;
</code>

<code>
X(b(1),c(1)) =  0; X(b(1),c(2)) =  1;
&nbsp;X(b(2),c(1)) =  1; X(b(2),c(2)) =  0;
</code>

Unlike a standard tensor, an ITensor has no preferred ordering of indices. We could have equally written `M(b(2),a(1)) = 12;` and obtained the same result.

To perform a contraction, just multiply M and X and store the result

`ITensor R = M * X;`

Matching indices are automatically summed. Because an ITensor has no index order, we could have also written `X * M.`


Another new change