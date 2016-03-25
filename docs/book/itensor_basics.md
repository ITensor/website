# ITensor Basics

The ITensor, or intelligent tensor, is the basic tensor of the ITensor library.

The simplest way to construct an ITensor is to provide its indices:

    auto i = Index("index i",2),
         j = Index("index j",3),
         k = Index("index k",4);

    auto T = ITensor(i,j,k);

This creates an ITensor T with all elements set to zero.

To confirm this is a rank 3 tensor (a tensor with 3 indices), call `rank(T)`:
    
    println("The rank of T is ",rank(T));
    //prints: The rank of T is 3

Alternatively you can call `T.r()`.

<div class="example_clicker">Click here to view a full working example</div>

    #include "itensor/itensor.h"
    using namespace itensor;

    int main()
    {
    auto i = Index("index i",2),
         j = Index("index j",3),
         k = Index("index k",4);
    
    auto T = ITensor(i,j,k);
    
    println("The rank of T is ",rank(T));

    return 0;
    }

<a name="elements"></a>
### Accessing ITensor Elements

To set a particular element, or component, of an ITensor call its `.set` method:

    T.set(i(2),j(1),k(3),4.56);

This element now has the value 4.56.

In a more conventional tensor interface, the above operation would look like:

    T(2,1,3) = 4.56; //not actual ITensor code!!

The reason the indices are passed along with their values in the ITensor `.set` method
is that nothing about the ITensor interface requires knowing the index order.

If we gave the Index-value pairs such as `j(2)` in a different order,
the `.set` method still accesses the correct element. A call such as 

    T.set(k(3),i(2),j(1),4.56);

has exactly the same outcome as the one above.

We can retrieve this element by calling the `.real` method:

    auto el = T.real(k(3),i(2),j(1));
    println("el = ",el);
    //prints: el = 4.56

This method is named "real" because it says we want the element to be
returned as a real number.

We can also set elements of ITensors to be complex numbers:

    T.set(i(2),k(3),j(1),7+8_i);

Now we must call the `.cplx` method to retrieve this element as a 
complex data type; calling `.real` would throw an exception:

    auto z = T.cplx(i(2),k(3),j(1));
    println("z = ",z);
    //prints: z = (7,8)

Calling `.cplx` always succeeds even if the tensor has only real elements.

### Printing ITensors 

A convenient way to print and ITensor is to use the `Print` macro:

    #include "itensor/util/print_macro.h"
    
    Print(T);
    //prints: 
    // T = 
    // ITensor r = 3: (index i,2,Link) (index j,3,Link) (index k,4,Link)

Calling `Print(expr)` essentially rewrites the code to be `println("expr = ",expr)`,
which is why there is a "T = " at the beginning of the output.

The output shows the rank and all the indices, but not the ITensor elements
because this could lead to a very large output.

To see the non-zero elements resulting from our earlier calls to `.set`, 
we can use the `PrintData` macro, which prints both 
the indices and the non-zero elements:

    PrintData(T);
    //prints: 
    // T = 
    // ITensor r = 3: (index i,2,Link) (index j,3,Link) (index k,4,Link)
    // (2,2,1) 7.00+8.00i
    // (1,2,3) 4.56+0.00i

### Basic Mathematical Operations

ITensors can be added, subtracted, and multiplied by scalars in the usual way:

    auto Q = 2*T;
    auto R = Q/3 + T*4_i;
    auto S = R - T;
    S *= 5;
    //etc.

Two ITensors can be added and subtracted if they have the same 
set of indices, regardless of index order. Internally, the tensor data
will be permuted if the index order is different, guaranteeing the correct 
result.

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


<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[Index Objects|book/index]]
</span>
<span style="float:right;"><img src="docs/arrowright.png" class="icon">
[[Contracting ITensors|book/itensor_contraction]]
</span>
