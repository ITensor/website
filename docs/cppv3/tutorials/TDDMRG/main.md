<span class='article_title'>Time Dependent DMRG</span>

<span class='article_sig'>Benedikt Bruognolo and Thomas E. Baker&mdash;September 17, 2015</span>

Time evolution is useful in a variety of applications:  quench dynamics, nonequlibrium physics, spectral functions, finite-temperature.  In order to calculate the time evolution, we need to apply the time evolution operator to the [[MPS|tutorial/MPS]].

<p align="center"><img src="docs/tutorials/TDDMRG/TDDMRG1.png" alt="Operator Diagram" style="width: 400px;"/></p>

$$
=e^{-i\hat{H} t}| \psi\rangle
$$ 

We can also do a time evolution in imaginary time (@@\beta=-it@@) then we evolve in temperature as @@e^{-\beta \hat{H}}| \psi\rangle@@. We will cover finite temperature calculations [[in another article|tutorials/METTS]]. 


There exist lots of different formulation of implementing time-evolution in the MPS framework. In this article, we focus on two of the most powerful approaches - Trotter-based and more efficient MPO-based time evolution - and we describe how to use them properly with ITensor. Both formulations use a discretized time grid, with @@N@@ grid points, by splitting the total time @@t@@ in a number of discretized time steps @@\tau = t/N@@.

## Trotter-based time evolution

We don't have an explicit expression for the unitary operator like the diagram above, but we approximate using a dcomposition in smaller gates that is computationally advantageous and only incurs a small error.

The Trotter-based time evolution is particularly well suited for systems with short ranged interactions. Assuming a chain model with only nearest-neighbor interactions, @@\hat{H} = \sum\_i \hat{h}\_i@@ (for example, the Heisenberg chain @@\hat{H}=\sum\_iJ\mathbf{S}\_i\mathbf{S}\_{i+1}@@), the basic idea is to group the local bond operators into two groups, consisting of terms acting only on even or odd-numbered bonds, respectively. 

Now we apply the Suzuki-Trotter decomposition to first order  to separate @@e^{-i\hat{H} \tau}@@ for a small time step @@\tau@@ into a product of even and odd terms like this 

<p align="center"><img src="docs/tutorials/TDDMRG/trotter.png" alt="Operator Diagram" style="width: 400px;"/></p>

or formally,
$$
e^{-i\hat{H} \tau}=e^{-i\hat{h}\_{1}\tau}e^{-i\hat{h}\_{2}\tau}e^{-i\hat{h}\_{3}\tau}e^{-i\hat{h}\_{4}\tau}\ldots + \mathcal{O}(\tau^2)
$$

We don't get this decomposition completely for free.  The full decomposition is given by the Baker-Campbell-Hausdorff formula.  Higher order decompositions use more terms of this expansion. In the case we present above, and due to the non-commutivity of neighboring bond terms, @@[\hat{h}\_i,\hat{h}\_{i+1}]\neq0@@ a so-called Trotter error of order @@O(\tau^2)@@ is introduced. Fortunately, this error can be controlled very well by using a small enough time-step and/or a higher order decomposition.

How do we apply the Trotter decomposed time evolution operator @@e^{-i\hat{H} \tau}@@ to an MPS? Starting at the first site of the chain, we apply a local gate and truncate using an SVD. Then we move down the chain to the second site. One full sweep through the chain completes one time step and is repeated until the desired time @@t@@ is reached.

ITensor makes the implementation of a Trotter-based time evolution very simple. The only thing we need to do is to generate the nearest-neighbor bond operator and exponentiate them using predefined ITensor routines. To this end, we generate a list consisting of all gates which should be applied to the MPS. 

    // Generate time-evolution gates
    // List of gates for time-evolution:
    using GateList = std::list<BondGate<IQTensor>>;
    using GateT = BondGate<IQTensor>;
    GateList gates;
    for(j = 1; j <= L-1;j++)
    { 
    IQTensor hh = J*sites.op("Sz",j)*sites.op("Sz",j+1); //nearest-neighbor bond
    hh += 0.5*J*sites.op("S+",j)*sites.op("S-",j+1);
    hh += 0.5*J*sites.op("S-",j)*sites.op("S+",j+1);
    //generates exp (hh) and includes it into list of gates
    gates.push_back(GateT(sites,j,j+1,GateT::tImag,tau,hh));
    }

 Then all thats left is to apply the gates to the MPS with `gateTEvol`.
 
    //options for time evolution
    TEvolObserver obs;
    //imaginary time evolution for exp(-beta H /2) |psi>
    gateTEvol(gates,beta/2.,tau,psi,obs,opts);
           
The Trotter-based time evolution is particularly well-suited for system with short-ranged interaction   
In more complicated 1D system and in effective 1D representations of 2D clusters, more complicated interaction terms appear. There are a number of strategies to deal with such longer-ranged interactions, one explicitly constructing the longer-ranged interaction (see MPO based evolution), the other using so-called swap gates, reducing it to a nearest-neighbour interaction.   

  We will note that the [[Mini-course|course]] on Trotter evolution shows that evolving in temperature drives the wavefunction into the ground state.  This is generally less effective, requiring many time steps, than using DMRG or another method.
 
