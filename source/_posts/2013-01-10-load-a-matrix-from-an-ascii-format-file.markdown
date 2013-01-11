---
layout: post
title: "Load A Matrix from An Ascii Format File (C++ and Python)"
date: 2013-01-10 11:48
comments: true
categories: [C++, Python, Scientific]
---

It is common for an scientific program to load an ASCII format matrix file, i.e.
an ASCII text file consisting of lines of float numbers separated by
whitespaces. In this post, I am gonna show my code (C++ and Python) to load a
matrix from an ASCII file.

<!-- more -->

## C++

The following C++ function is to load a matrix from an ASCII file into a
`vector< vector<double> >` object, some kind of "C++ style" 2D array.

```cpp
#include <istream>
#include <string>
#include <sstream>
#include <vector>

// load matrix from an ascii text file.
void load_matrix(std::istream* is,
        std::vector< std::vector<double> >* matrix,
        const std::string& delim = " \t")
{
    using namespace std;

    string      line;
    string      strnum;

    // clear first
    matrix->clear();

    // parse line by line
    while (getline(*is, line))
    {
        matrix->push_back(vector<double>());

        for (string::const_iterator i = line.begin(); i != line.end(); ++ i)
        {
            // If we i is not a delim, then append it to strnum
            if (delim.find(*i) == string::npos)
            {
                strnum += *i;
                continue;
            }

            // if strnum is still empty, it means the previous char is also a
            // delim (several delims appear together). Ignore this char.
            if (strnum.empty())
                continue;

            // If we reach here, we got a number. Convert it to double.
            double       number;

            istringstream(strnum) >> number;
            matrix->back().push_back(number);

            strnum.clear();
        }
    }
}
```

The code is also available on [GitHub Gist](https://gist.github.com/4500925).

## Python

The Python code loads the matrix into a [numpy.matrix]() object.

```python
def load_matrix_from_file(f):
    """
    This function is to load an ascii format matrix (float numbers separated by
    whitespace characters and newlines) into a numpy matrix object.

    f is a file object or a file path.
    """

    import types
    import numpy

    if type(f) == types.StringType:
        fo = open(f, 'r')
        matrix = load_matrix_from_file(fo)
        fo.close()
        return matrix
    elif type(f) == types.FileType:
        file_content = f.read().strip()
        file_content = file_content.replace('\r\n', ';')
        file_content = file_content.replace('\n', ';')
        file_content = file_content.replace('\r', ';')

        return numpy.matrix(file_content)

    raise TypeError('f must be a file object or a file name.')
```

The code is also available on [GitHub Gist](https://gist.github.com/4437648).

If you want to get a nested list instead of such a `numpy.matrix` object, you
can use the following lines to convert the object to a nested list:

```python
matrix = load_matrix_from_file('file_name')
nested_list = matrix.tolist()
```

[numpy.matrix]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
