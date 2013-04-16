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

### [nautilus-py-vim][]

A [nautilus][] extension aimed at helping start editing with Vim fast and
conveniently on GNOME.

nautilus-py-vim is an extension for nautilus, the GNOME file manager, and is
written in python. This extension adds several menu items in the nautilus
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

## Donate

I would appreciate it if you would like to support my projects by donating on
[GitTip][].



[Backup On The Go]: https://github.com/xuhdev/backup-on-the-go#readme
[CmdLauncher]: http://cmdlauncher.nongnu.org
[EditorConfig]: http://editorconfig.org
[G95 Fortran Compiler]: http://www.g95.org
[GNU Fortran Compiler]: http://gcc.gnu.org/wiki/GFortran
[GitTip]: https://www.gittip.com/xuhdev/
[Heroku]: https://www.heroku.com/
[IniParser]: http://www.vim.org/scripts/script.php?script_id=3434
[Intel Fortran Compiler]: http://software.intel.com/en-us/articles/intel-compilers
[SQLite]: http://www.sqlite.org
[SingleCompile]: http://www.topbug.net/SingleCompile
[Vim]: http://www.vim.org
[compiler/g95.vim]: http://www.vim.org/scripts/script.php?script_id=3492
[compiler/gfortran.vim]: http://www.vim.org/scripts/script.php?script_id=3496
[compiler/ifort.vim]: http://www.vim.org/scripts/script.php?script_id=3497
[ctags]: http://ctags.sf.net
[gccxml]: http://www.gccxml.org
[indent/java.vim]: http://www.vim.org/scripts/script.php?script_id=3899
[ini]: http://en.wikipedia.org/wiki/INI_file
[nautilus-py-vim]: http://xuhdev.bitbucket.org/nautilus-py-vim/nautilus-py-vim.html
[nautilus]: http://live.gnome.org/Nautilus
[syntax/dosini.vim]: http://www.vim.org/scripts/script.php?script_id=3747
[tags2db]: http://www.topbug.net/tags2db
[vimscript]: http://en.wikipedia.org/wiki/Vim_script
