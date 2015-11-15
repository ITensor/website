<span class='article_title'>Priming Indices in ITensor</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 21, 2015</span>

ITensor uses an `Index` for each argument in an `ITensor`. This `Index` describes the local degrees of freedom on each site; it contains the 'physics' of each site.  For example, an index on an @@S_z@@ operator corresponds to the spin up and spin down quantum number degrees of freedom.

If the physics ever changes on that site (we give an example next), then we should use a different index.  But what about sites that retain the physics but whose lines we don't want to contract?  For example, consider the @@S_z@@ operator.  The two physical indices attached to the operator:

<p align="center"><img src="docs/tutorials/primes/Sz.png" alt="MPS" style="height: 150px;"/></p>

should definitely never contract.  We want them to connect with wavefunction indices.  The prime indices (in this case, the vertical line) are only used as a way to prevent contraction.

We will detail in this article how to use primes on indices and best practices.

## When not to use Primes

An example where we might want to give a new name to a site is during coarse graining.  If we go from a fine lattice to a coarser one, then we have a diagram that looks like the diagram on the left:

<p align="center"><img src="docs/tutorials/primes/primingpractice.png" alt="MPS" style="height: 250px;"/></p>

The physics of the `Index` is changing on the coarser level.  We're describing a new lattice site with a different [[MPO|tutorials/MPO]] at this next level, so we introduce a new `Index` `t1`.  We don't want to call this new site `s1'` even though we are still never going to contract `s1'` with `s1`. But in light of the new physics, we should just rename the `Index` (left) instead of priming the `Index` (right).

## Functions that Prime Indices

In the following, we use "ITensor" to refer to either ITensors or IQTensors.

 * `prime(ITensor)` - Updates prime level of an ITensor by one
 * `prime(ITensor,int)` - Updates the prime level of an ITensor by "int" (can also be negative)
 * `prime(ITensor,Type)` - Updates all indices of type Type on an ITensor

For example, `prime(psi,Site)` raises the prime level of all indices labeled as Site.  Indices can be given custom IndexTypes such as Link, Site, etc.

 * `prime(ITensor,Index,int)` - Changes the prime level of the specific index "Index" on an ITensor by value "int"
 * `prime(ITensor,Type,int)` - Increment the prime level of all indices having type "Type" by "int". 

ITensor does not currently allow negative prime levels.

 * `noprime(ITensor)` - sets prime level of an ITensor to zero

 * `mapPrime(ITensor, inta, intb)` - changes prime level on all indices of an ITensor having level inta to level intb.

## An Exercise in Priming

For educational purposes, this will not take the most direct path to the solution.  We will use all the functions listed above.

We begin by defining four tensors:

    auto x = Index("x0",2,Xtype),//declares x0 as type Xtype
         y = Index("y0",2,Ytype),//declares y0 as type Ytype
         x1 = prime(x,1),
         x2 = prime(x,2),
         y1 = prime(y,1),
         y2 = prime(y,2);
    ITensor S1(x1,prime(x0,2),y0);
    ITensor S2(y1,x0,y0);
    ITensor S3(x1,x0,prime(y0,2));
    ITensor S4(y1,prime(x0,2),prime(y0,2));

This pattern of tensors appears in a [[TRG|book/trg]] calculation and this represents the final operation before updating the tensor for the next renormalization group step. In order to get a better idea of what these tensors look like, we should draw a picture:

<p align="center"><img src="docs/tutorials/primes/trg_tensors.png" alt="MPS" style="height: 350px;"/></p>

Right now, that's not what we want.  If we contracted all the tensors (`S1*S2*S3*S4`), then we'd get a scalar.  We want the diagrams to contract just as they are drawn:  horizontal lines with horizontal lines, vertical lines with vertical lines.  We also want some extra double primes on some of the level 1 indices (`x1`, `y1`). The tensors come out of the program this way and are a necessity in the TRG algorithm.  We must manipulate the primes to get the correct contraction:

<p align="center"><img src="docs/tutorials/primes/trg_final.png" alt="MPS" style="height: 350px;"/></p>

For educational purposes, let's prime one index:

    prime(S1,y0);

<p align="center"><img src="docs/tutorials/primes/trg1.png" alt="MPS" style="height: 200px;"/></p>

and then unprime it

    prime(S1,y0,-1);

This returns us to the original diagram.

Now we get serious.  Let's remove all primes from `S4`:

    A *= noprime(S4);//or mapPrime(S4,2,0)

<p align="center"><img src="docs/tutorials/primes/trg2.png" alt="MPS" style="height: 200px;"/></p>

This is a promising step considering the contractions we eventually want.  We then contract with `S3`:

    A *= S3;

<p align="center"><img src="docs/tutorials/primes/trg3.png" alt="MPS" style="height: 200px;"/></p>

Now we prime twice the `Xtype` indices on the next contraction:

    A = prime(A,Xtype,2);

<p align="center"><img src="docs/tutorials/primes/trg4.png" alt="MPS" style="height: 200px;"/></p>

Let's prime `S2` twice and contract it with `A`

    A *= prime(S2,2);

<p align="center"><img src="docs/tutorials/primes/trg5.png" alt="MPS" style="height: 400px;"/></p>

The dotted line contracted on `*`.  The last step is to contract `S1` and this gives us the correct result.

    A *= S1;

A more straightforward code would be:

    auto l13 = commonIndex(S1,S3);//Obtains a common index from both S1 and S3
    A = S1 * noprime(S4) * prime(S2,2) * prime(S3,l13,2);

