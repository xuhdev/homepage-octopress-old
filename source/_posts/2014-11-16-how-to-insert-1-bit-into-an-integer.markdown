---
layout: post
title: "How to Insert 1 Bit Into An Integer"
date: 2014-11-16 09:25:42 +0000
comments: true
categories: [C, C++]
---

Inserting a bit into an integer, means to insert a bit into a specific position of an integer, with the highest bit
removed. For example, for a one byte integer `11001010`, if I insert a `1` at digit position 4, which is marked here
`1100|1010` as `|`, the most significant bit, which is the left most `1`, would be eliminated and the rest of the 3 bits
on the left side of `|` would be shifted to the left for 1 bit.

This is not hard to implement, but surprisingly I cannot find any existing code snippet for such a simple job.

Here is the code snippet I wrote for C, but it can be easily translated into any other language. Here, `T` is any
integer type.

```c
// position is the position of the new bit to be inserted. insert_true indicates
// whether the newly inserted bit is true or false

T x; // The integer we are going to insert into
T y = x;
x <<= 1;
if (insert_true)
    x |= (((T) 1) << position);
else
    x &= ~(((T) 1) << position);
x &= ((~((T) 0)) << position);
y &= ~((~((T) 0)) << position);
x |= y;
```
