#Index Functions#

Standalone methods for manipulating objects implementing the [[Index|classes/index]] interface. 

The following methods are templates, so they work not only for [[Index|classes/index]] objects
but for any object supporting the relevant methods, such as [[IndexVal|classes/indexval]], [[IQIndex|iqindex]],
[[ITensor|classes/itensor]], [[IQTensor|classes/iqtensor]], etc.

* `T primed(T I, int inc = 1)` 

   Return a copy of  `I`, calling `I.prime(inc)` first.

   Works for any type `T` implementing `T::prime(int inc)`.

* `T primed(T I, IndexType type, int inc = 1)` 

   Return a copy of  `I`, calling `I.prime(type,inc)` first.

   Works for any type `T` implementing `T::prime(IndexType type, int inc)`.

* `T deprimed(T I, IndexType type = All)` 

   Return a copy of `I`, calling `I.noprime(type)` first.

   Works for any type `T` implementing `T::noprime(IndexType type)`.

* `T mapPrime(T I, int plevold, int plevnew, ` <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;`IndexType type = All)` 

   Return a copy of `I`, calling `I.mapprime(plevold,plevnew,type)` first.

   Works for any type `T` implementing <br/> `T::mapprime(int plevold, inv plevnew, IndexType type)`.


[[Back to Classes|classes]]

[[Back to Main|main]]

