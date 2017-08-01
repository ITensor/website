# Reading and Writing Objects to Disk #


* `writeToFile(string filename, T const& obj)`

  Opens a file with the name `filename` and writes the object `obj` to it.
  The type T of the object is deduced automatically.

  This function is defined in the file `itensor/global.h`.

  <div class="example_clicker">Click to Show Example</div>

      auto i = Index("index_i",2,Site);
      auto j = Index("index_j",5,Link);
      writeToFile("ifile",i);
      writeToFile("jfile",j);

      auto T = randomTensor(i,j);
      writeToFile("Tfile",T);
        

* `readFromFile<T>(string filename) -> T`

  Opens a file with the name `filename`, read an object of
  type `T`, and return that object.

  This function is defined in the file `itensor/global.h`.

  <div class="example_clicker">Click to Show Example</div>

      auto T = readFromFile<ITensor>("tensor_file");
      auto psi = readFromFile<MPS>("wavefunction_file");

* `readFromFile(string filename, T & obj)`

  Opens a file with the name `filename` and read an object of
  type `T` to the variable `obj`. The type `T` is automatically
  deduced.

  This function is defined in the file `itensor/global.h`.

  <div class="example_clicker">Click to Show Example</div>

      ITensor T;
      readFromFile("tensor_file",T);

      MPS psi;
      readFromFile("wavefunction_file",psi);
