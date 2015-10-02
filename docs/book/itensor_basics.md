# ITensor Basics

The ITensor, or intelligent tensor, is the basic tensor of the ITensor library.

The simplest way to construct an ITensor is to provide its indices:

    auto i = Index("index i",2),
         j = Index("index j",3),
         k = Index("index k",4);

    auto T = ITensor(i,j,k);

This makes an ITensor with all elements set to zero.

To confirm this is a rank 3 tensor (a tensor with 3 indices), call `rank(T)`:
    
    println("The rank of T is ",rank(T));
    //prints: The rank of T is 3

Alternatively you can use `T.r()`.

### Accessing ITensor Elements

To access the element of T where i is set to 2; j is set to 1; and k is set to 3
we call

    T.set(i(2),j(1),k(3),4.56);

This element now has the value 4.56.

In a more standard tensor interface, the above operation would have looked like:

    T(2,1,3) = 4.56; //not actual ITensor code!!

The reason one gives the indices along with their values in ITensor
is that nothing about the ITensor interface requires knowing the index order.

If we gave the Index-value pairs such as `j(2)` in a different order,
the `.set` method still accesses the correct element. A call such as 

    T.set(k(3),i(2),j(1),4.56);

has exactly the same outcome as the one above.

We can retrieve this element by calling the `.real` method:

    auto el = T.real(k(3),i(2),j(1));
    println("el = ",el);
    //prints: el = 4.56

This method is named "real" because it returns the requested 
element as a real number.

We can also set elements of ITensors to be complex numbers:

    T.set(i(2),k(3),j(1),7+8_i);

Now we must call the `.cplx` method to retrieve this element; calling
`.real` would throw an exception:

    auto z = T.cplx(i(2),k(3),j(1));
    println("z = ",z);
    //prints: z = (7,8)

Calling `.cplx` always succeeds even if the ITensor is real.

### Printing ITensors 

A convenient way to print and ITensor is to use the `Print` macro:

    Print(T);
    //prints: 
    // T = 
    // ITensor r = 3: (index i,2,Link) (index j,3,Link) (index k,4,Link)

Calling `Print(expr)` literally produces the code `println("expr = ",expr);`

    Print(prime(i));
    //prints: prime(i) = (index i,2,Link)'

By default an ITensor does not show its data when printed, because 
this can lead to very large output.

To see the result of our earlier calls to `.set`, we can print this ITensor
using the `PrintData` macro, which prints both the indices and the
non-zero elements of an ITensor:

    PrintData(T);
    //prints: 
    // T = 
    // ITensor r = 3: (index i,2,Link) (index j,3,Link) (index k,4,Link)
    // (2,2,1) 7.00+8.00i
    // (1,2,3) 4.56+0.00i

### Basic Tensor Operations

ITensors can be added, subtracted, and multiplied by scalars in the usual way:

    auto Q = 2*T;
    auto R = Q/3 + T*4_i;
    auto S = R - T;
    //etc.

Two ITensors can be added and subtracted if they have the same 
set of indices, regardless of index order.

The norm of an ITensor (square root of sum of squared elements) can be computed
using the `norm` function

    println("The norm of T is ",norm(T));





<br/>
<i>For a complete listing of all of the methods of class ITensor, view the
[[detailed documentation|classes/itensor]].</i>


<!-- Commented out for now

### Other ITensor Constructors

To construct a scalar ITensor with a single real or complex 
element x, call

    auto S = ITensor(x);

Constructing an ITensor with a set of Index-value pairs sets
the corresponding element to 1, leaving the rest zero:

    auto F = ITensor(i(2),k(1));

    println(F.real(i(2),k(1)));
    //prints: 1

    println(F.real(i(1),k(1)));
    //prints: 0

This constructor is very handy for creating ITensors which
"pick out" a single element of another tensor.

-->


<span style="float:left;"><img src="../../left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Index Objects|book/index]]
</span>
<!--
<span style="float:right;"><img src="../../right_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[Contracting ITensors|book/contracting_itensors]]
-->
</span>
