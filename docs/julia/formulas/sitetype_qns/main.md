# Make a Custom Local Hilbert Space with QNs

In a [[previous code formula|formulas/sitetype_basic]] we discussed the basic,
minimal code needed to define a custom local Hilbert space, using the example
of a @@S=3/2@@ spin Hilbert space. In those examples, the `space` function
defining the vector space of a @@S=3/2@@ spin only provides the dimension of 
the space. But the Hilbert space of a @@S=3/2@@ spin has additional structure, which
is that each of its four subspaces (each of dimension 1) can be labeled by 
a different @@S^z@@ quantum number.

In this code formula we will include this extra quantum information in the 
definition of the space of a @@S=3/2@@ spin.

## Code Preview

First let's see the minimal code needed to add the option for including
quantum numbers of our @@S=3/2@@ site type, then we will discuss what each part of
the code is doing.

    include:docs/VERSION/formulas/sitetype_qns/qn_spinthreehalf.jl

<img class="icon" src="docs/VERSION/install.png"/>&nbsp;<a href="docs/VERSION/formulas/site_type/minimal_spinthreehalf.jl">Download this example code</a>

Now let's look at each part of the code above.

### The space function

In the [[code formula for defining a basic site type|formulas/sitetype_basic]] we discussed 
that the function `space` tells the ITensor library the basic information about how
to construct an Index associated with a special Index tag, in this case the tag `"S=3/2"`.
As in that code formula, if the user does not request that quantum numbers be included
(the case `conserve_qns=false`) then all that the `space` function returns is the number
4, indicating that a `"S=3/2"` Index should be of dimension 4.

But if the `conserve_qns` keyword argument gets set to `true`, the `space` function we
defined above returns an array of `QN=>Int` pairs. (The notation `a=>b` in Julia constructs
a `Pair` object.) Each pair in the array denotes a subspace.
The `QN` part of each pair says what quantum number the subspace has, and the integer following
it indicates the dimension of the subspace.

After defining the `space` function this way, you can write code like:

    s = siteind("S=3/2"; conserve_qns=true)

to obtain a single `"S=3/2"` Index which carries quantum number information.
The `siteind` function built into ITensor relies on your custom `space` function
to ask how to construct a `"S=3/2"` Index but also includes some other Index tags
which are conventional for all site indices.

You can now also call code like:


    N = 100
    sites = siteinds("S=3/2",N; conserve_qns=true)

to obtain an array of N `"S=3/2"` indices which carry quantum numbers.

### The op Function in the Quantum Number Case

Note that the `op!` function overloads are exactly the same as for the
more basic case of defining an `"S=3/2"` Index type that does not carry
quantum numbers. There is no need to upgrade any of the `op!` functions
for the QN-conserving case. The reason is that all QN, block-sparse information
about an ITensor is deduced from the indices of the tensor, and setting elements
of such tensors does not require any other special code.

