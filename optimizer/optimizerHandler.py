from random import Random
#from time import time
from inspyred import ec
from inspyred.ec import emo
from inspyred.ec import terminators
from inspyred.ec import variators
from inspyred.ec import observers
from fitnessFunctions import fF,frange
#from fitnessFunctions import *
import sys
import inspyred
import logging
from scipy import optimize, array, ndarray
from numpy import random
import numpy as np
import copy
import array as array1
import random
import json
from functools import partial
import numpy

from math import sqrt

from deap import algorithms
from deap import base
from deap import benchmarks
from deap.benchmarks.tools import diversity, convergence, hypervolume
from deap import creator
from deap import tools
#from Image import NONE
#from jinja2._stringdefs import No
#from math import exp

#from inspyred.ec.terminators import max_evaluations

import multiprocessing
from math import sqrt
from optionHandler import optionHandler
from deap import algorithms
from deap import base
from deap import benchmarks
from deap.benchmarks.tools import diversity, convergence, hypervolume
from deap import creator
from deap import tools
#from Image import NONE
#from jinja2._stringdefs import No
#from math import exp
import Queue
import Core
#from inspyred.ec.terminators import max_evaluations
import cPickle as pickle

from pybrain.optimization.distributionbased.distributionbased import DistributionBasedOptimizer
from scipy import dot, exp, log, sqrt, floor, ones, randn
from pybrain.tools.rankingfunctions import RankingFunction

global moo_var
global brain_var
moo_var=False
brain_var=False

def setmodparams(reader_obje,model_obje,option_obje):
    global option
    global reader
    global model
    global usr_fun
    option=option_obje
    reader=reader_obje
    model=model_obje


def setmods(hoc_ob,secs):
    global hoc_obj
    global sections
    hoc_obj=hoc_ob
    sections=secs

def uniformz(random,size,bounds):
    """
    Creates random values from a uniform distribution. Used to create initial population.

    :param random: random number generator object
    :param args: ``dictionary``, must contain key "num_params" and either "_ec" or "self"

    :return: the created random values in a ``list``

    """
    candidate=[]
    for n in range(int(size)):
        candidate.append(random.uniform(bounds.lower_bound[n],bounds.upper_bound[n]))
    return candidate

def SetChannelParameters(section,segment,channel,params,values):
    """
    Sets the given channel's parameter to the given value. If the section is not known that
    indicates a serious internal error and the program will abort.

    :param section: the selected section's name as ``string``
    :param channel: the selected channel's name as ``string``
    :param params: the selected channel parameter's name as ``string``
    :param values: the value to be set

    """
    try:
        sections[section].push()
    except KeyError:
        sys.exit("No section named " + str(section) + " was found!")
    sec = hoc_obj.cas()
    lseg = [seg for seg in sec]
    #self.hoc_obj.cas().__setattr__(params,values)
    lseg[int(segment)].__setattr__(params,values)
    hoc_obj.pop_section()

def setParameters(section, params):
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
    from string import split, strip, replace
    #print section
    if option.GetUFunString() == "":
        for sec in section:
            if len(split(sec, " ")) == 4:
                SetChannelParameters(strip(split(sec, " ")[0]), strip(split(sec, " ")[1]), strip(split(sec, " ")[2]), strip(split(sec, " ")[3]),params[section.index(sec)])
            else:
                model.SetMorphParameters(strip(split(sec, " ")[0]), strip(split(sec, " ")[1]), params[section.index(sec)])
                #print 'setparams22'
    else:
        #cal the user def.ed function
        try:
            s = option.GetUFunString()
            print s
            s = replace(s, "h.", "self.model.hoc_obj.")
            exec(compile(replace(s, "h(", "self.model.hoc_obj("), '<string>', 'exec'))
            usr_fun_name = option.GetUFunString().split("\n")[4][option.GetUFunString().split("\n")[4].find(" ") + 1:option.GetUFunString().split("\n")[4].find("(")]
            usr_fun = locals()[usr_fun_name]
            usr_fun(fF(reader,model,option),params)
        except SyntaxError:
            print "Your function contained syntax errors!! Please fix them!"
        except IndexError:
            pass

def modelRunner(candidates, act_trace_idx):
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
    if isinstance(model, externalHandler):
        model.record[0] = []
        out_handler = open(option.base_dir + "/params.param", "w")
        for c in candidates:
            out_handler.write(str(c) + "\n")
        out_handler.write(str(act_trace_idx))
        out_handler.close()
        from subprocess import call
        error=call(model.GetExec())
        in_handler = open(option.base_dir + "/trace.dat", "r")
        for line in in_handler:
            model.record[0].append(float(line.split()[-1]))
        in_handler.close()
        try:
            in_handler = open(option.base_dir + "/spike.dat", "r")
            model.spike_times = []
        except OSError:
            pass
        for line in in_handler:
            model.spike_times.append(int(float(line) / (1000.0 / option.input_freq)))
            #print model.spike_times[1:10]
    else:
        section = option.GetObjTOOpt()
        settings = option.GetModelRun()#1. is the integrating step dt
        if option.type[-1]!= 'features':
            settings.append(reader.data.step)
        else:
            settings.append(0.05)
        setParameters(section, candidates)
        model.RunControll(settings)


    return error




def ReNormalize(l):
    """
    Performs a re-normalization based on the parameter bounds specified in the ``option`` object.

    :param l: a ``list`` of real values to be re-normalized

    :return: the re-normalized values in a ``list``

    """
    tmp = []
    for i in range(len(l)):
        tmp.append(l[i] * (option.boundaries[1][i] - option.boundaries[0][i]) + option.boundaries[0][i])
    return tmp


