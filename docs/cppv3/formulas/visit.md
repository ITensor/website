# Evaluate a Function on Each Element of a Tensor

ITensors provide a method `.visit(f)`. When you 
provide a function f, the visit method will loop over 
the tensor data and plug each element of the tensor into f.

Here are some examples:

## Printing Each Element of a Tensor

    auto T = ITensor(i,j,k);
    randomize(T);

    //Here doPrint is a "lambda" function
    auto doPrint = [](Real x) { println(x); };

    T.visit(doPrint);

## Computing the Max Element of a Tensor

    auto T = ITensor(i,j,k);
    T.randomize();

    Real maxEl = -1E12;
    //getMax is a lambda function with a "capture"
    auto getMax = [&maxEl](Real x) { if(x > maxEl) maxEl = x; };

    T.visit(getMax);

    Print(maxEl);
