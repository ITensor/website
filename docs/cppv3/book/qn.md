# Quantum Number (QN) Objects

As shown in examples on the previous pages, sectors of
a QN Index are labeled by QN objects, such as `QN("Sz",1)`
or `QN({"N",2},{"Sz",0})`. This page goes into more detail
about how these QN objects work, what mathematical rules
they obey, and how to construct them.

## QN Object Basics

At the simplest level, a QN is a small collection of name-value
pairs, where the name is a short string of up to seven characters
and the value is an integer.

For example, a QN constructed as `QN("N",2)` contains one pair
with the name "N" and the value 2.

A QN constructed as `QN({"Nb",1},{"Sz",2})` contains two pairs:
with the name "Nb" and the value 1, the other with the name "Sz"
and the value 2.

QN objects can be added, subtracted, and compared to each other.
For QNs like those above, addition and subtraction follows the usual
rules of integer arithmetic. Values of the same name are added to each
other. If one QN contains a name which is not present in another QN,
such a case is treated as if the other QN did have that name
but with the integer value equal to zero. This rule about missing names
being treated as zero applies to addition, subtraction, and comparison.

For example: `QN({"Sz",2},{"N",1}) + QN({"N",3}) == QN({"Sz",2},{"N",4})`.

The name-value pairs of a QN are not ordered, from a user perspective. 
Internally they are sorted by name, so you may provide them in any order 
and the QN system will handle the sorting for you.

Besides regular integer arithmetic, arithmetic modulo N (according to the group @@Z_N@@)
can also be defined for QN&mdash;we will discuss this case more below.

## Special Cases of the QN Constructor

Note that when constructing a QN containing just one name-value pair,
it is allowed to omit the curly braces: `QN("Sz",2)`.

Also, at most one of the names in a QN can be omitted, which is equivalent
to letting the name be the empty string `""`. This is for convenience
when no obvious name is available. For example, `QN(0)` and `QN(1)` are
valid QNs and equivalent to `QN({"",0})` and `QN({"",1})`.

## Modular Arithmetic

An important case of quantum numbers for physics applications are
quantum numbers obeying a @@Z_N@@ addition rule. Key examples include
superconductors conserving only fermion parity (@@Z_2@@) or clock-spin 
models obeying a @@Z_3@@ addition rule.

To specify a @@Z_N@@ addition rule for one or more QN name-value pairs,
simply specify the modulus @@N@@ as a third entry when defining that pair.
For example, `QN("P",0,2)` and `QN("P",1,2)` define QNs with pairs named "P"
(for parity) whose values are 0 and 1, and which obey a @@Z_2@@ addition rule.
Thus `QN("P",1,2)+QN("P",1,2) == QN("P",0,2)`.

Another example would be `QN({"Sz",1},{"T",2,3})` which defines a pair named
"Sz" with value 1 obeying usual integer arithmetic, whereas the pair named
"T" has value 2 and obeys @@Z_3@@ addition rules.

## Advanced, Experimental Features

Currently we are exploring a feature which would allow QN Indices to anticommute
to give QN ITensors fermionic behavior, without requiring users to do any 
bookkeeping such as with Jordan-Wigner string. We are reserving negative QN
modulus values for this purpose. Therefore please only set the modulus of a QN
name-value pair to a positive number, unless you are wanting automatic
fermion feature to be enabled. (Right now, AutoMPO uses a subset of these features.)
If you have any questions, please contact us at <i>support@itensor.org</i> or post
a question on the <a href="https://itensor.org/support/">Support Forum</a>.


<br/>

<span style="float:left;"><img src="docs/VERSION/arrowleft.png" class="icon">
[[QN Index|book/qnindex]]
</span>

<br/>

