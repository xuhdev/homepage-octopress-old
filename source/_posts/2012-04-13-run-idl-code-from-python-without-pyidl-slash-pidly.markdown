---
layout: post
title: Run IDL Code from Python without PyIDL/pIDLy
date: 2012-04-13 14:02
comments: true
categories: [Astronomy, IDL, Python, Software]
---

As one of the world's most popular computer languages, [Python][] has attracted
more and more astronomers' eyes. However, there are still many astronomy codes
written in [IDL][], which are currently not available in Python. In this way, it
becomes extremely important to invent a way to run IDL code within Python. While
[PyIDL][] and [pIDLy][] are two possible way to solve this problem, I would like
to recommend my own way, which could work on Python 3 and does not require
any third-party Python library, though it is not as powerful as [PyIDL][] or
[pIDLy][]. This method takes advantages of Python's
[subprocess][Python subprocess] module.

<!-- more -->

## Run One-Line IDL Code

Before we start, let's check an important IDL's command line option: `-e`.
When this argument is passed to IDL on command line, the IDL interpreter will
exit right after it runs the IDL code specified by `-e` option. For example,
when you execute the following command on your command line:

    idl -e 'print, "Hello, Python!"'

Something similar to the following should be printed on the screen:

    IDL Version 7.1.1 (linux x86_64 m64). (c) 2009, ITT Visual Information Solutions
    Installation number: xxxxxx
    Licensed for use by: xxxxx

    Hello, Python!

And you are back to Shell. This is essential: if we could run the `idl -e`
command in Python and read the output from Python, then running simple IDL code
within Python won't be a big problem. To implement this, Python's
[subprocess][Python subprocess] module, which is available since Python 2.4,
emerges in our minds. Let's try it:

{% codeblock lang:python %}
import subprocess

subp = subprocess.Popen("idl -e 'print, \"Hello, Python!\"'",
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True)

(idl_stdout, idl_stderr) = subp.communicate()

print(idl_stdout)   # for python 2.4, use "print idl_stdout" instead
{% endcodeblock %}

This should print something like this:

    Hello, Python!

You may ask: where is the IDL's welcome message? When you run IDL from your
shell, the `Hello, Python!` message and the welcome message and are both printed
on the screen, but in fact they are written to different streams: [stdout][] and
[stderr][]. When you run a command from Shell, the stdout and stderr will be
both printed on screen by default, but when we invoke the IDL process from
Python, we could separate the two streams. In the code above, the data from
stdout is put in `idl_stdout`, while the data from stderr is written in
`idl_stderr`. Since the stderr data is useless in most cases, `idl_stdout` is
what we need to deal with.

Furthermore, the stderr data could also become cleaner if you pass `-quiet` to
the idl command:

    idl -quiet -e 'print, "Hello, Python!"'

The output would be simply `Hello, Python!`, without any other word, since
`-quiet` option suppresses these messages. I will always pass `-quiet` option to
the idl command in the following examples.

Now let's try a real world example. We want to use the IDL [lumdist][] function
to calculate a object's luminosity distance given its redshift from our python
code. Here's the code to do it:


{% codeblock lang:python %}
import subprocess

z = 0.2         # the redshift

subp = subprocess.Popen("idl -quiet -e 'print, lumdist(" + repr(z) + ", /SILENT)'",
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True)

(dist, _) = subp.communicate()
dist = float(dist.strip())

print(dist)
{% endcodeblock %}

The value of `dist` is the luminosity distance. The output is:

    980.06791


## Run an IDL Script

The above method allows us to run a one-line IDL code, but in many cases we need
to run an IDL script. Let's go back to IDL command line first. IDL has a
command called `.run`, which allows us to run an external IDL script in your
filesystem. For example, a file named `hello.pro` in your file system has the
following lines:

{% codeblock %}
print, "Hello, I am a IDL script!"
END
{% endcodeblock %}

From your IDL command line, you could use `.run` to run the script:

    IDL> .run hello.pro

The output is:

    % Compiled module: $MAIN$.
    Hello, I am a IDL script!
    
The first line is written to stderr, we do not to care about it. The second
line is the output of the IDL script.

Things become simple now: commands such as `idl -quiet -e '.run idl_script.pro`
could let us run an IDL script from Python:

{% codeblock lang:python %}
import subprocess

subp = subprocess.Popen("idl -quiet -e '.run hello.pro'",
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True)

(idl_stdout, _) = subp.communicate()

print(idl_stdout)
{% endcodeblock %}

For convenience, we could define a Python function:

{% codeblock lang:python %}
def run_idl_script(script_file_name):
    import subprocess

    subp = subprocess.Popen("idl -quiet -e '.run " + script_file_name + "'",
            stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True)

    (idl_stdout, _) = subp.communicate()

    return idl_stdout
{% endcodeblock %}

This function will invoke the IDL interpreter to run the IDL script named
`script_file_name`, and return the output of the script. To use this function,
just call it like any other Python functions:

{% codeblock lang:python %}
output = run_idl_script('hello.pro')
{% endcodeblock %}

The value of `output` is the output of the IDL script `hello.pro`.

## 

Even though this post provides a way to run IDL code without any third-party
Python module, I still recommend you to consider the use of PyIDL and pIDLy:
they are more convenient to use. But when these modules are not available for
you, I believe this article should be useful for you.


[IDL]: http://www.exelisvis.com/ProductsServices/IDL.aspx
[PyIDL]: http://www.cacr.caltech.edu/~mmckerns/pyIDL.html
[Python subprocess]: http://docs.python.org/library/subprocess.html
[Python]: http://www.python.org
[lumdist]: http://idlastro.gsfc.nasa.gov/ftp/pro/astro/lumdist.pro
[pIDLy]: http://astronomy.sussex.ac.uk/~anthonys/pidly/
[stderr]: http://en.wikipedia.org/wiki/Standard_streams#Standard_error_.28stderr.29
[stdout]: http://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
