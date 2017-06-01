# Change Log #

<a name="v2.1.0"></a>
## [Version 2.1.0](https://github.com/ITensor/ITensor/tree/v2.1.0) (Jun 1, 2017) ##

* New default [[AutoMPO|classes/autompo]] backend that supports terms with operators acting on more than two sites. This backend also performs a series of SVDs to compress the resulting MPO to as small a bond dimension as possible, which can be extremely useful for MPOs representing long-range interactions, for example. (Thanks to Anna Keselman for a lot of hard work on this new system.)

* Changed Index (and IQIndex) internal ID numbers to be 64 bit. Fixes random crash bug during long tim evolution runs reported by multiple users. <span style="color:red;">Note:</span> this change is backwards incompatible with tensors or other objects such as MPS saved to disk in previous version of ITensor.

* New [[SiteSet|classes/siteset]] system. New design makes it easier to create SiteSets with a mixture of different local degrees of freedom (such as spin chains with alternating spin sizes). It is also now very cheap to copy a SiteSet as all copies point to the same underlying storage.

* New ScalarReal and ScalarCplx storage types. Leads to cleaner handling of scalar ITensors and IQTensors. (Thanks Chia-Min Chung for suggestions leading to this design.)

* Build system now optionally builds dynamic libraries. (Thanks Kyungmin Lee for contributing this.)