def combineFeatures(candidates, args={}):
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

    fitnes = []
    #option=optionHandler()
    features = option.feats
    #model_handler=modelHandler.modelHandlerNeuron(option_handler.model_path,option_handler.model_spec_dir,option_handler.base_dir)
    #print option.feats   #--> [<bound method fF.AP1_amp_abstr_data of <fitnessFunctions.fF instance at 0x7f669e957128>>] (ezt adja)
    weigths = option.weights
    if moo_var:
        temp_fit = []
    else:
        temp_fit = 0
    print candidates

    if brain_var:
        candidates=[candidates]
    #model.hoc_ob.cellpickler('cell.cpickle')
    if option.type[-1]!= 'features':
        window = int(option.spike_window)
    else:
        window=None
    model.CreateStimuli(option.GetModelStim())
    if option.type[-1]!= 'features':
        k_range=reader.number_of_traces()
    else:
        k_range=len(reader.features_data["stim_amp"])

    for l in candidates:
        if option.output_level == "1":
            print l
        l = ReNormalize(l)
        if option.output_level == "1":
            print l
        for k in range(k_range):     #for k in range(reader.number_of_traces()):
            try:
                add_data = [spike_frame(n - window, thres, n, 1, n + window, thres) for n in reader.additional_data.get(k)]
            except AttributeError:
                add_data = None
            args = {}
            args["add_data"] = add_data
            param = option.GetModelStimParam()
            parameter = param
            parameter[0] = param[0][k]
            if isinstance(parameter[0], unicode):
                model.SetCustStimuli(parameter)
            else:
                extra_param = option.GetModelRun()
                model.SetStimuli(parameter, extra_param)
            if (not modelRunner(l,k)):
                if option.output_level == "1":
                    print features, weigths
                if (option.type[-1]!='features'):
                    for f, w in zip(features, weigths):
                        if abs(len(model.record[0])-len(reader.data.GetTrace(k)))>1:
                            raise sizeError("model: " + str(len(model.record[0])) + ", target: " + str(len(reader.data.GetTrace(k))))
                        if moo_var:
                            temp_fit.append(f(model.record[0],
                                                              reader.data.GetTrace(k), args))
                        else:
                            temp_fit += w * (f(model.record[0],
                                                             reader.data.GetTrace(k), args))
                else:
                    for f, w in zip(features, weigths):
                        if moo_var:
                            temp_fit.append(FFun_for_Features(model.record[0],reader.features_data, f, k, args))
                        else:
                            temp_fit += w * FFun_for_Features(model.record[0],reader.features_data, f, k, args)
            else:
                temp_fit=100
        if moo_var:
            fitnes.append(ec.emo.Pareto(tuple(temp_fit)))
            del temp_fit[:]
        else:
            fitnes.append(temp_fit)
            temp_fit = 0
        if option.output_level == "1":
            print "current fitness: ",temp_fit
    if brain_var:
        return fitnes[0]
    else:
        return fitnes




# to generate a new set of parameters
class baseOptimizer():
    """
    An abstract base class to implement an optimization process.
    """
    def __init__(self):
        pass
    def SetFFun(self,option_obj):
        """
        Sets the combination function and converts the name of the fitness functions into function instances.

        :param option_obj: an ``optionHandler`` instance

        """

        try:
            self.ffun=self.fit_obj.fun_dict["Combinations"]
            MooFeatures=self.fit_obj.fun_dict2["Multiobj"]
        except KeyError:
            sys.exit("Unknown fitness function!")

        if option_obj.type[-1]!='features':
            try:
                option_obj.feats=map(lambda x:self.fit_obj.calc_dict[x],option_obj.feats)
            except KeyError:
                print "error with fitness function: ",option_obj.feats," not in: ",self.fit_obj.calc_dict.keys()




def normalize(v,args):
    """
    Normalizes the values of the given ``list`` using the defined boundaries.

    :param v: the ``list`` of values
    :param args: an object which has a ``min_max`` attribute which consists of two ``lists``
        each with the same number of values as the given list

    :return: the ``list`` of normalized values

    """
    c=copy.copy(v)
    for i in range(len(v)):
        c[i]=(v[i]-args.min_max[0][i])/(args.min_max[1][i]-args.min_max[0][i])
    return c



def uniform(random,args):
    """
    Creates random values from a uniform distribution. Used to create initial population.

    :param random: random number generator object
    :param args: ``dictionary``, must contain key "num_params" and either "_ec" or "self"

    :return: the created random values in a ``list``

    """
    size=args.get("num_params")
    bounds=args.get("_ec",args.get("self")).bounder
    candidate=[]
    for n in range(int(size)):
        candidate.append(random.uniform(bounds.lower_bound[n],bounds.upper_bound[n]))
    return candidate

class my_candidate():
    """
    Mimics the behavior of ``candidate`` from the ``inspyred`` package to allow the uniform
    handling of the results produced by the different algorithms.

    :param vals: the result of the optimization
    :param fitn: the fitness of the result

    """
    def __init__(self,vals, fitn=-1):
        self.candidate=ndarray.tolist(vals)
        self.candidate.extend(vals)
        self.fitness=fitn


class bounderObject(object):
    """
    Creates a callable to perform the bounding of the parameters.
    :param xmax: list of maxima
    :param xmin: list of minima
    """
    def __init__(self, xmax, xmin ):
            self.lower_bound = np.array(xmax)
            self.upper_bound = np.array(xmin)
    def __call__(self, **kwargs):
        """
        Performs the bounding by deciding if the given point is in the defined region of the parameter space.
        This is required by some algorithms as part of their acceptance tests.

        :return: `True` if the point is inside the given bounds.
        """
        x = kwargs["x_new"]
        tmax = bool(np.all(x <= self.lower_bound))
        tmin = bool(np.all(x >= self.upper_bound))
        return tmax and tmin



