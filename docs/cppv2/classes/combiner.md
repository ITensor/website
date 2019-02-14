# Combiner ITensor

A combiner is a type of ITensor used to "reshape" several indices into one Index whose size is the product of the smaller indices. The same combiner can be used to reverse this process.

To construct a combiner ITensor, call the `combiner` method with the indices you want to combine as arguments.

To retrieve the "combined" index that results from merging all of the indices provided, use the combinedIndex` function (see below).

Internally, a combiner is implemented as a type of ITensor with a special storage type. This storage performs no allocation of any elements whatsoever; instead it acts as a "tag" which causes contraction with a combiner to call special optimized routines to reshape a regular ITensor as efficiently as possible.


## Synopsis

    auto i = Index("i",3);
    auto j = Index("j",5);
    auto k = Index("k",7);
    auto l = Index("l",9);

    auto T = ITensor(i,j,k,l);
    randomize(T);

    auto C = combiner(i,k);

    //
    // Combine
    // 
    auto cT = C * T; //or T * C, which has same effect

    Print(hasindex(cT,i)); //prints: false
    Print(hasindex(cT,j)); //prints: true
    Print(hasindex(cT,k)); //prints: false
    Print(hasindex(cT,l)); //prints: true

    Print(rank(cT)); //prints: 3

    //Get the new Index which replaced i and k
    auto ci = commonIndex(C,cT);

    Print(ci.m()); //prints 21 = 7*3

    //
    // Uncombine
    // 
    auto nT = cT * C;

    //Check that nT == T
    Print(norm(nT-T)); //prints: 0.0

## Specification

* `combiner(Index i1, Index i2, ...) -> ITensor`

  Given one or more indices, return a combiner ITensor which can be used to combine these indices
  into a single, new Index `c`.

  The resulting ITensor will have all of the indices provided, plus one new Index `c` whose
  size is the product of sizes `i1.m() * i2.m() * ...`.

* `combiner(std::vector<Index> inds, Args args = Args::global()) -> ITensor`

  Given a std::vector of Index objects, return a combiner ITensor which combines these indices
  into a single new index.

  The resulting ITensor will have all of the indices provided, plus one new Index `c` whose
  size is the product of sizes `i1.m() * i2.m() * ...`.

  This function also recognizes the following optional named arguments:

  * "IndexName" (default: "cmb") &mdash; provide a string to use for the name of the new, combined Index
  * "IndexType" (default: Link) &mdash; set the [[IndexType|classes/indextype]] of the new, combined Index

## Related functions

* `combinedIndex(ITensor C) -> Index`
  
  Returned the "combined" index of the combiner C. This is the new Index that C has 
  which resulted from merging the indices passed to the `combiner` function.

  In debug mode, performs a run-time check that the ITensor C actually
  has combiner storage as it should. If this is not the case, an exception is thrown.

<br/>
_This page current as of version 2.1.0_
