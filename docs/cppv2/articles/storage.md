<span class='article_title'>New ITensor Storage and Code Design</span>

<span class='article_sig'>Miles Stoudenmire&mdash;March 25, 2016</span>

### Background

A long-term goal of ITensor is supporting not just "regular" dense tensors
and quantum number conserving tensors (a special case of block-sparsity),
but a much richer variety of sparse tensors. We also want to leave
the door open for more ambitious future designs, such as tensors with storage distributed
across multiple machines.

ITensor storage prior to version 2.0 was just a contiguous array of real numbers, which
is insufficient for handling arbitrary sparse tensor types. Though we were able to cleverly
repurpose this storage to implement diagonal-sparse ITensors, this was just a workaround
until we could find a better solution.

For ITensor 2.0 we considered a few standard solutions, 
but most had serious drawbacks. Two examples:

* We could template ITensors over their storage type. But this would require any
  function taking an ITensor argument to be a template too. Not only would this severely
  increase compile times, but it would put an unnecessary burden on users, especially newer
  users unfamiliar with templates, and it would make the notation of many functions unwieldy.

* We could derive all storage types from an abstract parent 
  storage class and implement their behavior by overloading a set of virtual 
  methods they all share. But what is the minimal set of methods
  common to all tensor storage types? In practice, the number of virtual methods 
  ballooned out of control. Also, this design requires awkward choices, such as having to
  implement binary operations (addition, multiplication) between different types as 
  a class method bound to one of the two types. Which type should define such an operation?

### The doTask system: "dynamic overloading"

The design we went with is fairly novel for C++, although it is second nature in a 
language such as [Julia](http://julialang.org) which eschews class methods and supports multiple dispatch.
In a nutshell, our design works as follows:
1. An ITensor is basically just a shared pointer to an opaque "box" type which
can hold any of the pre-registered storage types. The pointer of an ITensor T
can be accessed by calling T.store().
2. Storage types (Dense, Diag, Combiner, etc.) are different types, each with 
their own unique layout and class methods. There are no requirements for storage types:
they do not have to inherit from any base class. The only necessary step
to use a new storage type is to register it in the ITensor storage system.
3. Methods for manipulating tensor storage are free functions, all overloads
of a function named doTask(...). These methods are distinguished by their first
argument, which is a lightweight type called the "task object". For example, to compute
the norm of a storage object, at the ITensor (interface) level one calls:


     Real
     norm(ITensor T)
     {
     auto nrm = doTask(Norm(),T.store());
     return nrm;
     }

Calling `doTask(Norm(),T.store())` searches for a function with the signature
`doTask(Norm,StorageType S)`. For example, to implement this task type for 
the Dense storage type, one defines the following function:

     Real
     doTask(Norm,Dense const& D)
     {
     //... code to compute norm of D ...
     return nrm;
     }

Importantly, leaving a doTask
overload undefined for a particular storage type is not a compile-time error.
An undefined method only causes an error if an attempt is made to call it 
at run time. This design allows one to focus on writing only the code
that is needed to define the meaningful behavior of each type, with minimal
boilerplate or glue code.

Other advantages and features of the doTask system:

* The return type of doTask overloads for each task type are deduced automatically
  at compile type, and can be different for different task types.

* Storage types need not define any particular class methods. Most interaction
  with storage types is through external functions. This generally
  leads to better code design ("encapsulation") where only a minimal set of class
  methods deals with private class data.

* "Design as research": when researching better storage designs, one only needs
  to implement a small minimal set of doTask overloads, such as defining tensor contraction. 
  Later, when preparing the new type for widespread use the remaining behaviors 
  (for example, tensor addition or write-to-disk) can be defined.



