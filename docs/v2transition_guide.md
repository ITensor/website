
## Version 1.x to 2.0 Transition Guide

Below are the major interface changes in ITensor version 2.0 versus 1.x.
Most of this interface is already supported, although optional, in the 1.x branch.
Following version 2.0 these changes are mandatory.

### General Tips for Updating

* When updating, remove your old options.mk file
  and create a new one from the options.mk.sample file.
  You can save a backup your old file to recall your BLAS/LAPACK settings.

* It may not hurt to completely re-clone ITensor from github. For example, the include/ folder
  is no longer used in version 2.0 but may stay around on your machine if you upgrade
  by just doing a git pull.

### Changes to Basic Interface

Note that some of these changes already work under version 1.3.x. However, they are mandatory
following version 2.0.x.

* There is now an "all.h" header which gives a convenient way to include the entire library.

      #include "itensor/all.h"


* Include statements must now include paths to header files.

  Old-style version 1.x code

      #include "iqtensor.h"

  should be replaced by 

      #include "itensor/iqtensor.h"

  The appropriate path to use is the actual location of the file under the ITensor source directory.

  MPS and DMRG related codes are in the mps/ subfolder, for example

      #include "itensor/mps/dmrg.h"

* Use the `.real` and `.cplx` methods to access tensor elements.

  Old-style version 1.x code

      auto A = ITensor(i,j);
      ... //make changes to A
      Real val = A(i(2),j(3));

  should be replaced by 

      auto A = ITensor(i,j);
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

      auto A = ITensor(i,j);
      A(i(2),j(3)) = 4.56;

  should be replaced by 

      auto A = ITensor(i,j);
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

* The header `svdalgs.h` has been renamed to `decomp.h`

* Older codes may still be using the names "Opt" and "OptSet" for passing
optional named arguments to functions. From version 2.0 on, these older names
have been removed in favor of a single class called "Args". For more on 
using the Args system view [[this Args tutorial|tutorials/args]].

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
      auto S = C * T;

  Creating IQCombiners works the same way except i and j are of type IQIndex.


