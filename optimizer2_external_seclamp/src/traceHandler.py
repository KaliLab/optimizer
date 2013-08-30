import os
import sys
import string
import re

scales={"V/A":0.001,"mV/mA":1,"uV/uA":1000,"nV/nA":10**6,"pV/pA":10**9}
# generating doubles in the range with the given step
def real_range(start, step, end):
    return [float(n)*step for n in range(start,end)]

    
# exception class to handle zero size containers and too short strings
class sizeError(Exception):
    def __init__(self,massage):
        print "There was an error with the size/length of an object, probably not enough element in container. "
        print "Check the no_traces variable!"
        print massage
        sys.exit("Exiting...")
        
# class to handle traces (matrix form)
# stores the data, the scale, it's length, and the sampling frequency, 
# also calculates the necessary dt step for neuron 
class SpikeTimes():
    def __init__(self,dictionary,trace_type="spikes"):
        self.dict=dictionary       
        self.type=trace_type
        
        
class Trace:
    
    def __init__(self,no_traces,scale="mV/mA",t_length=1000,freq=100,trace_type=None):
        self.scale=scale
        self.t_length=t_length
        self.freq=freq
        self.step=float(1000/float(self.freq))
        self.no_traces=no_traces
        self.data=[]
        self.curent_scale=""
        self.type=trace_type
        try:
            self.curent_scale=scales[self.scale]
        except KeyError:
            print self.scale + "\n"
            sys.exit("Unknown voltage format, please choose one of the following: V, mV, uV, nV, pV \nExiting...\n")
            
    def SetTrace(self,d):
        self.data.append(d)
    # converts a hoc vector to python list
    def Convert(self,hoc_obj):
        temp=[]
        for n in range(int(hoc_obj.size())):
            temp.append(hoc_obj.x[n])
        self.SetTrace(temp)
        
    def Print(self):
        print "\n".join(map(str,(n for n in self.data)))
    # returns one column from the data matrix: returns one trace    
    def GetTrace(self,index):
        if index>self.no_traces:
            raise sizeError("There is no " + index + "trace in the structure")
        #print [n[index] for n in self.data]
        return [n[index] for n in self.data]
    

    def reScale(self,value):
        return value/self.curent_scale


class DATA():
    def __init__(self):
        self.data=None
        self.additional_data=None
        self.path_list=[]
        
    def number_of_traces(self):
        return self.data.no_traces
    
    def get_type(self):
        return self.data.type
    
    
    
    def detect_format(self,line):
    #TODO
    #neuron_rule recognizes traces with time
        #need more rule for spike timings and other
        pynn_rule=re.compile("# variable = [a-zA-Z]")
        neuron_rule_time=re.compile("[0-9]*(.[0-9]*)?\t-?[0-9]*(.[0-9]*)?")
        neuron_rule=re.compile("-?[0-9]*(.[0-9]*)?")
        spike_times_rule=re.compile("# variable = spikes")
        rules=[pynn_rule,neuron_rule_time,neuron_rule,spike_times_rule]
        result=[n!=None for n in [re.match(k,line) for k in rules ] ]
        print result
        print result.index(True)
        return [self.PyNNReader,self.traceReaderTime,self.traceReader,self.spikeTimeReader][result.index(True)]
    
    def Read(self,path=[os.getcwd()+"/inputTrace.txt"],no_traces=1,scale="mV",t_length=1000,freq=1000,trace_type="voltage"):
        self.path_list.append(path)
        f=open(path[0],"r")
        i=0
        tmp=[]
        while(i<9):
            tmp.append(f.readline())
            i+=1
        if trace_type.upper()!="SPIKE TIMES":
            self.data=self.detect_format(tmp[4])(path,no_traces,scale,t_length,freq,trace_type)
        else:
            self.additional_data=self.spikeTimeReader(path, no_traces, scale, t_length, freq, trace_type)
        
        
    def traceReader(self,path,no_traces,scale,t_length,freq,trace_type):        
        trace=Trace(no_traces, scale, t_length, freq,trace_type)
        print "no time"
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
        trace=Trace(no_traces, scale, t_length, freq,trace_type)
        print "time"
        for my_file in path:
            try:
                data_file=open(my_file,'r')
                for line in data_file:
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
                data_file.close()     
            except IOError:
                sys.exit("Can't open data file at " + self.full_path + " ! Exiting...")
        return trace
    
    def Print(self):
        print self.data
        print "\n"
        print self.t
       

    def PyNNReader(self,path,no_traces,scale,t_length,freq,trace_type):
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
                        tmp_dict[tmp[1]]=[float(tmp[0])]
        trace.data=map(list,zip(*(tmp_dict.values())))
        print len(self.data),len(self.data[0])
        print self.data[0][0:10]
        return trace
        
    def spikeTimeReader(self,path,no_traces,scale,t_length,freq,trace_type):
        for my_file in path:
            tmp_dict={}
            f=open(my_file,"r")
            for l in f:
                if l[0]=="#":
                    continue
                else:
                    tmp=l.strip().split()
                    try:
                        tmp_dict[int(tmp[1])].extend([float(tmp[0])])
                    except KeyError:
                        tmp_dict[int(tmp[1])]=[float(tmp[0])]
        
        self.additional_data=tmp_dict
# class to write data to file            
class traceWriter(Trace):
    #it receives a trace object and other settings
    #comment: comments to the file
    # flag_w: writes the recording data to the file
    # flag_m: writes the results to multiple files (columnwise)
    # separator: separating character in the file
    def __init__(self,tr_object,full_path,comment="",flag_write=1,sep="\n",flag_multi=0):
        Trace.__init__(self, tr_object.no_traces, tr_object.scale, tr_object.t_length, tr_object.freq)
        self.comment=comment
        self.path=full_path
        self.flag_w=flag_write
        self.flag_m=flag_multi
        self.separator=sep
        self.SetTrace(tr_object.data)
    def Write(self):
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
            
                
            
            
                
    
    