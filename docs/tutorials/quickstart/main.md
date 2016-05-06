<span class='article_title'>ITensor Quickstart Guide</span>

<span class='article_sig'>Thomas E. Baker&mdash; May 4, 2016</span>

This article provides code for a quick introduction to the fundamentals of ITensor. For a quickstart guide oriented towards performing a DMRG calculation, go [[here|tutorials/DMRGquickstart]].

The following sample program generates a code to establish several indices, `ITensors` and `IQTensors` as well as setting manipulating values of tensors.

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
    //These files contain functions we use below.  They are found through 
    //the Makefile.  Include "all.h" is a catch-all for every header file
    //that you might need.  This reduces compile time slightly.  Speed this up
    //by only including the header files you actually need (example: "/itensor/mps/dmrg.h").
    #include "all.h"

    using namespace itensor;// this tells ITensor specific functions where to be found, use everywhere

Now we declare the main program and define some indices (SHOW A DIAGRAM).

    int main()//master object in program--must be called main
    {
    //        +----------------+
    //>-------|  (2) Indicies  |-------<
    //        +----------------+
    //

    Index s1,s2,s3,s4,s4,s5;//initializes five indices
    ITensor T(s1),U(s1,s2),V(s3,s4,s5);

    IQIndex q1,q2,q3,q4,q5;//initializes five indices with the appropriate quantum numbers

STOPPED HERE...DEFINE IQTENSORS AND MANIPULATE THEM

Now we declare the `SiteSet` that is used in the MPS, MPO, and many other places.
    
    //        +------------------------+
    //>-------|       (3) SiteSet      |-------<
    //        +------------------------+
    //The SiteSet will tell the MPS and MPO classes what system and what 
    //indices are available.  ITensor comes with three premade SiteSets:  
    //SpinHalf, SpinOne, and Hubbard.  Making a custom system is discussed below.

    SpinHalf sites(N);//note that changing to a spin-1 model replaces 
                      //SpinHalf with SpinOne

Next we define the [[MPO|tutorials/MPO]].

    //        +------------------------+
    //>-------|       (4)  [[MPO|tutorials/MPO]]         |-------<
    //        +------------------------+
    //ITensor uses an automatic MPO generator from a simple string
    //This covers most cases you might want to use, but making your own
    //MPO is also a snap; see below!

    AutoMPO ampo(sites);
    for (int j = 1; j<=N-1;j++)
      {//makes a Heisenberg model
        ampo += -J/2,"S+",j,"S-",j+1;
        ampo += -J/2,"S-",j,"S+",j+1;
        ampo += -J,"Sz",j,"Sz",j+1;
      }
    auto H = MPO(ampo);

Then the MPS:

    //        +------------------------+
    //>-------|       (5)  [[MPS|tutorials/MPS]]         |-------<
    //        +------------------------+
    //Initializing an MPS will generate a random state.  
    //Making an initial state with some property is also included in the library.

    MPS psi(sites);

Now we load into the `Sweeps` class all the parameters we'd like to use in our computation.

    //        +----------------------------+
    //>-------| (6) Solve/Use a function   |-------<
    //        +----------------------------+
    //Specify parameters and perform an operation on your system.

    Sweeps sweeps(20);
    sweeps.maxm() = 10, 20, 40, 80, 100;//how many many body states to keep
                                        //the last entry is repeated

    dmrg(psi,H,sweeps,"Quiet");//run DMRG

The output from the `dmrg` function can be printed, sorted, put into another algorithm or whatever else is needed.

    //        +--------------------+
    //>-------|     (7) Output     |-------<
    //        +--------------------+
    //Read off the energy, calculate a correlation function, print out 
    //the wavefunction, etc.  It all goes here!

    printfln("Energy = %.20f",psiHphi(psi,H,psi));

    return 0;//return value for C++ program

    }



  <div class="example_clicker">Show Full Code!</div>

    #include "all.h"

    using namespace itensor;// this tells ITensor specific functions where to be found, use everywhere

    int main(int argc, char* argv[])//master object in program--must be called main
    {

    if(argc != 2)
      {//reminds us to give an input file if we don't
      cout << "Usage: " << argv[0] << " inputfile." <<endl;
      return 0;
      }
    string infilename(argv[1]);
    InputFile infile(infilename);
    InputGroup basic(infile,"basic");

    const int N = basic.getReal("N",20);//number of sites
    Real J = basic.getReal("J",1);

    SpinHalf sites(N);//note that changing to a spin-1 model replaces 
                      //SpinHalf with SpinOne

    AutoMPO ampo(sites);
    for (int j = 1; j<=N-1;j++)
      {//makes a Heisenberg model
        ampo += -J/2,"S+",j,"S-",j+1;
        ampo += -J/2,"S-",j,"S+",j+1;
        ampo += -J,"Sz",j,"Sz",j+1;
      }
    auto H = MPO(ampo);

    MPS psi(sites);

    Sweeps sweeps(20);
    sweeps.maxm() = 10, 20, 40, 80, 100;//how many many body states to keep
                                        //the last entry is repeated

    dmrg(psi,H,sweeps,"Quiet");//run DMRG

    printfln("Energy = %.20f",psiHphi(psi,H,psi));

    }


