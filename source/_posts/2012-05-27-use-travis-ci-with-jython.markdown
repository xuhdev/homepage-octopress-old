---
layout: post
title: "Use Travis CI with Jython"
date: 2012-05-27 17:22
comments: true
external-url: 
categories: [Python, Jython, Java, GitHub, Travis CI, Software Development]
---

_This page has been translated into [Spanish](http://www.webhostinghub.com/support/es/misc/utilice-travis-ci-con)
language by Maria Ramos from [Webhostinghub.com](https://plus.google.com/100699836350835346064/posts)._

_This post was updated on Feb 11, 2013, since the old way never works now.
However, the original post is still available
[here]({{ root_url }}/blog/old/2012-05-27-use-travis-ci-with-jython.html)._

[Travis CI][] is a hosted continuous integration service for the open source
community, helping run tests for your [GitHub][] projects for every single push
and pull request. However, by the time this post is written, Travis CI has not
officially supported [Jython][], a Python interpreter written in Java. This post
will help you setup a Jython testing environment for a Python project on Travis
CI.

<!-- more -->

## Setup a Basic Travis CI Configuration for Your Python Project

Before we add a Jython testing environment, we need to setup a basic
configuration for the Python project. By reading
[the Getting Started page][travis-getting-started] and
[Language-specific Guides for Python][travis-language-speicific-guides-python]
in the Travis CI Documentation, you should understand how Travis CI works, and
the basic stuff of building your own configurations. Let's suppose we have the
following basic configuration file `.travis.yml`:

{% codeblock .travis.yml lang:yaml %}
# specify python as the language
language: python

# python versions to be used for testing
python:
  - "2.6"
  - "2.7"

# test script
script: python setup.py test
{% endcodeblock %}

Now we could have our python project tested with Python 2.6 and 2.7 on Travis
CI. Then, let's add Jython as a Python interpreter for this project.


## Add Jython Support for Your Python Project

You cannot simply append a `jython` item to the `python` list if you want your
project tested with Jython, because Jython is not supported officially. But we
can do something to make it work.

Here we need to take advantage of [the Build Matrix][] feature of Travis CI.
First, add **env** entries to the `.travis.yml` file:

```yaml
python:
  - "2.6"
  - "2.7"

env:
  - JYTHON=true
  - JYTHON=false
```

Then what we need to do is to use Jython if `JYTHON=true`, and use C Python if
`JYTHON=false`. However, the testing matrix has 4 entries, two of which are
`JYTHON=true` entries, thus we need to let Travis CI ignore one of them. We
could achieve this by appending the following lines:

```yaml
matrix:
  exclude:
    - python: 2.6
      env: JYTHON=true
```

Then, tell Travis CI to install Jython by adding the following line to your
`.travis.yml` file:

```yaml
before_install: if [ "$JYTHON" == "true" ]; then sudo apt-get install jython; fi
```

By the time this post is written, the Jython version by `sudo apt-get install
jython` is `2.2.x`, which is a bit outdated. If you want to install a later
version of Jython, such as `2.5.2`, you could use the following lines instead of
the line above:

```yaml
before_install:
  - export JYTHON_URL='http://downloads.sourceforge.net/project/jython/jython/2.5.2/jython_installer-2.5.2.jar'
  - if [ "$JYTHON" == "true" ]; then wget $JYTHON_URL -O jython_installer.jar; java -jar jython_installer.jar -s -d $HOME/jython; export PATH=$HOME/jython:$PATH; fi
```

Then modify the test script to include the use of jython:

```yaml
before_script: if [ "$JYTHON" == "true" ]; then export PYTHON_EXE=jython; jython -c "print ''"; else export PYTHON_EXE=python; fi

script: $PYTHON_EXE setup.py test
```

Note that we run `jython -c "print ''"` before we run the testing script,
because something like the following may print when Jython run for the first
time, which may affect the testing result:

    *sys-package-mgr*: processing new jar, '/home/vagrant/jython/jython.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/resources.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/rt.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/jsse.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/jce.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/charsets.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/rhino.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/sunjce_provider.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/pulse-java.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/gnome-java-bridge.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/localedata.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/dnsns.jar'
    *sys-package-mgr*: processing new jar, '/usr/lib/jvm/java-6-openjdk/jre/lib/ext/sunpkcs11.jar'

The final `.travis.yml` should look like this:

{% codeblock .travis.yml lang:yaml %}
# specify python as the language
language: python

# python versions to be used for testing
python:
  - "2.6"
  - "2.7"

env:
  - JYTHON=true
  - JYTHON=false

matrix:
  exclude:
    - python: 2.6
      env: JYTHON=true

before_install: if [ "$JYTHON" == "true" ]; then sudo apt-get install jython; fi

before_script: if [ "$JYTHON" == "true" ]; then export PYTHON_EXE=jython; jython -c "print ''"; else export PYTHON_EXE=python; fi

script: $PYTHON_EXE setup.py test
{% endcodeblock %}

Or like this:

{% codeblock .travis.yml lang:yaml %}
# specify python as the language
language: python

# python versions to be used for testing
python:
  - "2.6"
  - "2.7"

env:
  - JYTHON=true
  - JYTHON=false

matrix:
  exclude:
    - python: 2.6
      env: JYTHON=true

before_install:
  - export JYTHON_URL='http://downloads.sourceforge.net/project/jython/jython/2.5.2/jython_installer-2.5.2.jar'
  - if [ "$JYTHON" == "true" ]; then wget $JYTHON_URL -O jython_installer.jar; java -jar jython_installer.jar -s -d $HOME/jython; export PATH=$HOME/jython:$PATH; fi

before_script: if [ "$JYTHON" == "true" ]; then export PYTHON_EXE=jython; jython -c "print ''"; else export PYTHON_EXE=python; fi

script: $PYTHON_EXE setup.py test
{% endcodeblock %}


In this way, there will be one more testing for Jython every time the testing is
triggered.


## A Real World Example

A real world example could be found
[here](https://github.com/editorconfig/editorconfig-core-py/blob/7ff7104fa4e79468772b18801c66f11aa58fef84/.travis.yml).
The real world example uses [cmake][] as its testing system so it looks a bit
different from the example above.


[the Build Matrix]: http://about.travis-ci.org/docs/user/build-configuration/#The-Build-Matrix
[GitHub]: http://github.com
[Jython]: http://www.jython.org
[Travis CI]: http://travis-ci.org
[cmake]: http://www.cmake.org
[travis-getting-started]: http://about.travis-ci.org/docs/user/getting-started/
[travis-language-speicific-guides-python]: http://about.travis-ci.org/docs/user/languages/python/
