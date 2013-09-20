import os
import sys
from string import index,split
from traceHandler import Trace

class externalHandler():
    def __init__(self,command):
        c=command.split()
        self.executable=c[0]
        self.model_file=c[1]
        self.options=c[2:len(c)-1]
        self.number_of_params=int(c[-1])
        self.record=[[]]
        
        os.chdir("/".join(self.model_file.split("/")[0:-1]))
        
    def SetNParams(self,o):
        for n in range(self.number_of_params):
            o.SetObjTOOpt("parameter"+str(n)) 
    
    def GetExec(self):
        tmp=[self.executable,self.model_file]       
        for o in self.options:
            tmp.append(o)
            
        return tmp
    
    def GetParameters(self):
        return None
    
    def CreateStimuli(self,s):
        pass
    
    def SetStimuli(self,p):
        pass

    
# class to handle the neuron models
class modelHandlerNeuron():
    
    # sets the location of the special file: mod files
    # asks for a base directory (it's like workspace in eclipse, temp files, and results will be written here)
    # imports the neuron modules
    # loads stdrun.hoc for the simulation
    def __init__(self,model_path,special_path,base=os.getcwd()):
        self.base_directory=base
        self.special=special_path
        self.model=model_path
        os.chdir(self.special)
        from neuron import h
        from nrn import *
        self.hoc_obj=h
        self.hoc_obj.load_file(str(self.model))
        self.hoc_obj.load_file("stdrun.hoc")
        self.vec=self.hoc_obj.Vector()
        os.chdir(self.base_directory)
        self.stimulus=None
        self.record=[]
        self.sections={}
        for n in h.allsec():
            self.sections[str(h.secname())]=n
        self.channels={}
        for sec in h.allsec():
            for seg in sec:
                for mech in seg:
                    self.channels[str(mech.name())]=mech
        
        
    
    # creates and adjusts the stimulus parameters
    # stims: 0.: stimulation type, 1.: place inside the section, 2.: section name
    def CreateStimuli(self,stims):
        self.stims=stims
        #try:
        #    print self.stims[0],"IClamp"
        #    print self.stims[0]=="IClamp"
        if self.stims[0]=="IClamp":
            self.stimulus=self.hoc_obj.IClamp(self.stims[1],sec=self.sections[self.stims[2]])
        elif self.stims[0]=="VClamp":
            self.stimulus=self.hoc_obj.SEClamp(self.stims[1],sec=self.sections[self.stims[2]])
    #    else:
    #        raise TypeError()
    # params: 0.: amplitude, 1.: delay, 2.:duration 
    def SetStimuli(self,params,extra_params):
        
        self.parameters=params
        if self.stims[0]=="IClamp":
            self.stimulus.amp=self.parameters[0]
            self.stimulus.delay=self.parameters[1]
            self.stimulus.dur=self.parameters[2]
        else:
            self.stimulus.amp1=extra_params[5]
            self.stimulus.amp2=self.parameters[0]
            self.stimulus.amp3=extra_params[5]
            
            self.stimulus.dur1=self.parameters[1]
            self.stimulus.dur2=self.parameters[2]
            self.stimulus.dur3=extra_params[0]-(self.stimulus.dur1+self.stimulus.dur2)
            
            self.stimulus.rs=0.01
            
        #except TypeError:
        #    sys.exit("Unknown stimulus type!")
        #except IndexError:
        #    sys.exit("Stimulation settings not specified!!")
    
    def SetCustStimuli(self,params):
        self.hoc_obj.load_file("vplay.hoc")
        self.parameters=params
        
        f=open(self.parameters[0],'r')
        tmp=[float(n) for n in f]
        self.vec=self.vec.from_python(tmp)
        #self.hoc_obj('h.vec.play(&stim.amp,dt)')
        #print (dir(self.hoc_obj.cas()(0.5).point_processes()[0]))
        #ref=self.hoc_obj.ref(self.stimulus.amp)
        self.vec.play(self.hoc_obj.cas()(0.5).point_processes()[0]._ref_amp,self.hoc_obj.dt)
        self.stimulus.delay=0
        self.stimulus.dur=1e9
        #self.stimulus.dur=self.parameters[2]
        f.close()
        
            
        
    # sets the channel parameters to the given value
    # the user must know the existing parameters of the channels in order to change them,
    # the program only detects the inserted channels 
    # sections: string: section name
    # channels: string:channel name
    # params: string list of channel parameters
    # values: float list of values in the order of the parameters
    # the user can specify one channel in one section at one time,
    # but can give multiple parameters and values
    def SetChannelParameters(self,section,channel,params,values):
        try:
            self.sections[section].push()
        except KeyError:
            sys.exit("No section named " + str(section) + " was found!")

        self.hoc_obj.cas().__setattr__(params,values)
        self.hoc_obj.pop_section()

        
    # sets the morphology parameters in the given section
    # one section, but multiple parameters at one time
    def SetMorphParameters(self,section,params,values):
        try:
            self.sections[section].push()
            self.hoc_obj.cas().__setattr__(params,values)
            self.hoc_obj.pop_section()
        except KeyError:
            sys.exit("No section named " + str(section) + " was found!")
        except AttributeError:
            self.hoc_obj.cas()(0.5).point_processes()[1].__setattr__(params,values)
            
        #except:
            #sys.exit("Morphology parameter "+params+" not found!")

    # gets the stimulation settings, passes it to the graphic layer    
    def GetStimuli(self):
        return [self.stim,self.stims,self.parameters]
    
    # returns the adjustable parameters in the model, passes it to the graphic layer
    # comment: the dir option returns everything in the channels class, but there is no exact distinction between
    # channel parameters and methods 
    # possible distinction: channel variables contains the channel's name CaN <-> gmax_CaN 
    def contains(self,string,ss):
        temp=""
        
        for n in string:
            try:
                index(n, ss)
                temp=temp+" "+str(n)
            except ValueError:
                pass
        return temp   
    
    # returns a string matrix, containing the section name, 
    # morphology parameters, mechanisms' names, and the mech's changeable parameters
    def GetParameters(self):
        matrix=[]
        temp=[]
        temp2=""
        temp3=""
        for sec in self.hoc_obj.allsec():
            temp.append(str(self.hoc_obj.secname()))
            defaults="L"+", cm"+", Ra"+", diam"+", nseg"
            for n in ["ena","ek","eca"]:
                try:
                    index(dir(self.hoc_obj),n)
                    defaults+=", "+n
                except ValueError:
                    continue
            for n in sec(0.5).point_processes():
                try:
                    index(n.hname(),"Clamp")
                    continue
                except ValueError:
                    not_param=set(['Section', '__call__', '__class__', '__delattr__', 
                               '__delitem__', '__doc__', '__format__', '__getattribute__', 
                               '__getitem__', '__hash__', '__init__', '__iter__', 
                               '__len__', '__new__', '__nonzero__', '__reduce__', 
                               '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', 
                               '__sizeof__', '__str__', '__subclasshook__', 
                               'allsec', 'amp', 'baseattr', 'cas', 
                               'delay', 'dur', 'get_loc', 'has_loc', 
                               'hname', 'hocobjptr', 'i', 
                               'loc', 'next', 'ref', 'setpointer'])
                    defaults+=", "+", ".join(list(set(dir(n)).difference(not_param)))
                    
                    
                
            temp.append(defaults)
            for seg in sec:
                for mech in seg:
                    #print dir(mech)
                    temp2=temp2+" "+str(mech.name())
                    if self.contains(dir(mech),str(mech.name()))!="":
                        temp3=temp3+self.contains(dir(mech),str(mech.name()))+" "
                temp.append( temp3  )
                temp.append(temp2)
                matrix.append(temp)
                temp2=""
                temp3=""
                temp=[]
                break
        return matrix
        
    # sets the simulation settings, like tstop, dt, Vrest, stb also creates the hoc object to store the recordings
    # runs the simulation
    # settings:
        #0:tstop
        #1:dt
        #2:recorded param
        #3:section
        #4:position
        #5:vrest
        #6:sampling rate
    def RunControll(self, settings):
        print settings
        #self.hoc_obj.cvode_active(1)#variable time step is active
        self.hoc_obj.tstop=settings[0]
        self.hoc_obj.steps_per_ms=1/settings[1]
        self.hoc_obj.dt=settings[1]
        vec=self.hoc_obj.Vector()
        if settings[2]=="i" and self.stims[0]=="VClamp":
            vec.record(self.hoc_obj.ref(self.hoc_obj.cas()(0.5).point_processes()[0].i))
        else:
            ref='_ref_'+settings[2]
            vec.record(getattr(self.sections[settings[3]](settings[4]),ref))
        # comment: create the hoc vector to record time and the measured parameter
        #print settings[5]
        self.hoc_obj.v_init=settings[5]
        self.hoc_obj.finitialize(settings[5])
        self.hoc_obj.run()
        self.record=self.Recordings(vec)
        vec.resize(0)
        
        #else:
            #sys.exit("Error occurred during simulation!")
        
    # creates a trace object from the recordings
    def Recordings(self,vector):
        tr=Trace(1,"",self.hoc_obj.tstop,self.hoc_obj.tstop/self.hoc_obj.dt)
        tr.Convert(vector)
        return tr.data
        # comment: pass the hoc vector to Convert, not the hoc_object
    
        
    
    