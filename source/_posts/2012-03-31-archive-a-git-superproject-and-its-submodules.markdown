---
layout: post
title: Archive a Git Superproject and Its Submodules
date: 2012-03-31 19:18
comments: true
categories: [Software Development, Git]
---

While [Git][] is a powerful and popular [Distributed Version Control System][],
Git's [Submodule feature](http://book.git-scm.com/5_submodules.html) and
[Archive feature](http://linux.die.net/man/1/git-archive) make Git even more
powerful. However, the two features seems not working together well: Git's
archive command does not provide a way to archive a Git repository and all of
its submodules (yet). Fortunately, many scripts that could do this for us are
available online, but not all of them work like a charm. After browsing the
Internet and trying them one by one, I found
[this python script][git-archive-all] every useful. It has helped me and I
believe it will also bring you luck.

<!-- more -->

## Install Python If You Don't Have It Installed

_Skip this paragraph if you know you have installed Python_

Since this script is written in [Python][], you need to install python first --
however, probably you don't need to do so, since most Linux distributions have
it installed by default. If you are unsure whether Python is installed on you
computer, run `python --version` in your shell. If you see a version number
printed, that means you have installed Python.

If you haven't installed python, see
[this page](http://wiki.python.org/moin/BeginnersGuide/Download). If you are
working on Windows, there is also a
[video on Youtube](http://youtu.be/4Mf0h3HphEA) teaching you how to install
python on Windows.

## Download git-archive-all and Use It

First, visit [git-archive-all homepage][git-archive-all] and download
[the git-archive-all script](https://github.com/Kentzo/git-archive-all/raw/master/git-archive-all).

### If you are working on a UNIX-like system

Give this file executable bit:

    chmod +x git-archive-all

Then copy this script to one of your directory in the
[PATH environment variable](http://en.wikipedia.org/wiki/PATH_\(variable\))
and switch your working directory to the root directory of your Git repository.
Run the following command to archive the Git repository and its submodules:

    git-archive-all [archive-file-name.format]

If the above command does not work (probably because your Python interpreter
executable is installed somewhere other than `/usr/bin`), try:

    python /path/to/git-archive-all [archive-file-name.format]

For example:

    git-archive-all my-archive.tar.gz

Then a compressed file `my-archive.tar.gz` will appear in your working
directory. You don't need to specify a compression format like the Git's
Archive command -- git-archive-all will decide the format based on the
suffix of your file name, such as [tar.gz][tar], [zip][].

### If you are working on Windows

Copy this script somewhere, launch
[Command Prompt](http://en.wikipedia.org/wiki/Command_Prompt) and switch the
working directory to the root of the Git repository. Then use the following
command to archive the Git repository and its submodules:

    python X:\path\to\git-archive-all [archive-file-name.format]

For example:

    python C:\python_scripts\git-archive-all my-archive.zip

Then a compressed file `my-archive.zip` will appear in your working directory.
You don't need to specify a compression format like the Git's Archive command --
git-archive-all will decide the format based on the suffix of your file name,
such as [tar.gz][tar], [zip][].

## 

The git-archive-all script has some other powerful features. If you are
interested, please visit [its homepage][git-archive-all].


[Distributed Version Control System]: http://en.wikipedia.org/wiki/Distributed_revision_control
[Git]: http://www.git-scm.com
[Python]: http://www.python.org
[git-archive-all]: https://github.com/Kentzo/git-archive-all
[tar]: http://en.wikipedia.org/wiki/Tar_(file_format)
[zip]: http://en.wikipedia.org/wiki/ZIP_(file_format)
