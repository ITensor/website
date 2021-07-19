# Make a Custom Local Hilbert Space / Physical Degree of Freedom

ITensor provides support for a range of common local Hilbert space types, 
or physical degrees of freedom, such as S=1/2 and S=1 spins; spinless and spinful
fermions; and more.

However, there can be many cases where you need to make custom
degrees of freedom. You might be working with an
exotic system, such as @@Z_N@@ parafermions for example, or need
to customize other defaults provided by ITensor.

In ITensor, such a customization is done by overloading functions
on specially designated Index tags. 
Below we give an brief introduction by example of how to make
such custom Index site types in ITensor. 
Other code formulas following this one explain how to build on this
example to expand the capabilities of your custom site type such as
adding support for quantum number (QN) conservation and defining
custom mappings of strings to states.

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

## Code Preview

First let's see the minimal code needed to define and use this new
@@S=3/2@@ site type, then we will discuss what each part of
the code is doing.

    include:docs/VERSION/formulas/sitetype_basic/minimal_spinthreehalf.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/site_type/minimal_spinthreehalf.jl">Download this example code</a>

Now let's look at each part of the code above.

### The SiteType

The most important aspect of this code is a special type, known as a `SiteType`,
which is a type made from a string. The string of interest here will be an Index
tag. In the code above, the `SiteType` we are using is

    SiteType"S=3/2"

What is the purpose of a `SiteType`? The answer is that we would like to be 
able to select different functions to call on an ITensor Index based on what tags
it has, but that is not directly possible in Julia or indeed most languages. 
However, if we can map a tag
to a type in the Julia type system, we can create function overloads for that type.
ITensor does this for certain functions for you, and we will discuss a few of these
functions below. So if the code encounters an Index such as `Index(4,"S=3/2")` it can 
call these functions which are specialized for indices carrying the `"S=3/2"` tag. 

### The space Function

One of the overloadable `SiteType` functions is `space`, whose job is to 
describe the vector space corresponding to that site type. For our
`SiteType"S=3/2"` overload of `space`, which gets called for any Index 
carrying the `"S=3/2"` tag, the definition is

    ITensors.space(::SiteType"S=3/2") = 4

Note that the function name is prepended with `ITensors.` before `space`.
This prefix makes sure the function is overloading other versions of the `space`
inside the `ITensors` module.

The only information needed about the vector space of a `"S=3/2"` Index in
this example is that it is of dimension four. So the `space` function returns
the integer `4`. We will see in more advanced examples that the returned value
can instead be an array which specifies not only the dimension of a `"S=3/2"`
Index, but also additional subspace structure it has corresponding to quantum
numbers.

After defining this `space` function, you can just write code like:

    s = siteind("S=3/2")

to obtain a single `"S=3/2"` Index, or write code like

    N = 100
    sites = siteinds("S=3/2",N)

to obtain an array of N `"S=3/2"` indices. The custom `space` function
will be used to determine the dimension of these indices, and the `siteind`
or `siteinds` functions provided by ITensor will help with extra things like
putting other Index tags that are conventional for site indices.

### The op Function

The `op` function is really the heart of the `SiteType` system. This is
the function that lets you define custom local operators associated
to the physical degrees of freedom of your `SiteType`. Then for example 
you can use indices carrying your custom tag with AutoMPO and the 
AutoMPO system will know how to automatically convert names of operators
such as `"Sz"` or `"S+"` into ITensors so that it can make an actual MPO.

In our example above, we defined this function for the case of the `"Sz"`
operator as:

    function ITensors.op!(Op::ITensor,
                          ::OpName"Sz",
                          ::SiteType"S=3/2",
                          s::Index)
      Op[s'=>1,s=>1] = +3/2
      Op[s'=>2,s=>2] = +1/2
      Op[s'=>3,s=>3] = -1/2
      Op[s'=>4,s=>4] = -3/2
    end

As you can see, the function is passed an ITensor `Op` and an Index `s`. The other
arguments are there to select which of the various functions named `op!` get called.
It is guaranteed by the `op` system that the ITensor `Op` will have indices `s` and `s'`.

The body of this overload of `ITensors.op!` is just setting the elements of the `Op`
ITensor to the correct values that define the `"Sz"` operator for an @@S=3/2@@ spin.

Once this function is defined, and if you have an Index such as

    s = Index(4,"S=3/2")

then, for example, you can get the `"Sz"` operator for this Index 
and print it out by doing:

    Sz = op("Sz",s)
    @show Sz

Again, through the magic of the `SiteType`
system, the ITensor library takes your Index, reads off its tags, 
notices that one of them is `"S=3/2"`, and converts this into the type 
`SiteType"S=3/2"` in order to call the specialized function `ITensors.op!` defined above.

You can use the `op` function yourself with a set of site indices created from
the `siteinds` function like this:

    N = 100
    sites = siteinds("S=3/2",N)
    Sz1 = op("Sz",sites[1])
    Sp3 = op("S+",sites[3])

Alternatively, you can write the lines of code above in the style
of `Sz1 = op("Sz",sites,1)`.

This same `op` function is used inside of AutoMPO when it converts its input into
an actual MPO. So by defining custom operator names you can pass any of these
operator names into AutoMPO and it will know how to use these operators.

## Further Steps

  - [[Add QN conservation to a custom local Hilbert space|formulas/sitetype_qns]]
  - [[Extending an existing local Hilbert space|formulas/sitetype_extending]]
  - See how the built-in site types are defined inside the ITensor library:
    * [S=1/2 sites](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/site_types/spinhalf.jl)
    * [S=1 sites](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/site_types/spinone.jl)
    * [Fermion sites](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/site_types/fermion.jl)
    * [Electron sites](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/site_types/electron.jl)
    * [tJ sites](https://github.com/ITensor/ITensors.jl/blob/master/src/physics/site_types/tj.jl)

