# Change Log #


<a name="v0.2.0"></a>
## [Version 0.2.0](https://github.com/ITensor/library/tree/master) (In progress) ##

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

- Fixed lapack_wrap.h to compile with ACML library.

- Fixed Combiner to automatically init when copied to avoid confusing situations where copies could have a different right() Index.

- Fixed bug in IndexSet constructor when 8 indices provided.

- Updated sample codes.


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

## Development Version ([in progress](https://github.com/ITensor/library/tree/develop)) ##

- Removed ITSparse and IQTSparse classes. Now ITensor class carries an internal flag specifying whether it is
  diagonal (type()==ITensor::Diag) or dense (type()==ITensor::Dense). Diagonal ITensors are created by using
  certain constructors such as the constructor taking a Vector of components.

- Infinite DMRG (iDMRG) algorithm, see idmrg.h.

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

- Can now construct OptSet objects from a string such as 

  "UseSVD=false,Cutoff=1E-8,IndexName=newind". 

  Writing only the name of an 
  Opt such as "Quiet" is equivalent to "Quiet=true". Can also combine Opts and strings with '&' operator, for example:

  Opt("Cutoff",1E-8) & Opt("Quiet") & "UseSVD=false,IndexName=newind".

- Renamed IQTensor::iten_empty() to just IQTensor::empty().

- Removed IQTensor::iten_size() method. For an IQTensor T, just use T.blocks().size() instead.

- Changed behavior of commonIndex when no common index found: used to throw an exception, now returns a default-constructed ("Null")
  index.

[[Back to Main|main]]

