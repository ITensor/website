# Single Element ITensor

A single element ITensor is an ITensor constructed using the `setElt` function.
It has exactly one non-zero element, which can be any element.

(Currently this type of ITensor uses dense storage but this is subject to change in the future.)

`setElt` is defined in "itensor/itensor_interface.h" and "itensor/itensor_interface_impl.h".

## Synopsis

    auto i = Index("i",4);
    auto j = Index("j",3);

    auto T = randomTensor(i,j);

    auto S = setElt(i(2));

    //Multiplying by S in this case will "quench"
    //the i Index of T to its second value:
    T *= S;

## Specification

`setElt(IndexVal iv1, IndexVal iv2, ...) -> ITensor`

Given one or more [[IndexVals|classes/indexval]], return an [[ITensor|classes/itensor]] with all elements set to zero
except the element corresponding to the IndexVals which is set to 1.0.

<div class="example_clicker">Click to Show Example</div>

     auto s = Index("s",3);
     auto l = Index("l",10);

     auto T = setElt(s(2),l(4));

     Print(T.real(s(1),l(1))); //prints: 0.0
     Print(T.real(s(2),l(1))); //prints: 0.0
     //...
     Print(T.real(s(2),l(4))); //prints: 1.0

<br/>
_This page current as of version 2.0.6_
