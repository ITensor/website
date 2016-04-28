# Running Your Program in Debug Mode

Compiling a code based on ITensor which is in "debug" mode is easy if you use
the Makefile provided in the `itensor/tutorial/project_template/` folder.

One you set up this Makefile correctly, by editing the fields at the top
then you can compile your program in optimized mode by just typing `make`
and in debug mode by typing `make debug`.

The command `make debug` creates an executable whose name is the usual
name of your program (what you set the `APP` variable to in the Makefile)
but with an extra `-g` appended at the end. So if `APP=myappname` then
doing `make debug` will produce an executable called `myappname-g`.

A program compiled in debug mode differs from an optimized program
in a few key ways:

* A debug-mode program contains many extra checks within ITensor which make sure you
  are using ITensor in the correct ways. For example, the `.real` method
  used to obtain ITensor components will perform bounds checking.

* Debug mode does not optimize your code, so that all of the original functions
  and function names are still used (otherwise the optimizer could inline 
  some functions into others).

* Debug mode inserts various debugging symbols which allow you to use a 
  program such as gdb (on Linux) or lldb (on Mac) to monitor the execution
  of your program and examine the call stack whenever you pause the program
  or when an error occurs.

When you suspect your program contains a bug, often it is helpful to run your
program in debug mode to see if ITensor reports a more helpful error message.
Some checking is disabled in fully optimized ITensor programs for maximum speed.

If ITensor still doesn't report a helpful enough error message, you can run
your debug-mode program in a C++ debugger to get a more fine-grained report
of what state your program was in when it crashed.

