#Optimizer
Optimizer is a graphical tool for fitting the parameters of neuronal models

Installation
============

Get a read only copy of optimizer
----------------------------------

Install `git` and type:


    git clone https://github.com/vellamike/optimizer.git

More information on this here: http://rogerdudler.github.com/git-guide/


Dependencies
-------------

The following python libraries are required:
  - python
  - numpy 
  - scipy 
  - matplotlib 
  - wxPython 
  - inspyred 
  - pyelectro

The following libraries are recommended:
  - neuron

You can get `numpy`, `scipy` and `inspyred` with `easy_install` or `pip` with the following command (for numpy):

  
    pip install numpy

or

    easy_install install numpy
   
You can get `matplotlib` with the following command:


    Debian / Ubuntu : sudo apt-get install python-matplotlib
    Fedora / Redhat : sudo yum install python-matplotlib

If you encounter any difficulties you can find a more detailed description at:
    
    http://matplotlib.org/users/installing.html

You can get `wxpython` with the following command:


    apt-get install python-wxgtk2.8 python-wxtools wx2.8-i18n
    
This command might not work if your OS has an earlier version in the standard software repository. If so, please follow the instructions at:
    
    http://wiki.wxpython.org/InstallingOnUbuntuOrDebian

Currently, Optimizer works properly only with version 2.8 of wxpython. Some distributions (e.g., Ubuntu 16.04) may install version 3.0 instead (or in addition to) 2.8. In this case, please remove version 3.0 and make sure to install only version 2.8. Support for later versions of wxpython will be added to Optimizer in the future.
    
You can get `pyelectro` from:
    
    https://github.com/vellamike/pyelectro.git
    
After cloning the repository you can install it by the standard installation method:


    python setup.py install
    
Installing Neuron as a python package is optional since Optimizer can use any executable to run the simulations.
WARNING: Many features of Optimizer are designed to work with Neuron, so we recommend that you install it!

Installing Neuron as a python package is beyond the scope of this tutorial as it is somewhat complicated, but you can find a step-by-step guide at:

    http://www.davison.webfactional.com/notes/accessing-hoc-python/

Install optimizer
------------------

Use the standard install method for Python packages:


    sudo python setup.py install


Run optimizer
-------------------

You can run Optimizer (with a GUI) directly from its installation folder with:

    python optimizer.py -g
    
Or for the command line version (you must specify a configuration file as well):

    python optimizer.py -c example.xml
    
    
Build documentation
-------------------

If you should require a local copy of the Optimizer documentation, you need a working install of
Sphinx, then run the command:


    sphinx-build ./doc <local build directory>

from the top-level optimizer directory where <local build directory>
should be replaced with a custom filepath.

Test Platforms
--------------

The package was tested on the following systems:

    1. Mandriva 2010.2 (kernel 2.6.33, glibc 2.11)
      - python 2.6.5
      - numpy 1.6.2
      - scipy 0.7.2
      - matplotlib 1.1.1
      - wxPython 2.8.10.1
      - inspyred 1.0
      - pyelectro
      - neuron 7.3

    2. CentOS 6.4 (kernel 2.6.32, glibc 2.12)
      - python 2.6.6
      - numpy 1.6.1
      - scipy 0.10.1
      - matplotlib 1.3.1
      - wxPython 2.8.12.0
      - inspyred 1.0
      - pyelectro
      - neuron 7.2
    
    3. Ubuntu 12.04.3 LTS (kernel 3.2.0-54-generic, glibc 2.15)
      - Python 2.7.3
      - numpy 1.7.0
      - scipy 0.11.0
      - matplotlib 1.1.1rc
      - wxPython 2.8.12.1
      - inspyred 1.0
      - pyelectro
      - neuron 7.2

    4. Ubuntu 14.04.4 LTS 
      - Python 2.7.6
      - numpy 1.8.2
      - scipy 0.13.3
      - matplotlib 1.3.1
      - wxPython 2.8.12.1
      - inspyred 1.0
      - pyelectro 0.1.6
      - neuron 7.4

Notes

    - Since Neuron with the python interpreter is not working perfectly on Windows, we recommend to use Ubuntu, Mint, or another common Linux distribution (installing and setting up a virtual os is not hard).
    - inspyred requires a feature which is only included in python 2.7 (not in python 2.6 or earlier), but there is a workaround for this problem: https://groups.google.com/forum/#!topic/inspyred/YwJb3ABVtL8

    
Developers
----------

Project Leader:

    - Szabolcs Káli:
        kali@koki.hu

Lead Developers:

    - Peter Friedrich:
        p.friedrich.m@gmail.com

    - Sára Sáray
	saraysari@gmail.com
	
Contributors:

    - Mike Vella

