# Making a Custom Site Type / Physical Degree of Freedom

ITensor provides support for a range of common site types, or physical 
degrees of freedom, such as S=1/2 and S=1 spins; spinless and spinful
fermions; and more.

However, there can be many cases where you need to customize your 
degrees of freedom or "site types" (referring to sites of a lattice model).
You might be working with an
exotic system, such as @@Z_N@@ parafermions for example, or need
to customize other defaults provided by ITensor.

Below we give an brief introduction by example of how to make
custom site Index types in ITensor,
followed by more examples adding extra details such as support for 
quantum number (QN) conservation.

Throughout we will focus on the example of @@S=3/2@@ spins. These
are spins taking the @@S^z@@ values of @@+3/2,+1/2,-1/2,-3/2@@.
So as tensor indices, they are indices of dimension 4.

The key operators we will make for this example are @@S^z@@, @@S^+@@,
and @@S^-@@, which are defined as:

\begin{align}
S^z &= 
\begin{bmatrix}
3/2 &  0  &  0  &  0 \\
 0  & 1/2 &  0  &  0 \\
 0  &  0  &-1/2 &  0 \\
 0  &  0  &  0  &-3/2\\
\end{bmatrix} \\

S^+ & = 
\begin{bmatrix}
 0  &  \sqrt{3}  &  0  &  0 \\
 0  &  0  &  2  &  0 \\
 0  &  0  &  0  &  \sqrt{3} \\
 0  &  0  &  0  &  0 \\
\end{bmatrix} \\

S^- & = 
\begin{bmatrix}
 0  &  0 &  0  &  0 \\
 \sqrt{3}  &  0  &  0  &  0 \\
 0  &  2  &  0  &  0  \\
 0  &  0  &  \sqrt{3}  &  0 \\
\end{bmatrix} \\
\end{align}

## Minimal Example: 

First let's see the minimal code needed to define and use this new
@@S=3/2@@ site type, then we will discuss what each part of
the code is doing.

    include:docs/VERSION/formulas/site_type/minimal_spinthreehalf.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/site_type/minimal_spinthreehalf.jl">Download this example code</a>

Now let's look at each part of the code above.

### The Tag Type

The first part of the code defines a special type, known as a `TagType`
which is basically a type (such as Int or Float64) but made from a 
string. After writing the line:

    const SpinThreeHalfSite = TagType"S=3/2"

there is now a new type in the Julia type system which is `TagType"S=3/2"`.
But because this is kind of awkward to write, we have created an alias 
for this type: `SpinThreeHalfSite`. It is just another way of writing the same type.

What is the purpose of a `TagType`? It is somewhat technical in detail, but at 
a simple level it allows ITensor to deduced which of a set of overloaded 
functions to call based on what tag or tags a particular Index has. So if the
code encounters an Index such as `Index(4,"S=3/2")` it can call functions
which are specialized for indices carrying the `"S=3/2"` tag. This can happen
even though Index tags are known only at run time.

### The siteinds Function

The function `siteinds` is defined for our new custom
`SpinThreeHalfSite` type as follows:

    function siteinds(::SpinThreeHalfSite,
                      N::Int; kwargs...)
      return [Index(4,"S=3/2,Site,n=$n") for n=1:N]
    end

All this function does is make an array, or vector of Index objects.
The important thing is that the Index objects in the returned array
carry the `"S=3/2"` tag. However, it's also customary and useful to put the `"Site"`tag which is ITensor's convention for site indices of MPS and MPO objects, as well as the tag `"n=$n"` which labels each Index as "n=1", "n=2", etc.

The `siteinds` function is not strictly necessary for working with special
degrees of freedom and `TagType`s. But it's convenient to have for 
constructing MPOs, MPS, and using AutoMPO, each of which asks for arrays
of Index objects as input when making new MPOs or MPS. 

After defining this `siteinds` function, you can just write code like:

    N = 100
    sites = siteinds("S=3/2",N)

The special `TagType` system in ITensor will automatically handle the
conversion of the argument `"S=3/2"`, which is just a string, into a type
so that the specialization above actually gets called. Try running this 
code and printing out the `sites` object: you will see that it's just
a regular Julia array of Index objects.

### The op Function

The `op` function is really the heart of the `TagType` system. This is
the function that lets you define custom local operators associated
to the physical degrees of freedom of your `TagType`. Then for example 
you can use indices carrying your custom tag with AutoMPO and the 
AutoMPO system will know how to automatically convert names of operators
such as `"Sz"` or `"S+"` into ITensors so that it can make an actual MPO.

