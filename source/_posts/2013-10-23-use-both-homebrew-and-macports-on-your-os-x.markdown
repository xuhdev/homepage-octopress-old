---
layout: post
title: "Use Both Homebrew and Macports on Your OS X"
date: 2013-10-23T15:21:24
comments: true
external-url: 
categories: [OS X, Homebrew, Macports]
---

[Homebrew][] and [Macports][] are two excellent package managers on OS X. At most of the time, Homebrew is fair enough:
it has a large package collections. But sometimes, there are just some packages not available in Homebrew while they are
in Macports. Although having both of them installed is not recommended, I still want to give it a try.

The basic rules here are using Homebrew packages as much as possible. When one package is not available in Homebrew,
install it from Macports (you will soon see why). We will wrap the executables installed by Macports with suitable
Environmental Variables.

<!-- more -->

## Install Homebrew and Macports

Following the installation instructions on their websites ([Homebrew][] and
[Macports](http://www.macports.org/install.php)) to install both of them. But remember not to modify environmental
variables related to Macports, such as `PATH`, `DYLD_LIBRARY_PATH`.

## Wrap Macports Executables with Appropriate Environmental Variables When You Use them

Before running any executables, we need to prepend `$MACPORTS_PREFIX/bin:$MACPORTS_PREFIX/sbin` to the `PATH`
environmental variable, `$MACPORTS_PREFIX/lib` to the `DYLD_LIBRARY_PATH` environmental variable, etc. where
`$MACPORTS_PREFIX` is the installation prefix of Macports (by default it is `/opt/local`. To do this, I wrote
a wrapper script:

```sh use_macports.sh https://gist.github.com/xuhdev/7127799
#!/bin/sh
 
## Wrap Macports command (any executables installed by Macports).
 
if [ "$#" -le 0 ]; then
  echo "Usage: $0 command [arg1, arg2, ...]" >&2
  exit 1
fi
 
if [[ -z $MACPORTS_PREFIX ]]; then
  MACPORTS_PREFIX='/opt/local'
fi
 
 
export PATH="$MACPORTS_PREFIX/bin:$MACPORTS_PREFIX/sbin:$PATH"
export DYLD_LIBRARY_PATH="$MACPORTS_PREFIX/lib:$DYLD_LIBRARY_PATH"
export CPATH="$MACPORTS_PREFIX/include:$CPATH"
 
command=$1
 
shift
 
exec $command $*
```

Copy this script to any directory in your `PATH` environmental variable. Then, to wrap any executables installed by
Macports, just run:

    use_macports.sh executable args1 args2 ...

For example, you need to run `port` command to install `texlive`:

    use_macports.sh port install texlive

For convenience, if you want to run `port` (or any other executables installed from MacPorts, e.g. `pdflatex` if texlive
is installed from MacPorts) directly without the lengthy command above, you can wrap frequently used commands into
scripts. For example, assuming `~/bin` is in your `PATH` environmental variable:

    echo 'exec use_macports.sh port $*' >~/bin/port
    chmod +x ~/bin/port

Executing the above line will give you a new "port" command which is actually a wrapper. So now you see, although it's
not a big deal, Macports packages require more energy to set up. That's why I try to use Homebrew if the package is
available there.

## When Using Homebrew to Install Packages ...

When using Homebrew to install packages, one noticeable thing is that sometimes `/opt/local` may interference the build
of the packages. In this case, you might want to try to run `brew install --env=std package_name` and `brew install
--env=super package_name` to see whether the build works, or you even need to rename `/opt/local` temporarily.

## Myself

I've used Macports to install evince and texlive, and there is no problem to use this method by far. If you have any
problems or concerns please feel free to comment.

_Update:_ There is now a known issue when using [kpsewhich][] with this method. It seems that kpsewhich cannot detect
its parameters correctly using this method.

[Homebrew]: http://brew.sh
[Macports]: http://macports.org
[kpsewhich]: http://texblog.net/hypertext-help/latex-tools/kpsewhich/