class annealing(baseOptimizer):
    """
    Implements the ``Simulated Annealing`` algorithm for minimization from the ``inspyred`` package.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. seealso::

        Documentation of the Simulated Annealing from 'inspyred':
            http://inspyred.github.io/reference.html#replacers-survivor-replacement-methods


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.SA(self.rand)
        self.evo_strat.terminator=terminators.evaluation_termination
        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.g_m=option_obj.m_gauss
        self.g_std=option_obj.std_gauss
        self.inint_T=option_obj.init_temp
        self.cooling_rate=option_obj.cooling_rate
        self.number_of_cpu=option_obj.number_of_cpu
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

#    def wrapper(self,candidates,args):
#        tmp=ndarray.tolist(candidates)
#        c=[]
#        for n in tmp:
#            c.append(n[0])
#        #c=self.bounder(c,args)
#        print [c]
#        return self.ffun([c],args)[0]

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print int(self.number_of_cpu)
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
                                             mp_evaluator=combineFeatures,
                                             mp_nprocs=int(self.number_of_cpu),
                                             max_evaluations=self.max_evaluation,
                                             mutation_rate=self.mutation_rate,
                                             temperature=self.inint_T,
                                             cooling_rate=self.cooling_rate,
                                             gaussian_mean=self.g_m,
                                             gaussian_stdev=self.g_std,
                                             num_params=self.num_params,
                                             maximize=self.maximize,
                                             bounder=self.bounder,
                                             seeds=self.starting_points,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file,
                                             )


    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))



class PSO(baseOptimizer):
    """
    Implements the ``Particle Swarm`` algorithm for minimization from the ``inspyred`` package.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. seealso::

        Documentation of the Particle Swarm from 'inspyred':
            http://pythonhosted.org/inspyred/reference.html

    """
    def __init__(self,reader_obj,model_obj,option_obj):

        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)

        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)

	#PSO algorithm
        self.evo_strat=inspyred.swarm.PSO(self.rand)

	#algorithm terminates at max number of generations
        self.evo_strat.terminator=terminators.generation_termination

	if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]

        self.max_evaluation=option_obj.max_evaluation
        self.pop_size=option_obj.pop_size

	#PSO attributes
        self.number_of_cpu=option_obj.number_of_cpu
        self.inertia=option_obj.inertia
        self.cognitive_rate=option_obj.cognitive_rate
        self.social_rate=option_obj.social_rate
	#self.neighborhood_size=int(round(option_obj.neighborhood_size))
	self.topology=inspyred.swarm.topologies.star_topology
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")

        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

#    def wrapper(self,candidates,args):
#        tmp=ndarray.tolist(candidates)
#        c=[]
#        for n in tmp:
#            c.append(n[0])
#        #c=self.bounder(c,args)
#        print [c]
#        return self.ffun([c],args)[0]

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print int(self.number_of_cpu)
        self.final_pop=self.evo_strat.evolve(generator=uniform,evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
                                             mp_evaluator=combineFeatures,
                                             mp_nprocs=int(self.number_of_cpu),
                                             max_generations=self.max_evaluation-1,
                                             pop_size=self.pop_size,
					     inertia=self.inertia,
					     cognitive_rate=self.cognitive_rate,
					     social_rate=self.social_rate,
                                             num_params=self.num_params,
                                             maximize=self.maximize,
                                             bounder=self.bounder,
                                             seeds=self.starting_points,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file
                                             )
	self.stat_file.close()
	self.ind_file.close()



    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))




class basinHopping(baseOptimizer):
    """
    Implements the ``Basinhopping`` algorithm for minimization from the ``scipy`` package.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. seealso::

        Documentation of the Simulated Annealing from 'scipy':
            http://docs.scipy.org/doc/scipy-dev/reference/generated/scipy.optimize.basinhopping.html

    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=random
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.temp=option_obj.temperature
        self.num_iter=option_obj.num_iter
        self.num_repet=option_obj.num_repet
        self.step_size=option_obj.step_size
        self.freq=option_obj.update_freq
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_params" : self.num_params,"self": self})
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

    def logger(self,x,f,accepted):
        self.log_file.write(np.array_str(x))
        self.log_file.write("\t")
        self.log_file.write(str(f))
        self.log_file.write("\t")
        self.log_file.write("accepted: "+str(accepted))
        self.log_file.write("\n")
        self.log_file.flush()



    def wrapper(self,candidates,args):
        """
        Converts the ``ndarray`` object into a ``list`` and passes it to the fitness function.

        :param candidates: the ``ndarray`` object
        :param args: optional parameters to be passed to the fitness function

        :return: the return value of the fitness function

        """
        tmp=ndarray.tolist(candidates)
        ec_bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        candidates=ec_bounder(tmp,args)
        return self.ffun([candidates],args)[0]



    def Optimize(self):
        """
        Performs the optimization.
        """

        self.log_file=open("basinhopping.log","w")
        list_of_results=[0]*int(self.num_repet)
        for points in range(int(self.num_repet)):
            self.log_file.write(str(points+1)+". starting point: ["+", ".join(map(str,self.starting_points))+"]")
            self.log_file.write("\n")
            list_of_results[points]=optimize.basinhopping(self.wrapper,
                         x0=ndarray((self.num_params,),buffer=array(self.starting_points),offset=0,dtype=float),
                         niter=int(self.num_iter),
                         T=self.temp,
                         stepsize=self.step_size,
                         minimizer_kwargs={"method":"L-BFGS-B",
                                           "jac":False,
                                           "args":[[]],
                                           "bounds": [(0,1)]*len(self.min_max[0]),
                                           "options": {"fprime": None,
                                                       "approx_grad": True,
                                                       "factr":100,
                                                       "iprint": 2,
                                                       "pgtol": 1e-06,
                                                       "maxfun" : 100}},
                         take_step=None,
                         accept_test=self.bounder,
                         callback=self.logger,
                         interval=int(self.freq),
                         disp=False,
                         niter_success=None)
            self.starting_points=uniform(self.rand,{"num_params" : self.num_params,"self": self})
            self.log_file.write("".join(["-"]*200))
        self.log_file.close()

        self.result=min(list_of_results,key=lambda x:x.fun)
        #print self.result.x
        self.final_pop=[my_candidate(self.result.x,self.result.fun)]

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=bounderObject([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))


