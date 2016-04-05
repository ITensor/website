# Index Functions #

Standalone methods for manipulating objects implementing the [[Index|classes/index]] interface. 

## Prime Level Functions

* `prime(Index I, int inc = 1) -> Index` 

   Return a copy of  `I` with prime level increased by 1 (or optional amount `inc`).

* `prime(Index I, IndexType type, int inc = 1) -> Index` 

   Return a copy of  `I` with prime level increased by 1 (or `inc`) if `I.type()` equals specified type.

* `noprime(Index I, IndexType type = All) -> Index` 

   Return a copy of `I` with prime level set to zero (optionally only if `I.type()` matches type).

* `mapprime(Index I, int plevold, int plevnew, IndexType type = All) -> Index` 

   Return a copy of `I` with prime level plevnew if `I.primeLevel()==plevold`. Otherwise has no effect.
   (Optionally, only map prime level if type of `I` matches specified type.)

## Other Functions

* `showm(Index I) -> string`

   Returns a string version of the size of Index I.
