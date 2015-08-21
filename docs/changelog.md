# Change Log #

<a name="v1.2.0"></a>
## [Version 1.2.0](https://github.com/ITensor/library/tree/v1.2.0) (Aug 13, 2015) ##

IndexType now a class instead of an enum; this makes IndexType's user extensible, see commit github:a92c17a

  <div class="example_clicker">Show Example</div>

    auto MyType = IndexType("MyType");
    auto i = Index("i",10,MyType);
    auto j = Index("j",10,Link);

    auto T = ITensor(i,j);

    Print(prime(T,MyType)); //only i will be primed

Makefiles now hide most compiler output for a nicer installation experience

<b>Bug fixes:</b>

- AutoMPO now works correctly independently of order of operators passed
- Updates to CMakeLists.txt files for cmake users (thanks Andrey Antipov)
- Added MSVC version of mkdtemp for Windows users (thanks Kyungmin Lee)
- Fixed bug in hams/TriHeisenberg.h (thanks Hitesh Changlani)

<a name="v1.1.1"></a>
## [Version 1.1.1](https://github.com/ITensor/library/tree/v1.1.1) (May 18, 2015) ##

<b>Bug fixes:</b>

- Fixed a compilation error due to a typo in lapack_wrap.h (thanks user lukyluket)
- Fixed a compilation error due to missing include in error.h
- Removed use of non-standard variable sized array in utility.cc (thanks user kyungminlee)

<a name="v1.1.0"></a>
## [Version 1.1.0](https://github.com/ITensor/library/tree/v1.1.0) (May 16, 2015) ##


<b>Major design changes:</b>
- Requires C++11. No more boost dependence.
- Removed uniqueReal system from Index due to occasional comparison failures. Now Index comparisons are exact integer comparisons.
- Changed ITensor storage from ref-counted Vector to just std::vector
- Major redesign of IQTensor storage to store ITensor blocks in an ordered array

<b>Major new features:</b>
- AutoMPO: helper class for constructing MPOs with a pencil-and-paper type interface

<b>Bug fixes:</b>
- Fixed invalid memory access in matrix/storelink.h (contributed by Steve White)
- New version of lapack_wrap.h. Previous version had been mistakenly using C99 variable-sized arrays which are not standard C++ (thanks Kyungmin Lee)
- Fixed improper handling of negative scale factors in svd algorithm (thanks to Hitesh Changlani and Bryan Clark)
- Fixes to MatrixRef: moved unsafe iterators from VectorRef to Vector and updated usage of these in ITensor
- Fixed bug in Args::add where const char* was converting to bool
- Removed incorrect usage of delete in Index::read. Replaced with std::unique_ptr.
- Fixed bug in psiHKphi where conj should be replaced by dag (thanks to Ori Alberton).

<b>Other improvements:</b>
- Index no longer uses ref-counted heap storage. Data is directly stored in Index object.
- Improvements to input.h utility library for reading input files
- Added explicit bool conversions to many objects to check if default constructed or not
- Reimplemented ITensor contraction using lightweight SimpleMatrixRef wrapper
- Renamed Opt and OptSet to Args and folded Opt class into private class Args::Val to simplify interface

<a name="v1.0.5"></a>
## [Version 1.0.5](https://github.com/ITensor/library/tree/v1.0.5) (Oct 7, 2014) ##

<b>Bug fixes:</b>

- Fixed incorrect use of `delete` (should have been `delete[]`) in `Index::read`.

<a name="v1.0.4"></a>
## [Version 1.0.4](https://github.com/ITensor/library/tree/v1.0.4) (Oct 2, 2014) ##

<b>Bug fixes:</b>

- Fixed off-by-one memory bug in `MatrixRef::Last()` function.

- Fixed bug where if ITensor scale was negative, ordering of eigenvalues in svd methods could get reversed.

- Fixed bug where ITensor scale not included in eigenvalues returned from diag_hermitian.


<a name="v1.0.0"></a>
## [Version 1.0.0](https://github.com/ITensor/library/tree/v1.0.0) (May 28, 2014) ##

<span style="color:red;">Warning:</span> this version contains many breaking changes.

<b>Major breaking changes:</b>

- Put all code into `namespace itensor`. In your code, put `using namespace itensor;` at the top
  or explicitly qualify types with the itensor:: prefix. (Or wrap header code in `namespace itensor {...};`.)

- Removed ITSparse and IQTSparse classes. Now ITensor class carries an internal flag specifying whether it is
  diagonal (type()==ITensor::Diag) or dense (type()==ITensor::Dense). Diagonal ITensors are created by using
  certain constructors such as the constructor taking a Vector of components.

- Changed name of Hermitian conjugate method `conj` to `dag` (for "dagger"). Added `conj` methods for ITensor and IQTensor
  which take complex conjugate only, without reversing any index arrows.

- Removed minm,maxm,cutoff parameters from MPS. Instead these are passed to various methods which work with MPS
  using the OptSet named argument system.

- MPS class no longer stores a vector of Spectrum objects.

