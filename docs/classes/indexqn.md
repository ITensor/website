# IndexQN

An IndexQN is a struct holding an [[Index|classes/index]] and a [[QN|classes/qn]]. Its primary
purpose is for labeling individual sectors of an [[IQIndex|classes/iqindex]].

## Synopsis

    auto i = Index("i",2);
    auto q = QN(+1);

    auto iq = IndexQN(i,q);

    Print(iq.index); //prints: (i,2,Link)
    Print(iq.qn); //prints: QN(1)

## Public Data Members

* `Index index`

* `QN qn`

## Class Methods

* `IndexQN(Index i, QN q)`
 
  Construct an IndexQN by providing an Index `i` and a QN `q`. <br/>
  Calling this constructor sets `index = i` and `qn = q`.

* `m() -> long`

  Return the size of the `.index` field of the IndexQN.

* `type() -> IndexType`

  Return the IndexType of the `.index` field of the IndexQN.

## Other Features of IndexQN

* IndexQN's are default constructible.

* An IndexQN can be explicitly converted to an Index. The resulting 
  Index equals the `.index` field of the IndexQN.

* An IndexQN `iq` can be written to or read from disk by calling 
  `iq.write(s)` or `iq.read(s)` where `s` is a stream object.

* An IndexQN `iq` can be compared (`==` and `!=`) to an Index `i`.<br/>
  The comparison is equivalent to doing `iq.index == i` or `iq.index != i`.

* IndexQN's can be printed.

<br/>
_This page current as of version 2.0.3_

