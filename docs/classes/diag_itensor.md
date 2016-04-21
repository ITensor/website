# Delta and Diagonal ITensor

A diagonal ITensor is an ITensor with diagonal-sparse storage such that only its
diagonal elements T<sub>iii...</sub> are non-zero. (Diagonal elements mean
elements obtained by setting each Index to the same value.)

Uses of diagonal ITensors include replacing one Index of an ITensor with 
another; tracing pairs of indices; and "tying" multiple indices into a single Index.

Diagonal ITensors can be constructed either by calling the `delta` or `diagTensor`
functions:

* The `delta` function returns a diagonal ITensor whose diagonal elements
  are all 1.0. This introduces extra efficiencies as no memory is actually allocated
  since all elements are known to be the same.

* The `diagTensor` function can be used to construct general diagonal ITensors
  with different elements along the diagonal.


## Synopsis


    //
    // Replace T's i Index with another Index l
    //
    auto T1 = ITensor(i,j,k);
    T1 *= delta(i,l);

    //
    // Trace (sum over) a pair of indices
    //
    auto T2 = ITensor(i,j,prime(i));
    T2 *= delta(i,prime(i));


    //
    // Tie multiple indices together
    //
    auto T3 = ITensor(i,prime(i),j,prime(i,2));
    T3 *= delta(i,prime(i),prime(i,2),prime(i,3));


## Specification

* `delta(Index i1, Index i2, ...) -> ITensor`

  Given two or more indices, returns an ITensor having these indices and diagonal
  storage. All diagonal elements have the value 1.0.

* `diagTensor(Container C, Index i1, Index i2, ...) -> ITensor`

  Given a container C (can be any container type) and a set of indices, 
  returns an ITensor with these indices whose diagonal elements are the entries
  of the container, starting from `C[0]`.

  The container must be as large as the minimum size of the indices.



