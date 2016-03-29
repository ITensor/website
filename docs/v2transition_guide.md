
## Version 1.x to 2.0 Transition Guide

Below are the major interface changes in ITensor version 2.0 versus 1.x.
Most of this interface is already supported, although optional, in the 1.x branch.
Following version 2.0 these changes are mandatory.

### Changes to Basic Interface


* Include statements now include paths to header files.

  Old-style version 1.x code

      #include "iqtensor.h"

  should be replaced by 

      #include "itensor/iqtensor.h"

  The appropriate path to use is the actual location of the file under the ITensor source directory.

  MPS and DMRG related codes are in the mps/ subfolder, for example

      #include "itensor/mps/dmrg.h"

* Use the `.real` and `.cplx` methods to access tensor elements.

  Old-style version 1.x code

      ITensor A(i,j);
      ... //make changes to A
      Real val = A(i(2),j(3));

  should be replaced by 

      ITensor A(i,j);
      ... //make changes to A

      //If A is known to be real
      auto val = A.real(i(2),j(3));

      //Or if A is complex
      auto val = A.cplx(i(2),j(3));

   Note that the `.cplx` method always succeeds even if the tensor is purely real. 
   If the tensor is a scalar (no indices) 
   use `.real()` or `.cplx()` to retrieve its value.


* Use the `.set` method to set tensor elements.

  Old-style version 1.x code

      ITensor A(i,j);
      A(i(2),j(3)) = 4.56;

  should be replaced by 

      ITensor A(i,j);
      A.set(i(2),j(3),4.56);

  One advantage of the new `.set` approach is one can pass a real or complex number to `.set`,
  whereas it was more cumbersome to create a complex ITensor before.

* Many previous ITensor and IQTensor class methods are now free functions.

  - `T.norm()` is now `norm(T)`

  - `T.randomize()` is now `randomize(T)`

  - Prefer `rank(T)` to `T.r()`

* The Vector and Matrix classes now have zero-indexed element access.
If you prefer a 1-indexed interface you can use the Vector1 and Matrix1
classes.

### Changes to Advanced Features

* The ITensor and IQTensor constructors taking a set of IndexVals (or IQIndexVals) and
  setting the corresponding element to 1.0 have been removed.
  Instead use the `setElt` function to make such tensors.
  For example if i and j are Index objects

      auto P = setElt(i(1),j(2));

  makes an ITensor P with the `i(1),j(2)` element set to 1.0 and the rest set to zero.

* Combiner and IQCombiner are no longer distinct types, but just a type of sparse ITensor or IQTensor.
  To create a combiner which combines indices i, j write the code

      auto C = combiner(i,j);

  To use the combiner just contract it with a tensor having indices i and j.

      auto T = ITensor(i,k,j,l);
      auto S = C*T;

  Creating IQCombiners works the same way except i and j are of type IQIndex.





