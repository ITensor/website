<span class='article_title'>ITensor Quickstart Guide</span>

<span class='article_sig'>Thomas E. Baker&mdash; April 28, 2016</span>

This article provides an introduction to using DMRG in ITensor.  For a more general quickstart guide, go [[here|tutorials/quickstart]].

ITensor provides many features for tensor network computations.  This quickstart guide goes through some of the basic features.  A full explanation is contained in other articles.

Using ITensor as a software package for DMRG or another tensor network method is simple and quick to get started.  Using the code in this article will get you going immediately.

The [[Tutorials|tutorials]] covers common methods and basics of tensor networks.  Here, we're going to go step by step through a sample code and discuss how you can modify it to what you need.  Here's an example of some real, starter ITensor code for a spin-1/2 chain.  

    #include "itensor/all.h"

    using namespace itensor;

    int main(int argc, char* argv[])
    {

    if(argc != 2)
      {
      cout << "Usage: " << argv[0] << " inputfile." <<endl;
      return 0;
      }
    string infilename(argv[1]);
    InputFile infile(infilename);
    InputGroup basic(infile,"basic");

    const int N = basic.getReal("N",20);//number of sites
    Real J = basic.getReal("J",1);

    SpinHalf sites(N);
    AutoMPO ampo(sites);
    for (int j = 1; j<=N-1;j++)
      {
        ampo += -J/2,"S+",j,"S-",j+1;
        ampo += -J/2,"S-",j,"S+",j+1;
        ampo += -J,"Sz",j,"Sz",j+1;
      }
    auto H = MPO(ampo);

    MPS psi(sites);

    Sweeps sweeps(20);
    sweeps.maxm() = 10, 20, 40, 80, 100;

    dmrg(psi,H,sweeps,"Quiet");

    printfln("Energy = %.20f",psiHphi(psi,H,psi));

    }

The code is rewritten with banners below.  We'll cover all seven of those elements in the next chapters, in order, with general advice for any system you want to study.

This program calculates the ground state energy of a spin-1/2 chain.  Putting this in a file called `hellodmrg.cc` and using a [[makefile|ITensorC++]] runs the code with the library.  Some other simple examples are contained in the `/samples` folder in the ITensor library.

If this looks completely new to you or there's something you don't understand, check out our [[C++ guide for ITensor|articles/ITensorC++]].

We start by declaring some header files that contain `SiteSets` and AutoMPO.  We also declare the ITensor namespace. These files contain functions we use below.  They are found through the Makefile.  Include "all.h" is a catch-all for every header file that you might need.  This reduces compile time slightly.  Speed this up by only including the header files you actually need (example: "/itensor/mps/dmrg.h").
 

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
   #include "itensor/all.h"

    using namespace itensor;

Now we declare the main program and `InputGroup` that [[holds the parameters|tutorials/input]] we want for the file. This part of the fie allows you to only compile the program once and change parameters at runtime.  We can also put in parameters by hand each time we need to change them...but that requires we recompile!  And that is pesky.

    int main(int argc, char* argv[])//master object in program--must be called main
    {
    //        +------------------------+
    //>-------|  (2) Input parameters  |-------<
    //        +------------------------+
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

Now we declare the `SiteSet` that is used in the MPS, MPO, and many other places. The SiteSet will tell the MPS and MPO classes what system and what indices are available.  ITensor comes with three premade SiteSets:  SpinHalf, SpinOne, and Hubbard.  Making a custom system is discussed [[in another article|tutorials/customSiteSet]].
    
    //        +------------------------+
    //>-------|       (3) SiteSet      |-------<
    //        +------------------------+

    SpinHalf sites(N);//Can changes SpinHalf to SpinOne (etc.) for a different model

Next we define the [[MPO|tutorials/MPO]]. ITensor uses an automatic MPO generator from a simple string. This covers most cases you might want to use, but making your own MPO is also [[available|tutorials/customMPO]].

    //        +------------------------+
    //>-------|       (4)  MPO         |-------<
    //        +------------------------+

    AutoMPO ampo(sites);
    for (int j = 1; j<=N-1;j++)
      {//makes a Heisenberg model
        ampo += -J/2,"S+",j,"S-",j+1;
        ampo += -J/2,"S-",j,"S+",j+1;
        ampo += -J,"Sz",j,"Sz",j+1;
      }
    auto H = MPO(ampo);

Then the MPS. Initializing an MPS will generate a random state.  `IQMPS`s must be inititalized in a given quantum number sector with the `InitState` intializer.  Making an initial state with some property is also included in the library.

    //        +------------------------+
    //>-------|       (5)  MPS         |-------<
    //        +------------------------+

    MPS psi(sites);

Now we load into the `Sweeps` class all the parameters we'd like to use in our computation.

    //        +----------------------------+
    //>-------| (6) Solve/Use a function   |-------<
    //        +----------------------------+

    Sweeps sweeps(20);
    sweeps.maxm() = 10, 20, 40, 80, 100;//how many many body states to keep
                                        //the last entry is repeated
    sweeps.niter() = 2;//number of Krylov vectors in Davidson algorithm (best choice)
    sweeps.cutoff() = 1E-10;//maximum weight of singular values to be kept in SVD

    dmrg(psi,H,sweeps,"Quiet");//run DMRG

The output from the `dmrg` function can be printed, sorted, put into another algorithm or whatever else is needed.

    //        +--------------------+
    //>-------|     (7) Output     |-------<
    //        +--------------------+

    printfln("Energy = %.20f",psiHphi(psi,H,psi));

    return 0;//return value for C++ program

    }

