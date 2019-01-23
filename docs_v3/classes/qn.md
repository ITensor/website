# QN 

A QN object is an ordered set of "quantum numbers". Quantum numbers are ordered sets of integers,
each of which follow either usual integer addition or @@Z\_N@@ addition rules.

When describing spin quantum numbers (total Sz, say), our convention is to work in units of spin 1/2.
Thus a QN object made as QN("Sz=",+1) means Sz=+0.5 in physics units. The reason for this is that
computers can perform integer arithmetic quickly and exactly. For particle quantum numbers (such as 
total boson or fermion number) integer values have their usual meaning.

QN objects have up to four "slots" which can be assigned values. 
Each slot also has a modulus which can take the following types of values:
* If the modulus is 1, the slot follows regular integer addition. 
* If the modulus is @@N>1@@, the slot obeys @@Z\_N@@ addition. 
* If the modulus is @@-N \leq 1 @@, the slot is fermionic. 
  A fermionic slot follows the same addition rules as a bosonic slot of modulus @@|N|@@;
  the minus sign on the modulus acts only as a "flag" indicating fermionic statistics.
  (As of version 2.x of ITensor we do not use these fermionic flags for any purpose, but have implemented
   them for future experimental automatic fermionic features to be released.)

The QN class recognizes certain conventions about the order and type of slots used. These are implemented by
the QN constructor which takes named arguments. For example, creating a QN as

    auto q = QN("Sz=",+3,"Nf=",5);

results in q having two slots: the first slot `"Sz"` will have a value of 3 and a modulus of 1 (since spin follows
usual integer addition rules); the second slot `"Nf"` has a value of 5 and 
a modulus of -1 (integer addition with a fermionic "flag"). 
Passing the arguments in a different order has the exact same result when using named slots ("Sz", "Nf"),
because the QN system recognizes certain names and keeps them in the right order internally.
QN objects made with named slots are also printed out in a nicer way than "custom" QN objects.

The special types of QN's with named slots are as follows:

* Spin Sz

      auto q1  = QN("Sz=",+1);
      auto q0  = QN("Sz=", 0);
      auto q-2 = QN("Sz=",-2);

* Spinless Boson 

      auto q0 = QN("Nb=",+1);
      auto q1 = QN("Nb=",+2);
      auto q2 = QN("Nb=",+3);

* Spinless Fermion

      auto q0 = QN("Nf=",+1);
      auto q1 = QN("Nf=",+2);
      auto q2 = QN("Nf=",+3);

* Spinful Boson

      auto qup = QN("Sz=",+1,"Nb=",1);
      auto qdn = QN("Sz=",-1,"Nb=",1);
      auto q2  = QN("Sz=", 0,"Nb=",2);

* Spinful Fermion

      auto qup   = QN("Sz=",+1,"Nf=",1);
      auto qdn   = QN("Sz=",-1,"Nf=",1);
      auto qsing = QN("Sz=", 0,"Nf=",2);

* Spinless Fermion Parity

      auto q0 = QN("Pf=",0);
      auto q1 = QN("Pf=",1);


* Spin and Fermion Parity

      auto qup   = QN("Sz=",+1,"Pf=",1);
      auto qdn   = QN("Sz=",-1,"Pf=",1);
      auto qsing = QN("Sz=", 0,"Pf=",0);


QN is defined in the header "itensor/qn.h".

## QN Class Methods

* ```
  QN(Name name1, int val1, 
     Name name2, int val2, ...)
  ``` 

  `QN(Args args)`

  Construct a QN from a set of name-value pairs (trailing spaces and equals signs after the names are ignored). 
  The order of these pairs is not important, as 
  recognized names (Sz,Nb,Nf,Pf) will automatically be put into a fixed order. (Sz is always first 
  if present, followed by one of Nb, Nf, or Pf.)

  The list of name-value pairs can also be passed via an [[Args|classes/args]] object.

  For examples of this constructor, see the special QN types above.


