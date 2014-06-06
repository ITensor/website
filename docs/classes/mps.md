# MPS and IQMPS #

MPS and IQMPS are matrix product states consisting of ITensors and IQTensors respectively. Otherwise both
classes have an identical interface.

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

[[Back to Classes|classes]]

[[Back to Main|main]]

