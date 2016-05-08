# Fermions and Jordan-Wigner String

<span class='article_sig'>Miles Stoudenmire&mdash;April 20, 2016</span>

Operators in ITensor are "bosonic". By this we mean that an ITensor or IQTensor which
represents an operator does not automatically "know" about fermion anticommutation rules.
Even if we put in minus signs to correctly define the action of a fermionic operator on a
single site of a lattice model, it will still lack the correct behavior in a 
system with multiple sites unless we enforce the right behavior. 

(Note that AutoMPO does automatically give the correct behavior&mdash;<a href="#autompo">more on this below</a>.)

So in ITensor (up to and including version 2.x) the way we deal with fermionic systems
is to actually work with bosonic operators plus non-local "string" operators, first
discussed by Jordan and Wigner. We always refer to these string operators using
the letter "F".

Let's first discuss Jordan-Wigner string in the context of spinless fermions, 
then turn to fermions with spin.

## Spinless Fermions

The local (single site) Hilbert space of a spinless fermions has two states
* vacuum state: @@|0\rangle@@
* occupied state: @@|1\rangle@@ 

### Basics of spinless creation and annihilation operators

The occupied state can be viewed as the result of acting on the vacuum state
with the creation operator @@c^\dagger@@, that is
$$
|1\rangle = c^\dagger\, |0\rangle
$$
The annihilation operator @@c@@ returns the system to the vacuum state
$$
|0\rangle = c\, |1\rangle
$$
You can view these equations as being the _definition_ of these operators.

In a many-body setting, a crucial fact is that creation and annihilation operators
acting on different sites anticommute
$$
c\_i c\_j = -c\_j c\_i
$$
$$
c^\dagger\_i c^\dagger\_j = -c^\dagger\_j c^\dagger\_i
$$
$$
c\_i c^\dagger\_j = -c^\dagger\_j c\_i + \delta\_{ij}
$$
(The @@\delta\_{ij}@@ in the last equation is important for a consistent definition of these
operators but will not much concern us here.)

### Spinless Jordan-Wigner transformation

The Jordan-Wigner transformation is a mathematical equivalence, or mapping, between
a Hilbert space of spinless fermions and a Hilbert space of "hard core" bosons.
(The term "hard core" bosons refers to the rule that these bosons cannot share the same site,
as if they had an infinitely repulsive short-range interaction.)
Under this mapping, the fermionic creation/annihilation operators map to non-local operators
in terms of the bosons. However, most of the non-local parts of these operators typically cancel.

Historically this mapping was introduced to solve a bosonic system by mapping it to a system
of non-interacting fermions. Here we are interested in the reverse: mapping fermions 
to bosons since it is simpler for computers to deal with bosons.

The Jordan-Wigner mapping is defined as follows:
\begin{align}
c\_j & = F\_1 F\_2 \cdots F\_{j-1} \,a\_j \\
c^\dagger\_j & = F\_1 F\_2 \cdots F\_{j-1} \, a^\dagger\_j
\end{align}
Here @@a\_j@@ and @@a^\dagger\_j@@ are the annihilation and creation operators for the bosons
(defined identically to the fermion creation/annihilation operators except @@a\_i@@ and @@a^\dagger\_j@@
commute when acting on different sites).
The operator @@F\_j@@ is defined as
$$
F\_j = (-1)^{n\_j} = 1-2 n\_j \ .
$$
In words, @@F\_j@@ is a diagonal operator which takes the value +1 if the site j is empty, and -1 if it is
occupied.
If it helps, you can think of the mappings above as being the definition of the operators @@a\_j@@ and
@@a^\dagger\_j@@.

