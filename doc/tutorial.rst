Optimizer tutorial
=================

Layer 1
-------

After the program started, the first layer will appear where the user can select the file containing the
input trace(s). The user must specify the path to this file, and the working directory (base directory)
where the outputs will be written. Apart from these the user must input the requested parameters of the
trace set he/she wants to use. After loading the selected file, the user can check if the traces were loaded
properly with the help of a plot which displays all the traces concatenated and with the help of a tree
display. The concatenation only performed for displaying purposes, the traces are otherwise handled
separately. The program only handles one input file (loading a new file will overwrite the existing one),
but with arbitrary number of traces.


.. figure:: um001.png
   :align: center
