# InitState #

A class for initializing matrix product states.

An InitState is constructed by providing (at minimum) an object derived from [[Model|classes/model]]. 
In the documentation below, a MethodPtr is the address of one of this Model object's methods. <!--'-->

For example, if the Model object provided is of type `SpinHalf`, the available MethodPtr's <!--'--> are
`&SpinHalf::Up` and `&SpinHalf::Dn` (in general, any method of the Model-type object that takes an int and returns an 
IQIndexVal).

## Constructors ##

* `InitState(Model model)` 

   Construct an InitState but do not yet set any sites.

* `InitState(Model model, MethodPtr mp)` 

   Construct an InitState, setting every site to the same state using the provided MethodPtr.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,&SpinOne::Up);

## Accessor Methods ##

* `InitState& set(int i, MethodPtr mp)` 

   Set the state of site `i` using the provided MethodPtr. Returns a reference to `*this`.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,&SpinOne::Up); //initially set all sites to Up
        init.set(5,&SpinOne::Z0); //set site 5 to the Z0 state
        init.set(95,&SpinOne::Dn); //set site 95 to the Dn state

* `InitState& setAll(MethodPtr mp)` 

   Set the state of all sites sites using the provided MethodPtr. Returns a reference to `*this`.

  <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model); //Initially all sites are not set
        init.setAll(&SpinOne::Dn); //set all sites to the Dn state

* `IQIndexVal operator()(int i)` 

   Return the state of site `i` as an IQIndexVal. (N.B IQIndexVal is automatically convertible to IndexVal.)

   <div class="example_clicker">Show Example</div>

        SpinOne model(100);
        InitState init(model,&SpinOne::Z0); //Set all states to Z0
        IQIndexVal iv5 = init(5);
        cout << "iv5.i = " << iv5.i << endl; //Prints "iv5.i == 2", since Z0 is the 2nd state
        cout << (iv5.iqind == model.si(5) ? "true" : "false") << endl; //Prints "true"


[[Back to Classes|classes]]

[[Back to Main|main]]

