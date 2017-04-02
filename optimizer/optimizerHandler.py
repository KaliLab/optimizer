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

import array
import random
import json

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
            self.mfun=self.fit_obj.fun_dict2["Multiobj"]
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
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=self.ffun,
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
        self.final_pop=self.evo_strat.evolve(generator=uniform,
					     evaluator=self.ffun,
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
        self.SetFFun(option_obj)
        self.rand=random
        self.seed=option_obj.seed
        self.rand.seed([self.seed])
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
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=self.ffun,
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
        self.final_pop=self.evo_strat.evolve(generator=uniform,
                                             evaluator=self.ffun,
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
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.pop_size=option_obj.pop_size
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)

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
        for i in range(int(self.pop_size)):
            act_candidate=uniform(self.rand, {"self":self,"num_params":self.num_params})
            act_fitess=self.ffun([act_candidate],{})
            log_f.write(str(act_candidate))
            log_f.write("\t")
            log_f.write(str(act_fitess))
            log_f.write("\n")
            if (act_fitess<self.act_min.fitness):
                self.act_min=my_candidate(array(act_candidate),act_fitess)


        self.final_pop=[self.act_min]
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
        print 'reader_obj'
        print reader_obj
        print 'model_obj'
        print model_obj
        print 'option_obj'
        print option_obj
        self.SetFFun(option_obj)
        self.rand=Random()
        print 'option_obj'
        print option_obj
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.emo.NSGA2(self.rand)
        print 'self.seed'
        print self.seed
        self.evo_strat.terminator=terminators.generation_termination
        print 'evo_strat.terminator'
        print self.evo_strat.terminator
        self.evo_strat.selector=inspyred.ec.selectors.default_selection
        print 'evo_strat.selector'
        print self.evo_strat.selector
        self.evo_strat.replacer=inspyred.ec.replacers.generational_replacement
        print 'evo_strat.replacer'
        print self.evo_strat.replacer
        self.evo_strat.variator=[variators.gaussian_mutation,
                                 variators.blend_crossover]
        if option_obj.output_level=="1":
            self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        else:
            self.evo_strat.observer=[observers.file_observer]
        print 'evo_strat.variator'
        print self.evo_strat.variator
        self.pop_size=option_obj.pop_size
        print 'option_obj.pop_size'
        print option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        print 'option_obj.max_evaluation'
        print option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        print 'option_obj.mutation_rate'
        print option_obj.mutation_rate
        self.num_params=option_obj.num_params
        print 'option_obj.num_params'
        print option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        print 'option_obj.boundaries'
        print option_obj.boundaries
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
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=self.mfun,
                                             pop_size=self.pop_size, seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             num_params=self.num_params,
                                             maximize=self.maximize, bounder=self.bounder,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file)
        print(self.final_pop)

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
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.emo.PAES(self.rand)
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
        self.final_pop=self.evo_strat.evolve(generator=uniform, evaluator=self.mfun,
                                             pop_size=self.pop_size, seeds=self.starting_points,
                                             max_generations=self.max_evaluation,
                                             mutation_rate=self.mutation_rate,
                                             num_params=self.num_params,
                                             maximize=self.maximize, bounder=self.bounder,
                                             num_elites=int(self.pop_size/2),
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file)

    def SetBoundaries(self,bounds):
        """
        Stores the bounds of the parameters and creates a ``bounder`` object which bounds
        every parameter into the range of 0-1 since the algorithms are using normalized values.

        :param bounds: ``list`` containing the minimum and maximum values.

        """
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))



