#ITensor#

Tensor class providing automatic contraction over matching indices. 

An ITensor is created with a fixed
number of Index objects specifying its indices. Because each Index has a unique id, the
ITensor interface does not depend on a specific Index order. For example, 
given an ITensor constructed with indices a and b, T(a(2),b(5)) and T(b(5),a(2)) refer to the same component.

##Constructors##

* `ITensor()` <br/> Default constructor. For a default-constructed ITensor `T`, `T.isNull() == true`. To construct a rank zero ITensor use the `ITensor(Real val)` constructor below.

* `ITensor(Index i1)` <br/> `ITensor(Index i1, Index i2)` <br/>  `ITensor(Index i1, Index i2, Index i3)` <br/> ... etc. up to 8 indices <br/> Construct an ITensor with the given indices. All components initialized to zero.

* `ITensor(Real val)` <br/> Construct a rank zero, scalar ITensor with single component set to val.

* `ITensor(IndexVal iv1)` <br/> `ITensor(IndexVal iv1, IndexVal iv2)` <br/>  `ITensor(IndexVal iv1, IndexVal iv2, IndexVal iv3)` <br/> ... etc. up to 8 IndexVals <br/> Construct an ITensor with indices iv1.ind, iv2.ind, etc., such that the component corresponding to iv1.i, iv2.i, etc. is equal to 1 and all other components equal to zero. For example, constructing an ITensor T by calling ITensor T(a(1),b(2),c(3)) makes all components of T zero except for T(a(1),b(2),c(3))==1.


##Element Access Methods##

* `Real& operator()(IndexVal iv1, IndexVal iv2, ...)` <br/> Access component of this ITensor such that i1.ind is set to value i1.i, i2.ind to i2.i, etc. For example, given a matrix-like ITensor M with indices r and c, can access the (2,1) component by calling M(r(2),c(1)). Result is independent of the order of the arguments and depends only on the set of IndexVals provided. For the previous example, M(r(2),c(1)) == M(c(1),r(2)).

* `Real toReal()` <br/> Return only component of a rank zero, scalar ITensor. If the ITensor has rank greater than zero, throws an exception.

* `void toComplex(Real& re, Real& im)` <br/> Return real and imaginary parts of a complex scalar ITensor by reference. If the ITensor has any extra Index besides IndReIm, throws an exception.

##Operators##

##Prime Level Methods##


[[Back to Classes|classes]]

[[Back to Main|main]]
