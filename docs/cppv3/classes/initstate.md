# InitState #

A class for initializing matrix product states.

An InitState is constructed by providing a type of [[SiteSet|classes/siteset]] such as a `SpinHalf` or `Fermion` site set.
In the documentation below, the allowed "state" strings depend on the SiteSet class used. 
For example, for the `SpinOne` siteset allowed state strings are "Up","Z0", and "Dn". For the `Electron` SiteSet they are "Emp","Up","Dn", and "UpDn". See the documentation for each SiteSet class for further details.

One an InitState object is constructed and all sites are set, 
it can be used in an MPS constructor to initialize that wavefunction to a specific product state.

## Example

    const int N = 100;
    auto sites = SpinHalf(N);
    //First set all spins to be "Up"
    auto state = InitState(sites,"Up");
    //Now set every other spin to be "Dn" (down)
    for(int j = 2; j <= N; j += 2)
        {
        state.set(j,"Dn");
        }

    auto neel_state = MPS(state);



## Constructors ##

* `InitState(SiteSet sites)` 

   Construct an InitState but do not yet set any sites.

* `InitState(SiteSet sites, std::string state)` 

   Construct an InitState, setting every site to the same state using the provided string.
   Allowed state string depend on the implementation of the particular SiteSet class provided.

  <div class="example_clicker">Show Example</div>

        SpinOne sites(100);
        InitState init(sites,"Up");

## Accessor Methods ##

* `InitState& set(int i, std::string state)` 

   Set the state of site `i` using the provided string. Returns a reference to `*this`.

  <div class="example_clicker">Show Example</div>

        SpinOne sites(100);
        InitState init(sites,"Up"); //initially set all sites to Up
        init.set(5,"Z0"); //set site 5 to the Z0 state
        init.set(95,"Dn"); //set site 95 to the Dn state