As an exercise, let us use the above mapping to check that they are consistent with the fact
that fermionic operators anticommute. Assuming @@i < j @@, let us first compute
\begin{align}
c\_i c\_j  & = (F\_1 F\_2 \cdots F\_{i-1})\, a\_i \, (F\_1 F\_2 \cdots F\_{j-1})\, a\_j \\
           & = F\_1^2 F\_2^2 \cdots F\_{i-1}^2\, (a\_i F\_{i})\, F\_{i+1} \cdots F\_{j-1}\, a\_j \\
           & = -a\_i \, F\_{i+1} \cdots F\_{j-1}\, a\_j
\end{align}
In the above lines above we used three important facts:
* When acting on different sites, the "F" and "a" operators commute.
* The square of an @@F\_j@@ operator is just the identity: @@F\_j^2=1@@
* @@a\_i F\_{i} = -a\_i@@ since either site i is occupied and the F gives a -1 or else acting with @@a\_i@@ gives zero anyway

Now let us check that using the mapping on the reversed operators give a consistent result
\begin{align}
-c\_j c\_i  & = (F\_1 F\_2 \cdots F\_{j-1})\, a\_j \, (F\_1 F\_2 \cdots F\_{i-1})\, a\_i \\
& = - F\_1^2 F\_2^2 \cdots F\_{i-1}^2\, (F\_{i} a\_i)\, F\_{i+1} \cdots F\_{j-1}\, a\_j \\
& = - a\_i \, F\_{i+1} \cdots F\_{j-1}\, a\_j
\end{align}
This time the @@F\_i@@ operator ended up on the left of the @@a\_i@@ operator and @@F\_i a\_i = a\_i@@.
The takeaway is that we got the exact same operator in the bosonic language, so we see that the
mapping is consistent with the fact that the fermions anticommute @@c\_i c\_j = - c\_j c\_i@@ . 

### Some Useful Mappings for Spinless Fermions

With the Jordan-Wigner transformation in hand, we can apply it to common operators 
one encounters when mapping fermionic Hamiltonians to bosonic ones, or when
measuring correlation functions involving creation/annihilation operators:


1. Next-neighbor "hopping" part of a 1d fermionic Hamiltonian:
   $$
   (c^\dagger\_i c\_{i+1} + c^\dagger\_{i+1} c\_i) = (a^\dagger\_i a\_{i+1} + a^\dagger\_{i+1} a\_i)
   $$
   If we write the same operator, but this time keeping the operators in increasing site order, we find:
   \begin{align}
   (c^\dagger\_i c\_{i+1} - c\_{i} c^\dagger\_{i+1}) & = (a^\dagger\_i a\_{i+1} + a\_i a^\dagger\_{i+1}) \\
   & = (a^\dagger\_i a\_{i+1} + a^\dagger\_{i+1} a\_{i})
   \end{align}
   which is completely consistent with the other version above.

2. Further-neighbor "hopping" term, assuming @@i < j @@
   $$
   (c^\dagger\_i c\_j + c^\dagger\_j c\_i) = (a^\dagger\_i F\_{i+1} F\_{i+2} \cdots F\_{j-1} a\_{j} + a\_{i} F\_{i+1} F\_{i+2} \cdots F\_{j-1} a^\dagger\_j)
   $$
   In this case we see that the starting and ending operators and signs are all the same, but there is a "string" of F operators
   between the first and last sites.

3. Operator pairs used in correlation functions

   Here we assume that i < j.
   \begin{align}
   c^\dagger\_i c\_j & = \ \ a^\dagger\_i \  F\_{i+1} F\_{i+2} \cdots F\_{j-1}\  a\_{j} \\
   c\_i c^\dagger\_j & = -a\_{i} \  F\_{i+1} F\_{i+2} \cdots F\_{j-1}\  a^\dagger\_{j}
   \end{align}
   <span>&nbsp;</span>

4. Next-neighbor pairing, or superconducting "field" term
   $$
   (c^\dagger\_i c^\dagger\_{i+1} + c\_{i+1} c\_{i}) = (a^\dagger\_{i} a^\dagger\_{i+1} + a\_i a\_{i+1})
   $$

## Fermions with Spin

