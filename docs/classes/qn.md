# QN #

<span style="color:red;font-style:italic;">Note: this documentation page refers to code prior to version 2.0</span>

Class for representing a set of Abelian quantum numbers. Currently QN supports three quantum numbers: `sz` representing the spin in the z direction,
`Nf` representing the particle number, and `Nfp` representing the fermion parity (number of fermions mod 2). Setting a particular quantum number to 
zero throughout a simulation indicates that it is not to be tracked.

## Constructors ##

* `QN(int sz = 0, int Nf = 0)`

  Construct a QN with spin (magnetic) quantum number `sz` and particle number `Nf`. 

* `QN(int sz, int Nf, int Nfp)`

  Construct a QN with spin (magnetic) quantum number `sz`, particle number `Nf`, and "fermion parity" `Nfp`. The parity `Nfp` is 
  required to equal `Nf` mod 2 unless `Nf` is set to zero, which indicates that `Nf` is not a good quantum number.

## Accessor Methods ##

* `int sz()`

  Retrieve the spin quantum number of this QN.

* `int Nf()`

  Retrieve the particle number of this QN.

* `int Nfp()`

  Retrieve the fermion parity of this QN. Because it is equal to the number of particles mod 2, it can only take the values 0 or 1.

* `string toString()`

  Returns a string representation of the QN.

## Operators ##

* `QN& operator+=()` <br/>
  `QN& operator-=()` <br/>
  (and related free methods)

  QN addition and subtraction, which act on the sz and Nf quantum numbers like regular integers, 
  whereas Nfp is computed from Nf mod 2.

* `QN& operator-()`

  Negation operator: negates sz and Nf like regular integers, while Nfp is computed from Nf mod 2.

* `QN& operator==()` <br/>
  `QN& operator!=()`

  QN equality comparison. Two QN objects compare equal if sz, Nf, and Nfp are all the same.

* `QN& operator<()` <br/>

  QN less than comparison, which is useful for sorting. Defined to sort QN objects by sz, then by Nf, then finally by Nfp.

* `QN& operator*=(Arrow dir)`

  Multiplication by an In Arrow flips the sign of the QN whereas an Out Arrow preserves the sign. Used in computing the quantum number
  flux of a collection of [[IQIndex|classes/iqindex]] objects.

