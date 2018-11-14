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
import time
import os

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
import queue
import Core
#from inspyred.ec.terminators import max_evaluations
import pickle as pickle

from pybrain.optimization.distributionbased.distributionbased import DistributionBasedOptimizer
from scipy import dot, exp, log, sqrt, floor, ones, randn
from pybrain.tools.rankingfunctions import RankingFunction

import pygmo as pg
import modelHandler
from itertools import combinations, product

global moo_var
global brain_var

brain_var=False

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

def normalize(values,args):
	"""
	Normalizes the values of the given ``list`` using the defined boundaries.

	:param v: the ``list`` of values
	:param args: an object which has a ``min_max`` attribute which consists of two ``lists``
		each with the same number of values as the given list

	:return: the ``list`` of normalized values

	"""
	copied_values = copy.copy(values)
	for i in range(len(values)):
		copied_values[i]=(values[i]-args.min_max[0][i])/(args.min_max[1][i]-args.min_max[0][i])
	return copied_values


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
	for i in range(int(size)):
		candidate.append(random.uniform(bounds.lower_bound[i],bounds.upper_bound[i]))
	return candidate

def uniformz(random,size,bounds):
	"""
	Creates random values from a uniform distribution. Used to create initial population.

	:param random: random number generator object
	:param args: ``dictionary``, must contain key "num_params" and either "_ec" or "self"

	:return: the created random values in a ``list``

	"""
	candidate=[]
	for i in range(int(size)):
		candidate.append(random.uniform(bounds.lower_bound[i],bounds.upper_bound[i]))
	return candidate

class oldBaseOptimizer():
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
				option_obj.feats=[self.fit_obj.calc_dict[x] for x in option_obj.feats]
			except KeyError:
				print("error with fitness function: ",option_obj.feats," not in: ",list(self.fit_obj.calc_dict.keys()))

# to generate a new set of parameters
class baseOptimizer():
	"""
	An abstract base class to implement an optimization process.
	"""
	def __init__(self, reader_obj, model_obj, option_obj):
		self.fit_obj = fF(reader_obj, model_obj, option_obj)
		self.SetFFun(option_obj)
		self.rand = random
		self.seed = int(option_obj.seed)
		self.rand.seed(self.seed)
		self.directory = option_obj.base_dir

		self.num_params = option_obj.num_params
		self.number_of_cpu=option_obj.number_of_cpu

		self.SetBoundaries(option_obj.boundaries)

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
				option_obj.feats=[self.fit_obj.calc_dict[x] for x in option_obj.feats]
			except KeyError:
				print("error with fitness function: ",option_obj.feats," not in: ",list(self.fit_obj.calc_dict.keys()))

	def SetBoundaries(self, bounds):
		"""
		Stores the bounds of the parameters and creates a ``bounder`` object which bounds
		every parameter into the range of 0-1 since the algorithms are using normalized values.

		:param bounds: ``list`` containing the minimum and maximum values.

		"""
		self.min_max = bounds
		self.bounder = ec.Bounder([0] * len(self.min_max[0]), [1] * len(self.min_max[1]))

class InspyredAlgorithmBasis(baseOptimizer):
	def __init__(self, reader_obj, model_obj, option_obj):
		baseOptimizer.__init__(self, reader_obj, model_obj, option_obj)

		self.pop_size = option_obj.pop_size
		self.max_evaluation = option_obj.max_evaluation

		self.maximize = False  # hard wired, always minimize
		self.stat_file = open(self.directory + "/stat_file.txt", "w")
		self.ind_file = open(self.directory + "/ind_file.txt", "w")


		try:
			# print type(option_obj.starting_points)
			if isinstance(option_obj.starting_points[0], list):
				self.starting_points = option_obj.starting_points
			else:
				self.starting_points = [normalize(option_obj.starting_points, self)]
		except TypeError:
			self.starting_points = None
		if option_obj.output_level == "1":
			print("starting points: ", self.starting_points)

		self.kwargs = dict(generator=uniform,
						   evaluator=inspyred.ec.evaluators.parallel_evaluation_mp,
						   mp_evaluator=self.ffun,
						   mp_nprocs=int(self.number_of_cpu),
						   pop_size=self.pop_size,
						   seeds=self.starting_points,
						   max_generations=self.max_evaluation,
						   num_params=self.num_params,
						   maximize=self.maximize,
						   bounder=self.bounder,
						   boundaries=self.min_max,
						   statistics_file=self.stat_file,
						   individuals_file=self.ind_file)
				
	def Optimize(self):
			"""
			Performs the optimization.
			"""
			logger = logging.getLogger('inspyred.ec')
			logger.setLevel(logging.DEBUG)
			file_handler = logging.FileHandler(self.directory + '/inspyred.log', mode='w')
			file_handler.setLevel(logging.DEBUG)
			formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
			file_handler.setFormatter(formatter)
			logger.addHandler(file_handler)

			self.final_pop = self.evo_strat.evolve(**self.kwargs)

			if hasattr(self.evo_strat, "archive"):
				self.final_archive = self.evo_strat.archive