* `QN(QNVal qv1, QNVal qv2, ...)`

  Construct a QN from a set of up to 4 QNVals, which themselves can be constructed from an initializer
  list `{v,m}` where

  * v is an integer value
  * m is an integer modulus

  <div class="example_clicker">Click to Show Example</div>

      //Make QN with first slot having value 0 and modulus 3
      //and second slot having value 2 and modulus 1
      auto qa = QN({0,3},{2,1});

      //Make QN with first slot having value 5 and modulus 1,
      //second slot having value 3 and modulus -1,
      //and third slot having value 1 and modulus 2
      auto qb = QN({5,1},{3,-1},{1,2});

* `QN(int v1, int v2, ...)`

  Make a QN with up to 4 slots, all having modulus 1 (regular integer addition behavior)
  and values v1, v2, etc.

  <div class="example_clicker">Click to Show Example</div>

      auto q0 = QN(0);
      auto q1 = QN(1);

      auto q0_3 = QN(0,3);
      auto q3_4 = QN(3,4);

* `.operator[](size_t n) -> int`

  Retrieve the value of the nth slot; n is 0-indexed.

  <div class="example_clicker">Click to Show Example</div>

      auto q = QN(2,7);
      Print(q[0]); //prints: q[0] = 2
      Print(q[1]); //prints: q[0] = 7

* `.operator()(size_t n) -> int`

  Retrieve the value of the nth slot; n is 1-indexed.

  <div class="example_clicker">Click to Show Example</div>

      auto q = QN(2,7);
      Print(q(1)); //prints: q(1) = 2
      Print(q(2)); //prints: q(2) = 7

* `.mod(size_t n) -> int`

  Retrieve the modulus of the nth slot; n is 1-indexed.

  <div class="example_clicker">Click to Show Example</div>

      auto a = QN(2);
      Print(a.mod(1)); //prints: a.mod(1) = 1

      auto b = QN({1,3},{0,2});
      Print(b.mod(1)); //prints: b.mod(1) = 3
      Print(b.mod(2)); //prints: b.mod(2) = 2

      auto c = QN("Sz=",+1,"Nf=",1);
      Print(c.mod(1)); //prints: c.mod(1) = 1
      Print(c.mod(2)); //prints: c.mod(2) = -1

## Other QN Features

* QN's can be compared with `==` and `!=` and ordered with `<`.

* QN's can be added, subtracted, and negated. <br/>
  Each slot obeys its own addition rule based on its modulus.

* A QN can be multiplied by an Arrow direction (`In` or `Out`) which
  flips the sign of QN's values appropriately. <br/>
  (Currently `In` 
  negates QN values while `Out` leaves them unchanged, but this behavior is
  an arbitrary convention and should not be relied upon in user code).

* QN's can be printed. If a QN conforms to one of the special cases explained 
  above, each slot's name will be printed along with its value. <br/> 
  For custom QN's each slot's value and modulus is explicitly printed.

* QN's can be read from and written to disk using `read(s,q)` and `write(s,q)`
  where s is a stream object and q is a QN.

## QN Value Access Functions

To aid in retrieving special QN slot values according to the special QN types
listed at the top of this page, users may use the following functions.

* `Sz(QN q) -> int`

   Return the value of the spin "Sz" slot of q.

* `Nb(QN q) -> int`

   Return the value of the boson number "Nb" slot of q.

* `Nf(QN q) -> int`

   Return the value of the fermion number "Nf" slot of q.

* `Pf(QN q) -> int`

   Return the value of the fermion parity "Pf" slot of q.

## QN Functions

* `isActive(QN q, int n) -> bool`

   Return `true` if slot n is active (i.e. has a non-zero modulus). <br/>
   n is 1-indexed.

* `isFermionic(QN q, int n) -> bool`

   Return `true` if slot n is fermionic (has negative modulus).<br/>
   n is 1-indexed.

* `paritySign(QN q) -> int`

   Return -1 if the QN has odd fermion parity. Otherwise
   return +1. The parity of a QN is product of the parity
   of each of its sectors. A sector has odd (-1) parity if 
   it is fermionic and has an odd-numbered value.<br/>

* `printFull(QN q)`

  Print the QN to standard out without using any special conventions.<br/>
  Explicitly prints the value and modulus of each active slot.


<br/>
_This page current as of version 2.0.6_
