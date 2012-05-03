---
layout: post
title: Generate Ctags Files for C/C++ Source Files and All of Their Included Header Files
date: 2012-03-17 14:29
comments: true
categories: [Software Development, ctags, C, C++, C/C++, editor, IDE, Vim]
---

_This post is for those people who use [Exuberant Ctags][ctags]. If you are
using
[other versions of ctags](http://en.wikipedia.org/wiki/Ctags#Variants_of_ctags),
this post may not be useful._

When using [ctags][] to generate the tags file for C/C++ projects, usually we
use the following command:

    ctags -R .

For some users that need more info of the symbols, they may use this command
instead:

    ctags –R --c++-kinds=+p --fields=+iaS --extra=+q .

No matter which one you use, the generated tags file only contains the symbols
in the files in your project source tree, but not any external file, such as
standard header files (e.g. stdio.h, stdlib.h), etc. thus editors or IDEs that
use tags files, such as [Vim][], are not able to locate symbols in external
header files. There was a solution: generate a tags file for any external header
files first, and let the editor or IDE read both the generated tags file and the
tags file for the project source tree. For example, the following command will
generate a tags file for all your system header files on UNIX/Linux:

    ctags –R --c++-kinds=+p --fields=+iaS --extra=+q /usr/include

This command usually takes a very long time to finish, and finally it gives a
quite large tags file, which causes the editor or IDE a long time to search this
tags file for symbols. To solve this problem, I came up with another idea.

Why must we generate a tags file containing all the symbols in the system
header? If we only generate the tags file only for the header files that are
related to our projects, would it be faster? That's the point of this idea. We
could first search for the header files that are included in our projects, and
then we use ctags to generate a tags file for these files and our source files,
in this way, a much smaller tags file that containing all the symbols that maybe
useful for the project is generated.

<!-- more -->

To do this, I wrote a shell script:

{% codeblock lang:sh ctags_with_dep.sh https://gist.github.com/raw/1729992/4eae76f78ba44d5fd0e705d51b0ededbeb0a7a6a/ctags_with_dep.sh Download the script %}
#!/bin/sh

# ./ctags_with_dep.sh file1.c file2.c ... to generate a tags file for these files.

gcc -M $* | sed -e 's/[\\ ]/\n/g' | \
        sed -e '/^$/d' -e '/\.o:[ \t]*$/d' | \
        ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
{% endcodeblock %}

This script is also available on [github gist](https://gist.github.com/1729992).
If you only want to use it,
[download](https://gist.github.com/raw/1729992/4eae76f78ba44d5fd0e705d51b0ededbeb0a7a6a/ctags_with_dep.sh)
the script and use the following command to generate the tags file:

    ./ctags_with_dep.sh file1.c file2.c file3.cpp ...

Read on if you want to know what's happening here. This script will first use
`gcc -M` to output the list of header files that are included in our C or C++
source files. However, the output could not be directly used by ctags, thus this
script uses [sed][] commands to filter the output. Finally, this script uses a
[pipe][] to put the file list to the [stdin]() of the ctags program -- ctags
will read the file list from stdin if `-L -` is passed to it on the command
line.

What if you have other directories besides the standard `/usr/include` that
containing the header files you need? You could do a little modification on this
script. For example, you have some header files in `~/include`, then you could
pass `-I ~/include` to the gcc command. Just like below:

```sh
    gcc -M -I ~/include $* | sed -e 's/[\\ ]/\n/g' | \
            sed -e '/^$/d' -e '/\.o:[ \t]*$/d' | \
            ctags -L - --c++-kinds=+p --fields=+iaS --extra=+q
```

If you have any suggestion on this idea, please let me know.


[Vim]: http://www.vim.org
[ctags]: http://ctags.sourceforge.net
[pipe]: http://en.wikipedia.org/wiki/Pipeline_(Unix)
[sed]: http://en.wikipedia.org/wiki/Sed
[stdin]: http://en.wikipedia.org/wiki/Standard_streams#Standard_input_.28stdin.29
