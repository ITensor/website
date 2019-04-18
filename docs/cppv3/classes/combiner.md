# Combiner ITensor

A combiner is a type of ITensor used to "reshape" several indices into one Index whose size is the product of the smaller indices. The same combiner can be used to reverse this process.

To construct a combiner ITensor, call the `combiner` method with the indices you want to combine as arguments.

To retrieve the "combined" index that results from merging all of the indices provided, use the combinedIndex` function (see below).

Internally, a combiner is implemented as a type of ITensor with a special storage type. This storage performs no allocation of any elements whatsoever; when a combiner ITensor is contracted with 
another ITensor, special optimized routines are called to reshape the regular ITensor into
the resulting ITensor with combined indices as efficiently as possible.

## Synopsis

    auto i = Index(3);
    auto j = Index(5);
    auto k = Index(7);
    auto l = Index(9);

    auto T = randomITensor(i,j,k,l);

    auto [C,c] = combiner(i,k);

    //
    // Combine
    // 
    auto cT = C * T; //or T * C, which has same effect

    Print(hasindex(cT,i)); //prints: false
    Print(hasindex(cT,j)); //prints: true
    Print(hasindex(cT,k)); //prints: false
    Print(hasindex(cT,l)); //prints: true
    Print(hasindex(cT,c)); //prints: true

    Print(order(cT)); //prints: 3

    Print(c == commonIndex(C,cT)); //prints: true

    Print(dim(c)); //prints 21 = 7*3

    //
    // Uncombine
    // 
    auto nT = cT * C;

    //Check that nT == T
    Print(norm(nT-T)); //prints: 0.0

## Specification

* `combiner(IndexSet is, Args args = Args::global()) -> std::tuple<ITensor,Index>`

  `combiner(Index i1, Index i2, ...) -> std::tuple<ITensor,Index>`

  Given an IndexSet, a container convertible to IndexSet, or a list of one or more indices, 
  return a combiner ITensor which can be used to combine these indices into a single, 
  new Index `c`, as well as the new Index `c`, in a tuple.

  The resulting ITensor will have all of the indices provided, plus one new Index `c` whose
  size is the product of sizes `dim(is(1)) * dim(is(2)) * ...`.

  The first version also recognizes the following optional named arguments:

  * "Tags" (default: "Link,CMB") &mdash; set the tags of the new, combined Index

## Related functions

* `combinedIndex(ITensor C) -> Index`
  
  Returned the "combined" index of the combiner C. This is the new Index that C has 
  which resulted from merging the indices passed to the `combiner` function.

  In debug mode, performs a run-time check that the ITensor C actually
  has combiner storage as it should. If this is not the case, an exception is thrown.

<br/>
_This page current as of version 3.0.0_
