# AutoMPO

AutoMPO is a very powerful system for translating sums
of local operators into an MPO (or IQMPO) tensor network.
The notation for AutoMPO input is designed to be as close
as possible to pencil-and-paper quantum mechanics notation.

The code for AutoMPO is located in the files "itensor/mps/autompo.h"
and "itensor/mps/autompo.cc".

# Synopsis


    //
    // Use AutoMPO to create the 
    // next-neighbor Heisenberg model
    //
    auto sites = SpinHalf(N); //make a chain of N spin 1/2's
    auto ampo = AutoMPO(sites);
    for(int j = 1; j < N; ++j)
        {
        ampo += 0.5,"S+",j,"S-",j+1;
        ampo += 0.5,"S-",j,"S+",j+1;
        ampo +=     "Sz",j,"Sz",j+1;
        }

	//Convert the AutoMPO object to an MPO
    auto H = MPO(ampo);

	//Or convert the AutoMPO object to a IQMPO
    auto qH = IQMPO(ampo);

	//....

    //
    // Create a model with further-range interactions
	// capturing a 2D lattice (with a 1D ordering of sites)
    //
    int Nx = 12, Ny = 6;
    auto ampo = AutoMPO(sites);
    auto lattice = squareLattice(Nx,Ny);
    for(auto b : lattice)
        {
        ampo += 0.5,"S+",b.s1,"S-",b.s2;
        ampo += 0.5,"S-",b.s1,"S+",b.s2;
        ampo +=     "Sz",b.s1,"Sz",b.s2;
        }
    auto H = IQMPO(ampo);

	//....

    //
    // Create the 1D Hubbard model
    //
    auto sites = Electron(N);
    auto ampo = AutoMPO(sites);
    for(int i = 1; i <= N; ++i)
        {
        ampo += U,"Nupdn",i;
        }
    for(int b = 1; b < N; ++b)
        {
        ampo += -t,"Cdagup",b,"Cup",b+1;
        ampo += -t,"Cdagup",b+1,"Cup",b;
        ampo += -t,"Cdagdn",b,"Cdn",b+1;
        ampo += -t,"Cdagdn",b+1,"Cdn",b;
        }
    auto H = IQMPO(ampo);

    //....

    //
    // Create a spin model with four-site terms
    //
    auto ampo = AutoMPO(sites);
    for(auto i : range1(N-4))
        {
        ampo += "Sz",i,"Sz",i+1,"Sz",i+2,"Sz",i+4;
        }
    for(auto i : range1(N-1))
        {
        ampo += 0.5,"S+",i,"S-",i+1;
        ampo += 0.5,"S-",i,"S+",i+1;
        }
    auto H = IQMPO(ampo);

## AutoMPO Interface

* `AutoMPO(SiteSet sites)`

  Construct an AutoMPO object.

* `AutoMPO += op`

  The += operator of an AutoMPO object adds a operator product into
  the sum of operators represented by the AutoMPO.

  Examples of valid input:
      
      ampo += "Sz",i;
      ampo += "Sz",i,"Sz",j;
      ampo += 0.2,"Sz",i,"Sz",j;
      ampo += 0.5,"S+",i,"S-",j;
      ampo += 0.5,"S+",i,"S-",j,"S+",k,"S-",l;

  The operator products on the right-hand side of the += operator
  begin with an optional real- or complex-valued coefficient, then
  continue with a comma separated list of string-integer pairs.
  The coefficient can be either a numeric literal or a variable
  of type Real (double) or Cplx (std::complex&lt;double&gt;).

  The string-integer pairs, such as `"Sz",i`, represent an operator
  @@S^z\_i@@.
  
  Which strings are acceptable as operator names are determined by
  the SiteSet used to construct the AutoMPO. All operator names must
  be valid input to the `.op` method of the SiteSet (which is used
  to construct local site operators as tensors).

* `.sites() -> SiteSet const&`

  Retrieve the SiteSet used to construct the AutoMPO.

## Converting an AutoMPO to an MPO or IQMPO

### 1. Automatic cast method:

  An AutoMPO object can be directly cast into either an MPO
  or an IQMPO, at which point the terms stored in the AutoMPO
  will be used to produce actual tensors used to define
  the resulting MPO or IQMPO.

  For example:

    auto ampo = AutoMPO(sites);
    ...
    auto H = MPO(ampo);
    auto qH = IQMPO(ampo);

### 2. toMPO function

  Calling the `toMPO` function lets you have greater
  control over how an AutoMPO is turned into an MPO (or IQMPO).
  You can pass various named arguments to control which backend
  is used to process the AutoMPO and to control the accuracy of
  this process.

  Examples:

    auto H = toMPO<ITensor>(ampo);
    auto qH = toMPO<IQTensor>(ampo);
    ...
    auto H = toMPO<ITensor>(ampo,{"Exact=",true});

  Named arguments recognized:

   * "Exact" &mdash; boolean (default: false). Set whether to use
     the 'exact' backend or the approximate backend. The approximate
     backend can handle operators acting
     on more than two sites, and compresses the resulting MPO by 
     doing a series of singular value decompositions (SVDs). 
     Normally these SVDs are very accurate but could become an 
     issue if an important term has an unusually small coefficient.
     The exact backend makes no approximations whatsoever, but is
     limited to at most two-site operators and can sometimes result
     in larger MPO bond dimensions than the approximate backend.

   * "Maxm" &mdash; integer (default: 5000). Set the maximum
     bond dimension of the resulting MPO when using the approximate
     backend. If Exact=true, this has no effect.

   * "Cutoff" &mdash; real. (default: 1E-13). Set the SVD truncation
     error cutoff used by the approximate backend. If Exact=true, this has
     no effect.


### 3. toExpH function
    
  The toExpH function converts an AutoMPO representing a sum of operators
  @@H@@ into an MPO (or IQMPO) which approximates the operator @@e^{-t H}@@
  for a small time step t, making an error of order @@t^2@@ _per time step_.
  The time step t can be real or complex.

  The method used to do this is based on the following article:
  <a href="http://journals.aps.org/prb/abstract/10.1103/PhysRevB.91.165112" target="_blank">Phys. Rev. B 91, 165112</a> (arxiv:1407.1832), and has the advantage that unlike
  naive approaches for exponentiating an MPO,
  the time-step error per site is independent of system size.

  Examples:

    auto ampo = AutoMPO(sites);
    ...
    Real tau = 0.1;
    //Real time evolution
    auto expH = toExpH<ITensor>(ampo,tau*Cplx_i);
    auto qexpH = toExpH<IQTensor>(ampo,tau*Cplx_i);
    ...
    //Imaginary time evolution
    auto expH = toExpH<ITensor>(ampo,tau);
    auto qexpH = toExpH<IQTensor>(ampo,tau);


<br/>
_This page current as of version 2.1.0_
