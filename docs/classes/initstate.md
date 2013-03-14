#InitState#

A class for initializing matrix product states.

An InitState is constructed by providing (at minimum) an object derived from [[Model|classes/model]]. 
In the documentation below, a MethodPtr is the address of one of this Model object's methods. <!--'-->

For example, if the Model object provided is of type `SpinHalf`, the available MethodPtr's <!--'--> are
`&SpinHalf::Up` and `&SpinHalf::Dn` (in general, any method of the Model-type object that takes an int and returns an 
IQIndexVal).

##Constructors##

* `InitState(Model model)` 

   Construct an InitState but do not yet set any sites.

* `Index(Model model, MethodPtr mp)` 

   Construct an InitState, setting every site to the same state using the provided MethodPtr.


##Accessor Methods##

* `InitState& set(int i, MethodPtr mp)` 

   Set the state of site `i` using the provided MethodPtr. Returns a reference to `*this`.

* `InitState& setAll(MethodPtr mp)` 

   Set the state of all sites sites using the provided MethodPtr. Returns a reference to `*this`.

* `IQIndexVal operator()(int i)` 

   Return the state of site `i` as an IQIndexVal. (N.B IQIndexVal is automatically convertible to IndexVal.)


[[Back to Classes|classes]]

[[Back to Main|main]]

