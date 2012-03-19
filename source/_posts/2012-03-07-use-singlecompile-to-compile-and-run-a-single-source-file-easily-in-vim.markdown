---
layout: post
title: "Use SingleCompile to Compile and Run a Single Source File Easily in Vim"
date: 2012-03-07 21:08
comments: true
file_title: 2012-03-07-use-singlecompile-to-compile-and-run-a-single-source-file-easily-in-vim
categories: [Vim, Development, Editor]
---

{% include custom/post_initialization.html %}

Although [Vim][] itself has already been a very powerful text editor, its
plugins make it even better. [SingleCompile][] is a plugin aimed at making it
more convenient to compile or run a single source file without leaving Vim.

Consider this situation: you've just written a small C file (or small python
script) with Vim for some tiny test, then you need to use `:!gcc %:p` to compile
the C source file and run the executable with `:!./a.out` command (Or use
`:!python %:p` to run the python script). Although a key mapping could make
this process a bit convenient, but many of Vim's advanced features will become
unavailable, such as [quickfix][], [compiler feature][].  [SingleCompile][]
was born to solve this problem, making this process more convenient and
powerful than simply defining a few key mappings:

-  Compile or run the source file quickly using [quickfix feature][quickfix]
   and [compiler feature][] of vim;
-  Auto detecting compilers and interpreters;
-  Fast switch between several installed compilers or interpreters;
-  Multi-language support;
-  Custom your own compiler/interpreter template;
-  View the result of last run command at any time(requires `tee` command);
-  Run the compiled program asynchronously and view the result at any time
   (see `:SCCompileRunAsync` in the help file).

Let's see more about SingleCompile.

<!-- more -->

### Installation

Just like most other Vim plugins, it's simple: Download the SingleCompile.zip
file from [SingleCompile homepage][SingleCompile] and extract it to your Vim
runtime directory(`~/.vim` on UNIX/Linux or
`$VIM_INSTALLATION_FOLDER\vimfiles` on windows). Execute `:helptags
~/.vim/doc` on UNIX/Linux or `:helptags $VIM_INSTALLATION_FOLDER\vimfiles\doc`
on Windows if you need to check the SingleCompile documentation. If you are
using [pathogen][] to manage your Vim plugins, use the following commands to
install it (on UNIX/Linux):

```sh
cd ~/.vim/bundle
git clone git://github.com/xuhdev/SingleCompile.git
```

The following key mappings should be very helpful for you. Insert them into
your `.vimrc` file if you think it useful:

```vim
nmap <F9> :SCCompile<cr>
nmap <F10> :SCCompileRun<cr>
```

The above two lines will make `F9` as the key to trigger the compilation and
`F10` to compile the source file and run.


### Use SingleCompile to Compile and Run a Source File

Let's try to create a new C source file called `hello.c`:

    vim hello.c

Copy the following content into the buffer:

```c hello.c
#include <stdio.h>

int main(void)
{
    printf("Hello, SingleCompile!\n");
    return 0;
}
```

Now execute `:SCCompileRun` (or press `F10` if you have set the key mapping
above). Then SingleCompile will automatically find a C compiler available on
your system (e.g. gcc on my Linux) and use this compiler to compile your
source file and run the executable file. The output should be displayed on
your screen then:

![]({{ post_file_url }}/1.png)

What if you want to check the result again after you press any key and the
output is dismissed? Simple, use `:SCViewResult` command to get it back:

![]({{ post_file_url }}/2.png)

If you have multiple compilers installed on your system, use `:SCChooseCompiler`
command to switch the compiler you want to use:

![]({{ post_file_url }}/3.png)

Let's try to add some syntax errors into the source file. Change the buffer
into the following:

```c hello.c
#include <stdio.h>

int main(void)
{
    printf("Hello, SingleCompile!\n");
    retur 0; /* a typo is here: the "return" loses its "n" */
}
```

Execute `:SCCompileRun` (or press `F10` if you have set the key mapping above),
then you will see some compilation errors displayed on the screen:

![]({{ post_file_url }}/4.png)

Press any key to dismiss the error messages. Now let's open the Vim
[quickfix][] window by executing `:cope`:

![]({{ post_file_url }}/5.png)

See? The error messages has been put in the Vim quickfix window, which makes
it quite easy to locate syntax errors!


### Interpreting Languages

For interpreting languages such as python, perl, things are similar:
interpreter auto detection, Quickfix, etc. But there is one notable difference:
`:SCCompile` and `:SCCompileRun` do the same job for such kind of languages --
they both call the interpreter to run your script, since there is no
compilation required for such langauges.


### More

SingleCompile is far more powerful than this. Execute `:h SingleCompile` within
Vim to see SingleCompile documentation if you want to know more about
SingleCompile.

[Vim]: http://www.vim.org
[SingleCompile]: http://www.vim.org/scripts/script.php?script_id=3115
[quickfix]: http://vimdoc.sourceforge.net/htmldoc/quickfix.html
[compiler feature]: http://vimdoc.sourceforge.net/htmldoc/quickfix.html#compiler-select
[pathogen]: https://github.com/tpope/vim-pathogen
