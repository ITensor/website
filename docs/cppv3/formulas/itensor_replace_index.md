# Replace an Index of an ITensor with Another Index

Say we have an ITensor with indices a,b,c (objects of type Index):

    auto T = ITensor(a,b,c);

and we want to replace the Index b with another Index x.

To do this we can use a `delta` tensor, which models an identity 
matrix or a Kronecker delta symbol. To create a delta tensor, use
the function `delta`:

    T = T * delta(b,x);

Now T will have the index x instead of b, but otherwise the same data.
The Index x should be chosen to have the same dimension as b.

Internally, creating a two-index delta tensor does not allocate any
storage in memory and contracting it with another tensor uses an
efficient algorithm that just substitutes one index for another.





