<span class='article_title'>ITensor Quickstart Guide</span>

<span class='article_sig'>Thomas E. Baker&mdash;November 3, 2015</span>

Using ITensor as a software package for DMRG or another tensor network method is simple and quick to get started.  Using the code in this article will get you going immediately.

The [[Tutorials|tutorials]] covers common methods and basics of tensor networks.  Here, we're going to go step by step through a sample code and discuss how you can modify it to what you need.  Here's an example of some real, starter ITensor code for a spin-1/2 chain.  The code is rewritten with banners below.  We'll cover all seven of those elements in the next chapters, in order, with general advice for any system you want to study.

This program calculates the ground state energy of a spin-1/2 chain.  Putting this in a file called `hellodmrg.cc` and using a [[makefile|ITensorC++]] runs the code with the library.  We provide a full version in the dropdown menu below.

If this looks completely new to you or there's something you don't understand, check out our [[C++ guide for ITensor|articles/ITensorC++]].

We start by declaring some header files that contain `SiteSets` and AutoMPO.  We also declare the ITensor namespace.

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
    //These files contain functions we use below.  They are found through 
    //the Makefile
    #include "core.h"
    #include "sites/spinhalf.h"
    #include "autompo.h"

    using namespace itensor;// this tells ITensor specific functions where to be found, use everywhere

Now we declare the main program and `InputGroup` that holds the parameters we want for the file.

    int main(int argc, char* argv[])//master object in program--must be called main
    {
    //        +------------------------+
    //>-------|  (2) Input parameters  |-------<
    //        +------------------------+
    //This part of the fie allows you to only compile the program once 
    //and change parameters at runtime.  We can also put in parameters by hand
    //each time we need to change them...but that requires we recompile!

    if(argc != 2)
      {//reminds us to give an input file if we don't
      cout << "Usage: " << argv[0] << " inputfile." <<endl;
      return 0;
      }
    string infilename(argv[1]);
    InputFile infile(infilename);
    InputGroup basic(infile,"basic");//[[loads a file of parameters|tutorials/input]]

    const int N = basic.getReal("N",20);//number of sites
    Real J = basic.getReal("J",1);

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

    //        +------------------------+
    //>-------|    (1) Header Files    |-------<
    //        +------------------------+
    //These files contain functions we use below.  They are found through 
    //the Makefile
    #include "core.h"
    #include "sites/spinhalf.h"
    #include "autompo.h"

    using namespace itensor;// this tells ITensor specific functions where to be found, use everywhere

    int main(int argc, char* argv[])//master object in program--must be called main
    {
    //        +------------------------+
    //>-------|  (2) Input parameters  |-------<
    //        +------------------------+
    //This part of the fie allows you to only compile the program once 
    //and change parameters at runtime.  We can also put in parameters by hand
    //and compile each time we need to change them.

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
    
    //        +------------------------+
    //>-------|       (3) SiteSet      |-------<
    //        +------------------------+
    //The SiteSet will tell the MPS and MPO classes what system and what 
    //indices are available.  ITensor comes with three premade SiteSets:  
    //SpinHalf, SpinOne, and Hubbard.  Making a custom system is discussed below.

    SpinHalf sites(N);//note that changing to a spin-1 model replaces 
                      //SpinHalf with SpinOne

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

    //        +------------------------+
    //>-------|       (5)  [[MPS|tutorials/MPS]]         |-------<
    //        +------------------------+
    //Initializing an MPS will generate a random state.  
    //Making an initial state with some property is also included in the library.

    MPS psi(sites);

    //        +----------------------------+
    //>-------| (6) Solve/Use a function   |-------<
    //        +----------------------------+
    //Specify parameters and perform an operation on your system.

    Sweeps sweeps(20);
    sweeps.maxm() = 10, 20, 40, 80, 100;//how many many body states to keep
                                        //the last entry is repeated

    dmrg(psi,H,sweeps,"Quiet");//run DMRG

    //        +--------------------+
    //>-------|     (7) Output     |-------<
    //        +--------------------+
    //Read off the energy, calculate a correlation function, print out 
    //the wavefunction, etc.  It all goes here!

    printfln("Energy = %.20f",psiHphi(psi,H,psi));

    }


