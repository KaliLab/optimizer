import os
import sys
import string
import re
import json
import collections

voltage_scales={"V":0.001,"mV":1,"uV":10**3}
current_scales={"uA":10**(-3),"nA":1,"pA":10**3}
features_scales={"V":0.001,"mV":1,"uV":10**3, "uA":10**(-3),"nA":1,"pA":10**3}
scales={"voltage" : voltage_scales, "current" : current_scales, "features" : features_scales, "other" : {"none" : 1}, "spike" : {"none" : 1}}
# generating doubles in the range with the given step
def real_range(start, step, end):
    """
    Not in use!
    Generates real values from the given range.

    :param start: begin of range
    :param step: step between the values
    :param end: the end of the range

    :return: ``list`` of real values

    """
    return [float(n)*step for n in range(start,end)]


# exception class to handle zero size containers and too short strings
class sizeError(Exception):
    """
    Exception class used by the trace handling related objects.

    :param message: error message to be displayed

    """
    def __init__(self,message):
        self.m=message
        print "There was an error with the size/length of an object, probably not enough element in container. "
        print message



class SpikeTimes():
    """
    Not in use!
    Stores spike times in ``dictionary`` indexed by the cell's id.

    :param dictionary: the ``dictionary`` which contains the data
    :param trace_type: type of the trace (should be fixed to "spikes")

    """
    def __init__(self,dictionary,trace_type="spikes"):
        self.dict=dictionary
        self.type=trace_type


class Trace:
    """
    Trace set object. Stores a trace set of a given type with every relevant data.

    :param no_traces: number of traces held by the object
    :param scale: the unit of the data (required for conversions)
    :param t_length: length of the trace(s)
    :param freq: sampling frequency
    :param trace_type: type of the trace set

    :attr: data:
        the traces are contained in the attribute named ``data`` in the order they were in the input file

    .. note::
        The sampling rate should be uniform in the set.

    .. note::
        The length of the traces should be the same, or the length of the shortest one
        should be considered.

    .. note::
        If the type of the trace is not recognized, the program will abort.
        The recognized types are "voltage", "current" and "other" ("spike" is not available yet).

    """
    def __init__(self,no_traces,scale="milli",t_length=1000,freq=100,trace_type=None):
        self.scale=scale
        self.t_length=t_length
        self.freq=freq
        self.no_traces=no_traces
        self.data=[]
        self.curent_scale=1
        self.type=trace_type
        if self.type=='features':
            self.step=None
        else:
            self.step=float(1000/float(self.freq))

        try:
            self.curent_scale=scales.get(trace_type,{}).get(self.scale,1)
        except KeyError:
            print self.scale + "\n"
            sys.exit("Unknown prefix")

    def SetTrace(self,d):
        """
        Adds the given trace to the container.

        :param d: ``list`` containing the trace

        """
        self.data.append(d)
    # converts a hoc vector to python list
    def Convert(self,hoc_obj):
        """
        Converts a hoc vector into a python ``list`` and stores it in the container.

        :param hoc_obj: a hoc vector object

        """
        temp=[]
        for n in range(int(hoc_obj.size())):
            temp.append(hoc_obj.x[n])
        self.SetTrace(temp)

    def Print(self):
        """
        Prints the contained data. Created for debugging purpose.
        """
        print "\n".join(map(str,(n for n in self.data)))
    # returns one column from the data matrix: returns one trace
    def GetTrace(self,index):
        """
        Returns the trace having the index ``index`` form the container. Always use this function to get a given
        trace as they are stored in a non intuitive way and direct access would probably cause errors.

        :param index: the index of the trace to get

        .. note::
            If the given index is out of range, a ``sizeError`` is raised.

        :return: the required trace

        """
        if index>self.no_traces:
            raise sizeError("There is no " + index + "trace in the structure")
        #print [n[index] for n in self.data]
        return [n[index] for n in self.data]


    def reScale(self,value):
        """
        Re-scales the given value based on the scale of the ``Trace`` object.

        :param value: the value to be rescaled

        :return: the rescaled value

        """
        return value/self.curent_scale