class fmin(baseOptimizer):
    """
    Implements a downhill simplex algorithm for minimization from the ``scipy`` package.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. seealso::

        Documentation of the fmin from 'scipy':
            http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html#scipy.optimize.fmin

    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=random
        self.seed=option_obj.seed
        self.rand.seed([self.seed])
        self.xtol=option_obj.x_tol
        self.ftol=option_obj.f_tol
        self.max_evaluation=option_obj.max_evaluation
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                raise TypeError
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_params" : self.num_params,"self": self})
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points



    def wrapper(self,candidates,args):
        """
        Converts the ``ndarray`` object into a ``list`` and passes it to the fitness function.

        :param candidates: the ``ndarray`` object
        :param args: optional parameters to be passed to the fitness function

        :return: the return value of the fitness function

        """
        tmp=ndarray.tolist(candidates)
        candidates=self.bounder(tmp,args)
        return self.ffun([candidates],args)[0]





    def Optimize(self):
        """
        Performs the optimization.
        """
        self.result=optimize.fmin(self.wrapper,
                                      x0=ndarray((self.num_params,),buffer=array(self.starting_points),offset=0,dtype=float),
#                                      x0=ndarray( (self.num_params,1) ,buffer=array([0.784318808, 4.540607953, -11.919391073,-100]),dtype=float),
#                                      args=[[]]
                                      args=((),),
                                      maxiter= self.max_evaluation,
                                      xtol= self.xtol,
                                      ftol= self.ftol,
                                      full_output=True
                                      )

        self.final_pop=[my_candidate(self.result[0],self.result[1])]

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))



class L_BFGS_B(baseOptimizer):
    """
    Implements L-BFGS-B algorithm for minimization from the ``scipy`` package.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. seealso::

        Documentation of the L-BFGS-B from 'scipy':
            http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin_l_bfgs_b.html#scipy.optimize.fmin_l_bfgs_b

    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=random
        self.seed=option_obj.seed
        self.rand.seed([self.seed])
        self.max_evaluation=option_obj.max_evaluation
        self.accuracy=option_obj.acc
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                raise TypeError
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_params" : self.num_params,"self": self})

        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points


    def wrapper(self,candidates,args):
        """
        Converts the ``ndarray`` object into a ``list`` and passes it to the fitness function.

        :param candidates: the ``ndarray`` object
        :param args: optional parameters to be passed to the fitness function

        :return: the return value of the fitness function

        """
        tmp=ndarray.tolist(candidates)
        candidates=self.bounder(tmp,args)
        return self.ffun([candidates],args)[0]




    def Optimize(self):
        """
        Performs the optimization.
        """
        self.result=optimize.fmin_l_bfgs_b(self.wrapper,
                                      x0=ndarray((self.num_params,),buffer=array(self.starting_points),offset=0,dtype=float),
#                                      x0=ndarray( (self.num_params,1) ,buffer=array([0.784318808, 4.540607953, -11.919391073,-100]),dtype=float),
                                      args=[[]],
                                      bounds= [(0,1)]*len(self.min_max[0]),
                                      maxfun= self.max_evaluation,
                                      fprime= None,
                                      approx_grad= True,
                                      factr= self.accuracy, #1e7 moderate acc, 10.0 ext high acc
                                      iprint= 2, #>1 creates log file
                                      pgtol= 1e-06
                                      )
        print self.result[-1]['warnflag']
        self.final_pop=[my_candidate(self.result[0],self.result[1])]

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))




class grid(baseOptimizer):
    """
    Implements a brute force algorithm for minimization by calculating the function's value
    over the specified grid.

    .. note::
        This algorithm is highly inefficient and should not be used for complete optimization.

    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object
    :param resolution: number of sample points along each dimensions (default: 10)

    """
    def __init__(self,reader_obj,model_obj,option_obj,resolution):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.num_params=option_obj.num_params
        self.num_points_per_dim=resolution
        #self.resolution=5
        #print self.resolution
        self.SetBoundaries(option_obj.boundaries)



    def Optimize(self,optimals):
        """
        Performs the optimization.
        """

        self.final_pop=[[],[]]
        _o=copy.copy(optimals)
        _o=normalize(_o, self)
        #import itertools
        points=[]
        fitness=[]
        tmp1=[]
        tmp2=[]
        for n in range(self.num_params):
            for c in frange(0,1, float(1)/self.num_points_per_dim):
                _o[n]=c
                tmp1.append(self.fit_obj.ReNormalize(_o))
                tmp2.append(self.ffun([_o],{}))
            points.append(tmp1)
            tmp1=[]
            fitness.append(tmp2)
            tmp2=[]
            _o=copy.copy(optimals)
            _o=normalize(_o, self)


        self.final_pop[0]=points
        self.final_pop[1]=fitness


    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))




# simple EO algorithm
class simpleEO(baseOptimizer):
    """
    Implements a custom version of ``Evolution Strategy`` algorithm for minimization from the ``inspyred`` package.
    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. note::
        The changed parameters compared to the defaults are the following:
            * replacer: genrational_replacement
            * variator: gaussian_mutation, blend_crossover

    .. seealso::

        Documentation of the options from 'inspyred':
            http://inspyred.github.io/reference.html#module-inspyred.ec


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.ES(self.rand)
        self.evo_strat.terminator=terminators.generation_termination
        self.evo_strat.selector=inspyred.ec.selectors.default_selection
        self.evo_strat.replacer=inspyred.ec.replacers.generational_replacement
        self.evo_strat.variator=[variators.gaussian_mutation,
                                 variators.blend_crossover]
        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.number_of_cpu=option_obj.number_of_cpu
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=combineFeatures,
                                             #mp_nprocs=int(self.number_of_cpu),
                                             pop_size=self.pop_size, seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             mutation_rate=self.mutation_rate,
                                             num_params=self.num_params,
                                             maximize=self.maximize, bounder=self.bounder,
                                             num_elites=int(self.pop_size/2),
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file,
#                                             blx_alpha=0.2,
                                             gaussian_stdev=0.5)

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))



class DEA(baseOptimizer):
    """
    Implements the ``Differential Evolution Algorithm`` algorithm for minimization from the ``inspyred`` package.
    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object


    .. seealso::

        Documentation of the options from 'inspyred':
            http://inspyred.github.io/reference.html#module-inspyred.ec


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.DEA(self.rand)
#    - *num_selected* -- the number of individuals to be selected (default 2)
#    - *tournament_size* -- the tournament size (default 2)
#    - *crossover_rate* -- the rate at which crossover is performed
#    (default 1.0)
#    - *mutation_rate* -- the rate at which mutation is performed (default 0.1)
#    - *gaussian_mean* -- the mean used in the Gaussian function (default 0)
#    - *gaussian_stdev* -- the standard deviation used in the Gaussian function
#   (default 1)
        self.evo_strat.terminator=terminators.generation_termination

        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        self.pop_size=option_obj.pop_size
        self.number_of_cpu=option_obj.number_of_cpu
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
	self.crossover_rate=option_obj.crossover_rate
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print int(self.number_of_cpu)
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
                                             mp_evaluator=combineFeatures,
                                             mp_nprocs_cpus=int(self.number_of_cpu),
                                             pop_size=self.pop_size,
                                             tournament_size=int(self.pop_size),
                                             num_selected=int(self.pop_size/10),
                                             seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             mutation_rate=self.mutation_rate,
					     crossover_rate=self.crossover_rate,
                                             num_params=self.num_params,
                                             maximize=self.maximize,
                                             bounder=self.bounder,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file,
                                             )

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))