class ScipyAlgorithmBasis(baseOptimizer):

	def __init__(self, reader_obj, model_obj, option_obj):
		baseOptimizer.__init__(self, reader_obj, model_obj, option_obj)

		try:
			if isinstance(option_obj.starting_points[0], list):
				raise TypeError
			else:
				self.starting_points = [normalize(option_obj.starting_points, self)]
		except TypeError:
			self.starting_points = uniform(self.rand, {"num_params": self.num_params, "self": self})
		if option_obj.output_level == "1":
			print("starting points: ", self.starting_points)

	def wrapper(self, candidates, args):
		"""
		Converts the ``ndarray`` object into a ``list`` and passes it to the fitness function.

		:param candidates: the ``ndarray`` object
		:param args: optional parameters to be passed to the fitness function

		:return: the return value of the fitness function

		"""
		tmp = ndarray.tolist(candidates)
		candidates = self.bounder(tmp, args)
		return self.ffun([candidates], args)[0]

class PygmoAlgorithmBasis(baseOptimizer):

	def __init__(self, reader_obj, model_obj, option_obj):
		baseOptimizer.__init__(self, reader_obj, model_obj, option_obj)

		pg.set_global_rng_seed(seed = self.seed)
		self.boundaries = option_obj.boundaries
		self.base_dir = option_obj.base_dir
		
		self.num_islands = int(option_obj.num_islands)

	def Optimize(self):

		self.prob = Problem(self.ffun,self.boundaries, self.num_islands, self.pop_size, self.max_evaluation, self.base_dir)
		self.archi = pg.archipelago(n=self.num_islands,algo=self.algorithm, prob=self.prob, pop_size=self.pop_size)
		
		self.archi.evolve()
		

		print(self.archi)
		
		self.archi.wait()
		print(self.archi)
		self.champions_x = self.archi.get_champions_x()
		self.champions_f = self.archi.get_champions_f()
		print(self.champions_x)
		print(self.champions_f)

		self.best_fitness = min(self.champions_f)
		self.best = normalize(self.champions_x[self.champions_f.index(self.best_fitness)], self)

class Problem:
	
	def __init__(self, fitnes_fun, bounds, num_islands=1, pop_size=1, max_evaluations=1, directory=''):
		self.bounds = bounds
		self.min_max = bounds
		self.fitnes_fun = fitnes_fun
		self.num_islands = num_islands
		self.pop_size = pop_size
		self.max_evaluations = max_evaluations
		self.pop_counter = 0
		self.gen_counter = 0
		self.directory = directory

		try:
			os.remove(self.directory + '/island_inds.txt')
		except OSError:
			pass

	def fitness(self, x):

		#print("individual: {0}".format(x))
		#print("normalized: {0}".format(normalize(x, self)))
		fitness = self.fitnes_fun([normalize(x,self)])
		print('PYGMO FITNES')
		#print("fitness: {0} at {1}".format(fitness, time.time()))
		with open(self.directory + '/island_inds.txt', 'a') as inds_file:
			inds_file.write("{0}, {1}, {2}, {3}, {4}\n".format(self.gen_counter, self.pop_counter, fitness, x, normalize(x, self)))
		self.pop_counter += 1
		if (self.pop_counter * self.num_islands) % (self.pop_size * self.num_islands) == 0:
			self.pop_counter = 0
			self.gen_counter += 1
			print("Generation: {0}".format(self.gen_counter))


		return fitness

	def get_bounds(self):
		return(self.bounds[0], self.bounds[1])


