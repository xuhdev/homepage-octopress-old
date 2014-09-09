---
layout: post
title: "Install and Use GNU Command Line Tools on Mac OS X"
date: 2013-04-14T00:32:45
comments: true
external-url: 
categories: [Mac OS X, GNU, Software Development]
---

If you are moving onto Mac OS X from Linux, you would probably find out that
the command line tools shipped with Mac OS X are not as powerful and easy to
use as the tools in Linux. The reason is that Mac OS X uses the BSD version
command line tools, which are different from the Linux version, while they are
both compliant with [POSIX][] standards. But we can easily install the GNU
tools by using [Homebrew][] in Mac OS X and set them as default.

Note: you need to notice that you may have some compatibility issues with shell scripts written specifically for OS X
after you have replaced your OS X commands with the GNU version. Although the very vast majority of shell scripts have
no problem, you just need to be aware that when there comes a problem, this may be the spot to check on.

<!-- more -->

## Install Homebrew

First, visit [Homebrew][] homepage and follow the installation instructions to
install Homebrew.

Shortcut: install the latest [XCode]() and then run the following command to
install:

    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

Then add the following line to your **.bashrc** or **.zshrc**:

    export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"


## Install the GNU Command Line Tools

First comes the most important one -- [GNU Coreutils][]:

    brew install coreutils

GNU Coreutils contains the most essential UNIX commands, such as **ls**,
**cat**.

Then you may probably want to install the following ones (For some of the packages, you need to run `brew tap
homebrew/dupes` first, but only once for your system):

    brew install binutils
    brew install diffutils
    brew install ed --default-names
    brew install findutils --default-names
    brew install gawk
    brew install gnu-indent --default-names
    brew install gnu-sed --default-names
    brew install gnu-tar --default-names
    brew install gnu-which --default-names
    brew install gnutls --default-names
    brew install grep --default-names
    brew install gzip
    brew install screen
    brew install watch
    brew install wdiff --with-gettext
    brew install wget

The `--default-names` option will prevent Homebrew from prepending **g**s to
the newly installed commands, thus we could use these commands as default ones
over the ones shipped by OS X.

Some command line tools already exist on OS X, but you may wanna a newer version:

    brew install bash
    brew install emacs
    brew install gdb  # gdb requires further actions to make it work. See `brew info gdb`.
    brew install gpatch
    brew install m4
    brew install make
    brew install nano

As a complementary set of packages, the following ones are not from GNU, but you can install and use a newer version
instead of the version shipped by OS X:

    brew install file-formula
    brew install git
    brew install less
    brew install openssh --with-brewed-openssl
    brew install perl518   # must run "brew tap homebrew/versions" first!
    brew install python --with-brewed-openssl
    brew install rsync
    brew install svn
    brew install unzip
    brew install vim --override-system-vi
    brew install macvim --override-system-vim --custom-system-icons
    brew install zsh

Now you should have an easier command line system in your OS X. Have fun with
them!

**Update**: You may also want to add `$HOMEBREW_PREFIX/opt/coreutils/libexec/gnuman` to the `MANPATH` environmental
variable, where `$HOMEBREW_PREFIX` is the prefix of Homebrew, which is `/usr/local` by default. (Thanks Matthew Walker!)
Alternatively, there is also a one-line setup which you could put in your shell configuration files
[here](https://gist.github.com/quickshiftin/9130153) by quickshiftin.



[GNU Coreutils]: http://en.wikipedia.org/wiki/GNU_Core_Utilities
[Homebrew]: http://brew.sh
[POSIX]: http://en.wikipedia.org/wiki/POSIX
[XCode]: https://developer.apple.com/xcode/
