# Index Objects

The most basic element of ITensor is not actually a tensor: it is a tensor index, 
an object of type&nbsp;`Index`. (By tensor index we mean i,j,k in an expression
like @@T_{ijk}@@ ). 

ITensors are "intelligent tensors" because they "know" what indices they have. 
This is possible since each Index carries extra information beyond its size.

The simplest way to construct an Index is to give its name and size:

    auto i = Index("index i",3);

Upon creation, an Index gets "stamped" with a hidden id number that allows copies 
of this Index to recognize each other:

    auto j = i;  //make a copy of i
    Print(j==i); //prints: j==i = true

To access the size of an Index, use its `.m()` method

    println("The size of ",i.name()," is ",i.m());
    //prints: The size of index i is 3

The convention of calling the size "m" comes from the DMRG literature.

<div class="example_clicker">Click here to view a full working example</div>

    #include "itensor/index.h"
    using namespace itensor;

    int main() 
    {
    auto i = Index("index i",3);
    println("The size of ",i.name()," is ",i.m());
    return 0;
    }


After creating an Index, most of its properties are permanently fixed. 
The philosophy of ITensor is that indices have a meaning at the time they are created.
A new Index can be created to take the place of an old one, but the semantic
meaning of a given Index object cannot be modified.

### Priming Indices

One property of an Index you can change is its prime level.

An Index starts out with prime level zero.
Two copies of the same Index with the same prime level compare equal.

Calling `prime(i)` will produce a copy of i with prime level raised by 1.
Because this copy has a different prime level, it will no longer compare equal to i.

    auto ip = prime(i);
    println("The prime level of ip is ",ip.primeLevel());
    //prints: The prime level of ip is 1
    printfln("ip==i is %s",ip==i);
    //prints: ip==i is false

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

The Index constructor accepts an optional `IndexType` argument:

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


<span style="float:left;"><img src="docs/arrowleft.png" class="icon">
[[ITensor Library Overview|book/intro]]
</span>
<span style="float:right;"><img src="docs/arrowright.png" class="icon">
[[ITensor Basics|book/itensor_basics]]
</span>