Fermions with spin have a local Hilbert space with four states
* vacuum state: @@|0\rangle@@
* up state: @@|\!\uparrow\rangle@@ 
* down state: @@|\!\downarrow\rangle@@ 
* doubly occupied state: @@|2\rangle@@ 

These states can be thought of as being "created" from the vacuum by the operators
@@c^\dagger\_{\uparrow}@@ and @@c^\dagger\_{\downarrow}@@. Importantly, 
the state @@|2\rangle@@ is defined to be
$$
|2\rangle = c^\dagger\_{\uparrow} c^\dagger\_{\downarrow} |0\rangle  \ .
$$
with the up operator coming before the down operator.
This implies that on the one hand @@c^\dagger\_{\uparrow} |\!\downarrow\rangle = |2\rangle@@
while on the other @@c^\dagger\_{\downarrow} |\!\uparrow\rangle = -|2\rangle@@.

### Spinful Jordan-Wigner Transformations

With the above definitions we can map spinful fermion operators to spinful boson operators as follows
\begin{align}
c\_{\uparrow j}   & = F\_1 F\_2 \cdots F\_{j-1} \ \ \  a\_{\uparrow j} \\
c\_{\downarrow j} & =  F\_1 F\_2 \cdots F\_{j-1} \, \big( F\_j\, a\_{\downarrow j} \big)
\end{align}
Note the extra @@F\_{j}@@ in the mapping for the down-spin operator. This operator
gives the extra minus sign needed when annihilating a down spin from the doubly occupied state.
Be careful with this extra @@F\_{j}@@ operator because while the "F" and "a" operators commute on
different sites they do not commute when sharing the same site.

### Some Useful Mappings for Spinful Fermions

With the spinful Jordan-Wigner mapping thus defined, we can use
it to transform common operators
one encounters when mapping fermionic Hamiltonians to bosonic ones, or when
measuring correlation functions involving creation/annihilation operators:

1. Next-neighbor "hopping" part of a 1d fermionic Hamiltonian:
   \begin{align}
   \sum\_\sigma (c^\dagger\_{\sigma,i} c\_{\sigma,i+1} + c^\dagger\_{\sigma,i+1} c\_{\sigma,i}) & = 
   \big[(a^\dagger\_{\uparrow,i} F\_i)\, a\_{\uparrow,i+1} + (F\_i a\_{\uparrow,i})\, a^\dagger\_{\uparrow,i+1}\big] \\
   & \ \mbox{} - \big[a^\dagger\_{\downarrow,i}\, (F\_{i+1} a\_{\uparrow,i+1}) + a\_{\downarrow,i}\, (a^\dagger\_{\uparrow,i+1} F\_{i+1}) \big]
   \end{align}
   Note the minus sign in front of the second term on the right-hand side.

2. Further-neighbor "hopping" term, assuming @@i < j @@
   \begin{align}
   \sum\_\sigma (c^\dagger\_{\sigma,i} c\_{\sigma,j} + c^\dagger\_{\sigma,j} c\_{\sigma,i}) & = 
   \big[(a^\dagger\_{\uparrow,i} F\_i)\,F\_{i+1} F\_{i+2} \cdots F\_{j-1}\,  a\_{\uparrow,j} + (F\_i a\_{\uparrow,i})\,F\_{i+1} F\_{i+2} \cdots F\_{j-1} \, a^\dagger\_{\uparrow,j}\big] \\
   & \ \mbox{} - \big[a^\dagger\_{\downarrow,i}\, F\_{i+1} F\_{i+2} \cdots F\_{j-1}\, (F\_{j} a\_{\uparrow,j}) + a\_{\downarrow,i}\,F\_{i+1} F\_{i+2} \cdots F\_{j-1}\, (a^\dagger\_{\uparrow,j} F\_{j}) \big]
   \end{align}

<a name="c_ops"></a>

