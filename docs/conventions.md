#ITensor Code Conventions#

None of these conventions are hard and fast, and there exist exceptions throughout the library.
However, the conventions below should be followed whenever possible and sensible.


##Classes and Structs##

* Class names are capitalized.

* Class methods are camel-cased e.g. `obj.doThing(...)` not `obj.do_thing(...)`.

* Private class data members are underscore spaced and end in an underscore.
  For example, `last_energy_` or `curr_index_`.

* Class methods modifying objects do not return a copy (but may return a reference). 
  For example, `I.doprime()` increases the prime level of `Index I` in place.

* Free methods modifying objects return a copy. For example, 
  `primed(I)` returns a copy of `I` with increased prime level.


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

* The return type of functions and class methods appears at the beginning of the line preceding the function name:

  <code>
  Real
  calculateSomething(const ITensor& A, const ITensor& B); </code> 
  Other keywords such as `friend` or `inline` should come after the return type unless disallowed by the compiler
  (such as when the return type is a reference).

##Functions##

* The preferred order of function arguments is:
    * Regular (copying, such as `int j`) and const reference (such as `const MPO& H`) arguments.
    * Non-const reference or pointer arguments.
    * Arguments with defaults (which must come last anyway).


##Operators##

* Single-site operator tensors have one unprimed Site index `S` and one primed Site Index `S'`.
  For IQTensor operators, IQIndex `S` has an In Arrow and `S'` an Out Arrow.

* Each tensor of a matrix product operator (MPO) follows the same conventions as single-site operators.


</br>

[[Back to Main|main]]