class RandomSearch(baseOptimizer):
    """
    Implements the ``Differential Evolution Algorithm`` algorithm for minimization from the ``inspyred`` package.
    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object


    .. seealso::

        Documentation of the options from 'inspyred':
            http://inspyred.github.io/reference.html#module-inspyred.ec


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        setmodparams(reader_obj,model_obj,option_obj)
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.pop_size=option_obj.pop_size
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.number_of_cpu=option_obj.number_of_cpu

        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points


    def Optimize(self):
        """
        Performs the optimization.
        """
        log_f=open("random.txt","w")
        init_candidate=uniform(self.rand, {"self":self,"num_params":self.num_params})
        self.act_min=my_candidate(array(init_candidate),self.ffun([init_candidate],{}))
        log_f.write(str(self.act_min.candidate))
        log_f.write("\t")
        log_f.write(str(self.act_min.fitness))
        log_f.write("\n")
        p=multiprocessing.Pool(int(self.number_of_cpu))
        act_candidate=[]
        for i in range(int(self.pop_size)):
            act_candidate.append(uniform(self.rand, {"self":self,"num_params":self.num_params}))
        act_candidate=[[x,] for x in act_candidate]
        act_fitess=p.map(combineFeatures,act_candidate)
        log_f.write(str(act_candidate))
        log_f.write("\t")
        log_f.write(str(act_fitess))
        log_f.write("\n")
        if (act_fitess<self.act_min.fitness):
            self.act_min=my_candidate(act_candidate,act_fitess)

        self.final_pop=[my_candidate(numpy.asarray(y[0]),z) for y,z in zip(act_candidate,act_fitess)]
    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))

# simple NSGA-II
class NSGAII(baseOptimizer):
    """
    Implements a custom version of ``Evolution Strategy`` algorithm for minimization from the ``inspyred`` package.
    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object

    .. note::
        The changed parameters compared to the defaults are the following:
            * replacer: genrational_replacement
            * variator: gaussian_mutation, blend_crossover

    .. seealso::

        Documentation of the options from 'inspyred':
            http://inspyred.github.io/reference.html#module-inspyred.ec


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        global moo_var
        moo_var=True
        self.evo_strat=ec.emo.NSGA2(self.rand)
        self.evo_strat.terminator=terminators.generation_termination
        self.evo_strat.selector=inspyred.ec.selectors.default_selection
        self.evo_strat.replacer=inspyred.ec.replacers.nsga_replacement

        self.evo_strat.variator=[variators.gaussian_mutation,
                                 variators.blend_crossover]
        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        self.pop_size=option_obj.pop_size

        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.number_of_cpu=option_obj.number_of_cpu
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
                                             mp_evaluator=combineFeatures,
                                             mp_nprocs=int(self.number_of_cpu),
                                             pop_size=self.pop_size, seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             num_params=self.num_params,
                                             maximize=self.maximize, bounder=self.bounder,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file)
	self.final_archive = self.evo_strat.archive
    moo_var=False

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))


class PAES(baseOptimizer):
    """
    Implements a custom version of ``PAES`` algorithm for minimization from the ``inspyred`` package.
    :param reader_obj: an instance of ``DATA`` object
    :param model_obj: an instance of a model handler object, either ``externalHandler`` or ``modelHandlerNeuron``
    :param option_obj: an instance of ``optionHandler`` object


    .. seealso::

        Documentation of the options from 'inspyred':
            http://inspyred.github.io/reference.html#module-inspyred.ec


    """
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        global moo_var
        moo_var=True
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.emo.PAES(self.rand)
        self.evo_strat.terminator=terminators.generation_termination
        self.evo_strat.selector=inspyred.ec.selectors.default_selection
        self.evo_strat.replacer=inspyred.ec.replacers.paes_replacement
        self.evo_strat.variator=[variators.gaussian_mutation,
                                 variators.blend_crossover]
        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        self.number_of_cpu=option_obj.number_of_cpu
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable

    def Optimize(self):
        """
        Performs the optimization.
        """
        logger = logging.getLogger('inspyred.ec')
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('inspyred.log', mode='w')
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        print int(self.number_of_cpu)
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
                                             mp_evaluator=combineFeatures,
                                             mp_nprocs=int(self.number_of_cpu),
                                             pop_size=self.pop_size, seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             mutation_rate=self.mutation_rate,
                                             num_params=self.num_params,
                                             maximize=self.maximize, bounder=self.bounder,
                                             num_elites=int(self.pop_size/2),
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file)
	self.final_archive = self.evo_strat.archive
    moo_var=False

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))