class SinglePygmoAlgorithmBasis(baseOptimizer):

	def __init__(self, reader_obj, model_obj, option_obj):
		baseOptimizer.__init__(self, reader_obj, model_obj, option_obj)

		pg.set_global_rng_seed(seed = self.seed)
		self.prob = SingleProblem(self.ffun,option_obj.boundaries)
		self.directory = option_obj.base_dir

		self.pop_kwargs = dict()

	def write_statistics_file(self):
		with open (self.directory + "/stat_file.txt", 'w+') as stat_file:  
			for line in self.log:
				#print(line, 'LINE')
				for i,element in enumerate(line):
					if i == len(line)-1:
						stat_file.write(str(element))
					else:
						stat_file.write(str(element) + ', ')
				stat_file.write('\n')

	def Optimize(self):

		self.population = pg.population(self.prob, **self.pop_kwargs)


		self.algorithm.set_verbosity(1)
		self.evolved_pop = self.algorithm.evolve(self.population)

		uda = self.algorithm.extract(self.algo_type)
		self.log = uda.get_log()
		print(log)
		self.write_statistics_file()

		self.best = normalize(self.evolved_pop.champion_x, self) 
		self.best_fitness = self.evolved_pop.champion_f

class SingleProblem:
	
	def __init__(self, fitnes_fun, bounds):
		self.bounds = bounds
		self.min_max = bounds
		self.fitnes_fun = fitnes_fun

	def __getstate__(self):
		bounds = self.bounds
		min_max = self.min_max
		f_f = self.fitnes_fun
		return (bounds, min_max, f_f)

	def __setstate__(self, state):
		self.bounds, self.min_max, self.fitnes_fun = state


	def fitness(self, x):
		return self.fitnes_fun([normalize(x,self)])

	def get_bounds(self):
		return(self.bounds[0], self.bounds[1])

class SinglePygmoDE(SinglePygmoAlgorithmBasis):
	
	def __init__(self,reader_obj,model_obj,option_obj):

		SinglePygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)
	
		self.max_evaluation=int(option_obj.max_evaluation)
		
		self.pop_kwargs['size'] = int(option_obj.pop_size)

		self.algo_type = pg.de        
		self.algorithm = pg.algorithm(pg.de(gen=self.max_evaluation, ftol=1e-15, tol=1e-15))


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


class annealing(InspyredAlgorithmBasis):
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
		InspyredAlgorithmBasis.__init__(self, reader_obj,model_obj,option_obj)

		self.kwargs['mutation_rate'] = option_obj.mutation_rate
		self.kwargs['gaussian_mean'] = option_obj.m_gauss
		self.kwargs['gaussian_stdev'] = option_obj.std_gauss
		self.kwargs['temperature'] = option_obj.init_temp
		self.kwargs['cooling_rate'] = option_obj.cooling_rate
		self.kwargs['max_evaluations'] = self.max_evaluation

		self.evo_strat=ec.SA(self.rand)
		self.evo_strat.terminator=terminators.evaluation_termination
		if option_obj.output_level=="1":
			self.evo_strat.observer=[observers.population_observer,observers.file_observer]
		else:
			self.evo_strat.observer=[observers.file_observer]

class PygmoDE(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.de(gen=self.max_evaluation, ftol=1e-15, tol=1e-15))

class PygmoCMAES(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		self.force_bounds = option_obj.force_bounds

		self.algorithm = pg.algorithm(pg.cmaes(gen=self.max_evaluation, ftol=1e-15, xtol=1e-15, force_bounds=bool(self.force_bounds)))

class PygmoPSO(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.pso(gen=self.max_evaluation))

class PygmoXNES(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		self.force_bounds = option_obj.force_bounds if option_obj.force_bounds else False
		print('BOUND :', self.force_bounds)

		self.algorithm = pg.algorithm(pg.xnes(gen=self.max_evaluation, ftol=1e-15, xtol=1e-15, force_bounds=bool(self.force_bounds)))

class PygmoBEE(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.bee_colony(gen=self.max_evaluation))

class PygmoSGA(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.sga(gen=self.max_evaluation))

class PygmoSADE(PygmoAlgorithmBasis):

	def __init__(self,reader_obj,model_obj,option_obj):

		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)

		if int(option_obj.pop_size)<7:
			print("***************************************************")
			print("SADE NEEDS A POPULATION WITH AT LEAST 7 INDIVIDUALS")
			print("***************************************************")
			self.pop_size = 7
		else:
			self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.sade(gen=self.max_evaluation, ftol=1e-15, xtol=1e-15))

