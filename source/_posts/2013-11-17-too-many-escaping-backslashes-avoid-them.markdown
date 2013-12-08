---
layout: post
title: "Too Many Escaping Backslashes? Avoid Them!"
date: 2013-11-17T00:56:56-08:00
comments: true
external-url: 
categories: [utility, python]
---

Backslash escaping is common in programming. Sometimes we may let a file go through a few filters or template engines,
such as [markdown][], [quik][], etc. and things become even worse if we are writing the template files from a string
which requires backslash escaping for any literal backslashes appearing in the string. On Windows, things are more
horrible than on Unices (You know why, right? _Hint: path separator_). Then, if you need a "real" backslash in the final
output, you may end up with four or eight or sixteen backslashes in the original file. This is horrible. To avoid this
situation, I wrote a short preprocessing script in Python to double or quadruple or octuple or zzzuple your backslashes.

<!-- more -->

```python backbackslash.py https://gist.github.com/xuhdev/7497802
# Often when your file needs to go through a few filters, the number of
# backslashes needed for escaping is just horrible! This small script just
# solves the problem. Works well on Python 2.6 and later as well as Python 3.

# This file is under public domain.

# Copyright (C) 2013 Hong Xu <hong@topbug.net>

from __future__ import print_function

import sys

def escape(content, times, escapechar='\\'):
    """
    Escape the @escapechar for @times times. The content is either a string or an iterative of strings.
    """

    es = escapechar
    for i in range(times):
        es = es + es

    if type(content) is str:
        return content.replace(escapechar, es)
    else:
        ret = []
        for c in content:
            ret.append(c.replace(escapechar, es))
        return ret

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: How many times will you escape?", file=sys.stderr)
        sys.exit(1)

    times = int(sys.argv[1])

    if len(sys.argv) >= 3:
        escapechar = sys.argv[2]
    else:
        escapechar = '\\'

    content = sys.stdin.readlines()

    content = escape(content, times, escapechar)

    for line in content:
        sys.stdout.write(line)
```

This file is also available on [Github Gist](https://gist.github.com/xuhdev/7497802).

I named it "backbackslash.py", which means to pull back backslashes. This script is pretty simple -- whenever the script
encountered a backslash (or other escaping character you specify), it copies the number of the backslashes to _2^N_,
where _N_ is the times of escaping you will do. To use this script, simply copy it somewhere, then run:

    python /path/to/backbackslash.py [number of times to escape] [optional escaping character] <input.ext >output.ext

For example, I have a markdown file, but I need it to go through quik first then markdown. In this way, one single
literal backslash would need four backslashes in the original file. So:

    python /path/to/backbackslash.py 2  <my_markdown.md >my_preprocessed_markdown.md

Then you can use the output file as the input of the template engines and filters.

This file can also used as in a Python script. See the `escape` function in the source file above. You'll find it pretty
easy to understand.

[markdown]: http://daringfireball.net/projects/markdown/
[quik]: https://github.com/avelino/quik
