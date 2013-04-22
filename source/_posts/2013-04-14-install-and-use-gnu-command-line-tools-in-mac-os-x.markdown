---
layout: post
title: "Install and Use GNU Command Line Tools in Mac OS X"
date: 2013-04-14T00:32:45-07:00
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

<!-- more -->

## Install Homebrew

First, visit [Homebrew][] homepage and follow the installation instructions to
install Homebrew.

Shortcut: install the latest [XCode]() and then run the following command to
install:

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

Then add the following line to your **.bashrc** or **.zshrc**:

    export PATH="$(brew --prefix coreutils)/libexec/gnubin:/usr/local/bin:$PATH"

## Install the GNU Command Line Tools

First comes the most important one -- [GNU Coreutils][]:

    brew install coreutils

GNU Coreutils contains the most essential UNIX commands, such as **ls**,
**cat**.

Then you may probably want to install the following ones:

    brew install findutils --default-names
    brew install gnu-indent --default-names
    brew install gnu-sed --default-names
    brew install gnutls --default-names
    brew install grep --default-names
    brew install tar --default-names
    brew install gawk
    brew install screen
    brew install wget

The `--default-names` option will prevent Homebrew from prepending **g**s to
the newly installed commands, thus we could use these commands as default ones
over the ones shipped by OS X.

Now you should have an easier command line system in your OS X. Have fun with
them!





[GNU Coreutils]: http://en.wikipedia.org/wiki/GNU_Core_Utilities
[Homebrew]: http://brew.sh
[POSIX]: http://en.wikipedia.org/wiki/POSIX
[XCode]: https://developer.apple.com/xcode/