class PygmoDE1220(PygmoAlgorithmBasis):

	def __init__(self,reader_obj,model_obj,option_obj):

		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)

		if int(option_obj.pop_size)<7:
			print("*****************************************************")
			print("DE1220 NEEDS A POPULATION WITH AT LEAST 7 INDIVIDUALS")
			print("*****************************************************")
			self.pop_size = 7
		else:
			self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.algorithm(pg.de1220(gen=self.max_evaluation, ftol=1e-15, xtol=1e-15))


class PSO(InspyredAlgorithmBasis):
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

		InspyredAlgorithmBasis.__init__(self,reader_obj,model_obj,option_obj)

		#PSO algorithm
		self.evo_strat=inspyred.swarm.PSO(self.rand)

		#algorithm terminates at max number of generations
		self.evo_strat.terminator=terminators.generation_termination

		if option_obj.output_level=="1":
			self.evo_strat.observer=[observers.population_observer,observers.file_observer]
		else:
			self.evo_strat.observer=[observers.file_observer]


		#PSO attributes
		self.kwargs["inertia"] = option_obj.inertia
		self.kwargs["cognitive_rate"] = option_obj.cognitive_rate
		self.kwargs["social_rate"] = option_obj.social_rate
		'''
		if (self.topology == "Star"):
			self.evo_strat.topology = inspyred.swarm.topologies.star_topology
		elif (self.topology == "Ring"):
			self.evo_strat.topology = inspyred.swarm.topologies.ring_topology
		#self.neighborhood_size=int(round(option_obj.neighborhood_size))
		'''
		self.kwargs["topology"] = inspyred.swarm.topologies.star_topology
	def Optimize(self):
		"""
		Performs the optimization.
		"""
		logger = logging.getLogger('inspyred.ec')
		logger.setLevel(logging.DEBUG)
		file_handler = logging.FileHandler(self.directory + '/inspyred.log', mode='w')
		file_handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		file_handler.setFormatter(formatter)
		logger.addHandler(file_handler)

		self.final_pop = self.evo_strat.evolve(**self.kwargs)

class basinHopping(ScipyAlgorithmBasis):
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
		ScipyAlgorithmBasis.__init__(self, reader_obj,model_obj,option_obj)

		self.temp=option_obj.temperature
		self.num_iter=option_obj.num_iter
		self.num_repet=option_obj.num_repet
		self.step_size=option_obj.step_size
		self.freq=option_obj.update_freq
		

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

		self.log_file=open(self.directory + "/basinhopping.log","w")
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
			print("starting points: ",self.starting_points)



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
			print("starting points: ",self.starting_points)


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
		print(self.result[-1]['warnflag'])
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


class simpleEO(InspyredAlgorithmBasis):
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
		InspyredAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.kwargs["mutation_rate"] = option_obj.mutation_rate
		self.kwargs["num_elites"] = int(self.pop_size/2)
		self.kwargs["gaussian_stdev"] = 0.5

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


class DEA(InspyredAlgorithmBasis):
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

		InspyredAlgorithmBasis.__init__(self,reader_obj,model_obj,option_obj)
		self.kwargs["tournament_size"] = int(self.pop_size)
		self.kwargs["num_selected"] = int(self.pop_size/10)
		self.kwargs["mutation_rate"] = option_obj.mutation_rate
		self.kwargs["crossover_rate"] = option_obj.crossover_rate

		self.evo_strat=ec.DEA(self.rand)
		self.evo_strat.terminator=terminators.generation_termination

		if option_obj.output_level=="1":
			self.evo_strat.observer=[observers.population_observer,observers.file_observer]
		else:
			self.evo_strat.observer=[observers.file_observer]


class RandomSearch(InspyredAlgorithmBasis):
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
		InspyredAlgorithmBasis.__init__(self,reader_obj,model_obj,option_obj)
		for file_name in ["stat_file.txt", "ind_file.txt"]:
			try:
				os.remove(file_name)
			except OSError:
				pass


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

		log_f.close()
		self.final_pop=[self.act_min]


# simple NSGA-II
class NSGAII(InspyredAlgorithmBasis):
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
		InspyredAlgorithmBasis.__init__(self, reader_obj,model_obj,option_obj)
		self.kwargs["mp_evaluator"] = self.mfun
		global moo_var
		moo_var = True
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



