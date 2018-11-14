from math import fsum, sqrt
from copy import copy
from pyelectro import analysis
from traceHandler import sizeError
import efel
import numpy as np
import scipy
import inspyred
from inspyred import ec
from inspyred.ec import emo
from inspyred.ec import variators
from inspyred.ec import observers
import modelHandler
import time

try:
    import copyreg
except:
    import copyreg

from types import MethodType
import os


def _pickle_method(method):
    func_name = method.__func__.__name__
    obj = method.__self__
    cls = method.__self__.__class__
    return _unpickle_method, (func_name, obj, cls)

def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
    return func.__get__(obj, cls)

try:
	copyreg.pickle(MethodType, _pickle_method, _unpickle_method)
except:
	copyreg.pickle(MethodType, _pickle_method, _unpickle_method)

def frange(start, stop, step):
        """
        Generates range of real values.

        :param start: beginning of range
        :param stop: end of range
        :param step: step size between values

        """
        r = start
        while r < stop:
            yield r
            r += step


class spike_frame():
    """
    Object to represent the important parts of a spike. The parameters stored are the following:

    :param start_pos: the index of the starting position
    :param start_val: the starting value of the spike
    :param peak: the index of the peak value of the spike
    :param peak_val: the peak value of the spike
    :param stop_pos: the index of the end of the spike
    :param stop_val: the value of the end of the spike

    """
    def __init__(self, start, start_val, peak, peak_val, stop, stop_val):
        self.start_pos = start
        self.start_val = start_val
        self.peak = peak
        self.peak_val = peak_val
        self.stop_pos = stop
        self.stop_val = stop_val

class spike(spike_frame):
    """
    The extension of the ``spike_frame`` class as it contains every point in the spike in addition to the
    crucial ones.
    """
    def __init(self, start, start_val, peak, peak_val, stop, stop_val, spike):
        spike_frame.__init__(self, start, start_val, peak, peak_val, stop, stop_val)
        self.s = spike#vector, with the spike in it


