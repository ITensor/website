# Creating Your Own Driver Code

Driver code means code containing a "main" function that will be compiled into an executable you can run.
Typically for a program called "myappname" the main function appears in a file called "myappname.cc".
(ITensor uses the convention that C++ source code files have the extension .cc, but other common conventions include
.cpp or .C.)

For convenience, ITensor includes a project template folder ready for you to use. To use it, follow these steps:

1. Assuming the ITensor source code is located in `/home/username/itensor` (where `username` is your actual username), and
assuming you want to create your new project under `/home/username/software`, issue the commands:

       mkdir -p /home/username/software 
       cp -r /home/username/itensor/tutorial/project_template \
             /home/username/software/myproject

    Here you will want to choose `myproject` to be the actual name of your program.

2. Go to the `/home/username/software/myappname` folder. Edit the `Makefile` there. Make sure `LIBRARY_DIR` is
set to the actual location of the ITensor source code on your computer.

3. Test your configuration by issuing the command `make`. This should build the `myappname` sample program, which you
can run by typing `./myappname`.

4. Finally, when changing `myappname.cc` to some other program name, make sure to also update the `APP` variable in the file
`Makefile` used by the `make` program. The `myclass.h` and `myclass.cc` files are included to show how to create helper
classes for your program to use. If you rename or remove these, make sure to edit the `Makefile` appropriately. Also you will 
need to modify or remove the line `#include "myclass.h"` inside of `myappname.cc`.