class PAES(InspyredAlgorithmBasis):
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
		InspyredAlgorithmBasis.__init__(self, reader_obj,model_obj,option_obj)

		self.kwargs["mp_evaluator"] = self.mfun

		global moo_var
		moo_var = True

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

		self.kwargs['mutation_rate'] = option_obj.mutation_rate
		self.kwargs['num_elites'] = int(self.pop_size/2)

class FullGrid(InspyredAlgorithmBasis):
	
	def __init__(self,reader_obj,model_obj,option_obj):
		InspyredAlgorithmBasis.__init__(self, reader_obj,model_obj,option_obj)

		self.evo_strat=ec.ES(self.rand)

		if option_obj.output_level=="1":
			self.evo_strat.observer=[observers.population_observer,observers.file_observer]
		else:
			self.evo_strat.observer=[observers.file_observer]
		

		self.resolution = [5,5,5]
		#self.resolution = list(map(lambda x: x if x>=3 else 3, self.resolution))
		
		if(len(self.resolution) < self.kwargs['num_params']):
			print("Not enough values for every parameter. Will expand resolution with threes.")
			self.resolution = self.resolution + [1] * (self.kwargs['num_params'] - len(self.resolution))
			print("New resolution is: ", self.resolution)
			

		elif(len(self.resolution) > self.kwargs['num_params']):
			print("Too many values. Excess resolution will be ignored.")
			self.resolution = self.resolution[0:self.kwargs['num_params']]
			print("New resolution is: ", self.resolution)
			
		
		
		self.grid = [] 
		self.alldims = []
	#self.point = option_obj.point
		#HH
		self.point = [0.12,0.036,0.0003]
		if(not self.point):
			print("No point given. Will take center of grid")
			self.point = list(map(lambda x: int(x/2), self.resolution))
			print("New point is: ", self.point)
			
		#CLAMP
		#self.point = [0.01, 2, 0.3, 3] 
		#align grid on point
		
		for j in range(len(option_obj.boundaries[0])):
			if(self.resolution[j] == 1):
				self.alldims.append([self.point[j]])
				continue
			
			#ugly way to ensure same resolution before and after point included
			upper_bound = option_obj.boundaries[1][j] - float((float(option_obj.boundaries[1][j]))/float(self.resolution[j]-1)/2)
			
			div = float((upper_bound)/(self.resolution[j]-1))
			lower_bound = (self.point[j]/div % 1) * div
			
			upper_bound = upper_bound + lower_bound
			
			self.alldims.append(list(np.linspace(lower_bound,upper_bound,self.resolution[j])))
			
			
		print(option_obj.boundaries)

		for i,t in enumerate(combinations(self.alldims, r=self.num_params-1)):
			plane_dimensions = list(t) 
			optimum_point = [self.point[self.num_params-1-i]]
			plane_dimensions.insert(self.num_params-1-i, optimum_point) 
			print("PLANE", plane_dimensions)

			for t in product(*plane_dimensions):
				print(list(t))
				#exit()
				if(len(self.point)-1-i)==0:
					print(list(t))
					#exit()
				print(list(t))
				self.grid.append(normalize(list(t),self))

				
			if(len(self.point)-1-i)==0:
				print(len(plane_dimensions[0]))


		print(self.grid)
		print(type(self.grid))

		self.kwargs["seeds"] = self.grid
		self.kwargs["max_generations"] = 0
		self.kwargs["pop_size"] = 1
		#candidate[-0.024653979238754356, -0.012413494809688589, 0.02948166788997238]
		#fitnes 0.746863844888 0.746863844888

		print("NOOOORM", normalize([0.12,0.036,0.0003],self))
		#self.grid = [normalize([0.12,0.036,0.0003],self), [ 0.42144982,  0.10608837,  0.18303551]]
		#print(self.grid)




def selIBEA(population, mu, alpha=None, kappa=.05, tournament_n=4):
	"""IBEA Selector"""
	print("selIBEA OK")
	if alpha is None:
		alpha = len(population)

	# Calculate a matrix with the fitness components of every individual
	components = _calc_fitness_components(population, kappa=kappa)
	print("Calc fitnes components OK")

	# Calculate the fitness values
	_calc_fitnesses(population, components)
	print("Calc fitnes OK")

	# Do the environmental selection
	population[:] = _environmental_selection(population, alpha)
	print("Env selection OK")

	# Select the parents in a tournament
	parents = _mating_selection(population, mu, tournament_n)
	print("Mating OK")
	print('\nPARENTS')
	print(parents)
	return parents


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
	print("box_ranges OK")
	# Replace all possible zeros to avoid division by zero
	# Basically 0/0 is replaced by 0/1
	box_ranges[box_ranges == 0] = 1.0

	components_matrix = numpy.zeros((pop_len, pop_len))
	for i in range(0, pop_len):
		diff = population_matrix - population_matrix[i, :]
		components_matrix[i, :] = numpy.max(
			numpy.divide(diff, box_ranges),
			axis=1)
	print("divide OK")
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
	for _ in range(mu):
		winner = _choice(population)
		for _ in range(tournament_n - 1):
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


