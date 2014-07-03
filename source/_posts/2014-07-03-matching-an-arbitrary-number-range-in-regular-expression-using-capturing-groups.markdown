---
layout: post
title: "Matching an Arbitrary Number Range in Regular Expression Using Capturing Groups"
date: 2014-07-03
comments: true
categories: [Regular Expressions]
---

To match an arbitrary number range in a regular expression, is to match a string with a specific pattern which contains
a number range. For example, to match with a pattern `test{0..100}`, where `{0..100}` denotes an integer not smaller
than `0` and not larger `100`, is such a case.

Although we already have [some](http://www.regular-expressions.info/numericranges.html)
[solutions](http://stackoverflow.com/questions/1377926/regular-expression-numeric-range) to match a number range in
regular expression, but they all make lengthy string and may lead to possible performance issue. In this post, I will
provide an alternative solution to this problem, but it requires you to have control over the captured groups of the
regex.

<!-- more -->

The basic idea is very simple: replace anywhere in the string where you need to match a number range with a capturing
group which matches any numbers you are interested (e.g. integers, real numbers, etc.), and test whether they are in the
number range later. A python example is shown below. The code snippet matches `a{number}b`, where `{number}` is an
integer within a the range of `small_int` and `large_int`.

```python
import re

matched = True

integer_regex = r'[\+\-]?[0-9]+'

matching_obj = re.match('a(' + integer_regex + ')b', string)

if matching_obj == None:
    raise Exception('No matching')

for num in matching_obj.groups():
    if float(num) < small_int or float(num) > large_int:
        raise Exception('No matching')

# successfully matched if we reach here
```

However, the code above is a bit stiff: each time you need to match a new string you have to repeat all the code.
Another more flexible version is shown below (for Python >= 3.4):

{% include_code Match Number Range in Regex lang:py regex-match-number-range.py %}

The function `match_number_range` replaces any occurrence of `{num1..num2}` with a regex which represents any integers
within capturing groups, then extracts them and compares the numbers later. However, you should never have any capturing
group in the original pattern, otherwise this simple function won't work.
