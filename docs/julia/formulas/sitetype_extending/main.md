# Extending an Existing Local Hilbert Space

In a [[previous code formula|formulas/sitetype_basic]] we discussed the basics
of how custom local Hilbert spaces a.k.a. site types can be defined from 
scratch in ITensor. However, there are cases where a custom site type is 
already designed for you, such as the site types `"S=1/2"`, `"S=1"`,
`"Fermion"`, `"Electron"` and others included with ITensor.

A nice feature of the ITensor `SiteType` system is that you can arbitrarily
extend operator and other definitions, even of existing `SiteTypes` created
in other code or by someone else.

## Extending op Function Definitions

Perhaps the most common part of the `SiteType` system one wishes to extend
are the various `op` or `op!` function overloads which allow code like

    s = siteind("S=1/2")
    Sz = op("Sz",s)

to automatically create the @@S^z@@ operator for an Index `s` based on the 
`"S=1/2"` tag it carries. A major reason to define such `op` overloads
is to allow the AutoMPO system to recognize various operator names, as
discussed more below.

Let's see how to introduce a new operator name into the ITensor `SiteType`
system for this existing site type of `"S=1/2"`. The operator we will
introduce is the projector onto the up spin state @@P\_\uparrow@@ which
we will denote with the string `"Pup"`. 

As a matrix acting on the space @@\{ |\!\uparrow\rangle, |\!\downarrow\rangle \}@@,
the @@P\_\uparrow@@ operator is given by

\begin{align}

P_\uparrow &= 
\begin{bmatrix}
 1 &  0 \\
 0  & 0 \\
\end{bmatrix}

\end{align}

To add this operator to the ITensor `op` system, we just need to introduce the following
code

    using ITensors

    function ITensors.op!(Op::ITensor,
                          ::OpName"Pup",
                          ::SiteType"S=1/2"
                          s::Index)
      Op[s'=>1,s=>1] = 1.0
    end

Note that we have to name the function `ITensors.op!` and not just `op!` so that it overloads
other functions of the name `op!` inside the ITensors module. 

Having defined the above code, we can now do things like

    s = siteind("S=1/2")
    Pup = op("Pup",s)

to obtain the `"Pup"` operator for our `"S=1/2"` Index `s`. Or we can do a similar
thing for an array of site indices:

    N = 40
    s = siteinds("S=1/2",N)
    Pup1 = op("Pup",s[1])
    Pup3 = op("Pup",s[3])

A key use of these `op` system extensions is allowing additional operator names to
be recognized by the AutoMPO system for constructing matrix product operator (MPO)
tensor networks. With the code above defining the `"Pup"` operator, we are now 
allowed to use this operator name in any AutoMPO code involving `"S=1/2"` site 
indices.