class fF(object):
    """
    Class encapsulating the implemented error functions.

    :param reader_object: a ``traceReader`` object containing the input trace(s)
    :param model_object: either ``modelHandlerNeuron`` or ``externalHandler`` object, this performs the model related tasks
    :param option_object: an ``optionHandler`` object with the stored settings

    Main attributes:
        :attr: thres: the spike detection threshold
        :attr: calc_dict: contains references to the existing fitness functions, using its names as keys
        :attr: user_fun_name: the name of the function defined by the user (optional)

    """
    def __init__(self, reader_object, model_object, option_object):
        self.fitnes = []
        self.thres = option_object.spike_thres
        #self.d_spike=[]
        #self.m_spike=[]
        self.model = model_object
        self.option = option_object
        self.reader = reader_object
        #self.current_pop=0
        self.fun_dict = {"Combinations": self.combineFeatures}
        self.fun_dict2 = {"Multiobj": self.MooFeatures}
        self.calc_dict = {"MSE": self.calc_ase,
                        "MSE (excl. spikes)": self.calc_spike_ase,
                        "Spike count": self.calc_spike,
                        "Spike count (stim.)": self.spike_rate,
                        "ISI differences": self.isi_differ,
                        "Latency to 1st spike": self.first_spike,
                        "AP amplitude": self.AP_overshoot,
                        "AHP depth": self.AHP_depth,
                        "AP width": self.AP_width,
                        "Derivative difference" : self.calc_grad_dif,
                        "PPTD" : self.pyelectro_pptd}
        '''
        try:
            #self.model.load_neuron()
            s = self.option.GetUFunString()
            s = replace(s, "h.", "self.model.hoc_obj.")
            exec(compile(replace(s, "h(", "self.model.hoc_obj("), '<string>', 'exec'))
            self.usr_fun_name = self.option.GetUFunString().split("\n")[4][self.option.GetUFunString().split("\n")[4].find(" ") + 1:self.option.GetUFunString().split("\n")[4].find("(")]
            self.usr_fun = locals()[self.usr_fun_name]
        except SyntaxError:
            print "Your function contained syntax errors!! Please fix them!"
        except IndexError:
            pass
        '''



    def setParameters(self, section, params):
        """
        Sets the specified parameters to the given values. If there is a function defined by the user
        it calls that instead.

        :param section: ``list`` of strings specifying precisely
            ("section","channel","channel parameter" or "section" "morphological parameter") the parameter to be set
        :param params: ``list`` of real values to be assigned to the parameters

        .. note::
            The parameters and the values must be in appropriate order and the user must guarantee that
            the parameters are in their valid ranges.

        """
        #print section
        if self.option.GetUFunString() == "":
            for sec in section:
                #print sec
                if len(str.split(sec, " ")) == 4:
                    self.model.SetChannelParameters(str.strip(str.split(sec, " ")[0]), str.strip(str.split(sec, " ")[1]), str.strip(str.split(sec, " ")[2]), str.strip(str.split(sec, " ")[3]),
                                                    params[section.index(sec)])

                else:
                    self.model.SetMorphParameters(str.strip(str.split(sec, " ")[0]), str.strip(str.split(sec, " ")[1]), params[section.index(sec)])
        else:
            #cal the user def.ed function
            self.usr_fun(self, params)




    def modelRunner(self, candidates, act_trace_idx):
        """
        Prepares the model for the simulation, runs the simulation and records the appropriate variable.
        If an external simulator is used then it writes the parameters to a file, called "params.param"
        executes command stored in the ``model`` member and tries to read the model's output from a file,
        called "trace.dat".

        :param candidates: the new parameter set generated by the optimization algorithm as a ``list`` of real values
        :param act_trace_idx: used by the external simulator to select current stimulation protocol

        """
        #params=candidates

    
        error=0
        from modelHandler import externalHandler
        if isinstance(self.model, externalHandler):
            pid = str(os.getpid())
            current_time = str(time.time()).replace('.','')
            self.model.record[0] = []
            print('PID ', pid, ' ************')
            
            with open(self.option.base_dir + "/params" + pid + current_time + ".param" , "w") as out_handler:
                for c in candidates:
                    out_handler.write(str(c) + "\n")
                out_handler.write(str(act_trace_idx))
            
            from subprocess import call
            error=call(self.model.GetExec(pid, current_time))

            try:
                with open(self.option.base_dir + '/trace' + pid + current_time + '.dat', "r") as in_handler:
                    for line in in_handler:
                        self.model.record[0].append(float(line.split()[-1]))
            except OSError:
                pass
             
            try:
                with open(self.option.base_dir + '/spike' + pid + current_time + '.dat', "r") as in_handler:
                    self.model.spike_times = []
                    for line in in_handler:
                        self.model.spike_times.append(int(float(line) / (1000.0 / self.option.input_freq)))
                        #print self.model.spike_times[1:10]
            except OSError:
                pass
            
            try:
                os.remove(self.option.base_dir + '/trace' + pid + current_time + '.dat')
                os.remove(self.option.base_dir + '/spike' + pid + current_time + '.dat')
            except OSError:
                pass
            

        else:
            section = self.option.GetObjTOOpt()
            settings = self.option.GetModelRun()#1. is the integrating step dt
            if self.option.type[-1]!= 'features':
                settings.append(self.reader.data.step)
            else:
                settings.append(0.05)
            self.setParameters(section, candidates)
            self.model.RunControll(settings)

        
        return error

    def ReNormalize(self, l):
        """
        Performs a re-normalization based on the parameter bounds specified in the ``option`` object.

        :param l: a ``list`` of real values to be re-normalized

        :return: the re-normalized values in a ``list``

        """
        tmp = []
        for i in range(len(l)):
            tmp.append(l[i] * (self.option.boundaries[1][i] - self.option.boundaries[0][i]) + self.option.boundaries[0][i])
        return tmp




    # spike detection
    def detectSpike(self, vect):
        """
        Detects spikes in the input using the spike detection threshold ``thres`` and generates ``spike_frames``.
        A spike is detected when the input value exceeds the threshold, after some increase, reaches a maximum,
        then drops under the threshold. These events (crossing the threshold while rising, maximum, crossing the threshold while droping)
        are used in the creation of the ``spike_frame`` instance which will represent the detected spike.

        :param vect: the trace as ``list`` of real values

        :return: a ``list`` of ``spike_frame`` instances

        """
        start_pos = 0
        stop_pos = 0
        start = 0
        temp1 = []
        for n in range(len(vect)):
            if vect[n] > self.thres and start == 0:
                start_pos = n
                start = 1
            elif vect[n] < self.thres and start == 1:
                stop_pos = n
                start = 0
                s = spike_frame(start_pos, vect[start_pos], start_pos+vect[start_pos:stop_pos].index(max(vect[start_pos:stop_pos])), max(vect[start_pos:stop_pos]), stop_pos, vect[stop_pos])
                temp1.append(s)
        return temp1


        #calculates the gradient at the given time
    def calc_grad_dif(self, mod_t, exp_t, args):
        """
        Calculates the normalized average squared differences of derivatives of the given traces.
        The gradient is calculated as follows:
        ::

            grad_a=((mod_t[i+1]-mod_t[i-1])/(2*dt))

        where dt is the step between to points in the trace

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: the normalized average squared differences of derivatives where the normalization is done
            by the squared range of the input trace
        """
        dt = self.reader.data.step
        grad_a = 0
        grad_b = 0
        grad_b_list=[]
        tmp = []
        for i in range(1, min(len(mod_t), len(exp_t)) - 1):
            grad_a = ((mod_t[i + 1] - mod_t[i - 1]) / (2 * dt))
            grad_b = ((exp_t[i + 1] - exp_t[i - 1]) / (2 * dt))
            tmp.append((grad_a - grad_b) ** 2)
            grad_b_list.append(grad_b)
        try:
            if self.option.output_level == "1":
                print("grad dif")
                print(fsum(tmp) / len(tmp) / (pow(max(grad_b_list) - min(grad_b_list), 2)))
        except OverflowError:
                return 1

        return fsum(tmp) / len(tmp) / (pow(max(grad_b_list) - min(grad_b_list), 2))



        #compares the number of spikes in the traces
        #counting only traces which are during the stimulus
    def spike_rate(self, mod_t, exp_t, args):
        """
        Calculates the normalized absolute difference in number of spikes that occur during the time of the stimulus.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: the normalized absolute difference in spike numbers

        """
        temp_fit = 0
        window = int(self.option.spike_window)
        stim_dur = self.option.stim_dur
        if stim_dur >= 1e9 or stim_dur==0:
            stim_dur = self.option.input_length
        add_data = args.get("add_data", None)
        spikes = [[], []]
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t[int(self.option.stim_del * self.option.input_freq / 1000):int(self.option.stim_del * self.option.input_freq / 1000 + stim_dur * self.option.input_freq / 1000)])
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))

        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t[int(self.option.stim_del * self.option.input_freq / 1000):int(self.option.stim_del * self.option.input_freq / 1000 + stim_dur * self.option.input_freq / 1000)])
        mod_spike = len(spikes[0])
        exp_spike = len(spikes[1])
        temp_fit += float(abs(mod_spike - exp_spike)) / float(exp_spike + mod_spike + 1)
        if self.option.output_level == "1":
            print("spike rate:")
            print("mod: ", len(spikes[0]))
            print("exp: ", len(spikes[1]))
            print(temp_fit)
        return temp_fit


        #compares the two traces based on the
        #differences in the interspike intervals (isi)
        #normalized
        #returns 2 if model trace has no spikes
        #The value of k was either
        #four ISIs or one-fifth of the total number of ISIs, whichever was the smaller
        #of the two
    def isi_differ(self, mod_t, exp_t, args):
        """
        Calculates the normalized average absolute ISI difference in the two traces.
        The first half of the spikes or the first four spikes (whichever is less) are excluded from the calculation.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        .. note::
            If neither trace contains spikes, the function returns zero.
            If one traces has no spikes, but the other has the function returns one.

        :return: the normalized average absolute ISI difference

        """
        add_data = args.get("add_data", None)
        window = int(self.option.spike_window)
        spikes = [[], []]
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))
        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        tmp = []
        #tmp.append(abs(len(spikes[0])-len(spikes[1]))/max( float(len(spikes[0])),float(len(spikes[1])-1) ))
        if (len(spikes[0]) < 2) and (len(spikes[1]) < 2):
            return 0
        if (len(spikes[0]) < 2) != (len(spikes[1]) < 2):
            return 1
        for s in range(min(len(spikes[0]), len(spikes[1])) - 1):
            tmp.append(abs((spikes[0][s + 1].peak - spikes[0][s].peak)
                        - (spikes[1][s + 1].peak - spikes[1][s].peak)))
        if len(spikes[0]) > len(spikes[1]):
            tmp.append((spikes[0][-1].peak - spikes[0][len(spikes[1])-1].peak))
        elif len(spikes[0]) < len(spikes[1]):
            tmp.append((spikes[1][-1].peak - spikes[1][len(spikes[0])-1].peak))

        if self.option.output_level == "1":
            print("isi difference:")
            print("mod: ", len(spikes[0]))
            print("exp: ", len(spikes[1]))
            print(fsum(tmp), " / ", len(exp_t), " = ", fsum(tmp) / len(exp_t))
        return fsum(tmp) / len(exp_t)


        #compares the two traces based on the latency of the first spikes
    def first_spike(self, mod_t, exp_t, args):
        """
        Calculates the normalized squared latency differences of the first spikes.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        .. note::
            If neither trace contains spikes, the function returns zero.
            If one traces has no spikes, but the other has the function returns one.

        :return: the normalized squared latency differences of the first spikes,
            where the normalization is done by the length of the length of ``exp_t``

        """
        add_data = args.get("add_data", None)
        spikes = [[], []]
        window = int(self.option.spike_window)
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))
        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)

        if (len(spikes[0]) < 1) and (len(spikes[1]) < 1):
            return 0
        if (len(spikes[0]) < 1) != (len(spikes[1]) < 1):
            return 1
        try:
            if self.option.output_level == "1":
                print("first spike")
                print("mod: ", len(spikes[0]))
                print("exp: ", len(spikes[1]))
                print(float(pow(spikes[0][0].start_pos - spikes[1][0].start_pos, 2)) / (len(exp_t)**2))
        except OverflowError:
            print("overflow")
            return 1
        return float(pow(spikes[0][0].start_pos - spikes[1][0].start_pos, 2)) / (len(exp_t)**2)


        #compares the traces based on the spike heights (heights calculated as the following:
        #abs(peak avlue-spike threshold) )
        #normalized
    def AP_overshoot(self, mod_t, exp_t, args):
        """
        Calculates the normalized average squared differences of AP overshoots. Overshoots are defined
        as the difference of the peak value from the threshold.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        .. note::
            Only the first k common spikes are compared, and there is no penalty for one trace
            having more spike than the other.

        .. note::
            If neither trace contains spikes, the function returns zero.
            If one traces has no spikes, but the other has the function returns one.

        :return: the normalized average squared differences of AP overshoots where the normalization is
            done by the maximal peak value in the input trace

        """
        add_data = args.get("add_data", None)
        spikes = [[], []]
        window = int(self.option.spike_window)
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))

        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        if (len(spikes[0]) < 1) and (len(spikes[1]) < 1):
            return 0
        if ((len(spikes[0]) < 1) != (len(spikes[1]) < 1)):
            return 1
        max_amp = max([x.peak_val - self.thres for x in spikes[1]])
        if max_amp == 0:
            max_amp = 1e-12
        tmp = [pow((s1.peak_val - self.thres) - (s2.peak_val - self.thres), 2) for s1, s2 in zip(spikes[0], spikes[1])]
        try:
            if self.option.output_level == "1":
                print("AP oveshoot:")
                print("mod: ", len(spikes[0]))
                print("exp: ", len(spikes[1]))
                print(fsum(tmp) / len(tmp) / (max_amp**2))
            return  fsum(tmp) / len(tmp) / (max_amp**2)
        except OverflowError:
            print("overflow")
            return 1


        #compares the two traces based on the after-hyperpolarization depth
        #basically finds the minimum value between spikes and compares them
        #normalized
        #calculate average value of the minimum voltage between two APs for both traces,
        #take absolute (or squared) difference,
        #normalize by (square of) the range of all exp voltage values
        #(subthreshold range would be even better, but may be more difficult).
    def AHP_depth(self, mod_t, exp_t, args):
        """
        Calculates the normalized squared average of the differences in after-hyperpolarization depth.
        The AHP-depth is defined as the minimum value between two spikes.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        .. note::
            If neither trace contains spikes, the function returns zero.
            If one traces has no spikes, but the other has the function returns one.

        :return: the normalized squared average of the differences in after-hyperpolarization depth,
            where the normalization is done by the squared sub-threshold range of the input trace

        """
        add_data = args.get("add_data", None)
        spikes = [[], []]
        window = int(self.option.spike_window)
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))

        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        if (len(spikes[0]) < 1) and (len(spikes[1]) < 1):
            return 0
        if (len(spikes[0]) < 1) != (len(spikes[1]) < 1):
            return 1
        e = []
        m = []
        for s1, s2 in zip(list(range(len(spikes[0]))), list(range(len(spikes[1])))):
            try:
                m.append(min(mod_t[spikes[0][s1].stop_pos:spikes[0][s2 + 1].start_pos]))
                e.append(min(exp_t[spikes[1][s2].stop_pos:spikes[1][s2 + 1].start_pos]))
            except IndexError:
                m.append(min(mod_t[spikes[0][s1].stop_pos:]))
                e.append(min(exp_t[spikes[1][s2].stop_pos:]))

        avg_e = fsum(e) / len(e)
        avg_m = fsum(m) / len(m)
        sub_t_e = [x for x in exp_t if x < self.thres]
        try:
            if self.option.output_level == "1":
                print("AHP depth:")
                print("mod: ", len(spikes[0]))
                print("exp: ", len(spikes[1]))
                print(pow(avg_e - avg_m, 2) / pow(max(sub_t_e) - min(sub_t_e), 2))
        except OverflowError:
                return 1
        tmp = pow(avg_e - avg_m, 2) / pow(max(sub_t_e) - min(sub_t_e), 2)
        return tmp


        #compares the traces based on the width of the action potentials
        #the width is computed at the base of the spike and at the middle of the spike
        #not normalized
    def AP_width(self, mod_t, exp_t, args):
        """
        Calculates the normalized squared average differences of the width of APs.
        The width is defined as follows:
        ::

            (s1.stop_pos-s1.start_pos)/2

        where s1 is a spike instance

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        .. note::
            If neither trace contains spikes, the function returns zero.
            If one traces has no spikes, but the other has the function returns one.

        :return: the normalized squared average differences of the width of APs, where the normalization
            is done by the average spike width of the input trace

        """
        add_data = args.get("add_data", None)
        spikes = [[], []]
        spikes[0] = self.detectSpike(mod_t)
        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        if (len(spikes[0]) < 1) and (len(spikes[1]) < 1):
            return 0
        if (len(spikes[0]) < 1) != (len(spikes[1]) < 1):
            return 1
        avg1 = []
        avg2 = []
        for s1, s2 in zip(spikes[0], spikes[1]):
            avg1.append((s1.stop_pos - s1.start_pos) / 2)
            avg2.append((s2.stop_pos - s2.start_pos) / 2)


        try:
            if self.option.output_level == "1":
                print("mod: ", len(spikes[0]))
                print("exp: ", len(spikes[1]))
                print("AP width:")
                print(pow((fsum(avg2) / len(avg2) - fsum(avg1) / len(avg1)) / (fsum(avg2) / len(avg2)), 2))
        except OverflowError:
            print("overflow")
            return 1
        return pow((fsum(avg2) / len(avg2) - fsum(avg1) / len(avg1)) / (fsum(avg2) / len(avg2)), 2)


        #calculates the averaged squared error's of the close proximity of spikes
    def calc_spike_ase(self, mod_t, exp_t, args):
        """
        Calculates the normalized average squared differences of the sub-threshold segments of the traces.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: the normalized average squared differences (for details, see calc_ase)

        """
        add_data = args.get("add_data", None)
        #tmp=[]
        spikes = [[], []]
        window = int(self.option.spike_window)
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        elif len(self.model.spike_times)!=0:
            #print "using spike times"
            for sp_t in self.model.spike_times:
                start_pos=sp_t-window
                if start_pos<0:
                    start_pos=0
                start_val=mod_t[start_pos]
                peak_pos=sp_t
                peak_val=mod_t[sp_t]
                end_pos=sp_t+window
                if end_pos>=len(mod_t):
                    end_pos=len(mod_t)-1
                end_val=mod_t[end_pos]

                spikes[0].append(spike_frame(start_pos,start_val,peak_pos,peak_val,end_pos,end_val))

        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        e = copy(mod_t)
        m = copy(exp_t)
        if (len(spikes[1]) < 1) and (len(spikes[0]) < 1):
            return self.calc_ase(mod_t, exp_t, args)
        for s_e in spikes[1]:
            e[int(s_e.start_pos - window):int(s_e.stop_pos + window)] = [0] * (int(s_e.stop_pos + window) - int(s_e.start_pos - window))
            m[int(s_e.start_pos - window):int(s_e.stop_pos + window)] = [0] * (int(s_e.stop_pos + window) - int(s_e.start_pos - window))

        for s_m in spikes[0]:
            m[int(s_m.start_pos - window):int(s_m.stop_pos + window)] = [0] * (int(s_m.stop_pos + window) - int(s_m.start_pos - window))
            e[int(s_m.start_pos - window):int(s_m.stop_pos + window)] = [0] * (int(s_m.stop_pos + window) - int(s_m.start_pos - window))
