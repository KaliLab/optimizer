#Optimizer
Optimizer is a graphical tool for fitting the parameters of neuronal models

Installation
============

Get a read only copy of optimizer
----------------------------------

Install `git` and type:


    git clone https://github.com/KaliLab/optimizer.git

More information on this here: http://rogerdudler.github.com/git-guide/


Dependencies
-------------

The following python libraries are required:
  - python
  - numpy 
  - scipy 
  - matplotlib 
  - PyQt5
  - inspyred 
  - pyelectro
  - eFEL
  - Pygmo
  - bluepyopt


The following libraries are recommended:
  - neuron

You can get `numpy`, `scipy`, `Pygmo`, `bluepyopt` and `inspyred` with `easy_install` or `pip` with the following command (for numpy):

  
    pip install numpy

or

    easy_install install numpy


You can get eFEL with `pip`:
    
    pip install efel

   
You can get `matplotlib` with the following command:


    Debian / Ubuntu : sudo apt-get install python-matplotlib
    
    Fedora / Redhat : sudo yum install python-matplotlib
    
    or:
    
    pip install matplotlib

If you encounter any difficulties you can find a more detailed description at:
    
    http://matplotlib.org/users/installing.html

    
    
You can get `pyelectro` from:
    
    https://github.com/vellamike/pyelectro.git
    
    or:
    
    pip install pyelectro
    
    
After cloning the repository you can install it by the standard installation method:


    python setup.py install
    
Installing Neuron as a python package is optional since Optimizer can use any executable to run the simulations.
WARNING: Many features of Optimizer are designed to work with Neuron, so we recommend that you install it!

Installing Neuron as a python package is beyond the scope of this tutorial as it is somewhat complicated, but you can find a step-by-step guide at:

    http://andrewdavison.info/notes/installation-neuron-python/

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

    1. Ubuntu 14.04.4 LTS 
    2. Fedora release 32 (Thirty Two) (neurofedora)

Notes

    - Since Neuron with the python interpreter is not working perfectly on Windows, we recommend to use Ubuntu, Mint, or another common Linux distribution (installing and setting up a virtual os is not hard).

    
Developers
----------

Project Leader:

    - Szabolcs Káli:
        kali@koki.hu

Lead Developer:

    - Máté Mohácsi
	mohacsi.mate@koki.mta.hu
	
    - Sára Sáray
	saray.sara@koki.mta.hu
	
    - Márk Török Patrik
	torok.mark.patrik@gmail.com

    - Peter Friedrich:
        p.friedrich.m@gmail.com
	
Contributors:

    - Mike Vella

