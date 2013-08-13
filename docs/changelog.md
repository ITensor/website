# Change Log #

* Version 0.2.0 (in progress)

  - Model classes now use strings for retrieving operators and site states (the latter are objects of type IQIndexVal).

  - IQTensor storage (class IQTDat) no longer holds a separate map of iterators to the ITensor blocks. Instead blocks are
    stored in a std::vector and found, when necessary, using a linear search. Testing indicates slight gain in speed if
    anything. Has the advantage of removing `mutable` modifier from IQTDat storage and simplifying IQTensor/IQTDat.

  - Major work on imagTEvol method. More stable to larger time steps and a wider variety of starting states.

  - Renamed IQTensor::iten_empty() to just IQTensor::empty().

  - Removed IQTensor::iten_size() method. For an IQTensor T, just use T.blocks().size() instead.

* [Version 0.1.0](https://github.com/ITensor/library/tree/v0.1.0) (July 16, 2013)

  - First numbered version.

  - Recently implemented new implementation of complex ITensors and IQTensors. 
    ITensors store an (initially null) pointer to their
    imaginary part. The imaginary part is allocated only if it is non-zero.



