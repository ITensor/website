
## Version 1.x to 2.0 Transition Guide

Below are the major interface changes in ITensor version 2.0 versus 1.x.
Most of this interface is already supported, although optional, in the 1.x branch.
Following version 2.0 these changes are mandatory.


* Include statements now include paths to header files.

  Old-style version 1.x code

      #include "iqtensor.h"

  should be replaced by 

      #include "itensor/iqtensor.h"

  The appropriate path to use is the actual location of the file under the ITensor source directory.

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

