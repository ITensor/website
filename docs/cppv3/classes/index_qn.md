# QN Index

An Index object can be given additional quantum number (QN) block structure when it is constructed. This structure cannot be changed afterward.

In addition to the QN structure, a set of tags and an Arrow direction (In,Out) can be specified when constructing an Index.

## Synopsis

    // Construct an Index with QN information
    auto I = Index(QN({"Sz", 2}),4,
                   QN({"Sz", 0}),8,
                   QN({"Sz",-2}),4);

    // Provide additional tags and Arrow direction
    auto J = Index(QN({"T", 1}),3,
                   QN({"T",-1}),3,
                   "J,Link",In);


    
