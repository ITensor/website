# Reading and Writing Objects #

## Writing objects to files

* `writeToFile(string filename, T const& obj)`

  Opens a file with the name `filename` and writes the object `obj` to it.
  The type T of the object is deduced automatically.

  This function is defined in the file `itensor/util/readwrite.h`.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index(2,"Site");
      auto j = Index(5,"Link");
      writeToFile("ifile",i);
      writeToFile("jfile",j);

      auto T = randomTensor(i,j);
      writeToFile("Tfile",T);
        
## Reading objects from files

* `readFromFile<T>(string filename) -> T` <br/>

  Opens a file with the name `filename`, read an object of
  type `T`, and return that object.

  This function is defined in the file `itensor/util/readwrite.h`.

  <div class="example_clicker">Click to Show Example</div>

      auto T = readFromFile<ITensor>("tensor_file");
      auto psi = readFromFile<MPS>("wavefunction_file");

      //Initialize MPS with SiteSet "sites" before reading from file:
      auto psi = readFromFile<MPS>("wavefunction_file",sites);

* `readFromFile(string filename, T & obj)`

  Opens a file with the name `filename` and read an object of
  type `T` to the variable `obj`. The type `T` is automatically
  deduced.

  This function is defined in the file `itensor/util/readwrite.h`.

  <div class="example_clicker">Click to Show Example</div>

      ITensor T;
      readFromFile("tensor_file",T);

      MPS psi;
      readFromFile("wavefunction_file",psi);

* `readFromFile<T>(string filename, InitArgs&&... iargs) -> T`

  Opens a file with the name `filename`, read an object of
  type `T`, and return that object.

  This version of the `readFromFile` function takes an arbitrary
  number of additional arguments which are passed to the constructor
  of the type T before reading the object from the file. This can
  be useful for cases where you want to construct the class
  before its .read method is called. A key example is the MPS or IQMPS
  class which can optionally be constructed with a SiteSet before calling
  its .read method to read in its tensors.

  This function is defined in the file `itensor/util/readwrite.h`.

  <div class="example_clicker">Click to Show Example</div>

      //Initialize MPS with SiteSet "sites" before reading from file:
      auto psi = readFromFile<MPS>("wavefunction_file",sites);

