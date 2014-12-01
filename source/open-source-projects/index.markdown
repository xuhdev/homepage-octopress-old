---
layout: page
title: My Open Source Projects
footer: false
comments: false
sidebar: false
---

## EditorConfig

[EditorConfig][] helps developers define and maintain consistent coding styles
between different editors and IDEs. The EditorConfig project consists of **a
file format** for defining coding styles and a collection of **text editor
plugins** that enable editors to read the file format and adhere to defined
styles.  EditorConfig files are easily readibly and they work nicely with
version control systems.

Visit [EditorConfig project page][EditorConfig] to know more about it.

## Backup On The Go

[Backup On The Go][] is a tool written in Ruby, which backs up (or mirror) your
GitHub repositories to BitBucket in the cloud. You could deploy it on
[Heroku][],  and it will automatically mirror your GitHub repositories to
BitBucket periodically.

## Quine-McCluskey minimizer

[Quine-McCluskey minimizer][] is a [Quine-McCluskey algorithm][] implementation
library modified from
[Stefan Moebius' command line only version](http://sourceforge.net/projects/mini-qmc).
It is modified to be used as a library. Also additional compatibility fixes and
documents are added.

## Vim Related Projects

[Vim][] is a highly configurable text editor built to enable efficient text
editing. It is an improved version of the vi editor distributed with most UNIX
systems. This page contains some of my projects related to Vim.


### [SingleCompile][]

A Vim plugin which makes it more convenient to compile or run a single source
file.

### [IniParser][]

This is a Vim plugin providing a set of functions to read and write [ini][]
format files for [vimscript][].

### [indent/java.vim][]

This is a Vim indent file for java source files. This indent file is based
on the java indent file maintained by Toby Allsopp, which was shipped
with the official Vim distribution before Vim version 7.3.408.

This script has been included in the official Vim distribution since
Vim version 7.3.409.

### [syntax/dosini.vim][]

Vim syntax file for dosini files (\*.ini).

This script has been included in the offical Vim distribution since Vim version
7.3.313.

### [Nautilus-Edit-with-Vim][]

A [Nautilus][] extension aimed at helping start editing with Vim fast and
conveniently on GNOME.

Nautilus-Edit-with-Vim is an extension for Nautilus, the GNOME file manager, and is
written in python. This extension adds several menu items in the Nautilus
right-click context menu for gvim, such as "Edit with gVim", etc, just like
gVim on Windows.

### [compiler/gfortran.vim][]

Vim compiler file for [GNU Fortran Compiler][].

This script has been included in the offical Vim distribution since Vim version
7.3.152.

### [compiler/ifort.vim][]

Vim compiler file for [Intel Fortran Compiler][].

This script has been included in the offical Vim distribution since Vim version
7.3.152.

### [compiler/g95.vim][]

Vim compiler file for [G95 Fortran Compiler][].

This script has been included in the offical Vim distribution since Vim version
7.3.152.

## tags2db

[Tags2db][tags2db] is a command line tool that convert tags files (ctags, gccxml,
etc.) to databases (sqlite, etc.).

Tags2db is a program that converts tags files ([ctags][], [gccxml][], etc.) to
database tables ([SQLite][], etc.). Currently only ctags, gccxml and SQLite
are supported. Other tags files such as etags, and other databases such as
MySQL will be supported in the future.

## CmdLauncher

[CmdLauncher][] helps people use command line tools in a graphical environment.

This project is aimed at helping people launch a command in a graphical way.
Command line tools are powerful, but some people, especially those who are not
computer experts, are unwilling to use command line tools because they need to
memorize many things to type a command. But CmdLauncher provide a simple way
for developers to make their console programs launch by selecting one from the
list, or choosing a file, or something else which could be done easily by
people who are not experts. What the command line program developers need to do
is to write a simple ini format file containing information of their command
line programs, which will be read by CmdLauncher.

## Minor Contributions

I've made minor contributions to a number of projects.

- [el-get][]
- [git-archive-all][]
- [Homebrew][]
- [Octopress][]
- [Octopress-Theme-Slash][]
- [oh-my-zsh][] [web-search plugin](https://github.com/robbyrussell/oh-my-zsh/commit/25313814775c08c64dc541fbadceb38c669c541a#diff-68cf51b8a790287ea23ff40ecb6632cb)
- [Vim][] patches
[7.3.063](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.063)
[7.3.079](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.079)
[7.3.094](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.094)
[7.3.113](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.113)
[7.3.115](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.115)
[7.3.174](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.174)
[7.3.191](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.191)
[7.3.234](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.234)
[7.3.293](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.293)
[7.3.493](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.493)
[7.3.844](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.844)
[7.3.845](ftp://ftp.vim.org/pub/vim/patches/7.3/7.3.845)
- [zsh][] patches
[31462](http://www.zsh.org/mla/workers/2013/msg00509.html)
[32064](http://www.zsh.org/mla/workers//2013/msg01094.html)
[32069](http://www.zsh.org/mla/workers/2013/msg01099.html)
[32428](http://www.zsh.org/mla/workers//2014/msg00218.html)
- [zsh-completion][]

## Donate

I would appreciate it if you would like to support my projects and blog by donating via BitCoins:

<a class="coinbase-button" data-code="112e87a7b41c6fc00222a0fc62e56feb" data-button-style="donation_large" href="https://coinbase.com/checkouts/112e87a7b41c6fc00222a0fc62e56feb">Donate Bitcoins</a><script src="https://coinbase.com/assets/button.js" type="text/javascript"></script>

[Backup On The Go]: https://github.com/xuhdev/backup-on-the-go#readme
[CmdLauncher]: http://cmdlauncher.nongnu.org
[EditorConfig]: http://editorconfig.org
[G95 Fortran Compiler]: http://www.g95.org
[GNU Fortran Compiler]: http://gcc.gnu.org/wiki/GFortran
[Heroku]: https://www.heroku.com
[Homebrew]: http://brew.sh
[IniParser]: http://www.vim.org/scripts/script.php?script_id=3434
[Intel Fortran Compiler]: http://software.intel.com/en-us/articles/intel-compilers
[Octopress]: http://octopress.org
[Octopress-Theme-Slash]: http://tommy351.github.io/Octopress-Theme-Slash
[Quine-McCluskey algorithm]: https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm
[Quine-McCluskey minimizer]: https://github.com/xuhdev/Quine-McCluskey-minimizer#readme
[SQLite]: http://www.sqlite.org
[SingleCompile]: http://singlecompile.topbug.net
[Vim]: http://www.vim.org
[compiler/g95.vim]: http://www.vim.org/scripts/script.php?script_id=3492
[compiler/gfortran.vim]: http://www.vim.org/scripts/script.php?script_id=3496
[compiler/ifort.vim]: http://www.vim.org/scripts/script.php?script_id=3497
[ctags]: http://ctags.sf.net
[el-get]: https://github.com/dimitri/el-get
[gccxml]: http://www.gccxml.org
[git-archive-all]: https://github.com/Kentzo/git-archive-all
[indent/java.vim]: http://www.vim.org/scripts/script.php?script_id=3899
[ini]: http://en.wikipedia.org/wiki/INI_file
[Nautilus-Edit-with-Vim]: http://nautilusvim.topbug.net
[Nautilus]: http://live.gnome.org/Nautilus
[oh-my-zsh]: https://github.com/robbyrussell/oh-my-zsh
[syntax/dosini.vim]: http://www.vim.org/scripts/script.php?script_id=3747
[tags2db]: http://www.topbug.net/tags2db
[vimscript]: http://en.wikipedia.org/wiki/Vim_script
[zsh]: http://www.zsh.org
[zsh-completion]: https://github.com/zsh-users/zsh-completions
