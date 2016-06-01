# IndexType #

IndexType is a lightweight label for Index objects. 

IndexTypes are useful for manipulating and retrieving Index
objects based on a certain grouping (the meaning is up to 
the user). For example, you may want to only adjust the prime
level of Index objects of type `Site` while leaving other 
indices unchanged.

An IndexType is implemented internally as a constant, fixed-size
string of up to 7 characters.

ITensor pre-defines a number of IndexTypes for you to use
(see the <a href="#predef">full list</a> below).

IndexType is defined in "itensor/indextype.h".

## Synopsis

    auto MyType = IndexType("MyType");

    auto i = Index("i",2,MyType);
    Print(i.type()); //prints: i.type() = MyType


## Class Methods ##

* `IndexType(const char* name)`

  Constructor taking a string constant. If the string exceeds 7 
  characters only the first 7 will be used.

* `.size() -> size_t` 

   Returns the maximum size `7ul`. 

* `.c_str() -> const char*` 

   Returns the constant string stored inside the IndexType.

* `.operator[](int i) -> char&` 

  Access the i'th character in the IndexType's storage.

## Other IndexType Functions

* ```
  add(Args            & args, 
      Args::Name const& name, 
      IndexType         it)
  ```

  Add an IndexType valued field to an Args named argument object.

  <div class="example_clicker">Click to Show Example</div>

      auto MyType = IndexType("MyType");
      auto args = Args("Maxm",50,"DoStep",true);
      add(args,"BondType",MyType);
      Print(args.defined("BondType")); //prints 'true'

* ```
  getIndexType(Args const& args, 
               Args::Name const& name) 
  -> IndexType
  ```

  Retrieve the value of a named argument from an Args object
  as an IndexType.
  Throws an exception if there is no argument with this name.

  <div class="example_clicker">Click to Show Example</div>

      auto type = getIndexType(args,"BondType");

* ```
  getIndexType(Args const& args, 
              Args::Name const& name, 
              IndexType default) 
  -> IndexType
  ```

  Retrieve the value of a named argument from an Args object
  as an IndexType. If the Args object does not have a field with
  the given name, returns the default IndexType provided.

  <div class="example_clicker">Click to Show Example</div>

      auto type = getIndexType(args,"BondType",Link);

<a name="predef"></a>
## Pre-defined IndexTypes

Below are IndexType variables pre-defined by ITensor for you to use:

* `Site` &mdash; conventionally used for physical, or "site" indices of wavefunctions
* `Link` &mdash; conventionally used for link, virtual, or bond indices of tensor networks
* `All` &mdash; special argument to functions taking an IndexType,
  indicating the behavior should apply to any IndexType. Users are not allowed
  to create Index objects with the `All` type.
* `NullInd` &mdash; specal IndexType indicating that no IndexType was provided

For convenience, ITensor also pre-defines the following IndexTypes, leaving their interpretation up to the user:
* `AType`
* `BType`
* `CType`
* `DType`
* `VType`
* `WType`
* `XType`
* `YType`


<br/>
_This page current as of version 2.0.6_
