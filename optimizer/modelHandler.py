import os
import sys
from traceHandler import Trace
import optimizerHandler
import importlib

try:
    import copyreg
except:
    import copyreg

from types import MethodType



class externalHandler():
    """
    Handles models which are using a simulator other than Neuron.
    :param command: the command string which should be executed

    .. note::
        The command must consist of the following parts:
           * the command to execute
           * the model file
           * options (optional)
           * number of parameters to optimize

    """
    def __init__(self,command):
        c=command.split()
        self.executable=c[0]
        self.model_file=c[1]
        self.options=c[2:len(c)-1]
        self.number_of_params=int(c[-1])
        self.record=[[]]
        self.spike_times=None

        os.chdir("/".join(self.model_file.split("/")[0:-1]))

    def SetNParams(self,o):
        """
        Sets the number of parameters in the given object by calling it's ``SetObjTOOpt`` method.

        :param o: the object whose method will be called

        .. note::
            This is necessary because the other parts expects that the option handler objects knows the parameters subjects to optimization. Since this is not true in the case of an external simulator, this workaround is needed.

        """
        for n in range(self.number_of_params):
            o.SetObjTOOpt("parameter"+str(n))

    def GetExec(self ,unique_ID=''):
        """
        Creates the command that runs the simulator with the model and with the appropriate options.
        :return: a ``list`` of strings ready for execution
        """
        tmp=[self.executable,self.model_file]
        for o in self.options:
            tmp.append(o)
        tmp += [unique_ID]
        return tmp

    def GetParameters(self):
        return None

    def CreateStimuli(self,s):
        pass

    def SetStimuli(self,p,e):
        pass

    def load_neuron(self):
        pass

# class to handle the neuron models
class modelHandlerNeuron():
    """
    Imports the necessary modules to handle Neuron models and loads the model
    as well as the additional mechanisms. Creates containers for the sections and the channels for easier handling.

    :param model_path: the path to the model file
    :param special_path: the path to the special file (.mod files)
    :param base: the base working directory

    """


    def __init__(self,model_path,special_path,base=os.getcwd()):
        from neuron import h
        import neuron


        print('*********** NEURON LOADED ***********')
        self.base_directory=base
        self.special=special_path
        self.model=model_path
  
        neuron.load_mechanisms(self.special)
        
        #os.chdir(self.special)
        #from neuron import h
        #from nrn import *
        

        self.hoc_obj=None
        self.vec=None
        self.stimulus=None
        self.record=[]
        self.spike_times=None
        self.sections={}

    def load_neuron(self):
        #from neuron import h
        from neuron import h
        import neuron
        neuron.load_mechanisms(self.special)
        self.hoc_obj=h
        self.hoc_obj.load_file(str(self.model))
        self.hoc_obj.load_file("stdrun.hoc")
        self.vec=self.hoc_obj.Vector()
        os.chdir(self.base_directory)
        self.stimulus=None
        self.record=[]
        self.spike_times=None
        self.sections={}
        for n in h.allsec():
            self.sections[str(h.secname())]=n
        self.channels={}
        #optimizerHandler.setmods(self.hoc_obj,self.sections)
        for sec in h.allsec():
            for seg in sec:
                for mech in seg:
                    self.channels[str(mech.name())]=mech



    # creates and adjusts the stimulus parameters
    # stims: 0.: stimulation type, 1.: place inside the section, 2.: section name
    def CreateStimuli(self,stims):
        """
        Creates a Neuron pointprocess which is responsible for the stimulation of the model.

        .. note::
            The type of the point process is either an ``IClamp`` or a ``SEClamp``.

        :param stims: a ``list`` with the following values:

           * stimulation type as ``string``
           * position inside section
           * name of the section

        """
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
        """
        Sets the parameters of the stimulating object. The parameters are the following:
            * amplitude
            * delay
            * duration

         or

            * amplitude1
            * amplitude2
            * amplitude3
            * duration1
            * duration2
            * duration3

        :param params: the ``list`` of parameters containing the first 3 values from the above list
        :param extra_params: ``list`` of parameters containing additional values to set up the ``SEClamp``

        .. note::
            The rs parameter of the ``SEClamp`` is set to 0.01

        """

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
        """
        Uses the vector.play method from Neuron to create a time varying stimulus.
        The stimulus is read from the given file.

        :param params: ``list`` with the name of the file containing the stimulus as first element

        .. note::
            The delay value must be set to zero and the duration must be set to 1e9, but these are
            not the actual parameters of the stimulus. This is necessary for Neuron in order to work.

        """

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
    def SetChannelParameters(self,section,segment,channel,params,values):
        """
        Sets the given channel's parameter to the given value. If the section is not known that
        indicates a serious internal error and the program will abort.

        :param section: the selected section's name as ``string``
        :param channel: the selected channel's name as ``string``
        :param params: the selected channel parameter's name as ``string``
        :param values: the value to be set

        """
        try:
            self.sections[section].push()
        except KeyError:
            sys.exit("No section named " + str(section) + " was found!")
        sec = self.hoc_obj.cas()
        lseg = [seg for seg in sec]
        #self.hoc_obj.cas().__setattr__(params,values)
        
        setattr(lseg[int(segment)],params,values)
        self.hoc_obj.pop_section()


    # sets the morphology parameters in the given section
    # one section, but multiple parameters at one time
    def SetMorphParameters(self,section,params,values):
        """
        Sets the given morphological parameter to the given value.
        If the section is not known that indicates a serious internal error and the program will abort.
        If the section has no parameter with the given name
        then it is interpreted as a parameter of a pointprocess and the function will set the parameter assuming the pointprocess exists in the middle (0.5) at the given section and there is only one other pointprocess in the section.

            .. note::
                This workaround is implemented because some mechanisms are implemented as pointprocesses.

            :param section: the name of the section as ``string``
            :param params: the name of the parameter as ``string``
            :param values: the value to set

        """

        try:
            self.sections[section].push()
            #self.hoc_obj.cas().__setattr__(params,values)
            setattr(self.hoc_obj.cas(), params, values)
            self.hoc_obj.pop_section()
        except KeyError:
            sys.exit("No section named " + str(section) + " was found!")
        except AttributeError:
            setattr(self.hoc_obj.cas()(0.5).point_processes()[1], params,values)

        #except:
            #sys.exit("Morphology parameter "+params+" not found!")