def selIBEA(population, mu, alpha=None, kappa=.05, tournament_n=4):
    """IBEA Selector"""
    def _calc_fitness_components(population, kappa):
        """returns an N * N numpy array of doubles, which is their IBEA fitness """
        # DEAP selector are supposed to maximise the objective values
        # We take the negative objectives because this algorithm will minimise
        population_matrix = numpy.fromiter(
            iter(-x for individual in population
                 for x in individual.fitness.wvalues),
            dtype=numpy.float)
        pop_len = len(population)
        feat_len = len(population[0].fitness.wvalues)
        print pop_len
        print feat_len
        population_matrix = population_matrix.reshape((pop_len, feat_len))

        # Calculate minimal square bounding box of the objectives
        box_ranges = (numpy.max(population_matrix, axis=0) -
                      numpy.min(population_matrix, axis=0))

        # Replace all possible zeros to avoid division by zero
        # Basically 0/0 is replaced by 0/1
        box_ranges[box_ranges == 0] = 1.0

        components_matrix = numpy.zeros((pop_len, pop_len))
        for i in xrange(0, pop_len):
            diff = population_matrix - population_matrix[i, :]
            components_matrix[i, :] = numpy.max(
                numpy.divide(diff, box_ranges),
                axis=1)

        # Calculate max of absolute value of all elements in matrix
        max_absolute_indicator = numpy.max(numpy.abs(components_matrix))

        # Normalisation
        if max_absolute_indicator != 0:
            components_matrix = numpy.exp(
                (-1.0 / (kappa * max_absolute_indicator)) * components_matrix.T)

        return components_matrix


    def _calc_fitnesses(population, components):
        """Calculate the IBEA fitness of every individual"""

        # Calculate sum of every column in the matrix, ignore diagonal elements
        column_sums = numpy.sum(components, axis=0) - numpy.diagonal(components)

        # Fill the 'ibea_fitness' field on the individuals with the fitness value
        for individual, ibea_fitness in zip(population, column_sums):
            individual.ibea_fitness = ibea_fitness


    def _choice(seq):
        """Python 2 implementation of choice"""

        return seq[int(random.random() * len(seq))]


    def _mating_selection(population, mu, tournament_n):
        """Returns the n_of_parents individuals with the best fitness"""

        parents = []
        for _ in xrange(mu):
            winner = _choice(population)
            for _ in xrange(tournament_n - 1):
                individual = _choice(population)
                # Save winner is element with smallest fitness
                if individual.ibea_fitness < winner.ibea_fitness:
                    winner = individual
            parents.append(winner)

        return parents


    def _environmental_selection(population, selection_size):
        """Returns the selection_size individuals with the best fitness"""

        # Sort the individuals based on their fitness
        population.sort(key=lambda ind: ind.ibea_fitness)

        # Return the first 'selection_size' elements
        return population[:selection_size]

    if alpha is None:
        alpha = len(population)

    # Calculate a matrix with the fitness components of every individual
    components = _calc_fitness_components(population, kappa=kappa)

    # Calculate the fitness values
    _calc_fitnesses(population, components)

    # Do the environmental selection
    population[:] = _environmental_selection(population, alpha)

    # Select the parents in a tournament
    parents = _mating_selection(population, mu, tournament_n)

    return parents


class deapIBEA(baseOptimizer):



    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        global moo_var
        moo_var=True
        self.seed=option_obj.seed
        self.pop_size=int(option_obj.pop_size)
        self.max_evaluation=int(option_obj.max_evaluation)
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.number_of_cpu=option_obj.number_of_cpu
        self.SetBoundaries(option_obj.boundaries)
        BOUND_LOW = self.min_max[0]
        BOUND_UP = self.min_max[1]
        NDIM = 30
        minimweights=[ -x for x in option_obj.weights]*self.reader.number_of_traces() #turn weights for minimizing
        creator.create("FitnessMin", base.Fitness, weights=minimweights)
        creator.create("Individual", array1.array, typecode='d', fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        def uniformd(low, up, size=None):
            try:
                return [random.uniform(a, b) for a, b in zip(low, up)]
            except TypeError:
                return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]
        self.toolbox.register("attr_float", uniformd, BOUND_LOW, BOUND_UP, NDIM)
        self.toolbox.register("evaluate", combineFeatures)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
        self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)
        pool=multiprocessing.Pool(processes=int(self.number_of_cpu))
        self.toolbox.register("map",pool.map)

    def Optimize(self):



            population = self.toolbox.population(self.pop_size)
            MU=self.pop_size
            NGEN=self.max_evaluation
            kappa=.05
            CXPB=0.9
            #population, kappa
            stats = tools.Statistics(lambda ind: ind.fitness.values)
            # stats.register("avg", numpy.mean, axis=0)
            # stats.register("std", numpy.std, axis=0)
            stats.register("std", numpy.std, axis=0)
            stats.register("min", numpy.min, axis=0)
            stats.register("avg", numpy.mean, axis=0)
            stats.register("max", numpy.max, axis=0)
            self.logbook = tools.Logbook()
            self.logbook.header = "gen", "evals", "min", "max", "avg", "std"
                #record = stats.compile(pop)
                #self.logbook.record(gen=0, evals=len(invalid_ind), **record)
            self.final_pop = []

            stats = tools.Statistics(lambda ind: ind.fitness.values)
            # stats.register("avg", numpy.mean, axis=0)
            # stats.register("std", numpy.std, axis=0)
            stats.register("min", numpy.min, axis=0)
            stats.register("max", numpy.max, axis=0)
            valid_ind= []
            logbook = tools.Logbook()
            logbook.header = "gen", "evals", "std", "min", "avg", "max"
            for i in range(len(population)):
                poparr = []
                if not population[i].fitness.valid:
                    for j in range(0,len(population[i])):
                        poparr.append(population[i][j])
                    valid_ind.append([poparr])
            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in population if not ind.fitness.valid]
            fitnesses = self.toolbox.map(self.toolbox.evaluate,[[x,] for x in population])
            for ind, fit in zip(population, fitnesses):
                ind.fitness.values = fit[0]


            pop = selIBEA(population, len(population))

            record = stats.compile(pop)
            logbook.record(gen=0, evals=len(invalid_ind), **record)
            self.logbook.record(gen=0, evals=len(invalid_ind), **record)
            population2=[]
            fitnesses2=[]
            # Begin the generational process
            for gen in range(1, NGEN):
                # Vary the population
                offspring = tools.selTournament(pop, len(pop),2)
                offspring = [self.toolbox.clone(ind) for ind in offspring]

                for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
                    if random.random() <= CXPB:
                        self.toolbox.mate(ind1, ind2)

                    self.toolbox.mutate(ind1)
                    self.toolbox.mutate(ind2)
                    del ind1.fitness.values, ind2.fitness.values

                valid_ind= []

                # Evaluate the individuals with an invalid fitness
                invalid_ind = [ind for ind in population if not ind.fitness.valid]
                fitnesses = self.toolbox.map(self.toolbox.evaluate,[[x,] for x in population])
                for ind, fit in zip(offspring, fitnesses):
                    ind.fitness.values = fit[0]

                # Select the next generation population
                pop = selIBEA(pop+offspring, MU)
                record = stats.compile(pop)
                self.logbook.record(gen=gen, evals=len(invalid_ind), **record)

                self.final_pop.append(pop)
                self.final_pop.append(fitnesses)



    def SetBoundaries(self,bounds):

        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        print 'self.min_max'
        print self.min_max[0]
        print self.min_max[1]
        print 'self.bounder'
        print self.bounder


