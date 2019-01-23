
## Version 2.x to 3.0 Transition Guide

Below are the major interface changes in ITensor version 3.0 versus 2.x.

### Changes to Basic Interface

* The IQTensor class has been merged into the ITensor class. Similarly,
  IQIndex has been merged into the Index class, IQMPS has been merged into MPS, etc.

* An Index no longer has a name or IndexType. Instead, it has a set of Tags (stored as a
  TagSet), which are a set of small strings used to identify a specific Index of an ITensor.

* TODO

