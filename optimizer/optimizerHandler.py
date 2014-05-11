from random import Random
#from time import time
from inspyred import ec
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
        except KeyError:
            sys.exit("Unknown fitness function!")
        try:
            option_obj.feats=map(lambda x:self.fit_obj.calc_dict[x],option_obj.feats)
        except KeyError:
            print "error with fitness function: ",option_obj.feats," not in: ",self.fit_obj.calc_dict.keys()
            pass
        
    

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
    :param args: ``dictionary``, must contain key "num_inputs" and either "_ec" or "self"
    
    :return: the created random values in a ``list``
    
    """
    size=args.get("num_inputs")
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
    
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})),self)]
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
                                             num_inputs=self.num_inputs, 
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
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
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
                         x0=ndarray((self.num_inputs,),buffer=array(self.starting_points),offset=0,dtype=float),
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
                                                       "maxfun" : 1000}},
                         take_step=None,
                         accept_test=self.bounder,
                         callback=self.logger,
                         interval=int(self.freq),
                         disp=False,
                         niter_success=None)
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
            self.log_file.write("".join(["-"]*200))
        self.log_file.close()
        
        self.result=min(list_of_results,key=lambda x:x.fun)
        print self.result.x
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
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                raise TypeError
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
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
                                      x0=ndarray((self.num_inputs,),buffer=array(self.starting_points),offset=0,dtype=float), 
#                                      x0=ndarray( (self.num_inputs,1) ,buffer=array([0.784318808, 4.540607953, -11.919391073,-100]),dtype=float),
                                      args=[[]],  
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
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        try:
            if isinstance(option_obj.starting_points[0],list):
                raise TypeError
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
            
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
                                      x0=ndarray((self.num_inputs,),buffer=array(self.starting_points),offset=0,dtype=float), 
#                                      x0=ndarray( (self.num_inputs,1) ,buffer=array([0.784318808, 4.540607953, -11.919391073,-100]),dtype=float),
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
        self.num_inputs=option_obj.num_inputs
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
        for n in range(self.num_inputs):
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
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})),self)]
        try:
            print type(option_obj.starting_points)
            if isinstance(option_obj.starting_points[0],list):
                self.starting_points=option_obj.starting_points
            else:
                self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        print "optimizer",self.starting_points
                
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
                                             num_inputs=self.num_inputs, 
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
    
        


        
        
