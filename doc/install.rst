Installation
============

Get a read only copy of optimizer
----------------------------------

Install `git` and type:

::

    git clone git://github.com/vellamike/optimizer.git

More information on this here:
.. : http://rogerdudler.github.com/git-guide/


Dependencies:
-------------

The following python libraries and version number are required:

- argparse>=1.2.1
- matplotlib>=1.3.0
- inspyred>=1.0
- numpy>=1.7.1
- pyparsing>=2.0.1
- wx>=1.0.0

You can get them with `easy_install` or `pip` with the following
command (the following exammple is for numpy):

::
   
   pip install numpy

or

::
   
   easy_install install numpy


Install optimizer
------------------

Use the standard install method for Python packages:


::

    sudo python setup.py install

Build documentation
-------------------

To build a local copy of documentation you need a working install of
Sphinx, then run the command:

::

    sphinx-build ./doc <local build directory>

from the top-level optimizer directory where <local build directory>
should be replaced with a custom filepath.
