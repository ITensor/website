#ITensor Code Conventions#


##Classes and Structs##

* Class methods modifying objects do not return a copy (although they may return a reference). 
  Free methods modifying objects return a copy. For example, `I.doprime()` increases the primeLevel of `Index I` in place
  whereas `primed(I)` returns a copy of `I` with increased primeLevel.

* The first letter of a class name is always capitalized.

##Formatting##

* All code should be idented using 4 spaces for each indent level ("soft tabs").

* Braces following function or class declarations, etc., should be on their own line and 
  be indented to the same level as the enclosed code. For example:

  <code>
  Real
  absSqrt(Real x)
      {
      if(x >= 0)
          return sqrt(x);
      else
          return sqrt(-x);
      }</code>

##Functions##

* Non-const reference or pointer arguments to a function always come after const reference or regular (copying) function arguments.
  The only exception is for arguments with default values which must come last.

* The return type of a function appears at the beginning of the line preceding the function name:

  <code>
  Real
  calculateSomething(const ITensor& A, const ITensor& B); </code> 
  Other keywords such as `friend` or `inline` should come after the return type unless disallowed by the compiler.


##Operators##

* Single-site operators are tensors with one unprimed Site index `S` and one primed Site Index `S'`.
  For the case of IQIndices, IQIndex `S` has an In Arrow and `S'` an Out Arrow.

* Each site tensor of an matrix product operators (MPO) follows the same Site-index convention as single-site operators.


</br>

[[Back to Main|main]]
