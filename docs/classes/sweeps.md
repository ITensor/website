# Sweeps

The Sweeps class makes it easy to specify the "accuracy parameters" used when doing DMRG calculations.
After setting the number of sweeps in the constructor, you can set parameters such as the 
truncation error cutoff to use for each sweep by providing the cutoffs in a comma-separated list.

## Synopsis

    auto sweeps = Sweeps(5); //do 5 sweeps

    //set max "m" or bond dimension for each sweep
    sweeps.maxm() = 10,20,40,80,160;
    //set truncation error cutoff for each sweep
    sweeps.cutoff() = 1E-5,1E-8,1E-10;

    //if fewer parameters are given than number of
    //sweeps (as above) then the last value is used
    //for all remaining sweeps.

## Names and meaning of "accuracy parameters"

* `maxm` &mdash; the bond dimension of any bond of the MPS cannot exceed the maxm value.

* `minm` &mdash; the bond dimension of any bond of the MPS will be at least 
  as large as minm, however singular values that are exactly zero will still be truncated.

* `cutoff` &mdash; the truncation error cutoff to use when computing SVD or density matrix
  diagonalizations. For more information on how the cutoff is defined, see the page
  on [[tensor decompositions|classes/decomp]].

* `niter` &mdash; controls maximum number of Davidson ("exact diagonalization") iterations to use
  in the core step of DMRG. (Regrettably, for historical reasons within ITensor, 
  niter actually corresponds to the number of basis states used, so the minimum value of niter that
  will result in any optimization happening must be niter >= 2. )

* `noise` &mdash; magnitude of the noise term to be added to the density matrix to aid convergence.
  If noise is set to zero, no noise term will be computed.


## Constructors

* ```
  Sweeps(int nsweeps,
         int minm = 1,
         int maxm = 500,
         Real cutoff = 1E-8,
         Real noise = 0.)
  ```
  Construct a Sweeps object specifying the number of sweeps (nsweeps).

  You can optionally provide fixed values of minm, maxm, cutoff to use 
  on every sweep (these can be changed later).

* ```
  Sweeps(Args const& args)
  ```
  Construct a Sweeps object by specifying a set of named arguments.

  Required arguments:
  - "Nsweep" &mdash; number of sweeps
  - "Maxm" &mdash; maximum bond dimension of MPS
  - "Cutoff" &mdash; truncation error threshold used for density matrix truncation

  Optional arguments:

  - "Minm" &mdash; maximum bond dimension of MPS
  - "Noise" &mdash; coefficient of density matrix noise term
  - "Niter" &mdash; maximum number of Davidson iterations


* `Sweeps(int nsweeps, InputGroup & sweep_table)`

  Construct a Sweeps object from an InputGroup of the following form:

      input_group_name
      {

      ...

      table_name
           {
           maxm   minm  cutoff  niter  noise
           20     20    1E-8    4      1E-8
           40     20    1E-8    3      1E-9
           80     20    1E-10   2      1E-10
           160    20    1E-12   2      0
           240    20    1E-12   2      0
           }

      ...

      }
    
  Then the following code can be used to read in this table
  and construct a sweeps object:
      
      auto input = InputGroup(filename,"input_group_name");
      auto sw_table = InputGroup(input,"table_name");
      auto sweeps = Sweeps(5,sw_table);
        

## Comma-separated list input methods

For the following methods, the returned type is a "SweepSetter" object which
collects numbers in a comma-separated list, then provides these numbers
to the associated Sweeps object.

If fewer values are provided than the number of sweeps, the last
value will be used for all remaining sweeps.

* `.maxm() -> SweepSetter<int>` 

  Set the maxm value used for each sweep from a comma-separated list.

  <div class="example_clicker">Show Example</div>

      sweeps.maxm() = 10,40,80,160,160,800;

* `.cutoff() -> SweepSetter<Real>` 

  Set the cutoff value used for each sweep from a comma-separated list.

  <div class="example_clicker">Show Example</div>

      sweeps.cutoff() = 1E-8,1E-10;

* `.minm() -> SweepSetter<int>` 

  Set the minm value used for each sweep from a comma-separated list.

* `.niter() -> SweepSetter<int>` 

  Set the niter value used for each sweep from a comma-separated list.

* `.noise() -> SweepSetter<Real>` 

  Set the noise value used for each sweep from a comma-separated list.


## Other methods

* `.nsweep() -> int` <br/>
  `.size() -> int`

  Retrieve the number of sweeps represented by this Sweeps object.

* `.minm(int sw) -> int`

  Retrieve the minm value set for sweep number `sw`.

* `.maxm(int sw) -> int`

  Retrieve the maxm value set for sweep number `sw`.

* `.cutoff(int sw) -> Real`

  Retrieve the cutoff value set for sweep number `sw`.

* `.noise(int sw) -> Real`

  Retrieve the noise value set for sweep number `sw`.

* `.niter(int sw) -> int`

  Retrieve the niter value set for sweep number `sw`.

* `.setminm(int sw, int newminm)`

  Set a new minm value for sweep number `sw`.

* `.setmaxm(int sw, int newmaxm)`

  Set a new maxm value for sweep number `sw`.

* `.setcutoff(int sw, Real newcutoff)`

  Set a new cutoff value for sweep number `sw`.

* `.setnoise(int sw, Real newnoise)`

  Set a new noise value for sweep number `sw`.

* `.setniter(int sw, int newniter)`

  Set a new niter value for sweep number `sw`.

* `.read(std::istream & s)` <br/>
  `.write(std::ostream & s)`
 
  Read or write this Sweeps object from/to a binary stream.
