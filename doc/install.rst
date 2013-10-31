Installation
============

A working version is installable via pip:
----------------------------------------

::

    pip install optimizer

This is always the latest (stable) branch corresponding to the master
branch on github.


Get a read only copy of optimizer
----------------------------------

Install `git`_ and type:

::

    git clone git://github.com/vellamike/optimizer.git

More information on this here:
.. _Git: http://rogerdudler.github.com/git-guide/


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