class deapNSGA(baseOptimizer):


    def __init__(self,reader_obj,model_obj,option_obj,algo):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        global moo_var
        moo_var=True
        self.seed=option_obj.seed
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.number_of_cpu=option_obj.number_of_cpu
        self.SetBoundaries(option_obj.boundaries)
        BOUND_LOW = self.min_max[0]
        BOUND_UP = self.min_max[1]
        NDIM = 30
        print 'option_obj'
        minimweights=[ -x for x in option_obj.weights]*reader.number_of_traces() #turn weights for minimizing
        print minimweights
        creator.create("FitnessMin", base.Fitness, weights=minimweights)
        creator.create("Individual", array1.array, typecode='d', fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        def uniformd(low, up, size=None):
            try:
                return [random.uniform(a, b) for a, b in zip(low, up)]
            except TypeError:
                return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]
        self.toolbox.register("attr_float", uniformd, BOUND_LOW, BOUND_UP, NDIM)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", combineFeatures)
        self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
        self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)
        if algo=='spea':
            self.toolbox.register("select", tools.selSPEA2)
            print 'spea'
        else:
            self.toolbox.register("select", tools.selNSGA2)
            print 'nsga'
        pool=multiprocessing.Pool(processes=int(self.number_of_cpu))
        self.toolbox.register("map",pool.map)
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_params" : self.num_params,"self": self})),self)]
        try:
            #print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        if option_obj.output_level=="1":
            print "starting points: ",self.starting_points

        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable

    def Optimize(self):
        """
        Performs the optimization.
        """
    # Problem definition
    # Functions zdt1, zdt2, zdt3, zdt6 have bounds [0, 1]


    # Functions zdt4 has bounds x1 = [0, 1], xn = [-5, 5], with n = 2, ..., 10
    # BOUND_LOW, BOUND_UP = [0.0] + [-5.0]*9, [1.0] + [5.0]*9
    # Functions zdt1, zdt2, zdt3 have 30 dimensions, zdt4 and zdt6 have 10

        random.seed(self.seed)

        NGEN = int(self.max_evaluation)
        MU = int(self.pop_size)
        CXPB = 2

        stats = tools.Statistics(lambda ind: ind.fitness.values)
        # stats.register("avg", numpy.mean, axis=0)
        # stats.register("std", numpy.std, axis=0)
        stats.register("std", numpy.std, axis=0)
        stats.register("min", numpy.min, axis=0)
        stats.register("avg", numpy.mean, axis=0)
        stats.register("max", numpy.max, axis=0)
        self.logbook = tools.Logbook()
        self.logbook.header = "gen", "evals", "min", "max", "avg", "std"
        pop = self.toolbox.population(n=MU)

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in pop if not ind.fitness.valid]
        valid_ind= []
        for i in range(len(pop)):
            poparr = []
            if not pop[i].fitness.valid:
                for j in range(0,len(pop[i])):
                    poparr.append(pop[i][j])
                valid_ind.append([poparr])

        #fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)

        fitnesses = self.toolbox.map(self.toolbox.evaluate,valid_ind)
        print "fits"
        print fitnesses
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit[0]

        # This is just to assign the crowding distance to the individuals
        # no actual selection is done
        pop = self.toolbox.select(pop, len(pop))
        #for value in range(2,7):
        #    if (len(pop) % value) == 0:
        #        tourn=value;
        tourn=int(self.pop_size)
        record = stats.compile(pop)
        self.logbook.record(gen=0, evals=len(invalid_ind), **record)
        birth = 0
        finalfits=[]
        poparray2=[]
        self.final_pop = []
        for gen in range(1, NGEN):
        # Vary the population
            offspring = tools.selTournament(pop, len(pop),tourn)
            offspring = [self.toolbox.clone(ind) for ind in offspring]

            stats = tools.Statistics(lambda ind: ind.fitness.values)
            stats.register("std", numpy.std, axis=0)
            stats.register("min", numpy.min, axis=0)
            stats.register("avg", numpy.mean, axis=0)
            stats.register("max", numpy.max, axis=0)

            for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
                if random.random() <= CXPB:
                    self.toolbox.mate(ind1, ind2)

                    self.toolbox.mutate(ind1)
                    self.toolbox.mutate(ind2)
                del ind1.fitness.values, ind2.fitness.values

        #Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            valid_ind= []
            for i in range(len(offspring)):
                poparr = []
                if not offspring[i].fitness.valid:
                    for j in range(0,len(pop[i])):
                        poparr.append(pop[i][j])
                    valid_ind.append([poparr])

            #fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
            fitnesses = self.toolbox.map(self.toolbox.evaluate,valid_ind)

            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit[0]

        # Select the next generation population
            self.final_pop.append(pop) #]append([poparray2 , finalfitness[i] , (birth-len(pop)+i)])
            self.final_pop.append(fitnesses)
            pop = self.toolbox.select(pop + offspring, MU)
            record = stats.compile(pop)
            print 'stats'
            print record

            self.logbook.record(gen=gen, evals=len(invalid_ind), **record)
        #self.final_pop = []
                #self.final_pop.candidate = []
                #self.final_pop.fitness = []
                #self.finap_pop.birthdate = []



            #self.final_pop.candidate.append(poparray2)
            #self.final_pop.fitness.append(finalfitness[i])
            #self.finap_pop.birthdate.append((birth-len(pop)+i))
        self.final_pop.append(poparray2) #]append([poparray2 , finalfitness[i] , (birth-len(pop)+i)])
        self.final_pop.append(finalfits)
        moo_var=False
        #<Individual: candidate = [0.07722800626371065, 0.2423814486289446, 0.5850818875172326, 0.889195037637904],>
        #fitness = (0.6016907118977254, 0.03124087065642784), birthdate = 1479060665.16>

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        print 'self.min_max'
        print self.min_max[0]
        print self.min_max[1]
        print 'self.bounder'
        print self.bounder