class deapIBEA(oldBaseOptimizer):



	def __init__(self,reader_obj,model_obj,option_obj):
		self.fit_obj=fF(reader_obj,model_obj,option_obj)
		self.SetFFun(option_obj)
		self.rand=Random()
		self.directory = option_obj.base_dir
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
		minimweights=[ -x for x in option_obj.weights]*reader_obj.number_of_traces() #turn weights for minimizing
		creator.create("FitnessMin", base.Fitness, weights=minimweights)
		creator.create("Individual", array1.array, typecode='d', fitness=creator.FitnessMin)
		self.toolbox = base.Toolbox()
		def uniformd(low, up, size=None):
			try:
				return [random.uniform(a, b) for a, b in zip(low, up)]
			except TypeError:
				return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]
		self.toolbox.register("attr_float", uniformd, BOUND_LOW, BOUND_UP, NDIM)
		self.toolbox.register("evaluate", self.mfun)
		self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr_float)
		self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
		self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
		self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)
		pool=multiprocessing.Pool(processes=int(self.number_of_cpu))
		self.toolbox.register("map",pool.map)
		self.stat_file=open(self.directory + "/stat_file.txt", "w")

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
			print(self.logbook)
			self.stat_file.write(self.logbook.__str__())

			


	def SetBoundaries(self,bounds):

		self.min_max=bounds
		self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
		print('self.min_max')
		print(self.min_max[0])
		print(self.min_max[1])
		print('self.bounder')
		print(self.bounder)


class deapNSGA(oldBaseOptimizer):


	def __init__(self,reader_obj,model_obj,option_obj,algo):
		self.fit_obj=fF(reader_obj,model_obj,option_obj)
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
		minimweights=[ -x for x in option_obj.weights]*reader_obj.number_of_traces() #turn weights for minimizing
		print(minimweights)
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
		self.toolbox.register("evaluate", self.mfun)
		self.toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0)
		self.toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=20.0, indpb=1.0/NDIM)
		if algo=='spea':
			self.toolbox.register("select", tools.selSPEA2)
			print('spea')
		elif algo=='ibea':
			self.toolbox.register("select", selIBEA)
			print('ibea')
		else:
			self.toolbox.register("select", tools.selNSGA2)
			print('nsga')
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
			print("starting points: ",self.starting_points)

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
				valid_ind.append([normalize(poparr,self)])

		#fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)

		fitnesses = self.toolbox.map(self.toolbox.evaluate,valid_ind)
		print("fits")
		print(fitnesses)
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
					valid_ind.append([normalize(poparr, self)])

			#fitnesses = self.toolbox.map(self.toolbox.evaluate, invalid_ind)
			fitnesses = self.toolbox.map(self.toolbox.evaluate,valid_ind)

			for ind, fit in zip(invalid_ind, fitnesses):
				ind.fitness.values = fit[0]

		# Select the next generation population

			pop2 = [arr.tolist() for arr in pop]
			poparray2 += pop2 #]append([poparray2 , finalfitness[i] , (birth-len(pop)+i)])
			
			fitnesses = [fit[0] for fit in fitnesses]
			finalfits += fitnesses
			pop = self.toolbox.select(pop + offspring, MU)

			record = stats.compile(pop)

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
		print('self.min_max')
		print(self.min_max[0])
		print(self.min_max[1])
		print('self.bounder')
		print(self.bounder)





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
		print((self._allEvaluated))
		print((len(self._allEvaluated)))
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



class NES(oldBaseOptimizer):



	def __init__(self,reader_obj,model_obj,option_obj):
		self.fit_obj=fF(reader_obj,model_obj,option_obj)
		global brain_var
		brain_var=True
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
			lp=SNES(self.ffun,initparam,verbose=True,batchSize=MU)
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
		print('self.min_max')
		print(self.min_max[0])
		print(self.min_max[1])
		print('self.bounder')
		print(self.bounder)