- Addition + operator and += operator no longer defined for MPS/MPO. Instead use the `sum` and `plusEq` functions.

- Spectrum class no longer used to pass accuracy parameters to `svd` and related methods. Instead use the OptSet system.

- Renamed "model" folder to "sites". Renamed `Model` class to `SiteSet`.

- New design for HamBuilder class. Now models an MPO initialized to the identity after which one can modify any 
  number of site operators using the `set` method. Supports multiplication by Real scalars as well. 
  After one sets all desired site operators, a HamBuilder instance can be automatically converted to an MPO or IQMPO.

  <div class="example_clicker">Show Example</div>

        SpinHalf model(100);

        vector<MPO> terms;

        //Can set operators using "set" method
        HamBuilder pm23(model);
        pm23.set("Sp",2,"Sm",3);
        pm23 *= 0.5;
        terms.push_back(pm23);

        //Or using constructor
        terms.push_back(0.5*HamBuilder(model,"Sp",2,"Sm",3));

- Replaced automatic MPO to IQMPO conversion with a named method toIQMPO().

- Made certain MPS/MPO methods external (linkInd, applyGate, averageM, checkOrtho, etc).

<b>Major new features:</b>

- Removed all dependence on boost C++ library when compiling with USE_CPP11=yes in options.mk.

- Included `boost_minimal` folder so that downloading boost is not required when using C++98 (USE_CPP11=no).

- Can now construct OptSet objects from a string such as 

   `"UseSVD=false,Cutoff=1E-8,IndexName=newind"`.

  Writing only the name of an 
  Opt such as "Quiet" is equivalent to "Quiet=true". Can also combine Opts and strings with '&' operator, for example:

  `Opt("Cutoff",1E-8) & Opt("Quiet") & "UseSVD=false,IndexName=newind"`.

- If ITensor is compiled with USE_CPP11, can initialize OptSet arguments using a bracketed list of Opt names and values.

  `some_function(arg1,arg2,{"UseSVD",false,"Cutoff",1E-8});`

  where some_function is a function accepting an OptSet as its last argument.

- Improved printing methods based on the Tinyformat library. Defined print, println, printf, and printfln. These are
  type safe methods with an interface similar to the std C library printf function. The printf methods take a formatting
  string as their first argument. The functions ending in "ln" print a newline at the end.

- Added improved idmrg functions.

- MPS/MPO A(int) and Anc(int) accessors now take negative arguments. For i < 0, A(i) = A(N-i+1).
  For example, use psi.A(-1) to access last site tensor of an MPS psi.

<b>Other major changes:</b>

- Deprecated the functions `primed` and `deprimed` in favor of just `prime` and `noprime` for consistency with Index and
  ITensor class interface.

- Opt names limited to 20 characters for efficiency (this limit can be modified by editing `utilities/options.h` and recompiling).

