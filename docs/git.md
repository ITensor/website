# Git Quick Start Guide

[Git](http://git-scm.com) is a version control system useful for synchronizing source code across multiple machines.
Although it has many powerful features, you only need a few commands to get started.

## Cloning Git Repositories

In Git terminology, multiple versions of a code project are stored in a database called a repository or a "repo".
Cloning a repo means making a copy of the source code onto your system (including the database files storing all 
previous versions of the software).

To clone the [ITensor repo](http://github.com/ITensor/ITensor) from Github (a website which stores and provides access to various repos), issue
the following command on your computer:

    git clone git@github.com:ITensor/ITensor.git itensor

The last argument is the name of the folder you want git to put the ITensor source code into.
You can choose any name you like for this folder, or rename it later without causing any problems.


## Updating Code Which is Linked to a Git Repository

To get the latest version of source code you originally obtained via the `git clone` command, simply `cd` to 
the folder containing your copy of the repo and issue the command:

    git pull

Assuming you have not modified the code, this command should successfully pull down the latest version from Github.

To confirm that you have the version you want, you can use the `git log` command or use a [Git GUI program](http://git-scm.com/downloads/guis)
to view the local state of your repo.

If you have modified the code and are ok with undoing your changes in order to obtain the latest version, issue 
the command:

    git reset --hard

<span style="color:red;">Warning</span>: the above command will undo all unsaved (uncommitted) changes to tracked files in your local copy of the repo.


## Forking a Repo

If you wish to make changes to the ITensor source code, say to maintain your own modified version or to contribute to ITensor development,
you should create a "fork" of the ITensor repo.

To do this, first obtain an account on [Github](http://github.com) and log into this account.

Then, visit the ITensor repo page [http://github.com/ITensor/ITensor](http://github.com/ITensor/ITensor) and click the large gray "Fork" button
at the upper right. This will create a copy of the ITensor repo that belongs to you.

You can now clone this repo to your personal computer(s) and edit it at will. If you make commits and push them back to Github, you can 
issue "Pull Requests" which ask the ITensor developers to pull your changes into the main ITensor repo. For detailed information about pull requests,
visit this [Github help page on this topic](https://help.github.com/articles/using-pull-requests).

## Basic Git Workflow

When you change files in a Git repo, you can type the command

    git status

from anywhere inside the repo folder to see a list of which tracked files have been modified.

Saving changes you have made (making a "commit") and sending them to a remote repo, 
say on Github, proceeds in three steps. (This is in contrast to Subversion,
in which one typically does this all in one step.)

First you must add the changes you want to commit. To do so, issue the command:

    git add <filename>

for each file whose changes you want to include in the commit. You can use `git status` to see which files have been added.
Any files added this way are said to be "staged". 

Once all desired changes have been staged, issue the command:

    git commit -m "<message>"

which will create the commit and tag it with a message describing the changes. If you leave off the <br/> `-m "<message>"` part of the
command, git will open your default text editor to allow you to enter a message.

You can (and should) make multiple small commits this way even when you are not connected to the Internet.

Finally, after making commits, to push them to your remote repo (for example, your personal Github fork of ITensor),
issue the command:

    git push

to send all commits not already on the remote server.

For help with more advanced Git features, there are numerous articles online which can be found through your favorite search engine.


[[Back to Main|main]]