### On the Aup, Adagup, etc. versus Cup, Cdagup, etc. Hubbard SiteSet Operators

The Hubbard site set in ITensor provides operators "Cup", "Cdagup", "Cdn", "Cdagdn"
as well as "Aup", "Adagup", "Adn", "Adagdn". The presence of the "C..." operators
can be confusing because while these are defined to correctly behave as fermionic
operators for a single site, they do not anti-commute on different sites. To
correctly define many-body fermionic Hamiltonians or other many-body fermionic
operators (such as a operator like @@c^\dagger\_i c\_j@@) it is still necessary
to account for fermion anticommutation using Jordan-Wigner "F" operators.

Here is a table of how the "Aup", "Adagup", etc. operators act on a single site:
\begin{align}
a\_{\uparrow} |\!\uparrow\rangle & = |0\rangle & a\_{\downarrow} |\!\downarrow\rangle & = |0\rangle \\
a\_{\uparrow} |\!\uparrow\downarrow\rangle & = |\!\downarrow\rangle & a\_{\downarrow} |\!\uparrow\downarrow\rangle & = |\!\uparrow\rangle \\
a^\dagger\_{\uparrow} |0\rangle & = |\!\uparrow\rangle & a^\dagger\_{\downarrow} |0\rangle & = |\!\downarrow\rangle \\
a^\dagger\_{\uparrow} |\!\downarrow\rangle & = |\!\uparrow\downarrow\rangle & a^\dagger\_{\downarrow} |\!\uparrow\rangle & = |\!\uparrow\downarrow\rangle
\end{align}

In contrast, here is how the "Cup", "Cdagup", etc. operators act _on a single site_:
\begin{align}
c\_{\uparrow} |\!\uparrow\rangle & = |0\rangle & c\_{\downarrow} |\!\downarrow\rangle & = |0\rangle \\
c\_{\uparrow} |\!\uparrow\downarrow\rangle & = |\!\downarrow\rangle & c\_{\downarrow} |\!\uparrow\downarrow\rangle & = -|\!\uparrow\rangle \\
c^\dagger\_{\uparrow} |0\rangle & = |\!\uparrow\rangle & c^\dagger\_{\downarrow} |0\rangle & = |\!\downarrow\rangle \\
c^\dagger\_{\uparrow} |\!\downarrow\rangle & = |\!\uparrow\downarrow\rangle & c^\dagger\_{\downarrow} |\!\uparrow\rangle & = -|\!\uparrow\downarrow\rangle
\end{align}
Note the minus signs associated with adding or removing a down fermion to/from the doubly-occupied state. These
minus signs occur because in our convention (and as discussed above) the up state is ordered before the down state 
within a single site.

Using the "Cup", "Cdn", etc. operators in ITensor is _optional_ when doing measurements properties of MPS or when making 
your own MPO "by hand" (i.e. not using AutoMPO). It is often clearer to use the "Aup", "Adn", etc.
operators because it makes it clear that one is working with hard-core bosons plus Jordan-Wigner string.

On the other hand, if you want to create a Hamiltonian for a fermionic system using AutoMPO, using the operator
names "Cup", "Cdn" etc. is not optional. This is because AutoMPO recognizes these special operator names and
uses internal rewriting rules to add Jordan-Wigner "F" string in between them. (See next section.)


<a name="autompo"></a>

## Fermions and AutoMPO

The one place where fermions and Jordan-Wigner string are handled automatically for you in the ITensor library
is in AutoMPO. AutoMPO recognizes operators whose names start with "C" as being fermionic, and uses
special internal rewriting rules to map them to non-local bosonic operators correctly before producing
the MPO tensors.

Even though AutoMPO will produce a correct MPO, if you use this MPO in DMRG, for example, to find a ground
state of a fermionic system, when measuring correlation functions such as @@\langle c^\dagger\_i c\_j \rangle@@
it is still required that you insert the necessary Jordan-Wigner string operators yourself.


