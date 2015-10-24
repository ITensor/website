# Index Objects

The most basic element of ITensor is not actually a tensor: it is a tensor index, 
an object of type&nbsp;`Index`.
ITensors are "intelligent tensors" because they "know" what indices they have. 
This is possible since each Index carries extra information.
In addition to having a fixed size, or dimension, an Index has:

* An internal id number for checking whether two Index objects are equal.

* A prime level starting at zero which can be raised or lowered to make an Index distinct
from others with the same id.

* An IndexType tag saying what kind of index it is. By default an Index has type `Link`. 
By convention, physical indices are assigned the type `Site`. Indices can have custom user-defined IndexTypes.

* A name used to display the Index.

The simplest way to construct an Index is to give its name and size:

    auto i = Index("index i",3);

To access the size, use the `.m()` method

    println("The size of ",i.name()," is ",i.m());
    //prints: The size of index i is 3

The convention of calling the size "m" comes from the DMRG literature.

After creating an Index, its properties are permanently fixed. The philosophy
of ITensor is that indices have a meaning at the time they are created.
One ITensor can be replaced by another with different indices, but an Index 
itself cannot be changed. 

### Index Comparison

Two copies of the same Index with the same prime level compare equal:

    auto i = Index("index i",3);
    auto ic = i;
    printfln("ic==i is %s",ic==i);
    //prints: ic==i is true

Calling `prime(i)` will produce a copy of i with prime level raised by 1.
Because this copy has a different prime level, it will no longer compare equal to i.

    auto ip = prime(i);
    println("The prime level of ip is ",ip.primeLevel());
    //prints: The prime level of ip is 1
    printfln("ip==i is %s",ip==i);
    //prints: ip==i is false

### Priming Indices

There are many convenient ways to manipulate Index prime levels.
The `prime` function accepts an optional increment amount:

    auto i3 = prime(i,3);
    println(i3.primeLevel());
    //prints: 3

Calling `noprime` resets the prime level to zero.

    auto i0 = noprime(i3);
    println(i0.primeLevel());
    //prints: 0

We will see more ways to manipulate primes as we 
work with ITensors that have multiple indices.

### Printing Indices

Printing an Index shows useful information about it:

    println(i);
    //prints: (index i,3,Link)

The output shows the name, size, and IndexType of i (the default is Link).

The prime level is displayed at the end:

    println(prime(i,2));
    //prints: (index i,3,Link)''

    println(prime(i,10));
    //prints: (index i,3,Link)'10

### Index Types

The Index constructor optionally accepts an `IndexType` argument:

    auto s2 = Index("site 2",2,Site); //IndexType set to Site

Giving indices different IndexTypes becomes useful when working with many indices
because it allows us to change the prime level of all indices of a certain type.

It is possible to define a custom IndexType:

    auto MyType = IndexType("MyType");
    auto m1 = Index("m1",5,MyType);
    auto m2 = Index("m2",7,MyType);

An IndexType is just a fixed-size string, and can be up to 7 characters long. 
The type of an Index can be obtained by calling the `.type()` method.

    println("The type of m1 is ",m1.type());
    //prints: The type of m1 is MyType

<br/>
<i>For a complete listing of all of the methods of class Index, view the
[[detailed documentation|classes/index]].</i>


<span style="float:left;"><img src="docs/book/images/left_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[ITensor Library Overview|book/intro]]
</span>
<span style="float:right;"><img src="docs/book/images/right_arrow.png" width="20px" style="vertical-align:middle;"/> 
[[ITensor Basics|book/itensor_basics]]
</span>