class SNES(DistributionBasedOptimizer):
    """ Separable NES (diagonal).
    [As described in Schaul, Glasmachers and Schmidhuber (GECCO'11)]
    """

    # parameters, which can be set but have a good (adapted) default value
    centerLearningRate = 1
    covLearningRate = None
    batchSize = None
    uniformBaseline = True
    from pybrain.tools.rankingfunctions import HansenRanking
    shapingFunction = HansenRanking()
    initVariance = 0.2

    # fixed settings
    mustMaximize = True
    storeAllEvaluations = True
    storeAllEvaluated = True
    # for very long runs, we don't want to run out of memory
    clearStorage = False
    mn=1
    idx=0
    # minimal setting where to abort the search
    varianceCutoff = 1e-20

    def _stoppingCriterion(self):
        if DistributionBasedOptimizer._stoppingCriterion(self):
            return True
        elif max(abs(self._sigmas)) < self.varianceCutoff:
            return True
        else:
            return False

    def _initLearningRate(self):
        """ Careful, robust default value. """
        return 0.6 * (3 + log(self.numParameters)) / 3 / sqrt(self.numParameters)

    def _initBatchSize(self):
        """ as in CMA-ES """
        return 4 + int(floor(3 * log(self.numParameters)))

    def _additionalInit(self):
        if self.covLearningRate is None:
            self.covLearningRate = self._initLearningRate()
        if self.batchSize is None:
            self.batchSize = self._initBatchSize()

        self._center = self._initEvaluable.copy()
        self._sigmas = ones(self.numParameters) * self.initVariance

    @property
    def _population(self):
        if self._wasUnwrapped:
            return [self._allEvaluated[i].params for i in self._pointers]
        else:
            return [self._allEvaluated[i] for i in self._pointers]

    @property
    def _currentEvaluations(self):
        fits = [self._allEvaluations[i] for i in self._pointers]
        if self._wasOpposed:
            fits = [-x for x in fits]
        return fits

    def _produceSample(self):
        return [random.gauss(x,x/4) for x in self._initEvaluable]

    def _sample2base(self, sample):
        """ How does a sample look in the outside (base problem) coordinate system? """
        return self._sigmas * sample + self._center

    def _base2sample(self, e):
        """ How does the point look in the present one reference coordinates? """
        return (e - self._center) / self._sigmas

    def _produceSamples(self):
        """ Append batch size new samples and evaluate them. """
        if self.clearStorage:
            self._allEvaluated = []
            self._allEvaluations = []


        tmp = [self._sample2base(self._produceSample()) for _ in range(self.batchSize)]
        """procs=multiprocessing.Pool(int(4))
        self._allEvaluations.extend(procs.map(combineFeatures, tmp))
        procs.close()
        self._allEvaluated.extend(tmp)"""
        list(map(self._oneEvaluation, tmp))
        self._pointers = list(range(len(self._allEvaluated) - self.batchSize, len(self._allEvaluated)))

    def _learnStep(self):
        # produce samples
        self._produceSamples()
        samples = list(map(self._base2sample, self._population))
        #compute utilities
        """if min(self._allEvaluations)<self.mn:
            self.mn=min(self._allEvaluations)
            print self.mn
            self.idx=self._allEvaluations.index(self.mn)
            print self._allEvaluated[self.idx]"""
        file=open("nes.txt","w")
        list(map(self._oneEvaluation, [self._allEvaluated[self.idx]]))
        print(self._allEvaluated)
        print(len(self._allEvaluated))
        a=[(sum(x)/len(x)) for x in self._allEvaluated]
        print(a)
        file.write(str(a))
        utilities = self.shapingFunction(self._currentEvaluations)
        file.close()
        utilities /= sum(utilities)  # make the utilities sum to 1
        if self.uniformBaseline:
            utilities -= 1. / self.batchSize

        # update center
        dCenter = dot(utilities, samples)
        self._center += self.centerLearningRate * self._sigmas * dCenter
        # update variances
        covGradient = dot(utilities, [s ** 2 - 1 for s in samples])
        dA = 0.5 * self.covLearningRate * covGradient
        self._sigmas = self._sigmas * exp(dA)



class NES(baseOptimizer):



    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        global brain_var
        brain_var=True
        setmodparams(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.pop_size=int(option_obj.pop_size)
        self.max_evaluation=int(option_obj.max_evaluation)
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.number_of_cpu=option_obj.number_of_cpu
        self.SetBoundaries(option_obj.boundaries)
        self.starting_points=option_obj.starting_points


    def Optimize(self):

            MU=self.pop_size
            NGEN=self.max_evaluation
            #population, kappa
            stats = tools.Statistics(lambda ind: ind.fitness.values)
            # stats.register("avg", numpy.mean, axis=0)
            # stats.register("std", numpy.std, axis=0)
            stats.register("std", numpy.std, axis=0)
            stats.register("min", numpy.min, axis=0)
            stats.register("avg", numpy.mean, axis=0)
            stats.register("max", numpy.max, axis=0)
            self.logbook = tools.Logbook()
            self.logbook.header = "gen", "evals", "min", "max", "avg", "std"
                #record = stats.compile(pop)
                #self.logbook.record(gen=0, evals=len(invalid_ind), **record)
            self.final_pop = []
            #pop = self.toolbox.population(n=MU)
            # Begin the generational process
            #pop=[x.tolist() for x in pop]
            from pybrain.optimization import OriginalNES
            initparam=numpy.average(self.min_max, axis=0)
            file=open("nes.txt","a")
            lp=SNES(combineFeatures,initparam,verbose=True,batchSize=MU)
            lp.minimize=True
            c=lp.learn(NGEN)
            #lp._allEvaluations
            brain_var=False
            file.close()
            self.final_pop.append([c[0]])
            self.final_pop.append([c[1]])



    def SetBoundaries(self,bounds):

        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        print 'self.min_max'
        print self.min_max[0]
        print self.min_max[1]
        print 'self.bounder'
        print self.bounder
