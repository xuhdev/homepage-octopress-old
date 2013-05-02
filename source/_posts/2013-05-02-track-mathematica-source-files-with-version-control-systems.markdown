---
layout: post
title: "Track Mathematica Source Files with Version Control Systems"
date: 2013-05-02T01:06:50-07:00
comments: true
file_title: 2013-05-02-track-mathematica-source-files-with-version-control-systems
categories: [Mathematica, git, Version Control, hg, bazaar, svn]
---

{% include custom/post_initialization.html %}

[Mathematica][] is a famous computational software program in science,
engineering, etc. However, the source code of Mathematica is usually stored in
the format of [Mathematica Notebook][], which is hard to track with a
[Version Control System][], such as [git][], [mercurial][], etc. Here I'm
providing a solution to solve this problem.

<!-- more -->

For example, for a Mathematica notebook with the following simple lines:

    In[1]:= Integrate[x^2, {x, 0, 1}]
    Out[1]= 1/3

The contents in this file could be as long as below (You can inspect the
contents of the notebook by opening it with a text editor):

{% raw %}

    (* Content-type: application/vnd.wolfram.mathematica *)

    (*** Wolfram Notebook File ***)
    (* http://www.wolfram.com/nb *)

    (* CreatedBy='Mathematica 9.0' *)

    (*CacheID: 234*)
    (* Internal cache information:
    NotebookFileLineBreakTest
    NotebookFileLineBreakTest
    NotebookDataPosition[       157,          7]
    NotebookDataLength[      1245,         52]
    NotebookOptionsPosition[       926,         35]
    NotebookOutlinePosition[      1280,         51]
    CellTagsIndexPosition[      1237,         48]
    WindowFrame->Normal*)

    (* Beginning of Notebook Content *)
    Notebook[{

    Cell[CellGroupData[{
    Cell[BoxData[
     RowBox[{"Integrate", "[", 
      RowBox[{
       RowBox[{"x", "^", "2"}], ",", 
       RowBox[{"{", 
        RowBox[{"x", ",", "0", ",", "1"}], "}"}]}], "]"}]], "Input",
     CellChangeTimes->{{3.5765021681673822`*^9, 3.5765021750753613`*^9}}],

    Cell[BoxData[
     FractionBox["1", "3"]], "Output",
     CellChangeTimes->{3.576502176105269*^9}]
    }, Open  ]]
    },
    WindowSize->{740, 668},
    WindowMargins->{{4, Automatic}, {Automatic, 4}},
    FrontEndVersion->"9.0 for Mac OS X x86 (32-bit, 64-bit Kernel) (January 25, \
    2013)",
    StyleDefinitions->"Default.nb"
    ]
    (* End of Notebook Content *)

    (* Internal cache information *)
    (*CellTagsOutline
    CellTagsIndex->{}
    *)
    (*CellTagsIndex
    CellTagsIndex->{}
    *)
    (*NotebookFileOutline
    Notebook[{
    Cell[CellGroupData[{
    Cell[579, 22, 238, 6, 28, "Input"],
    Cell[820, 30, 90, 2, 82, "Output"]
    }, Open  ]]
    }
    ]
    *)

    (* End of internal cache information *)

{% endraw %}

Then how should we track a Mathematica source file if it's a mess like this? The
solution is simply: use plain text files to track.

First, edit your Mathematica Notebook files to do integrals, solve equations,
etc. as you usually do. After that, click on **Save As...** under the **File**
menu:

![]({{ post_file_url }}/1.png)

Then choose the format as **Plain Text (*.txt)**:

![]({{ post_file_url }}/2.png)


OK, now we have a file with the simple content. If we follow the example above,
the contents of the file should be:

    In[1]:= Integrate[x^2,{x,0,1}]
    Out[1]= 1/3

You can then track this file with your favorite version control system.

When you want to load this file, first, click on **Open...** under **File**
menu. Then choose the file format as **Text File** in the Open File Dialog:

![]({{ post_file_url }}/3.png)

Finally, choose the plain text file you saved before in the file browser, and
enjoy!


[Mathematica]: http://www.wolfram.com/mathematica/
[Mathematica Notebook]: http://www.wolfram.com/technology/nb/
[Version Control System]: http://en.wikipedia.org/wiki/Revision_control
[git]: http://git-scm.com/
[mercurial]: http://mercurial.selenic.com/
