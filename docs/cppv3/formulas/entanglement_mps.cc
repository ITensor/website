//Run DMRG to get a ground state `psi`
auto N = 20;
auto sites = SpinHalf(N);
auto ampo = AutoMPO(sites);
for( auto j : range1(N-1) )
    {
    ampo += 0.5,"S+",j,"S-",j+1;
    ampo += 0.5,"S-",j,"S+",j+1;
    ampo +=     "Sz",j,"Sz",j+1;
    }
auto H = toMPO(ampo);
auto state = InitState(sites,"Up");
for( auto n : range1(N) ) if( n%2==0 ) state.set(n,"Dn");
auto sweeps = Sweeps(5); //number of sweeps is 5
sweeps.maxdim() = 10,20,100,100,200;
sweeps.cutoff() = 1E-10;
auto [energy,psi] = dmrg(H,randomMPS(state),sweeps,"Silent");

//Given an MPS called "psi",
//and some particular bond "b" (1 <= b < length(psi))
//across which we want to compute the von Neumann entanglement
auto b = 10;

//"Gauge" the MPS to site b
psi.position(b); 

//SVD this wavefunction to get the spectrum
//of density-matrix eigenvalues
auto l = leftLinkIndex(psi,b);
auto s = siteIndex(psi,b);
auto [U,S,V] = svd(psi(b),{l,s});

//Apply von Neumann formula
//to the squares of the singular values
Real SvN = 0.;
for(auto i : dim(u))
    {
    auto Sii = elt(S,u=i,v=i);
    auto p = Sii*Sii;
    if(p > 1E-12) SvN += -p*log(p);
    }
printfln("Across bond b=%d, SvN = %.10f",b,SvN);

