from neuron import h
from nrn import *        
load_hoc_obj=h

        #self.hoc_obj.execute('load_file("'+str(self.model)+'")')
        #self.hoc_obj.execute('load_file("stdrun.hoc")')
       
load_hoc_obj.load_file(str("hh_pas.hoc"))
load_hoc_obj.load_file("stdrun.hoc")
        #self.vec=h.Vector
load_vec=load_hoc_obj.Vector()
