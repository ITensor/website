# AutoMPO

AutoMPO is a very powerful system for translating sums
of local operators into an MPO (or IQMPO) tensor network.
The notation for AutoMPO input is designed to be as close
as possible to pencil-and-paper quantum mechanics notation.


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
    auto sites = Hubbard(N);
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

