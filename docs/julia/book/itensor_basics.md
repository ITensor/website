# ITensor Basics

The ITensor, or intelligent tensor, is the basic tensor of the ITensor library.

The simplest way to construct an ITensor is to provide its indices:

    i = Index(2,"i")
    j = Index(3,"j")
    k = Index(4,"k")

    T = ITensor(i,j,k)

This creates an ITensor T with all elements set to zero.

To confirm this is an order 3 tensor (a tensor with 3 indices), call `order(T)`:
    
    println("The order of T is ",order(T))
    //prints: The order of T is 3

<div class="example_clicker">Click here to view a full working example</div>

    using ITensors

    let
      i = Index(2,"index i")
      j = Index(3,"index j")
      k = Index(4,"index k")
      
      T = ITensor(i,j,k);
      
      println("The order of T is ",order(T));

      return
    }

<a name="elements"></a>
### Accessing ITensor Elements

To set a particular element, or component, of an ITensor, use the following code:

    T[i=>2,j=>1,k=>3] = 4.56

This sets the i=2,j=1,k=3 element of the tensor to the value 4.56.

In a more conventional tensor interface, the above operation might 
look something like

    T[2,1,3] = 4.56; # not actual ITensor code!!

where the user would have to remember that the first entry corresponds to index
i, the second to index j, and the third to index k.

For an ITensor, the reason the indices are provided along with their values
is that nothing about the ITensor interface requires knowing the index order.

If we gave the Index-value pairs such as `j=>2` in a different order,
we will still accesses the correct element. A call such as 

    T[k=>3,i=>2,j=>1] = 4.56

has exactly the same outcome as the call

    T[i=>2,j=>1,k=>3] = 4.56

We can retrieve an element in a similar way:

    x = T[k=>3,i=>2,j=>1]
    @show x # prints: x = 4.56

We can also make complex-valued ITensors and set their elements:

    T = ITensor(ComplexF64,i,j,k)
    T[i=>2,k=>3,j=>1] = 7+9im

### Printing ITensors 

A convenient way to print an ITensor is to use the `@show` macro:

    @show T
    # prints: 
    #  T = 
    #  IndexSet{2,Index{Int64}}
    #  Dim 1: (dim=2|id=426|"i")
    #  Dim 2: (dim=3|id=311|"j")
    #  ITensors.NDTensors.Dense{Complex{Float64},Array{Complex{Float64},1}}
    #   2x3
    # 
    #   0.0 + 11.0im  0.0 + 0.0im  0.0 + 0.0im
    #   0.0 + 0.0im   0.0 + 0.0im  0.0 + 0.0im

As you can see, a lot of useful information gets printed, including
all of the elements of the ITensor. To see just the indices
of an ITensor, you can do this:

    @show inds(T)
    # prints: 
    #  inds(T) = (dim=2|id=426|"i") (dim=3|id=311|"j") 

### Basic Mathematical Operations

ITensors can be added, subtracted, and multiplied by scalars in the usual way:

    Q = 2*T
    R = Q/3 + T*4_i
    S = R - T
    S *= 5
    # etc.

Two ITensors can be added and subtracted if they have the same 
set of indices, regardless of the index ordering. Internally, the tensor data
will be permuted if the index ordering is different, guaranteeing the correct 
result.

The norm of an ITensor (square root of sum of squared elements) can be computed
using the `norm` function

    println("The norm of T is ",norm(T))


<br/>

<span style="float:left;"><img src="docs/VERSION/arrowleft.png" class="icon">
[[Index Objects|book/index]]
</span>
<span style="float:right;"><img src="docs/VERSION/arrowright.png" class="icon">
[[Contracting ITensors|book/itensor_contraction]]
</span>

<br/>