class deapIBEA(baseOptimizer):

    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.pop_size=int(option_obj.pop_size)
        self.max_evaluation=int(option_obj.max_evaluation)
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        BOUND_LOW = self.min_max[0]
        BOUND_UP = self.min_max[1]
        NDIM = 30
        minimweights=[ -x for x in option_obj.weights] #turn weights for minimizing
        creator.create("FitnessMin", base.Fitness, weights=minimweights)
        creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        def uniformd(low, up, size=None):
            try:
                return [random.uniform(a, b) for a, b in zip(low, up)]
            except TypeError:
                return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]
        self.toolbox.register("attr_float", uniformd, BOUND_LOW, BOUND_UP, NDIM)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
        self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)

    def Optimize(self):

            population = self.toolbox.population(self.pop_size)
            mu=self.max_evaluation
            alpha = len(population)
            kappa=.05
            tourn=4
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
            tourn=int(self.pop_size)
                #record = stats.compile(pop)
                #self.logbook.record(gen=0, evals=len(invalid_ind), **record)
            self.final_pop = []
            # Evaluate the individuals with an invalid fitness
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
                population_matrix = population_matrix.reshape((pop_len, feat_len))

                # Calculate minimal square bounding box of the objectives
                box_ranges = (numpy.max(population_matrix, axis=0) -
                              numpy.min(population_matrix, axis=0))
                components_matrix = numpy.zeros((pop_len, pop_len))
                for i in xrange(0, pop_len):
                    diff = population_matrix - population_matrix[i, :]
                    components_matrix[i, :] = numpy.max(numpy.divide(diff,box_ranges),axis=1)

                # Calculate max of absolute value of all elements in matrix
                max_absolute_indicator = numpy.max(numpy.abs(components_matrix))

                # Normalisation
                components_matrix = numpy.exp((-1.0 / (kappa * max_absolute_indicator)) *
                                              components_matrix.T)
                return components_matrix



            def _calc_fitnesses(population, components):
                """Calculate the IBEA fitness of every individual"""
                # Calculate sum of every column in the matrix, ignore diagonal elements
                column_sums = numpy.sum(components, axis=0) - numpy.diagonal(components)
                ibfitness=[]
                # Fill the 'ibea_fitness' field on the individuals with the fitness value
                for individual, ibea_fitness in zip(population, column_sums):
                    ibfitness.append(ibea_fitness)
                    individual.ibea_fitness = ibea_fitness

                return ibfitness

            def _mating_selection(population, mu, tourn):
                """Returns the n_of_parents individuals with the best fitness"""

                parents = []
                for gen in xrange(mu):
                    winner = random.choice(population)
                    stats = tools.Statistics(lambda ind: winner.ibea_fitness)
                    stats.register("std", numpy.std, axis=0)
                    stats.register("min", numpy.min, axis=0)
                    stats.register("avg", numpy.mean, axis=0)
                    stats.register("max", numpy.max, axis=0)
                    record = stats.compile(population)

                    for _ in xrange(tourn - 1):
                        individual = random.choice(population)
                        # Save winner is element with smallest fitness
                        if individual.ibea_fitness < winner.ibea_fitness:
                            winner = individual
                    parents.append(winner)
                    self.logbook.record(gen=gen, evals=len(fitnesses), **record)

                return parents

            def _environmental_selection(population, selection_size):
                """Returns the selection_size individuals with the best fitness"""

                # Sort the individuals based on their fitness
                population.sort(key=lambda ind: fitnesses)

                # Return the first 'selection_size' elements
                return population[:selection_size]
            population2 = []
            for x in range(mu):

                invalid_ind = [ind for ind in population if not ind.fitness.valid]
                valid_ind= []
                for i in range(len(population)):
                    poparr = []
                    if not population[i].fitness.valid:
                        for j in range(0,len(population[i])):
                            poparr.append(population[i][j])
                        valid_ind.append(poparr)

                            #fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)

                fitnesses = self.mfun(tuple(valid_ind))
                print fitnesses
                print "_________"
                for individual, fit in zip(invalid_ind, fitnesses):
                    individual.fitness.values = fit

                    #for value in range(2,7):
                    #    if (len(pop) % value) == 0:
                    #        tourn=value;
                components = _calc_fitness_components(population, kappa)
                print components
                        # Calculate the fitness values
                fitnesses=_calc_fitnesses(population, components)

                        # Do the environmental selection
                population[:] = _environmental_selection(population, alpha)

                # Select the parents in a tournament
                population = _mating_selection(population, mu, tourn)

                for i in range(0,len(population)):
                    population2.append(population[i])

            poparray2 = []
            for i in range(len(population2)):
                poparray = []
                for j in range(0,len(population2[i])):
                    poparray.append(population2[i][j])
                poparray2.append(poparray)




            self.final_pop.append(poparray2) #]append([poparray2 , finalfitness[i] , (birth-len(pop)+i)])
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
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_params=option_obj.num_params
        self.SetBoundaries(option_obj.boundaries)
        BOUND_LOW = self.min_max[0]
        BOUND_UP = self.min_max[1]
        NDIM = 30
        print 'option_obj'
        minimweights=[ -x for x in option_obj.weights] #turn weights for minimizing
        print minimweights
        creator.create("FitnessMin", base.Fitness, weights=minimweights)
        creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
        self.toolbox = base.Toolbox()
        def uniformd(low, up, size=None):
            try:
                return [random.uniform(a, b) for a, b in zip(low, up)]
            except TypeError:
                return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]
        self.toolbox.register("attr_float", uniformd, BOUND_LOW, BOUND_UP, NDIM)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", benchmarks.zdt2)
        self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
        self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)
        if algo=='spea':
            self.toolbox.register("select", tools.selSPEA2)
            print 'spea'
        else:
            self.toolbox.register("select", tools.selNSGA2)
            print 'nsga'
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
                valid_ind.append(poparr)

        #fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)

        fitnesses = self.mfun(tuple(valid_ind))

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

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
                    valid_ind.append(poparr)

            #fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
            fitnesses = self.mfun(tuple(valid_ind))

            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit
                if gen == (NGEN-1):
                    finalfits.append(fit)
        # Select the next generation population

            pop = self.toolbox.select(pop + offspring, MU)
            record = stats.compile(pop)
            print 'stats'
            print record
            self.logbook.record(gen=gen, evals=len(invalid_ind), **record)
        #self.final_pop = []
                #self.final_pop.candidate = []
                #self.final_pop.fitness = []
                #self.finap_pop.birthdate = []

        poparray2 = []
        for i in range(len(pop)):
            poparray = []
            for j in range(0,len(pop[i])):
                poparray.append(pop[i][j])
            poparray2.append(poparray)

            #self.final_pop.candidate.append(poparray2)
            #self.final_pop.fitness.append(finalfitness[i])
            #self.finap_pop.birthdate.append((birth-len(pop)+i))
        self.final_pop.append(poparray2) #]append([poparray2 , finalfitness[i] , (birth-len(pop)+i)])
        self.final_pop.append(finalfits)
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