### Swap Gates

Pending.
   
## MPO-based evolution
Dealing with long-ranged terms using swap gates can not only become painful in terms of bookkeeping, it might also reduce the efficiency of carrying out the time evolution. Moreover, different types of interactions such as exponentially decaying terms cannot be captured nicely in terms of two-site gates. In these cases, we can resort to an alternative, MPO-based strategy to carry out the time evolution. This essentially boils down to approximating the evolution operator @@ e^{-i \hat{H} t}@@ by an MPO and applying the MPO to the MPS using `exactApplyMPO` or `fitApplyMPO` to carry out a  time step.  `exactApplyMPO` will apply the MPO exactly while `fitApplyMPO` will apply the MPO but truncate the bond dimension.  Truncation compresses the MPS but may decrease accuracy.  

<p align="center"><img src="docs/tutorials/TDDMRG/TDDMRG2.png" alt="MPO to MPS" style="width: 400px;"/></p>

How does does one find a good MPO approximation for the evolution operator? MPO-based time evolution can be carried out by an Euler step @@1 - i t \hat{H}@@; however, this is usually a bad idea, as it introduces an error per site which diverges with increasing system size. Recently, [1] introduced a more local and improved version of a Runge-Kutta stepper, which has very compact MPO representation. The error per site remains constant with increasing system size, which greatly improves over previous MPO-based evolution schemes.

So how this approximation scheme work? One starts from expressing the evolution operator of a Hamiltonian which can be decomposed in terms of a sum of terms @@\hat{H} = \sum_x \hat{H}_x@@ as a Taylor series

$$
e^{-i \hat{H} t}  =  1 - i t \sum\_x \hat{H}\_x  - \frac{1}{2} t^2 \sum\_{x,y} \hat{H}\_x \hat{H}\_y +  \frac{i}{6} t^3 \sum\_{x,y,z} \hat{H}\_x \hat{H}\_y \hat{H}\_z \ldots
$$

This full series obviously does not  have a simple MPO representation. However, one may define @@x<y@@ if the sites affected by @@\hat{H}\_x@@ are strictly to the left of those affected by @@H\_y@@. Keeping all non-overlapping terms in the sums, one obtains an approximation of the evolution operator of the form

$$
U\_{\rm I} (t)  =  1 - i t \sum\_x \hat{H}\_x  - t^2 \sum\_{x<y} \hat{H}\_x \hat{H}\_y +  it^3 \sum\_{x<y<z} \hat{H}\_x \hat{H}\_y \hat{H}\_z \ldots 
$$	

One may approximate @@e^{-i \hat{H} t}@@ by @@U_\mathrm{I}@@.

It turns out that  @@U\_{\rm I} (t) @@ has a exact MPO representation, with the remarkable property that the bond dimension of this MPO scales exactly as the bond dimension of the MPO representation of the Hamiltonian. One can even do better, and consider  a collection of terms @@\langle x,y,z\ldots \rangle@@ in which no two cross the same bond. Employing this strategy, the approximation of the evolution operator is given by 

$$
U\_{\rm II} (t)  =  1 - i t \sum\_x \hat{H}  - \frac{1}{2} t^2 \sum\_{\langle x,y \rangle} \hat{H}\_x \hat{H}\_y +  \frac{i}{6} t^3 \sum\_{\langle x,y,z \rangle} \hat{H}\_x \hat{H}\_y \hat{H}\_z \ldots 
$$

For typical interactions far fewer terms are dropped than in @@U\_{\rm I} (t) @@. Although no exact MPO representation is available for  @@U\_{\rm II} (t)@@, its MPO approximation still improves greatly over  @@U\_{\rm I} (t)@@ while using the same MPO bond dimension. 

Using ITensor, we don't have to worry about how to construct the MPO representation of  @@U\_{\rm I} (t)@@ or @@U\_{\rm II} (t)@@  explicitly. Starting from setting up the Hamiltonian via the `AutoMPO` feature, we can setup a first order MPO approximation of the evolution operator, @@U_\mathrm{II}@@(???), using `toExpH`,

    Real tau;//Complex for imaginary time evolution
    auto expH = toExpH<IQTensor>(ampo,tau);

    fitApplyMPO(1.0,psi,expH,psi,opts);//or exactApplyMPO

As in Trotter-based time evolution, one can construct approximations with errors at higher order @@\mathcal{O}(Lt^p)@@ in @@t@@, which allow one to use much larger time steps. The code example below shows how to construct a second order step (@@p=3@@).

    Complex taua(tau/2.,tau/2.),
    taub(tau/2.,-tau/2.);
    auto expHa = toExpH<IQTensor>(ampo,taua);
    auto expHb = toExpH<IQTensor>(ampo,taub);

    fitApplyMPO(1.0,psi,expHa,psi,opts);//or exactApplyMPO
    fitApplyMPO(1.0,psi,expHb,psi,opts);//or exactApplyMPO

   
## References

[1] - Zaletel, Mong, Karrasch, Moore, and Pollman, Phys. Rev. B 91, 165112 (2015) 
 
