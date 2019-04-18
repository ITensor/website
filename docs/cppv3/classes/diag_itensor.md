# Delta and Diagonal ITensor

A diagonal ITensor is an ITensor with diagonal-sparse storage such that only its
diagonal elements T<sub>iii...</sub> are non-zero. (Diagonal elements mean
elements obtained by setting each Index to the same value.)

Uses of diagonal ITensors include replacing one Index of an ITensor with 
another; tracing pairs of indices; and "tying" multiple indices into a single Index.

Diagonal ITensors can be constructed either by calling the `delta` or `diagITensor`
functions:

* The `delta` function returns a diagonal ITensor whose diagonal elements
  are all 1.0. This introduces extra efficiencies as no memory is actually allocated
  since all elements are known to be the same.

* The `diagITensor` function can be used to construct general diagonal ITensors
  with different elements along the diagonal.


The functions `delta` and `diagITensor` are defined in "itensor/itensor.h"; also
see "itensor/itensor_impl.h".

## Synopsis

    auto i = Index(2,"i");
    auto j = Index(2,"j");
    auto k = Index(2,"k");
    auto l = Index(2,"l");

    //
    // Replace T's i Index with another Index l
    //
    auto T1 = randomITensor(i,j,k);
    T1 *= delta(i,l);

    //
    // Trace (sum over) a pair of indices
    //
    auto T2 = randomITensor(i,j,prime(i));
    T2 *= delta(i,prime(i));

    //
    // Tie multiple indices together
    //
    auto T3 = randomITensor(i,prime(i),j,prime(i,2));
    T3 *= delta(i,prime(i),prime(i,2),prime(i,3));


## Specification

* `delta(IndexSet is) -> ITensor`

  `delta(Index i1, Index i2, ...) -> ITensor`

  Given an IndexSet, a container of Indices convertible to an IndexSet, or two or more indices, 
  returns an ITensor having these indices and diagonal storage. 
  All diagonal elements have the value 1.0.

* `diagITensor(Container C, IndexSet is) -> ITensor`

  `diagITensor(Container C, Index i1, Index i2, ...) -> ITensor`

  Given a container C (can be any container type) and a set of indices, 
  returns an ITensor with these indices whose diagonal elements are the entries
  of the container, starting from `C[0]`.

  The container must be as large as the minimum size of the indices.


<br/>
_This page current as of version 3.0.0_
