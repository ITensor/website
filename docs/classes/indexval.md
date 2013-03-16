#IndexVal#

##(subclass of [[Index|classes/index]])##

An IndexVal represents an Index set to a specific value.

IndexVal is a subclass of [[Index|classes/index]] offering the same methods, but in addition
IndexVals carry an integer `i` representing a particular value the Index can take.


##Constructors##

* `IndexVal()`

  Default constructor. For a default-constructed IndexVal `iv`, `iv.isNull() == true`.

* `IndexVal(Index I, int i)`

  Construct an IndexVal from an Index `I` and integer value `i`.
  The value `i` must be >= 1 and <= `I.m()`.

  <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site);
        IndexVal iv(s1,2);
        Print(iv.i); //Prints 2

##Public Data Members##

* `int i`

  The value of this IndexVal. For an IndexVal `iv`, `iv.i` must be >= 1 and <= `iv.m()`.

##Operators##

* `bool operator==(IndexVal other)`  

  `bool operator!=(IndexVal other)`  

  Return `true` (for ==, `false` for !=) if this IndexVal equals other as an Index and this->i == other.i.


[[Back to Classes|classes]]

[[Back to Main|main]]

