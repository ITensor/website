# MPS and IQMPS #

MPS and IQMPS are matrix product states consisting of ITensors and IQTensors respectively. Otherwise both
classes have an identical interface. In the documentation below, MPS may refer to either an MPS or IQMPS 
if used in a generic context. The type `Tensor` refers to `ITensor` for an MPS and `IQTensor` for an IQMPS.

An MPS can be constructed from either a [[SiteSet|classes/siteset]] or an [[InitState|classes/initstate]].

## Synopsis ##

    const int N = 100;
    SpinHalf sites(N);

    MPS psi(sites); //create random product MPS

    //Shift MPS gauge such that site 1 is
    //the orthogonality center ("left-canonical gauge")
    psi.position(1);

    //Contract link index of first and second
    //MPS site tensors to create two site wavefunction
    ITensor bondWF = psi.A(1)*psi.A(2);

    //Shift MPS gauge to a different site j ("mixed-canonical gauge")
    psi.position(j);

    //Modify tensor at site j
    //"nc" stands for "non-const"
    psi.Anc(j).randomize();

    //Initialize an IQMPS to a specific product state,
    //in this case the Neel state
    InitState state(sites);
    for(int i = 1; i <= N; ++i)
        {
        if(i%2 == 0) state.set(i,"Up");
        else         state.set(i,"Dn");
        }

    IQMPS qpsi(state);


## Constructors ##

* `MPS()` <br/>
  `IQMPS()`

  Default constructor. A default constructed state `psi` evaluates to false in a boolean context.

  <div class="example_clicker">Show Example</div>

      MPS psi;
      if(!psi) println("psi is default constructed");

* `MPS(SiteSet sites)`

  Construct an `MPS` with physical sites given by a `SiteSet`. The `MPS` will be initialized to a random product state.

* `IQMPS(SiteSet sites)`

  Construct an `IQMPS` with physical sites given by a `SiteSet`. The `IQMPS` site tensors will not be initialized.

* `MPS(InitState state)` <br/>
  `IQMPS(InitState state)`

  Construct an `MPS` or `IQMPS` and set its site tensors to be in the product state specified by the `InitState` argument.

## Accessor Methods

* `int N()`

  Returns the number of lattice sites of the MPS.

* `const Tensor& A(int i)`

  Returns a const reference (read-only access) to the MPS tensor at site `i`.

* `Tensor& Anc(int i)`

  Returns a non-const reference (read-write access) to the MPS tensor at site `i`.

  If read-only access is sufficient, use the `A(i)` method instead of this one.
  If site `i` is not the orthogonality center, calling `Anc(i)` will set `leftLim()`
  to `i-1` or `rightLim()` to `i+1` depending on whether `i` comes before or after 
  the center site&mdash;this can lead to additional overhead later when calling `position(j)`
  to gauge the MPS to a different site.

* `int rightLim()` <br/>
  `void rightLim(int j)`

  Returns (or sets) the right orthogonality limit. If `rightLim()` returns the value `j`, all tensors
  at sites `i >= j` are guaranteed to be right orthogonal.
  Only set the `rightLim` manually if you are certain that this condition is met.

* `int leftLim()` <br/>
  `void leftLim(int j)`

  Returns (or sets) the left orthogonality limit. If `leftLim()` returns the value `j`, all tensors
  at sites `i <= j` are guaranteed to be left orthogonal.
  Only set the `leftLim` manually if you are certain that this condition is met.

* `bool isOrtho()`

  Returns `true` if the MPS has an orthogonality center that is a single site. This is equivalent to
  the condition that `leftLim()+1 == rightLim()-1`, in which case the center site is `leftLim()+1`.

* `int orthoCenter()`

  Returns the location of the center site (unique site which is the orthogonality center of the MPS).
  Throws an `ITError` if the orthogonality center is not well defined i.e. if `isOrtho()==false`.

* `const SiteSet& sites()`

  Returns a const reference to the `SiteSet` associated with the lattice sites of this MPS.

# Modifying and Re-gauging MPS

* `position(int j)`

  Sets the orthogonality center to site `j` by performing singular value decompositions of tensors
  between `leftLim()` and `rightLim()`. After calling `position(j)`, tensors at sites `i < j` are
  guaranteed left-orthogonal and tensors at sites `i > j` are guaranteed right-orthogonal. Left
  and right orthogonal site tensors can be omitted from operator expectation values for sites not 
  in the support of the operator.

  Note: calling `position(j)` may in general change the "virtual" indices between some or all of
  the MPS tensors.

* `orthogonalize(OptSet opts = Global::opts())`

  Fully re-gauge and compress the MPS by performing two passes: one to make all of the tensors orthogonal with minimal truncation,
  and another to truncate the MPS to the requested accuracy.

  Opts recognized:
  * "Cutoff": truncation error cutoff
  * "Maxm": maximum bond dimension of MPS

* `svdBond(int b, Tensor AA, Direction dir, OptSet opts = Global::opts())`

  Replace the tensors at sites `b` and `b+1` (i.e. on bond `b`) with the tensor `AA`, which will be decomposed
  using a factorization equivalent to an SVD. If the `Direction` argument `dir==Fromleft`, then after the call
  to `svdBond`, site `b+1` will be the orthogonality center of the MPS. Similarly, if `dir==Fromright` then `b`
  will be the orthogonality center.

* `svdBond(int b, Tensor AA, Direction dir, const LocalOpT& PH, OptSet opts = Global::opts())`

  Equivalent to `svdBond` above but with an additional argument `PH` (for "projected Hamiltonian") which
  is used to compute the "noise term" which will be added to the density matrix used to decompose `AA`.


