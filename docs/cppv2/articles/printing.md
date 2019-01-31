<span class='article_title'>How to print quantities in ITensor</span>

<span class='article_sig'>Thomas E. Baker&mdash;August 18, 2015</span>

ITensor provides several methods for printing data to the terminal or files.  We give a list of them here.

## Printing to the terminal

 - `print("something")` prints something to the terminal
 - `println("something")` prints something to the terminal with a new line following it
 - `printf("A number with %.12f digits",num)` prints a number with 12 digit accuracy
 - `printf("An integer %.d",integer)` prints an integer

`printf` is a well-known C printing function and the format strings have been [[standardized|http://www.cplusplus.com/reference/cstdio/printf/]]. The actual ITensor implementation is just a wrapper around a free library called [["tinyformat"|https://github.com/c42f/tinyformat]]. The main difference is that tinyformat is type safe, unlike the C printf. One other key point about tinyformat is that they recommed using %s as a default format specifier unless you specifically need another specifier (such as %f for floating point). 

 - `printfln` prints a number and then a new line

If you print an ITensor or IQTensor with the %f formatting specifier it will show all the tensor data, whereas %s will only show the indices.

## To a file

See [[Reading and Writing MPS or MPO To/From Disk|recipes/readwrite_mps]].

## During a DMRG calculation

See [[code sample|articles/samples]] for an introduction to the `dmrg` observer. 
## C++ Defaults

While ITensor provides special functions for printing, the standard functions in C++ can be used (such as [[cout|http://www.cplusplus.com/reference/ios/ios_base/precision/]]).

