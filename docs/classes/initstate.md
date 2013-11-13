# InitState #

A class for initializing matrix product states.

An InitState is constructed by providing (at minimum) an object derived from [[Model|classes/model]]. 
In the documentation below, the allowed "state" strings depend on the Model class used. For example, 
for the SpinOne model allowed state strings are "Up","Z0", and "Dn". For the Hubbard Model they are 
"Emp","Up","Dn", and "UpDn". See the documentation for each Model class for further details.

One an InitState object is constructed and all sites are set, it can be used in an MPS or IQMPS 
constructor to initialize that wavefunction to a specific product state.

## Synopsis ##

    const int N = 100;
    SpinHalf model(N);
    //First set all spins to be Up
    InitState state(model,"Up");
    //Now set every other spin to be Dn
    for(int j = 2; j <= N; j += 2)
        {
        state.set(j,"Dn");
        }

    MPS neel(state);



## Constructors ##

* `InitState(Model model)` 

   Construct an InitState but do not yet set any sites.

* `InitState(Model model, std::string state)` 

   Construct an InitState, setting every site to the same state using the provided string.
   Allowed state string depend on the implementation of the particular Model class provided.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,"Up");

## Accessor Methods ##

* `InitState& set(int i, std::string state)` 

   Set the state of site `i` using the provided string. Returns a reference to `*this`.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,"Up"); //initially set all sites to Up
        init.set(5,"Z0"); //set site 5 to the Z0 state
        init.set(95,"Dn"); //set site 95 to the Dn state

* `InitState& setAll(std::string state)` 

   Set the state of all sites sites using the provided string. Returns a reference to `*this`.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model); //Initially all sites are not set
        init.setAll("Dn"); //set all sites to the Dn state

* `IQIndexVal operator()(int i)` 

   Return the state of site `i` as an IQIndexVal. (N.B IQIndexVal is automatically convertible to IndexVal.)

   <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,"Z0"); //Set all states to Z0
        IQIndexVal iv5 = init(5);
        cout << "iv5.i = " << iv5.i << endl; //Prints "iv5.i == 2", since Z0 is the 2nd state
        cout << (iv5.iqind == model.si(5) ? "true" : "false") << endl; //Prints "true"


[[Back to Classes|classes]]

[[Back to Main|main]]

