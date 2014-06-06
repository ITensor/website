# IndexVal #

An IndexVal represents an Index fixed to a specific value.

IndexVal holds both an Index in a field called "`index`" and 
an integer "`i`" representing a particular value the Index can take.
This value is 1-indexed and must be >= 1 and <= `index.m()`.


## Constructors ##

* `IndexVal()`

  Default constructor. For a default-constructed IndexVal `iv`, `iv.isNull() == true`.

* `IndexVal(Index I, int i)`

  Construct an IndexVal from an Index `I` and integer value `i`.
  The value `i` must be >= 1 and <= `I.m()`.

  <div class="example_clicker">Show Example</div>

        Index s1("Site 1",4,Site);
        IndexVal iva(s1,3),
                 ivb(s1,1);
        Print(iva.i); //Prints 3
        Print(ivb.i); //Prints 1

## Public Data Members ##

* `Index index`

  The index referred to by this `IndexVal`. Conceptually and IndexVal represents fixing the `Index index` to the integer `i`.

* `int i`

  The value of this IndexVal. For an IndexVal `iv`, `iv.i` must be >= 1 and <= `iv.m()`.

## Accessor Methods ##

* `int m()` 

  Return the bond dimension of the `Index` `index`.

## Prime Level Methods ##

* `prime(int inc = 1)`  

  Increment prime level of `index`. (Optionally, increment by amount `inc`.)

* `prime(IndexType type, int inc = 1)`  

  Increment prime level of `index` if Index type() matches type. (Optionally, increment by amount `inc`.)

* `noprime(IndexType type = All)`  

  Reset prime level of `index` to zero. (Optionally, only if `type()==type` or `type` is `All`.)

* `mapprime(int plevold, int plevnew, IndexType type = All)`  

  If `index` has prime level plevold, change to plevnew. Otherwise has no effect. (Optionally, map prime level only if `type()==type` or `type` is `All`.)

## Operators ##

* `bool operator==(IndexVal other)`  

  `bool operator!=(IndexVal other)`  

  Return `true` (for ==, `false` for !=) if this IndexVal equals other as an Index and this->i == other.i.

[[Back to Classes|classes]]

[[Back to Main|main]]