* New [[MPS::orthogonalize|classes/mps#orthogonalize]] algorithm. Orthogonalizes MPS in a single pass without using a more heuristic two-pass approach like the older routine did.

* Fixed a faulty optimization of IQTensor combiners for the case of combining a single IQIndex. (Thanks Chia-Min Chung for reporting this.)

* Changed logic for deducing the arrow direction of the IQIndex produced by a combiner when the combined indices have different arrow directions. (Thanks Lars-Hendrick Frahm for bringing this to my attention.)

* New SpinTwo SiteSet. (Thanks Samuel Gozel for contributing.)

* New parallel.h tools for sending tensors and other data via MPI. (Thanks Lars Frahm for improvements to this also.)

* More efficient implementation of gateTEvol template routine.


<a name="v2.0.11"></a>
## [Version 2.0.11](https://github.com/ITensor/ITensor/tree/v2.0.11) (Sep 8, 2016) ##

* Fixed poor convergence of idmrg, which was due to a poorly chosen value for a pseudo-inverse cutoff

* Fixed a declaration of an overload of the "overlap" functions

* Added "S+" and "S-" operator names to tJ SiteSet (thanks Mingru Yang for this suggestion)

* Merged pull #108 from user ybarlev, improving lattice generating functions

* Merged pull #107 from user kyungminlee, improving OpenBLAS compatibility

* Updated Davidson code to support multiple targeting

* Merge pull #106 from using mingpu, improving reading of Sweeps from a table in a file

* Fixed bug in printing of SiteSets

* Some improvements to tutorial codes

<a name="v2.0.10"></a>
## [Version 2.0.10](https://github.com/ITensor/ITensor/tree/v2.0.10) (Jun 19, 2016) ##

* Fixed bug where denmatDecomp and diagHermitian were passing wrong scale factor to showEigs method (did not affect results, only printing of density matrix eigenvalues)

* factor decomposition now returns a Spectrum object computing by the svd

* Added optional method to MPS/IQMPS: you can use Aref(int i) as an alternative to Anc(int i)

* Added -lpthread to suggested flags for PLATFORM=lapack in options.mk.sample

<a name="v2.0.9"></a>
## [Version 2.0.9](https://github.com/ITensor/ITensor/tree/v2.0.9) (Jun 8, 2016) ##

* Reorganized library code for big speedup of driver-code compile times.

* Restored computation of quantum numbers of entanglement spectrum. It is now only done if requested
  by passing the (boolean) named arg "ComputeQNs".

* Fixed bug where AutoMPO was not working for non-QN conserving operators (thanks Yifan Tian).

* Fixed bug where Truncate=false was getting set back to true if other truncation args (Cutoff, Maxm) were set
  (thanks Bill Huggins).

* Fixed autovector to allow types with non-constexpr default constructor.

* Changed averageM(MPS) to return a Real instead of an int.

* Broke up some big source files to aid compilation on Windows using cygwin.


<a name="v2.0.8"></a>
## [Version 2.0.8](https://github.com/ITensor/ITensor/tree/v2.0.8) (May 24, 2016) ##

* Fixed major bug in davidson algorithm where Gram-Schmidt was not being repeated after orthog failure.

* Improved behavior of Truncate argument to svd and diagHermitian. Now gets set to true automatically if a truncation parameter (such as Cutoff or Maxm) is set.

* Split tensor decomposition and MPS code into separate .cc files to help with linker limitations on Windows.

* Removed static vectors from lapack_wrap.cc to make calls to these wrappers thread safe.

* Fixed compilation errors and an off-by-one bug in stats.h

* Fixed issue with using exactApplyMPO with same input and output MPS

* Added sweepnext1 for single site sweeping algorithms

* nmultMPO now uses a small default cutoff if none is provided

<a name="v2.0.7"></a>
## [Version 2.0.7](https://github.com/ITensor/ITensor/tree/v2.0.7) (May 2, 2016) ##

* Product of IndexVal and scalar now works for complex scalars too

* Combined prime function taking Index objects and function taking IndexType arguments 
  into single function which can take combinations of both.

* Function findIQInd now returns default-constructed IQIndex if not found; previously would throw an exception.

* orderedC function now switches ITensor storage to complex if it was real instead of throwing an exception.


<a name="v2.0.6"></a>
## [Version 2.0.6](https://github.com/ITensor/ITensor/tree/v2.0.6) (Apr 27, 2016) ##

* Fixed some cases which failed to compile when using the .apply method on ITensor and IQTensor with diagonal storage.

* Fixed addition of Diag ITensors to work in all real or complex combinations.

* Added second argument to expHermitian function, which is necessary for including a complex factor in the exponential.

* Merged pull request #104 from Kyungmin Lee, which includes cstdlib header in error.h

<a name="v2.0.5"></a>
## [Version 2.0.5](https://github.com/ITensor/ITensor/tree/v2.0.5) (Apr 25, 2016) ##

* Added `expHermitian` function for exponentiating Hermitian tensors

* Added new `eigen` function for computing eigenvectors and eigenvalues of a general tensor

* Fixed `ordered` and `orderedC` to make sure ITensor is allocated

* Building library now updates timestamp of `all.h`, `all_basic.h`, and `all_mps.h` files

<a name="v2.0.4"></a>
## [Version 2.0.4](https://github.com/ITensor/ITensor/tree/v2.0.4) (Apr 18, 2016) ##

* Introduced convenience headers all.h, all_basic.h, and all_mps.h. Thanks for Siva Swaminathan for emphasizing the need for these.

* Merge pull requests by Kyungmin Lee which fix various issues when using ITensor on Windows.

* Updated tutorial/project_template/ code.

<a name="v2.0.3"></a>
## [Version 2.0.3](https://github.com/ITensor/ITensor/tree/v2.0.3) (Apr 11, 2016) ##

* Fixed LocalOp::diag method to correctly use new `delta` function to tie indices.
  Thanks to Xiongjie Yu for the bug report (bug #96).

* Merged pull request #94 (by Github user xich) which fixes incorrect definition of
  operator+ for IndexSetIter.

* Merged pull request #83 from Kyungmin Lee which fixes cputime.cc when using MSVC compiler.

* Changed how ITensor write-to-disk system works. Fixed some subtle compilation issues
  where write methods weren't being called. Now each storage type implements a 
      write(ostream& s, StorageType const& s) 
  free function.

* Better error messages when doTask overloads are not implemented.

* Passing a complex number with exactly zero imaginary part to `.set` no longer switches storage to complex.

* Fixed `.set` method when arguments include a mix of IndexVals and IQIndexVals.

* Merged pull request #93 from Mingru Yang which fixes out-of-date code in `tutorial/project_template` folder.

<a name="v2.0.2"></a>
## [Version 2.0.2](https://github.com/ITensor/ITensor/tree/v2.0.2) (Apr 2, 2016) ##

* Added the factor decomposition, which uses the SVD to factorize a tensor into just two factors by multiplying the square root of the singular values into the U and V matrices.

* Added helpful functions which return vectors of "bonds" for common two-dimensional lattices. These are extremely useful for making 2D Hamiltonians as MPOs using AutoMPO. See the [[code formula example|formulas/2d_dmrg]].

<a name="v2.0.1"></a>
## [Version 2.0.1](https://github.com/ITensor/ITensor/tree/v2.0.1) (Mar 30, 2016) ##

This version fixes a few bugs:

* Fixed issue where AutoMPO was failing when operators were not provided in order. Also fixes issue with fermions and periodic boundary conditions. Thanks to Jordan Venderley for reporting this.

* Fixed out-of-date interface of LocalMPO_MPS and LocalMPOSet which was preventing excited state DMRG code from compiling.

* Fixed some places where a divide-by-zero error could occur.

This version also includes a new mapprime function which takes an arbitrary number of arguments of the form Index,plevold,plevnew (meaning replace the Index with prime level plevold with prime level plevnew) or of the form IndexType,plevold,plevnew (same but for any Index of that IndexType).
For example, 

    auto T = ITensor(i,prime(j,2),k);
    T.mapprime(i,0,3,j,2,1);

Now T's index i will have prime level 3 and index j will have prime level 1.


<a name="v2.0.0"></a>
## [Version 2.0.0](https://github.com/ITensor/ITensor/tree/v2.0.0) (Mar 25, 2016) ##

<span style="color:red;">Warning:</span> this version contains many breaking changes;
see the [[version 2 transition guide|v2transition_guide]].

Version 2.0 of ITensor is a major update to the internals of the ITensor and IQTensor 
classes. Tensors now store their data in "storage objects" which can have arbitrary
data layouts. The code to manipulate tensor storage deals with the different storage
types through a dynamic multiple dispatch design, revolving around overloads
of the function doTask(TaskType,...) where TaskType is a "task object" saying
which task should be carried out (contraction, addition, mutiplication by a scalar, etc.).

Major changes:

* [[New storage system|articles/storage]] for tensors with "dynamic overloading" a.k.a. multiple dispatch
  for doTask functions carrying out operations on storage types.

* ITensor and IQTensor now share exactly the same interface (they are instantiations
  of the same template class). ITensors and IQTensors are distinguished by what
  type of indices they have (Index versus IQIndex) and what storage types they have.

* New "TensorRef" library for basic tensor operations, such as tensor slicing and 
  permutation. Matrix and vector operations are implemented as a special case of 
  tensor operations.

* Fixed "long run crash" bug that was plauging version 1.x. Most likely fixed
  by better memory safety of TensorRef library.

* No longer any limit on the number of indices ITensors can have.
  This makes ITensor even more useful for two-dimensional
  algorithms such as TRG, PEPS, MERA etc.

* New QN (quantum number) system. To create a quantum number using the
  standard recognized fields (spin "Sz", boson number "Nb", fermion number "Nf",
  or fermion parity "Pf") call the QN constructor as

      auto q = QN("Sz=",-1,"Nf=",1);

  More advanced QNs can be created by provided a list of value-modulus pairs.
  The modulus is an integer saying how addition is defined for that particular
  "slot" of the QN. For example, a QN constructed as `QN({a,1},{b,3})`
  will have the value "a", modulus 1 in slot one and value "b", modulus 3 in slot two. 
  When adding QNs of this type, the first slot will obey regular integer
  addition (@@Z_1@@ in an abuse of notation) while the second slot will obey
  @@Z_3@@ addition rules.

Other changes:

* The Combiner and IQCombiner types no longer exist. Instead, a combiner is
  just a special type of ITensor or IQTensor. To obtain a combiner which
  combines the indices i,j,k, call the function

      auto C = combiner(i,j,k);

  The tensor C will have a fourth index whose size is the product of the sizes
  of i,j, and k.

* It is now mandatory to prefix header file names with their path inside
  the ITensor folder. For example, 

      #include "itensor/iqtensor.h" 
      #include "itensor/mps/dmrg.h"

* User-created IndexTypes are now supported. Internally, an IndexType is now
  just a fixed-size string of up to 7 characters. To make an IndexType
  called "MyType" just do 

      auto MyType = IndexType("MyType");
      auto i = Index("i",5,MyType);





<a name="v1.3.0"></a>
## [Version 1.3.0](https://github.com/ITensor/ITensor/tree/v1.3.0) (Oct 29, 2015) ##

For better compatibility with the upcoming version 2.0 release, this version introduces a new file layout so that users have the option of including header files such as dmrg.h using the code:
`#include "itensor/mps/dmrg.h"`
The itensor/mps/ prefix in this include will become mandatory in version 2.0. This new layout improves readability, and moves away from a more complex build system where header files were copied to the include/ folder (which is still done but only for backwards compatibility).

Other changes:
* Introduced randomTensor(Index...) function for better compatibility with upcoming version 2.0.
* Fixed bug #89: missing scale_.real() reported by @BapRoyer
* Added external rank(T) methods as alternative to T.r()
* Added experimental operator[] to Index which returns a copy with primelevel set to specified value.
* Updated Index printing format to `(name,size,type)'plev`


<a name="v1.2.4"></a>
## [Version 1.2.4](https://github.com/ITensor/library/tree/v1.2.4) (Sep 30, 2015) ##

Both ITensor and IQTensor now support the following element access methods, where I1, I2, ... are Index objects (or IQIndex objects in the case of IQTensor):

    T.set(I1(n1),I2(n2),..., x); //set element to x,
                                 //can be a Real or Cplx scalar

    T.real(I1(n1),I2(n2),...) //return element as real number
                              //throws if non-zero imag part

    T.cplx(I1(n1),I2(n2),...) //return element as complex number

<a name="v1.2.3"></a>
## [Version 1.2.3](https://github.com/ITensor/library/tree/v1.2.3) (Sep 23, 2015) ##

- Fixed major bug where svd of a complex ITensor with a negative scale could fail because the sign of the scale was only being included in the real part of the result. Thanks to Benoit Vermersch for pointing out this bug.

- Introduced fabs(LogNumber) function.

- Some tweaks to how Index, IndexSet, and ITensor are printed.

<a name="v1.2.2"></a>
## [Version 1.2.2](https://github.com/ITensor/library/tree/v1.2.2) (Sep 17, 2015) ##

- Fixed a bug in IQTensor const element access, thanks Shenghan Jiang

- Added stdx utility library which adds convenient extensions to the std library

- Added timers utility for profiling

<a name="v1.2.1"></a>
## [Version 1.2.1](https://github.com/ITensor/library/tree/1.2.1) (Aug 20, 2015) ##

- Created `setA` method for MPS/IQMPS. More self-documenting name and usage than 
  current `Anc` method.

  <div class="example_clicker">Show Example</div>

      auto psi = MPS(sites);
      auto T = ITensor(sites(j));
      T(j(1)) = 1./sqrt(2.);
      T(j(2)) = 1./sqrt(2.);
      psi.setA(j,T);

- `svd` functions now support setting `IndexType` and names of left and right 
  indices of singular value tensor.

  <div class="example_clicker">Show Example</div>

      auto T = ITensor(s1,s2,j);
      ITensor U(s1),D,V;
      svd(T,U,D,V,{"LeftIndexName","L",
                   "RightIndexName","R",
                   "IndexType",Xtype});
      //can also specify "LeftIndexType" and "RightIndexType" separately

- Added `count.h` mini-library. Allows range based iteration over integer ranges.

  <div class="example_clicker">Show Example</div>

      #include "count.h"

      auto v = std::vector<int>(10);
      for(auto n : count(v.size()))
          v[n] = n+n;

      //go from 2,...,v.size()-1
      for(auto n : count(2,v.size()))
          v[n] = n+n;

      //index(v) does count(v.size())
      for(auto n : index(v))
          v[n] = n+n;

      //count1 does 1-indexed counting
      auto T = ITensor(J);
      for(auto j : count1(J.m()))
          T(J(j)) = sqr(j);

- Added external `norm(T)` functions for ITensor and IQTensor.

- Fixed bug where truncation error was not properly reported by ITensor svd function.


<a name="v1.2.0"></a>
## [Version 1.2.0](https://github.com/ITensor/library/tree/v1.2.0) (Aug 13, 2015) ##

<b>New features:</b>

- IndexType now a class instead of an enum; this makes IndexType's user extensible, see commit github:a92c17a

  <div class="example_clicker">Show Example</div>

      auto MyType = IndexType("MyType");
      auto i = Index("i",10,MyType);
      auto j = Index("j",10,Link);

      auto T = ITensor(i,j);

      Print(prime(T,MyType)); //only i will be primed

- Makefiles now hide most compiler output for a nicer installation experience

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
