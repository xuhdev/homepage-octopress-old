---
layout: post
title: "Use Travis CI with Jython"
date: 2012-05-27 17:22
comments: true
external-url: 
categories: [Python, Jython, GitHub, Travis CI]
published: false
---

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
can do something to make it work. First, append `jython` to the `python` list:





[GitHub]: http://github.com
[Jython]: http://www.jython.org
[Travis CI]: http://travis-ci.org
[travis-getting-started]: http://about.travis-ci.org/docs/user/getting-started/
[travis-language-speicific-guides-python]: http://about.travis-ci.org/docs/user/languages/python/
