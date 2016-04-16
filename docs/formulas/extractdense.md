# Extract the Storage of a Dense ITensor

Dense ITensors store their data in an object of type `Dense<Real>` or `Dense<Cplx>`. These types 
are basically just a lightweight wrapper around a `std::vector<Real>` or a `std::vector<Cplx>`.

Here is a definition of `Dense<V>` which is equivalent to the one used in ITensor

    template<typename V>
    class Dense
        {
        std::vector<V> store;

        //There are also class methods such as
        //various constructors etc.
        //...
        };

Say we have the following ITensor

    auto i = Index("i",2);
    auto j = Index("j",3);
    auto k = Index("k",4);

    auto T = ITensor(i,j,k);
    randomize(T);

and we want to extract its data, which is stored internally in a `Dense<Real>` object.
There are two ways to do this:
1. Using `applyFunc` to apply a function to T's storage
2. Using the `doTask` system to create functions "dynamically overloaded" on T's storage type

## Using applyFunc

It is simple to extract the data as a `std::vector<Real>` using the function
`applyFunc`, which first extracts the storage type of the ITensor then applies 
the provided function to it:

    auto extractReal = [](Dense<Real> const& d)
        {
        return d.store;
        };

    auto v = applyFunc(extractReal,T.store());

In the code above, `extractReal` is a lambda function that takes a `Dense<Real>` (by const reference
so it does not make a copy) and returns its storage, which is a `std::vector<Real>`. The call to 
`applyFunc` takes `extractReal` as its first argument, and takes T's "storage pointer" `T.store()`
as its second. It performs some magic to unwrap the storage pointer and discover that it is of type `Dense<Real>`
in order to successfully call `extractReal`. If the storage had been of a different type, then `applyFunc`
would throw an exception.

## Using doTask

A more low-level approach to manipulating ITensor storage is to define an overload of `doTask`.
First we need to define "task objects" which label our tasks.

    struct ExtractReal {};
    struct ExtractCplx {};

Next we define our overloads of `doTask`

    std::vector<Real>
    doTask(ExtractReal, Dense<Real> const& d)
        {
        return d.store;
        }

    std::vector<Cplx>
    doTask(ExtractCplx, Dense<Cplx> const& d)
        {
        return d.store;
        }

Finally we call `doTask` on T's storage pointer, which will automatically unwrap its type 
and call the appropriate overload

    //If T has Dense<Real> storage:
    auto v = doTask(ExtractReal{},T.store());

    //If T has Dense<Cplx> storage:
    auto v = doTask(ExtractCplx{},T.store());
