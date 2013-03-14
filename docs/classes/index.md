#Index#

An Index represents a single tensor index with fixed dimension m.

In addition an Index has an IndexType (typically `Site` or `Link`&mdash;see [[index conventions|itensor_conventions]]),
a name for printing purposes (of type `std::string`), a unique id (or unique real, of type `Real`), and a prime level (of type `int`).

All copies of an Index have the same dimension and type, but their prime levels can be adjusted 
(and are automatically reflected in their unique real).
Indices compare equal if they have the same primelevel and are copies of the same original Index (equivalently, if they have the same unique real).


##Constructors##

* `Index()`

  Default constructor. For a default-constructed Index `J`, `J.isNull() == true`.

* `Index(string name, int m, IndexType it, int primelevel = 0)` 

  Construct an Index with specified fields described above.

  <div class="example_clicker">Show Example</div>

        Index s1("Site 1",2,Site);

##Accessor Methods##

* `int m()` 

  Return the bond dimension.

* `int primeLevel()` 

  Return the prime level.

* `void primeLevel(int n)`  

  Set prime level to n.

* `Real uniqueReal()`  

  Return the Real id number of this Index (same value for all copies of an Index having the same prime level).

* `IndexType type()`  

  Return the `IndexType` of this Index. Can be `Site`, `Link`, or `ReIm`.

* `string name()`  

  Return the name of this Index, including prime level information.

* `string rawname()`  

  Return the name of this Index without prime level information.

* `bool isNull()`  

  Return true if Index is default-constructed.

* `Arrow dir()`  

  Return the `Arrow` direction of this Index. Always returns `Out`. Currently only for interface compatibility with [[IQIndex|classes/iqindex]].


##Prime Level Methods##

* `void prime(int inc = 1)`  

  Increment prime level of this Index instance. (Optionally, increment by amount `inc`.)

* `void prime(IndexType type, int inc = 1)`  

  Increment prime level if Index type() matches type. (Optionally, increment by amount `inc`.)

* `void noprime(IndexType type = All)`  

  Reset prime level to zero. (Optionally, only if `type()==type` or `type` is `All`.)

* `void mapprime(int plevold, int plevnew, IndexType type = All)`  

  If Index has prime level plevold, change to plevnew. Otherwise has no effect. (Optionally, map prime level only if `type()==type` or `type` is `All`.)

##Operators##

* `IndexVal operator()(int i)`  

  Return an [[IndexVal|classes/indexval]] representing this Index set to value `i`.

  <div class="example_clicker">Show Example</div>

        Index mi("My Index",10);

        IndexVal iv = mi(2); //call Index mi's operator() method

        cout <<< (iv.ind == mi ? "true" : "false") << endl; //Prints true
        cout << mi.i << endl; //Prints 2

* `bool operator==(Index other)`  

  `bool operator!=(Index other)`  

  Return `true` (for ==, `false` for !=) if this Index and other are copies of the same original Index and have the same prime level. (Internally uses unique real for efficient comparison.)

* `bool operator<(Index other)`  

  Return `true` if `this->uniqueReal()` is less than `other.uniqueReal()`. Useful for sorting and finding Index instances in collections.

* `bool noprimeEquals(Index other)`  

  Return `true` if this Index and other are copies of the same original Index, regardless of prime level.

##Other Class Methods##

* `void write(std::ostream s)`  

  Write Index to stream in binary form.

* `void read(std::istream s)`  

  Read Index from stream in binary form.

* `void conj()`  

  Has no effect. Currently only for interface compatibility with [[IQIndex|classes/iqindex]].

[[Back to Classes|classes]]

[[Back to Main|main]]