#        tmp.append(self.calc_ase(a[0:spikes[1][0].start_pos-window],
#                                 b[0:spikes[1][0].start_pos-window],args))
#        for i,s in enumerate(spikes[1]):
#            try:
#                tmp.append(self.calc_ase(a[s.stop_pos+window:spikes[1][i+1].start_pos-window],
#                                         b[s.stop_pos+window:spikes[1][i+1].start_pos-window],args ))
#            except IndexError:
#                tmp.append(self.calc_ase(a[spikes[1][i].stop_pos+window:],b[spikes[1][i].stop_pos+window:],args ))
#        print fsum(tmp)/len(tmp)
        if self.option.output_level == "1":
            print("spike_ase")
            print("mod: ", len(spikes[0]))
            print("exp: ", len(spikes[1]))
            print(self.calc_ase(m, e, args))
        return self.calc_ase(m, e, args)

    def calc_ase(self, mod_t, exp_t, args):
        """
        Calculates the normalized average squared difference of the traces.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: the normalized average squared difference, where the normalization is done by
            the squared range of the input trace

        """
        temp = []
        for n in range(min([len(exp_t), len(mod_t)])):
            try:
                temp.append(pow(exp_t[n] - mod_t[n], 2))
            except OverflowError:
                return 1
            #except TypeError:
            #    return 1
        try:
            if self.option.output_level == "1":
                print("ase")
                print(fsum(temp) / len(temp) / (pow(max(exp_t) - min(exp_t), 2)))
        except OverflowError:
                return 1
        return fsum(temp) / len(temp) / (pow(max(exp_t) - min(exp_t), 2))


    def calc_spike(self, mod_t, exp_t, args):
        """
        Calculates the normalized absolute differences of the number of spikes in the traces.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: the normalized absolute differences of the number of spikes, where the normalization is done
            by the sum of the number of spikes in both traces plus one

        """
        add_data = args.get("add_data", None)
        temp_fit = 0
        spikes = [[], []]
        #window = self.option.spike_window
        if (self.model.spike_times == None):
            spikes[0] = self.detectSpike(mod_t)
        else:
            #only the number of spikes is needed (e.g the length of the timing vector)
            spikes[0] = self.model.spike_times
        #print spikes[0]
        if add_data != None:
            spikes[1] = add_data
        else:
            spikes[1] = self.detectSpike(exp_t)
        mod_spike = len(spikes[0])
        exp_spike = len(spikes[1])
        try:
            #temp_fit+=float(abs(mod_spike-exp_spike))/max( float(exp_spike),float(mod_spike-1) )
            temp_fit += float(abs(mod_spike - exp_spike)) / float(exp_spike + mod_spike + 1)
        except ZeroDivisionError:
            temp_fit += 1
        if self.option.output_level == "1":
            print("spike count")
            print("mod: ", mod_spike)
            print("exp: ", exp_spike)
            print(temp_fit)
        return temp_fit




    def pyelectro_pptd(self, mod_t, exp_t, args):
        """
        Returns error function value from comparison of two phase
        pptd maps as described by Van Geit 2007.

        :param mod_t: the trace obtained from the model as ``list``
        :param exp_t: the input trace as ``list``
        :param args: optional arguments as ``dictionary``

        :return: resulting fitness value

        """
        t_gen = frange(0, self.option.run_controll_tstop + self.option.run_controll_dt, self.option.run_controll_dt)
        t = []
        for n in t_gen:
            t.append(n)
        t = t[0:len(exp_t)]
        mod_t = mod_t[0:len(exp_t)]
        try:
            error = analysis.pptd_error(t, mod_t, t, exp_t, dvdt_threshold=None)

            #normalised_error = analysis.normalised_cost_function(error, 0.001)

            Q = 0.001 # from earlier code - its effect should be tested
            #if Q==None:
            #Q=7/(300*(target**2))
            normalised_error=1-1/(Q*(error)**2+1)

            return normalised_error

        except ValueError:
            return 1

    def get_efel_values(self, traces, feature):

        import warnings
        warnings.filterwarnings("ignore", category=RuntimeWarning)

        traces_results = efel.getFeatureValues(traces,[feature])

        warnings.filterwarnings("default", category=RuntimeWarning)
        return traces_results


    def FFun_for_Features(self, mod_t, features_data, feature, k, args={}):

        exp_mean = 0
        exp_std = 0
        # generating time trace for efel
        t_gen = frange(0, self.option.run_controll_tstop + self.option.run_controll_dt, self.option.run_controll_dt)
        t = []
        for n in t_gen:
            t.append(n)
        t = t[0:len(mod_t)]

        # converting list to numpy array for efel
        mod_t_np=np.array(mod_t)
        t_np=np.array(t)

        temp_fit=0
        trace = {}
        traces=[]
        trace['T'] = t_np
        trace['V'] = mod_t_np
        trace['stim_start'] = [self.option.stim_del]
        trace['stim_end'] = [self.option.stim_del + self.option.stim_dur]
        traces.append(trace)

        efel.setThreshold(self.thres)

        '''

        used_features=list(features)

        AP_num = efel.getFeatureValues(traces,['Spikecount'])
        for i in range (len(features)):
            if AP_num[0]['Spikecount'] == 0 and features_data[features[i]]["requires_spike"]=="True":
                used_features.remove(features[i])
                temp_fit += 10  #MEnnyi legyen a bunti?

            if AP_num[0]['Spikecount'] <2 and "ISI" in features_data[features[i]]:
                used_features.remove(features[i])
                temp_fit += 1

        '''

        #traces_results = efel.getFeatureValues(traces,[feature])      #list
        traces_results = self.get_efel_values(traces, feature)
        #print traces_results

        exp_mean = features_data[feature]["mean"][k]
        exp_std = features_data[feature]["std"][k]
        mod_result=traces_results[0][feature]
        #print feature

        #print "exp mean", exp_mean
        #print "exp std", exp_std
        #print "model", mod_result

        if mod_result is not None and mod_result.size > 1:
            mod_result = scipy.mean(mod_result)      #for features (AHP_depth, AP_duration_half_width) that gives a list as a result, the mean of the results is used
        elif mod_result is not None and mod_result.size!=0:                    # mod_result is a numpy array with one element, 0 element for AP1_amp or APlast_amp if no AP generated by the model
            mod_result=mod_result[0]

        if (mod_result == None or mod_result == 0 or mod_result.size==0) and (exp_mean != None and exp_std != None):
            temp_fit=250
        elif exp_mean == None and exp_std == None :
            temp_fit=0
        #elif exp_mean != None and exp_std != None :
        else:
            result = abs(exp_mean - mod_result) / exp_std
            temp_fit = result

        #print temp_fit
        return temp_fit

    def combineFeatures(self, candidates, args={}):
        """
        Creates the weighted combination of fitness functions and calculates the combined fitness for every
        set of parameters created during the optimization proccess by seting the model parameters,
        running the simulation and evaluating the resulting trace. The selected fitness functions and the
        weights are determined from the ``option`` object.
        determined

        :param candidates: the candidates generated by the algorithm as a ``list`` of ``lists``
        :param args: optional arguments

        .. note::
            If additional information is loaded as well, then it's passed to the fitness functions along with
            the actual data traces.

        :return: the ``list`` of fitness values corresponding to the parameter sets

        """
        #modelHandler.modelHandlerNeuron(self.option.model_path,self.option.model_spec_dir,self.option.base_dir)
        self.fitnes = []
        features = self.option.feats

        #print self.option.feats   #--> [<bound method fF.AP1_amp_abstr_data of <fitnessFunctions.fF instance at 0x7f669e957128>>] (ezt adja)
        weigths = self.option.weights
        temp_fit = 0
        if self.option.type[-1]!= 'features':
            window = int(self.option.spike_window)
        else:
            window=None
        if(self.option.simulator == 'Neuron'):
            self.model.load_neuron()

        try:
            #self.model.load_neuron()
            s = self.option.GetUFunString()
            s = str.replace(s, "h.", "self.model.hoc_obj.")
            exec(compile(str.replace(s, "h(", "self.model.hoc_obj("), '<string>', 'exec'))
            self.usr_fun_name = self.option.GetUFunString().split("\n")[4][self.option.GetUFunString().split("\n")[4].find(" ") + 1:self.option.GetUFunString().split("\n")[4].find("(")]
            self.usr_fun = locals()[self.usr_fun_name]
        except SyntaxError:
            print("Your function contained syntax errors!! Please fix them!")
        except IndexError:
            pass


        self.model.CreateStimuli(self.option.GetModelStim())

        if self.option.type[-1]!= 'features':
            k_range=self.reader.number_of_traces()
        else:
            k_range=len(self.reader.features_data["stim_amp"])


        for l in candidates:
            if self.option.output_level == "1":
                print(l)
            l = self.ReNormalize(l)
            if self.option.output_level == "1":
                print(l)
            for k in range(k_range):     #for k in range(self.reader.number_of_traces()):
                try:
                    add_data = [spike_frame(n - window, self.thres, n, 1, n + window, self.thres) for n in self.reader.additional_data.get(k)]
                except AttributeError:
                    add_data = None
                args = {}
                args["add_data"] = add_data
                param = self.option.GetModelStimParam()
                parameter = param
                parameter[0] = param[0][k]
                if isinstance(parameter[0], str):
                    self.model.SetCustStimuli(parameter)
                else:
                    extra_param = self.option.GetModelRun()
                    self.model.SetStimuli(parameter, extra_param)
                if (not self.modelRunner(l,k)):
                    if self.option.output_level == "1":
                        print(features, weigths)
                    if (self.option.type[-1]!='features'):
                        for f, w in zip(features, weigths):
                            if abs(len(self.model.record[0])-len(self.reader.data.GetTrace(k)))>1:
                                raise sizeError("model: " + str(len(self.model.record[0])) + ", target: " + str(len(self.reader.data.GetTrace(k))))
                            temp_fit += w * (f(self.model.record[0],
                                                              self.reader.data.GetTrace(k), args))

                    else:
                        for f, w in zip(features, weigths):
                            temp_fit += w * self.FFun_for_Features(self.model.record[0],
                                                                self.reader.features_data, f, k, args)
                else:
                        temp_fit=100
            self.fitnes.append(temp_fit)
            if self.option.output_level == "1":
                print("current fitness: ",temp_fit)
            temp_fit = 0

        if(self.option.simulator == 'Neuron'):
            self.model=modelHandler.modelHandlerNeuron(self.option.model_path,self.option.model_spec_dir,self.option.base_dir)

        print('\n fitnes {}\n'.format(self.fitnes))

        return self.fitnes

    def getErrorComponents(self, index_of_trace, model_output):
        """
        Creates the components of the fitness value for a pair of traces using the fitness functions
        and the weigths specified in the ``option`` object.

        :param index_of_trace: the index of the input trace (in case of multiple traces)
        :param model_output: the model trace as ``list``

        :return: a ``list`` containing the weight, the function instance, and the component's fitness value
            for every function instance i.e every component

        """

        features = self.option.feats
        weigths = self.option.weights
        fit_list = []
        window = self.option.spike_window
        try:
            add_data = [spike_frame(n - window, 0, n, 1, n + 50, 0) for n in self.reader.additional_data.get(index_of_trace)]
        except AttributeError:
            add_data = None
        args = {}
        args["add_data"] = add_data
        if (self.option.type[-1]!='features'):
            for f, w in zip(features, weigths):
                fit_list.append([w, f, (f(model_output, self.reader.data.GetTrace(index_of_trace), args))])
        else:
            for f, w in zip(features, weigths):
                fit_list.append([w, f, self.FFun_for_Features(model_output,
                                                    self.reader.features_data, f, index_of_trace, args)])# index_of_trace is index of stim_amp here
        return fit_list


    def MooFeatures(self, candidates, args={}):
        """
        Creates the weighted combination of fitness functions and calculates the combined fitness for every
        set of parameters created during the optimization proccess by seting the model parameters,
        running the simulation and evaluating the resulting trace. The selected fitness functions and the
        weights are determined from the ``option`` object.
        determined

        :param candidates: the candidates generated by the algorithm as a ``list`` of ``lists``
        :param args: optional arguments

        .. note::
            If additional information is loaded as well, then it's passed to the fitness functions along with
            the actual data traces.

        :return: the ``list`` of fitness values corresponding to the parameter sets

        """

        self.fitnes = []
        features = self.option.feats

        #print self.option.feats   #--> [<bound method fF.AP1_amp_abstr_data of <fitnessFunctions.fF instance at 0x7f669e957128>>] (ezt adja)
        weigths = self.option.weights
        temp_fit = []
        if self.option.type[-1]!= 'features':
            window = int(self.option.spike_window)
        else:
            window=None
        self.model.CreateStimuli(self.option.GetModelStim())

        if self.option.type[-1]!= 'features':
            k_range=self.reader.number_of_traces()
        else:
            k_range=len(self.reader.features_data["stim_amp"])

        for l in candidates:
            if self.option.output_level == "1":
                print(l)
            l = self.ReNormalize(l)
            if self.option.output_level == "1":
                print(l)
            for k in range(k_range):     #for k in range(self.reader.number_of_traces()):
                try:
                    add_data = [spike_frame(n - window, self.thres, n, 1, n + window, self.thres) for n in self.reader.additional_data.get(k)]
                except AttributeError:
                    add_data = None
                args = {}
                args["add_data"] = add_data
                param = self.option.GetModelStimParam()
                parameter = param
                parameter[0] = param[0][k]
                if isinstance(parameter[0], str):
                    self.model.SetCustStimuli(parameter)
                else:
                    extra_param = self.option.GetModelRun()
                    self.model.SetStimuli(parameter, extra_param)
                if (not self.modelRunner(l,k)):
                    if self.option.output_level == "1":
                        print(features, weigths)
                    if (self.option.type[-1]!='features'):
                        for f, w in zip(features, weigths):
                            if abs(len(self.model.record[0])-len(self.reader.data.GetTrace(k)))>1:
                                raise sizeError("model: " + str(len(self.model.record[0])) + ", target: " + str(len(self.reader.data.GetTrace(k))))
                            temp_fit.append( (f(self.model.record[0],
                                                              self.reader.data.GetTrace(k), args)))

                    else:
                        for f, w in zip(features, weigths):
                            temp_fit.append( self.FFun_for_Features(self.model.record[0],
                                                                self.reader.features_data, f, k, args))
                else:
                        temp_fit.append(0)

            print(temp_fit)
            self.fitnes.append(ec.emo.Pareto(tuple(temp_fit)))

            if self.option.output_level == "1":
                print("current fitness: ",temp_fit)
            del temp_fit[:]         #remove list elements


        return self.fitnes
