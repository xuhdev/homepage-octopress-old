---
layout: post
title: "Back up (Migrate) Homebrew Packages"
date: 2013-12-07T22:59:52+00:00
comments: true
external-url: 
categories: [Homebrew, OS X]
---

As one of the most popular package manager on OS X, [Homebrew][] is indeed a very nice tool to manage packages. However,
when you want to back up your packages, or migrate the packages onto another machine, Homebrew didn't invent such a
tool. If you are moving to an OS X of the same version, you can simply copy the Homebrew directory (default is
`/usr/local`) to your new machine. Otherwise, we need to find a way to install the exactly same packages on your new
machine. In order to accomplish the goal, I wrote a small piece of bash script to generate a restore script to install
the packages.

<!-- more -->

## The Backup (Migration) Script

The script itself is quite short:

```sh backup-homebrew.sh https://gist.github.com/xuhdev/7854010
#!/bin/bash
 
echo '#!/bin/bash'
echo ''
echo 'failed_items=""'
echo 'function install_package() {'
echo 'echo EXECUTING: brew install $1 $2'
echo 'brew install $1 $2'
echo '[ $? -ne 0 ] && $failed_items="$failed_items $1" # package failed to install.'
echo '}'
 
brew tap | while read tap; do echo "brew tap $tap"; done
 
brew list | while read item;
do
echo "install_package $item '$(brew info $item | /usr/bin/grep 'Built from source with:' | /usr/bin/sed 's/^[ \t]*Built from source with:/ /g; s/\,/ /g')'"
done
 
echo '[ ! -z $failed_items ] && echo The following items were failed to install: && echo $failed_items'
```

For those impatient readers, you could simply download the script, and execute

    bash backup-homebrew.sh >restore-homebrew.sh && chmod +x restore-homebrew.sh

Then you should have something similar to the following in your `restore-homebrew.sh`:

```sh restore-homebrew.sh
#!/bin/bash

failed_items=""
function install_package() {
echo EXECUTING: brew install $1 $2
brew install $1 $2
[ $? -ne 0 ] && $failed_items="$failed_items $1"  # package failed to install.
}
brew tap homebrew/dupes
brew tap homebrew/games
brew tap homebrew/science
brew tap homebrew/versions
brew tap josegonzalez/php
install_package ant ''
install_package apple-gcc42 ''
install_package armadillo ''
install_package atk ''
install_package autoconf ''
install_package autoconf213 ''
install_package autojump ''
install_package automake ''
install_package bash ''
...
```

Copy `restore-homebrew.sh` to your new machine, install Homebrew and then execute this script.

## What does the script do?

The script `backup-homebrew.sh` first defines `install_package` in the restore script, which is used to install packages
and maintain the list of packages which are failed to install. Then, it uses `brew taps` to list all the [taps][] you
have and generate the corresponding script to tap those taps. Next, it uses `brew list` to obtain all the packages you
have and uses `brew info` to get the options you used to install a package. For each package, it generates one line
which uses `install_package` function to install the package with the options. Finally, it generates the line which
lists the packages that are failed to install.


[Homebrew]: http://brew.sh
[taps]: https://github.com/mxcl/homebrew/wiki/brew-tap