In our example above, we defined this function as:

    function op(::SpinThreeHalfSite,
                s::Index,
                opname::AbstractString; kwargs...)
    
      Op = ITensor(s',dag(s))
    
      if opname == "Sz"
        Op[s'(1), s(1)] = +3/2
        Op[s'(2), s(2)] = +1/2
        Op[s'(3), s(3)] = -1/2
        Op[s'(4), s(4)] = -3/2
      elseif opname == "S+"
        Op[s'(1),s(2)] = sqrt(3)
        Op[s'(2),s(3)] = 2
        Op[s'(2),s(3)] = sqrt(3)
      elseif opname == "S-"
        Op[s'(2), s(1)] = sqrt(3)
        Op[s'(3), s(2)] = 2
        Op[s'(4), s(3)] = sqrt(3)
      else
        throw(ArgumentError("Operator name '$opname' not recognized for SpinThreeHalfSite"))
      end
      return Op
    end

As you can see, the function is passed an Index `s` and an operator name `opname`.
Then it constructs an empty ITensor which is ready to have its elements set.
Finally the function inspects `opname` to see if it is one of the recognized operator names, and if so, sets its elements appropriately to the values defining that operator and returns it. To make more operators, all you have to do is to define more branches of the `if...elseif...end` statement to include more recognized operator names.

Once this function is defined, and if you have an Index such as

    s = Index(4,"S=3/2")

then, for example, you can call the `op` function as

    Sz = op(s,"Sz")
    @show Sz

to request the `"Sz"` operator for this Index. Again, through the magic of the `TagType`
system, the ITensor library takes your Index, reads off its tags, 
notices that one of them is `"S=3/2"`, and converts this into the type 
`SpinThreeHalfSite` in order to call the specialized function defined above.

You can use the `op` function yourself with a set of site indices created from
the `siteinds` function like this:

    N = 100
    sites = siteinds("S=3/2",N)
    Sz1 = op(sites[1],"Sz")
    Sz3 = op(sites[3],"Sz")

Alternatively, you can write the lines of code above as `Sz3 = op(sites,"Sz",3)`.

This same `op` function is used inside of AutoMPO when it converts its input into
an actual MPO. So by defining custom operator names you can pass any of these
operator names into AutoMPO and it will know how to use these operators.

## Example with Quantum Number Conservation

The above example showed most of the key aspects of the `TagType` system
for making custom site index types, or custom physical degrees of freedom.
But for simplicity the example left out an aspect which can be very 
important for state-of-the-art physics calculations, which is the possibility
of quantum number (QN) conservation.
Conserving quantum numbers can be very important for obtaining correct physical
results, speeding up calculations, and calculating eigenstates other than
the ground state in DMRG.

Without going into full detail here, quantum numbers in ITensor are defined
at the level of tensor indices or Index objects. When an Index object is 
constructed, instead of just specifying its dimension, you can instead 
provide an ordered collection of *QN subspaces* each corresponding to 
a specific quantum number (QN) object and having its own sub-dimension.
(The dimension of the resulting Index is a sum of its subspace dimensions.)

For most cases in physics, all this means is that you have to think through
the "settings" of the physical Index you are defining, and specify which
QNs you want each of these settings to correspond to. So for our @@S=3/2@@
example what we want the four possible states to correspond to are 
the @@S^z@@ quantum number to have the values @@S^z= +3/2,+1/2,-1/2,-3/2@@.

In ITensor code, this corresponds to giving our `"S=3/2"` tagged Index objects
QN structure as follows:

    s = Index(QN("Sz",+3)=>1,
              QN("Sz",+1)=>1,
              QN("Sz",-1)=>1,
              QN("Sz",-3)=>1;
              tags="S=3/2")

We can check that this Index has a dimension of four like in our simpler example
above by calling `dim(s)` and seeing that `dim(s)==4`. This follows from the 
fact that there are four subspaces of dimension 1: `QN("Sz",+3)=>1`, `QN("Sz",+1)=>1`,
etc. Note that the @@S^z@@ values are given in units of 1/2; this is the convention
used by ITensor so that we can store all quantum numbers as integers.

### QN-conserving siteinds Function

After this rather long technical background, actually making your custom
site or `TagType` definition offer QN conservation is rather simple. Just
replace the `siteinds` function by the following definition:

    function siteinds(::SpinThreeHalfSite,
                      N::Int; kwargs...)
      s = Index(QN("Sz",+3)=>1,
                QN("Sz",+1)=>1,
                QN("Sz",-1)=>1,
                QN("Sz",-3)=>1)
      return [sim(s;tags="Site,S=3/2,n=$n") for n=1:N]
    end

Note the similarity to the simpler example above. The only differences are that:
1. When we define Index objects to go into the array, we specify a set of 
   QN=>Int pairs instead of just a total dimension
2. We make a single prototype Index `s` for convenience, then paste separate
   tags onto clones of this Index using the `sim` function. This is just so
   we don't have to put the long definition of all the QN subspaces into
   the line of code that constructs the array to return.

Finally, if we want, we can upgrade the `siteinds` function to handle either
the QN-conserving case or the regular, non-QN-conserving case through a set
of keyword arguments. This is optional, but if you are interested the 
defintion of `siteinds` with this capability looks like:

    function siteinds(::SpinThreeHalfSite,
                      N::Int; kwargs...)
      conserve_qns = get(kwargs,:conserve_qns,false)
      if conserve_qns
        s = Index(QN("Sz",+3)=>1,QN("Sz",+1)=>1,QN("Sz",-1)=>1,QN("Sz",-3)=>1)
        return [sim(s;tags="Site,S=3/2,n=$n") for n=1:N]
      end
      return [Index(4,"Site,S=3/2,n=$n") for n=1:N]
    end

The function above is just a merger of the two different ways of writing
`siteinds` in the two examples above, with the keyword argument `conserve_qns`
toggling whether to use the QN-conserving way of constructing the indices or not.

### Putting It All Together

Note that the `siteinds` function is the only part of the code that has
to be upgraded to conserve QNs. The rest of the code, such as the `op` function,
and other code that depends on it automatically has the QN information propagated
out to it through the information in each Index object.

So when we combine the above pieces together, we get the following QN-conserving
(or not) code:

    include:docs/VERSION/formulas/site_type/spinthreehalf.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/site_type/spinthreehalf.jl">Download this example code</a>



