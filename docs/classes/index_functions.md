#Index Functions#

Standalone methods for manipulating objects of type `Index`.

* `Index primed(Index I, int inc = 1)` 

   Return a copy of `Index` I with prime level increased by 1 (or optional amount `inc`).

* `Index primed(Index I, IndexType type, int inc = 1)` 

   If `I.type() == type` or `type==All`, return a copy of Index I with prime level increased by 1 (or optional amount `inc`).

* `Index deprimed(Index I)` 

   Return a copy of Index I with prime level set to zero.

* `Index mapPrime(Index I, int plevold, int plevnew, IndexType type = All)` 

   Return a copy of I with new prime level plevnew if `I.primeLevel()==plevold`. (Optionally if `I.type()==type` or `type==All`.)


[[Back to Classes|classes]]

[[Back to Main|main]]

