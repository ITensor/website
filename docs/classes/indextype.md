# IndexType #

IndexType is a lightweight label for Index objects. 

IndexTypes are useful for manipulating and retrieving Index
objects based on a certain grouping (the meaning is up to 
the user). For example, we may want to only adjust the prime
level of Index objects of type `Site` while leaving other 
indices unchanged.

An IndexType is implemented internally as a constant, fixed-size
string of up to 7 characters.


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

  <div class="example_clicker">Show Example</div>

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

  <div class="example_clicker">Show Example</div>

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

  <div class="example_clicker">Show Example</div>

      auto type = getIndexType(args,"BondType",Link);


<br/>
_This page current as of version 2.0.3_
