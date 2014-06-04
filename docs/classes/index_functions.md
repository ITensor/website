# Index Functions #

Standalone methods for manipulating objects implementing the [[Index|classes/index]] interface. 

The following methods are templates, so they work not only for [[Index|classes/index]] objects
but for any object supporting the relevant methods, such as [[IndexVal|classes/indexval]], [[IQIndex|iqindex]],
[[ITensor|classes/itensor]], [[IQTensor|classes/iqtensor]], etc.

* `T prime(T I, int inc = 1)` 

   Return a copy of  `I` with prime level increased by 1 (or optional amount `inc`).

   Works for any type `T` implementing `T::prime(int inc)`.

* `T prime(T I, IndexType type, int inc = 1)` 

   Return a copy of  `I` with prime level increased by 1 (or `inc`) if `I.type()` equals specified type.

   Works for any type `T` implementing `T::prime(IndexType type, int inc)`.

* `T noprime(T I, IndexType type = All)` 

   Return a copy of `I` with prime level set to zero (optionally only if `I.type()` matches type).

   Works for any type `T` implementing `T::noprime(IndexType type)`.

* `T mapPrime(T I, int plevold, int plevnew, IndexType type = All)` 

   Return a copy of `I` with prime level plevnew if `I.primeLevel()==plevold`. Otherwise has no effect.
   (Optionally, only map prime level if type of `I` matches specified type.)

   Works for any type `T` implementing <br/> `T::mapprime(int plevold, inv plevnew, IndexType type)`.


[[Back to Classes|classes]]

[[Back to Main|main]]

