<span class='article_title'>Introduction to AutoMPO</span>

<span class='article_sig'>Thomas E. Baker &amp; Miles Stoudenmire &mdash;Nov 9, 2017</span>

Instead of programming an [[matrix product operator (MPO)|tutorials/MPO]] by hand, 
which can be very technical, ITensor has a feature called AutoMPO which automatically generates MPOs
and IQMPOS (quantum number conserving MPOs) from human readable input.  

Here is a code snippet for making an MPO for the Heisenberg model Hamiltonian 
for a one-dimensional spin-half system with N=100 sites:

    int N = 100;
    auto siets = SpinHalf(N);
    auto ampo = AutoMPO(sites);
    for(int j = 1; j < N; j+= 1)
      {
      ampo += 0.5,"S+",j,"S-",j+1;
      ampo += 0.5,"S-",j,"S+",j+1;
      ampo +=     "Sz",j,"Sz",j+1;
      }
    auto H = toMPO(ampo);

After one obtains the MPO H, it can be used as input for a DMRG calculation, or 
for evaluating observables such as correlation functions, among many other examples.

Let's go through the code above line by line to see what AutoMPO is doing.

The AutoMPO `+=` operator accepts the input:

    [value],"[operator name]",[site]

for single-site operators, or

    [value],"[operator name]",[site],"[operator name]",[site]

for two-site operators, etc. Operators acting on an arbitrary number of
sites are allowed, such as four-site operators common in
quantum chemistry calculations.

The `"[operator name]"` string must be recognizable by the site set used to construct the AutoMPO.
For example, the `SpinHalf` site set recognizes operator names such as "Sz" and "S+", whereas the `Electron` site set recognizes operators such as "Cdagup" and "Ntot".  

The coefficient `[value]` can be real or complex. If the coefficient is omitted, it will be assumed to be 1.0.  Using the AutoMPO syntax above, the user only has to focus on adding the correct terms, and AutoMPO will handle the conversion of the operator names to tensors and the construction of the resulting MPO or IQMPO.

One advantage of AutoMPO is its generic treatment of operators, regardless of the underlying site set 
(or Hilbert space). Let's say we want to use the code above to create an MPO that is the Heisenberg Hamiltonian for a spin one chain. We only need to make one replacement: the line that reads `auto sites = SpinHalf(N);` can be changed to

    auto sites = SpinOne(N);

And the AutoMPO will use the definition of the spin operators appropriate to an @@S=1@@ spin.
You can even make a custom `SiteSet` and use that if needed.

Another key advantage of AutoMPO is that the operators in each term need not be spatially close together. This is useful for making Hamiltonian MPOs for doing DMRG calculations of two-dimensional systems.