class DATA():
    """
    The main data container class.
    :attr: data: holds the ``Trace`` object which contains the trace set

    .. note::
        This class will be able to hold multiple data sets with multiple types.

    """
    def __init__(self):
        self.data=None
        self.additional_data=None
        self.features_data=None
        self.path_list=[]
        self.features_dict={}

    def number_of_traces(self):
        """
        Gets the number of traces held by the object.

        :return: number of traces

        """
        '''
        if data_type!='features':
            return int(self.data.no_traces)
        else:
            return int(len(self.features_data["stim_amp"]))
        '''
        return int(self.data.no_traces)

    def get_type(self):
        """
        Gets the type of the trace set.

        :return: type

        """
        return self.data.type



    def detect_format(self,line):
        """
        Automatically detects the format of the file and returns a reader functions which can process it correctly.
        The recognized formats are the following:

            * simple text file with data columns separated by "\\\\t"
            * simple text file, containing time trace as well and data columns separated by "\\\\t"
            * default recording result from PyNN with 9 line of headers
            * spike timing file from PyNN with 9 line of headers (not used)

        :param line: one line from the file, which the recognition is based on

        :return: a reader function

        """
    #TODO
    #need more rule for spike timings and other
        pynn_rule=re.compile("# variable = [a-zA-Z]")
        neuron_rule_time=re.compile("[0-9]*(.[0-9]*)?\s-?[0-9]*(.[0-9]*)?")
        neuron_rule=re.compile("-?[0-9]*(.[0-9]*)?$|(-?[0-9]*(.[0-9]*)?\t)")
        spike_times_rule=re.compile("# variable = spikes")
        rules=[pynn_rule,neuron_rule_time,neuron_rule,spike_times_rule]
        result=[n!=None for n in [re.match(k,line) for k in rules ] ]
        #print result
        #print result.index(True)
        return [self.PyNNReader,self.traceReaderTime,self.traceReader,self.spikeTimeReader][result.index(True)]

    def Read(self,path=[os.getcwd()+"/inputTrace.txt"],no_traces=1,scale="mV",t_length=1000,freq=1000,trace_type="voltage"):
        """
        The main reader function. This calls the recognition function ``detect_format``
        and uses the obtained reader function to read the data.

        :param path: list of data path(s) (currently only one file is handled)

        (see the explanation of the other parameters in the description of ``Trace``)

        .. note::
            The function uses the 5. line of the file for recognition.

        """
        self.path_list.append(path)
        #print path
        f=open(path[0],"r")
        i=0
        tmp=[]
        while(i<9):
            tmp.append(f.readline())
            i+=1
        if trace_type=="spike":
            self.additional_data=self.spikeTimeReader(path, no_traces, scale, t_length, freq, trace_type)
        elif trace_type=="features":
            self.features_data=self.abstractDataReader(path)
        else:
            self.data=self.detect_format(tmp[4])(path,no_traces,scale,t_length,freq,trace_type)


        #print self.data.data[0:10]


    def traceReader(self,path,no_traces,scale,t_length,freq,trace_type):
        """
        Reads a simple text file with data columns separated by "\t".
        (the parameters are the same as in the ``Read`` function)

        :return: a ``trace`` object holding the content of the file

        .. note::
            If the given file is not accessible the program will abort.

        .. note::
            If the number of traces in the file and the corresponding parameter is not equal,
            a ``sizeError`` is raised.

        """
        trace=Trace(no_traces, scale, t_length, freq,trace_type)
        #print "no time"
        #print trace.type
        for my_file in path:
            try:
                data_file=open(my_file,'r')
                for line in data_file:
                    temp=map(trace.reScale,map(float,line.split()[0:trace.no_traces]))
                    if len(temp)<1:
                        raise sizeError("Data_matrix is empty!\n")
                    else:
                        trace.SetTrace(temp)
                data_file.close()
            except IOError:
                sys.exit("Can't open data file at " + my_file + " ! Exiting...")
        return trace




    def traceReaderTime(self,path,no_traces,scale,t_length,freq,trace_type):
        """
        Reads a simple text file, containing time trace as well and data columns separated by "\\t".
        (the parameters are the same as in the ``Read`` function)

        :return: a ``trace`` object holding the content of the file

        .. note::
            If the given file is not accessible the program will abort.

        .. note::
            If the number of traces in the file and the corresponding parameter is not equal,
            a ``sizeError`` is raised.

        """
        trace=Trace(no_traces, scale, t_length, freq,trace_type)
        #print "time"
        for my_file in path:
            try:
                data_file=open(my_file,'r')
                for line in data_file:
                    try:
                        temp=map(trace.reScale,map(float,line.split()))
                        temp.reverse()
                        temp.pop()
                        temp.reverse()
                    #print temp
                        if len(temp)==trace.no_traces:
                            #self.t.append(real_range(0,self.step,int(self.t_length)))
                            trace.SetTrace(temp)
                        else:
                            raise sizeError("The input file probably does not contain the time. Please check the settings!\n")
                    except ValueError:
                        continue
                data_file.close()
            except IOError:
                sys.exit("Can't open data file at " + self.full_path + " ! Exiting...")
        return trace



    def PyNNReader(self,path,no_traces,scale,t_length,freq,trace_type):
        """
        Reads a default recording result from PyNN with 9 line of headers
        (the parameters are the same as in the ``Read`` function)

        :return: a ``trace`` object holding the content of the file

        .. note::
            If the given file is not accessible the program will abort.

        .. note::
            If the number of traces in the file and the corresponding parameter is not equal,
            a ``sizeError`` is raised.

        """
        trace=Trace(no_traces, scale, t_length, freq,trace_type)
        for my_file in path:
            tmp_dict={}
            f=open(my_file,"r")
            for l in f:
                if l[0]=="#":
                    continue
                else:
                    tmp=l.strip().split()
                    try:
                        tmp_dict[tmp[1]].extend([trace.reScale(float(tmp[0]))])
                    except KeyError:
                        tmp_dict[tmp[1]]=[trace.reScale(float(tmp[0]))]
        trace.data=map(list,zip(*(tmp_dict.values())))
        #print len(self.data),len(self.data[0])
        #print self.data[0][0:10]
        return trace

    def spikeTimeReader(self,path,no_traces,scale,t_length,freq,trace_type):
        """
        Not available yet!
        Reads a spike timing file from PyNN with 9 line of headers
        (the parameters are the same as in the ``Read`` function)

        :return: a ``dictionary`` object holding the content of the file

        .. note::
            If the given file is not accessible the program will abort.

        .. note::
            If the number of traces in the file and the corresponding parameter is not equal,
            a ``sizeError`` is raised.

        .. note::
            In the future, it will return a ``SpikeTimes`` object instead.

        """
        for my_file in path:
            tmp_dict={}
            f=open(my_file,"r")
            for l in f:
                if l[0]=="#":
                    continue
                else:
                    tmp=l.strip().split()
                    try:
                        tmp_dict[int(float(tmp[1]))].extend([float(tmp[0])])
                    except KeyError:
                        tmp_dict[int(float(tmp[1]))]=[float(tmp[0])]
        no_spike_ind=list(set(range(no_traces))-set(tmp_dict.keys()))
        for i in no_spike_ind:
            tmp_dict[i]=[]
        self.additional_data=tmp_dict

    def convert(self, dict_to_conv):
        if isinstance(dict_to_conv, basestring):
            return str(dict_to_conv)
        elif isinstance(dict_to_conv, collections.Mapping):
            return dict(map(self.convert, dict_to_conv.iteritems()))
        elif isinstance(dict_to_conv, collections.Iterable):
            return type(dict_to_conv)(map(self.convert, dict_to_conv))
        else:
            return dict_to_conv


    def abstractDataReader(self,path):

        for my_file in path:
            data_dict={}
            data_dict = collections.OrderedDict(sorted(data_dict.items()))
            #self.features_dict={}
            amps_keys=[]
            amplitude_keys=[]
            try:
                with open(my_file) as f:
                    self.features_dict = json.load(f, object_pairs_hook=collections.OrderedDict)


                data_dict["stim_amp"]=self.features_dict["stimuli"]["amplitudes"]
                data_dict["stim_delay"]=self.features_dict["stimuli"]["delay"]
                data_dict["stim_duration"]=self.features_dict["stimuli"]["duration"]
                features_names=self.features_dict["features"].keys()
                for i in range (len(features_names)):
                    data_dict[features_names[i]]={}
                    data_dict[features_names[i]]["mean"]=[None]*len(data_dict["stim_amp"])
                    data_dict[features_names[i]]["std"]=[None]*len(data_dict["stim_amp"])
                    data_dict[features_names[i]]["weight"]=self.features_dict["features"][features_names[i]]["weight"]
                    #data_dict[features_names[i]]["requires_spike"]=self.features_dict["features"][features_names[i]]["requires_spike"]

                    amps_keys=self.features_dict["features"][features_names[i]].keys()
                    amps_keys.pop(0)
                    for j in range(len(amps_keys)):
                        amp=float(amps_keys[j].split('_',1)[1])
                        amp_index=data_dict["stim_amp"].index(amp)
                        data_dict[features_names[i]]["mean"][amp_index]=self.features_dict["features"][features_names[i]][amps_keys[j]]["Mean"]
                        data_dict[features_names[i]]["std"][amp_index]=self.features_dict["features"][features_names[i]][amps_keys[j]]["Std"]

            except IOError:
                sys.exit("Can't open data file at " + my_file + " ! Exiting...")
        return data_dict