#    # gets the stimulation settings, passes it to the graphic layer
#    def GetStimuli(self):
#        """
#
#        """
#        return [self.stim,self.stims,self.parameters]
#
    def contains(self,string,ss):
        """
        Checks if substring is in the given ``list``
        and creates a string which contains only the matching elements separated by spaces.

        :param string: ``list`` of strings
        :param ss: the substring to be matched

        :return: a string which contains only the matching elements separated by spaces

        """
        temp=""

        for n in string:
            try:
                str.index(n, ss)
                temp=temp+" "+str(n)
            except ValueError:
                pass
        return temp

    # returns the adjustable parameters in the model, passes it to the graphic layer
    # comment: the dir option returns everything in the channels class, but there is no exact distinction between
    # channel parameters and methods
    # possible distinction: channel variables contains the channel's name CaN <-> gmax_CaN
    # returns a string matrix, containing the section name,
    # morphology parameters, mechanisms' names, and the mech's changeable parameters
    def GetParameters(self):
        """
        Collects every member of every section object and filters out those that are not parameters of
        the model. The function will collect:

            * every parameter of the the mechanisms
            * every mechanism
            * some default parameters that are always included in a model,
              and pointprocesses that are not some sort of Clamp

        :return: the filtered content of the model in a string matrix

        """

        matrix=[]
        temp=[]
        parname=[]
        mechs_pars=[]
        defaults=[]
        seg_num=0

        for sec in self.hoc_obj.allsec():
            temp.append(str(self.hoc_obj.secname()))

            defaults=["", "morphology",["L" , "cm" , "Ra", "diam"]]
            mechs_pars.append(defaults)

            for seg in sec:

                for mech in seg:

                    self.hoc_obj('strdef mtname, msname')
                    self.hoc_obj('mtname=" "')
                    self.hoc_obj('objref mechs')
                    self.hoc_obj.mtname=mech.name()
                    self.hoc_obj('mechs=new MechanismStandard(mtname)')
                    self.hoc_obj('k = mechs.count()')
                    parnum=int(self.hoc_obj.k)
                    self.hoc_obj('j=0')
                    for j in range(parnum):
                        self.hoc_obj.j = j
                        self.hoc_obj('k = mechs.name(msname, j)')
                        parname.append(self.hoc_obj.msname)
                    mechs_pars.append([seg_num, mech.name(),parname])
                    #mechs_pars.append(parname)
                    parname=[]
                seg_num+=1

                temp.append(mechs_pars)
            mechs_pars=[]
                    #temp.append(channels)
            seg_num=0
            matrix.append(temp)

            temp=[]
                #mechs_pars=[]
                #break
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
        """
         Sets up the recording procedure and the simulation, then runs it.

        :param settings: the settings of the recording and the parameters of the simulation:

            * length of simulation
            * integration step size
            * parameter to record
            * section to record from
            * position inside the section
            * initial voltage

        """
        #self.hoc_obj.cvode_active(1)#variable time step is active
        self.hoc_obj.tstop=settings[0]
        self.hoc_obj.steps_per_ms=1/settings[1]
        self.hoc_obj.dt=settings[1]
        vec=self.hoc_obj.Vector()
        if settings[2]=="i" and self.stims[0]=="VClamp":
            #vec.record(getattr(h.cas()(0.5).point_processes()[0],"_ref_i"))
            vec.record(getattr(self.sections[settings[3]](settings[4]).point_processes()[0],"_ref_i"))
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
        """
        Converts the hoc vector obtained from the simulation and converts it into a ``Trace`` object.

        :param vector: a hoc vector

        :return: the data trace from the created object

        """
        tr=Trace(1,"",self.hoc_obj.tstop,self.hoc_obj.tstop/self.hoc_obj.dt)
        tr.Convert(vector)
        return tr.data
        # comment: pass the hoc vector to Convert, not the hoc_object