- Unit test library now based on [Catch](https://github.com/philsquared/Catch) unit test framework.

- Removed sandbox folder.

- Added idmrg sample code.

<b>Other breaking changes:</b>

- Removed deprecated Model named virtual function interface.

- Removed deprecated InitState class method pointer interface.

- Simplified InputFile, InputGroup interface.

- Removed IQTensor::iten_size() method. For an IQTensor T, just use T.blocks().size() instead.

- Renamed IQTensor::iten_empty() to just IQTensor::empty().

- Changed behavior of commonIndex when no common index found: used to throw an exception, now returns a default-constructed ("Null")
  index.

<a name="v0.2.4"></a>
## [Version 0.2.4](https://github.com/ITensor/library/tree/v0.2.4) (April 24, 2014) ##

- Updated license to v1.1, adding suggested wording for citing ITensor and clarifying when it should be cited.

<b>New features:</b>

- More convenient interface to InputGroup class defined in utilities/input.h. Returns parameters instead of pass-by-reference, allowing
  single-line syntax. Also allows specifying default arguments; parameters without defaults are mandatory. github:58dfc538

- Can store edge tensors in MPS or MPO classes by assigning to Anc(0) or Anc(N+1). Useful for infinite DMRG, for example.

<b>Bug fixes and maintenance:</b>

- Fixed some cases where local includes were using angle brackets <...> instead of quotes "..."

- Removed .ih files from MatrixRef library. Non-standard extension was causing issues with certain compiler.

- Fixed some friend declarations that were declaring default arguments (causing breakage under cerain compilers).

- Removed deprecated 'register' keyword from MatrixRef code.

- Fixed a typo: S+ and S- were swapped in the SpinHalf class

- Added missing inline declaration to BondGate<IQTensor>::makeSwapGate.


<a name="v0.2.3"></a>
## [Version 0.2.3](https://github.com/ITensor/library/tree/v0.2.3) (January 21, 2014) ##

<b>New features:</b>

- Model class "op" method now allows operator strings of the form "Op1*Op2" where "Op1" and "Op2" are
  valid operators. The method returns the on-site product of these two operators, similar to calling multSiteOps.

- Can now combine two OptSets using the & operator.

<b>Bug fixes and maintenance:</b>

- Updated tutorial codes to compile with latest library.

- Fixed some namespace/naming conflicts with boost and the std lib (especially involving std::array).

- Updated sample and sandbox codes to use newer interface conventions.

- Fixed BondGate swap operator for the IQTensor case.

- Cleanup of unit tests.

- Added acml lapack wrapper for zgeev.


<a name="v0.2.2"></a>
## [Version 0.2.2](https://github.com/ITensor/library/tree/v0.2.2) (November 11, 2013) ##

- Changed gateTEvol function to be templated over the gate container type.

- Added typedefs Gate and IQGate for BondGate<ITensor> and BondGate<IQTensor>, respectively.

<a name="v0.2.1"></a>
## [Version 0.2.1](https://github.com/ITensor/library/tree/v0.2.1) (November 6, 2013) ##

<b>New features:</b>

- ITensor::randomize and IQTensor::randomize can now generate a random complex tensor if passed the "Complex" Opt.

<b>Internal improvements:</b>

- New simplified implementation of Condenser.


<b>Bug fixes:</b>

- Fixed possible compiler errors when using C++11 standard libraries.

- Fixed error where svd (ITensor case) could sometimes return incorrect singular values (by not including scale factor).

- MPSt::applygate now correctly passes opts to svdBond.

<a name="v0.2.0"></a>
## [Version 0.2.0](https://github.com/ITensor/library/tree/v0.2.0) (October 22, 2013) ##

<b>Interface improvements:</b>

- Model classes now use strings for retrieving operators and site states (the latter are objects of type IQIndexVal).
  The older model class interfaces (e.g. model.sz(5) for a SpinHalf or SpinOne model) are still supported but the new style is preferred&mdash;see 
  the example below.

  <div class="example_clicker">Show Example</div>

        int N = 100;
        SpinHalf model(N);

        //Retrieving site indices
        model(5); //returns an IQIndex
        model.si(5); //this form still works too
        model.siP(5); //primed version of same index
        
        //Retrieving site operators
        model.op("Sz",3);
        model.op("Sp",10);
        model.op("Id",11); //identity operator
        model.op("Sp*Sz",11); //on-site product of two operators
                              //any string of the form A*B works
                              //if A and B are defined operator names

        //Retrieving a site state (of type IQIndexVal)
        model(5,"Up");
        model(5,"Dn");


- InitState class for initializing MPS now uses strings too. Related MPS/IQMPS constructor no
  longer requires redundant Model argument.

  <div class="example_clicker">Show Example</div>

        int N = 100;
        SpinHalf model(N);

        //Initialize an IQMPS to a Neel state
        InitState initState(model);
        for(int i = 1; i <= N; ++i)
            {
            initState.set(i,(i%2==1 ? "Up" : "Dn"));
            }

        IQMPS psi(initState);

<b>Internal improvements:</b>

- IQTensor storage (class IQTDat) no longer holds a separate map of iterators to the ITensor blocks. Instead blocks are
  stored in a std::vector and found using linear search. 
  * Much simpler IQTensor code.
  * No measured loss in speed.
  * Allows removing `mutable` modifier from IQTDat storage.
  * Now possible to set separate tolerance for Index uniqueReals and the ApproxReal class.

<b>Bug fixes:</b>

- Fixed major bug (#45) where ITensor addition was incorrect when adding certain complex ITensors.

- Fixed major bug (#46) where tieIndices was failing for complex tensors.

- Fixed lapack_wrap.h to compile with ACML library.

- Fixed Combiner to automatically init when copied to avoid confusing situations where copies could have a different right() Index.

- Fixed bug in IndexSet constructor when 8 indices provided.

- Updated sample codes.

- Fixed MPO constructor taking a Model class and ifstream to read from disk.



<a name="v0.1.1"></a>
## [Version 0.1.1](https://github.com/ITensor/library/tree/v0.1.1) (August 17, 2013) ##

<b>Major bug fixes:</b>

- IQCombiner now auto-initializes (constructs its "right" IQIndex) when copied. For an IQCombiner "c", this prevents, for example, 
  situations where conj(c) and c could have completely different right IQIndices.

- The error/Error functions now abort instead of throwing an ITError exception. To throw an ITError just use `throw ITError("Message");`
  explicitly.

- Fixed incorrect/buggy constructor for Spectrum objects where an explicit cutoff, maxm, etc. specified.

- Fixed an overflow bug in the ExpM helper class for sweeps where doing a large number of sweeps could cause the maxm to become negative.

<b>Internal improvements:</b>

- Major work on imagTEvol method. More stable to larger time steps and a wider variety of starting states.

<a name="v0.1.0"></a>
## [Version 0.1.0](https://github.com/ITensor/library/tree/v0.1.0) (July 16, 2013) ##

- First numbered version.

- Recently improved handling of complex ITensors and IQTensors. 
ITensors store an (initially null) pointer to their
imaginary part. The imaginary part is allocated only if it is non-zero.

</br>

<!--## [Development Version](https://github.com/ITensor/library/tree/develop) (in progress) ##-->