# class to write data to file
#it receives a trace object and other settings
#comment: comments to the file
# flag_w: writes the recording data to the file
# flag_m: writes the results to multiple files (columnwise)
# separator: separating character in the file
class traceWriter(Trace):
    """
    Not used!
    Writes the content of the given trace object to the given file(s).

    :param tr_object: trace object which must have ``data`` attribute
    :param full_path: the path of the output file
    :param comment: some header information
    :param flag_write: indicates if the properties of the trace is written or not
    :param sep: data separator ``string``
    :param flag_multi: indicates if the separate traces should be written into separate files

    """
    def __init__(self,tr_object,full_path,comment="",flag_write=1,sep="\n",flag_multi=0):
        Trace.__init__(self, tr_object.no_traces, tr_object.scale, tr_object.t_length, tr_object.freq)
        self.comment=comment
        self.path=full_path
        self.flag_w=flag_write
        self.flag_m=flag_multi
        self.separator=sep
        self.data=tr_object.data
    def Write(self):
        """
        Performs the writing.

        .. note::
            If ``flag_multi`` was set to true, then the traces will be written to multiple files.

        """
        if self.flag_m==1:
            for f_n in self.no_traces:
                f=open(self.path[f_n],'w')
                f.write(self.comment)
                if self.flag_w==1:
                    f.write(str(self.scale) + " " + str(self.t_length) + " " + str(self.freq) + "\n")
                f.write(self.GetTrace(f_n))
        else:
            f=open(self.path[0],'w')
            f.write(self.comment+"\n")
            if self.flag_w==1:
                f.write(str(self.scale) + " " + str(self.t_length) + " " + str(self.freq) + "\n")
            for n in self.data:
                temp=map(str,n)
                f.write(self.separator.join(string.strip(k,"[]") for k in temp))
                f.write("\n")
