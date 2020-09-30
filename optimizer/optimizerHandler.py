from random import Random
from inspyred import ec
from inspyred.ec import emo
from inspyred.ec import terminators
from inspyred.ec import variators
from inspyred.ec import observers
from fitnessFunctions import fF,frange
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
import numpy
import time
import os
import bluepyopt as bpop
from math import sqrt
import bluepyopt.ephys as ephys


import multiprocessing
from math import sqrt
from optionHandler import optionHandler
from deap import algorithms
from deap import base
from deap import benchmarks
from deap.benchmarks.tools import diversity, convergence, hypervolume
from deap import creator
from deap import tools
import queue
import Core

from scipy import dot, exp, log, sqrt, floor, ones, randn

import pygmo as pg
import modelHandler
from itertools import combinations, product


from PyQt5 import QtCore, QtGui, QtWidgets
from types import MethodType
try:
    import copyreg
except:
    import copyreg

import functools
try:
    import cPickle as pickle
except ImportError:
    import pickle
				

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
			self.mfun=self.fit_obj.fun_dict["Multiobj"]
			self.deapfun=self.fit_obj.fun_dict["Deapwrapper"]
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
			self.mfun=self.fit_obj.fun_dict["Multiobj"]
			self.deapfun=self.fit_obj.fun_dict["Deapwrapper"]
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
		self.prob = Problem(self.ffun,self.boundaries, self.num_islands, self.pop_size, 1, self.base_dir)
		
		
		"""try:
			self.archi = pickle.load(open(str(self.base_dir)+'/pygmo_save.pkl', 'rb'))
			print('save loaded')
		except:
			print('no previous save found')
			self.archi = pg.archipelago(n=self.num_islands,algo=self.algorithm, prob=self.prob, pop_size=self.pop_size)
		print(self.max_evaluation)"""
		self.mpbfe=pg.mp_bfe()
		self.mpbfe.init_pool(self.number_of_cpu)
		self.bfe=pg.bfe(self.mpbfe)
		try:
			self.algorithm.set_bfe(self.bfe)
		except:
			"no bfe"
		self.pgalgo=pg.algorithm(self.algorithm)
		self.archi = pg.archipelago(n=self.num_islands,algo=self.pgalgo, prob=self.prob, pop_size=self.pop_size,b=self.bfe)
		self.archi.evolve(self.max_evaluation)
		self.archi.wait()
		self.mpbfe.shutdown_pool()
		
		pickle.dump(self.archi,open(str(self.base_dir)+'/pygmo_save.pkl', 'wb'))
		self.archi.wait()
		
		
		self.champions_x = self.archi.get_champions_x()
		self.champions_f = self.archi.get_champions_f()
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

		fitness = self.fitnes_fun([normalize(x,self)])
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
		print(self.population)
		print(self.evolved_pop)
		pickle.dump(self.evolved_pop,open('pygmo_save.pkl', 'wb'))

		
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

class Single_Differential_Evolution_Pygmo(SinglePygmoAlgorithmBasis):
	
	def __init__(self,reader_obj,model_obj,option_obj):

		SinglePygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)
	
		self.max_evaluation=int(option_obj.max_evaluation)
		
		self.pop_kwargs['size'] = int(option_obj.pop_size)

		self.algo_type = pg.de        
		self.algorithm = pg.de(gen=1)


class my_candidate():
	"""
	Mimics the behavior of ``candidate`` from the ``inspyred`` package to allow the uniform
	handling of the results produced by the different algorithms.

	:param vals: the result of the optimization
	:param fitn: the fitness of the result

	"""
	def __init__(self,vals, fitn=-1):
		self.candidate=ndarray.tolist(vals)
		#self.candidate.extend(vals)
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


class Simulated_Annealing_Inspyred(InspyredAlgorithmBasis):
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

class Differential_Evolution_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.de(gen=1)

class Covariance_Matrix_Adaptation_ES_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		self.force_bounds = option_obj.force_bounds
		self.algorithm = pg.cmaes(gen=1,ftol=1e-15, xtol=1e-15, force_bounds=bool(self.force_bounds))

class Particle_Swarm_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.pso(gen=1)

class Particle_Swarm_Gen_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		
		self.algorithm = pg.pso_gen(gen=1)

class Multi_Objective_Ant_Colony_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		
		self.algorithm = pg.maco(gen=1)

class Extended_Ant_Colony_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
	
		self.algorithm = pg.gaco(gen=1)

class Non_Dominated_Particle_Swarm_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		
		self.algorithm = pg.nspso(gen=1)

class Non_Dominated_Particle_Swarm_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		
		self.algorithm = pg.nsga2(gen=1)


class Exponential_Evolution_Strategies_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)
		self.force_bounds = option_obj.force_bounds if option_obj.force_bounds else False
		print('BOUND :', self.force_bounds)

		self.algorithm = pg.xnes(gen=1,ftol=1e-15, xtol=1e-15, force_bounds=bool(self.force_bounds))

class Bee_Colony_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.bee_colony(gen=1)

class Simple_Genetic_Algorithm_Pygmo(PygmoAlgorithmBasis):
	def __init__(self, reader_obj, model_obj, option_obj):
		PygmoAlgorithmBasis.__init__(self, reader_obj, model_obj, option_obj)

		self.max_evaluation=int(option_obj.max_evaluation)
		self.pop_size = int(option_obj.pop_size)

		self.algorithm = pg.sga(gen=1)

class Self_adaptive_DE_Pygmo(PygmoAlgorithmBasis):

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

		self.algorithm = pg.sade(gen=1,ftol=1e-15, xtol=1e-15)

class Differential_Evolution_1220_Pygmo(PygmoAlgorithmBasis):

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

		self.algorithm = pg.de1220(gen=1,ftol=1e-15, xtol=1e-15)


class Particle_Swarm_Inspyred(InspyredAlgorithmBasis):
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

class Basinhopping_Scipy(ScipyAlgorithmBasis):
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


class Nelder_Mead_Scipy(baseOptimizer):
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



class L_BFGS_B_Scipy(baseOptimizer):
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


class Evolutionary_Algorithm_Inspyred(InspyredAlgorithmBasis):
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


class Differential_Evolution_Inspyred(InspyredAlgorithmBasis):
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


class Random_Search_Base(baseOptimizer):
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
		baseOptimizer.__init__(self, reader_obj, model_obj, option_obj)		
		self.directory = str(option_obj.base_dir)
		self.max_evaluation = option_obj.max_evaluation
		self.pop_size = option_obj.pop_size
		self.pickled_args={}
		self.gen_min=[]
		self.pool = multiprocessing.Pool(processes=int(self.number_of_cpu))
		for file_name in ["stat_file.txt", "ind_file.txt"]:
			try:
				os.remove(file_name)
			except OSError:
				pass
				


	def Optimize(self):
		"""
		Performs the optimization.
		"""
		init_candidate=uniform(self.rand, {"self":self,"num_params":self.num_params})
		self.act_min=my_candidate(array(init_candidate),self.ffun([init_candidate],{}))
		
		for i in range(int(self.max_evaluation)):
			act_candidate=[]
			act_fitess=[]
			for j in range(int(self.pop_size)):
				act_candidate.append([uniform(self.rand, {"self":self,"num_params":self.num_params})])
			
			try:
				act_fitess=self.pool.map(self.ffun,act_candidate)
			except (OSError, RuntimeError) as e:
				raise

			
			for act_fit,act_cand in zip(act_fitess,act_candidate):
				if (act_fit<self.act_min.fitness):
					self.act_min=my_candidate(array(act_cand),act_fit)
					
				
			self.gen_min.append(self.act_min)		

		self.pool.close()
		with open(self.directory+"/random.txt","w") as f:
			for x in self.gen_min:
				f.write(str(x.candidate))
				f.write("\t")
				f.write(str(x.fitness))
				f.write("\n")

		self.final_pop=list(self.gen_min)


# simple NSGA-II
class Nondominated_Sorted_Inspyred(InspyredAlgorithmBasis):
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



class Pareto_Archived_ES_Inspyred(InspyredAlgorithmBasis):
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
		#self.kwargs['num_elites'] = int(4)

class FullGrid_Pygmo(InspyredAlgorithmBasis):
	
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
		






	def SetBoundaries(self,bounds):

		self.min_max=bounds
		self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
		print('self.min_max')
		print(self.min_max[0])
		print(self.min_max[1])
		print('self.bounder')
		print(self.bounder)


class Indicator_Based_Bluepyopt(oldBaseOptimizer):


	def __init__(self,reader_obj,model_obj,option_obj):
		self.fit_obj=fF(reader_obj,model_obj,option_obj)
		self.SetFFun(option_obj)
		self.option_obj=option_obj
		self.seed=option_obj.seed
		self.directory = str(option_obj.base_dir)
		self.pop_size=option_obj.pop_size
		self.max_evaluation=option_obj.max_evaluation
		self.num_params=option_obj.num_params
		self.number_of_cpu=option_obj.number_of_cpu
		self.SetBoundaries(option_obj.boundaries)
		self.param_names=self.option_obj.GetObjTOOpt()
		if self.option_obj.type[-1]!="features":
			self.number_of_traces=reader_obj.number_of_traces()
		else:
			self.number_of_traces=len(reader_obj.features_data["stim_amp"])
		feats=self.get_feat_names(self.option_obj.GetFitnessParam())
		self.feats_and_weights=[x for x in zip(feats[0],feats[1])]
		self.params=zip(self.param_names,self.min_max[0],self.min_max[1])
		



	def Optimize(self):
		
		#try:
		from ipyparallel import Client
		print("******************PARALLEL RUN : IBEA *******************")
		os.system("ipcluster start -n "+str(int(self.number_of_cpu))+"  &")
		time.sleep(60)
		c = Client(timeout=60)
		view = c.load_balanced_view()
		view.map_sync(os.chdir, [str(os.path.dirname(os.path.realpath(__file__)))]*int(self.number_of_cpu))
		map_function=view.map_sync
		optimisation = bpop.optimisations.DEAPOptimisation(evaluator=DeapEvaluator(self.params,self.deapfun,self.feats_and_weights,self.min_max,self.number_of_traces),seed=self.seed,offspring_size = int(self.pop_size),map_function=map_function,selector_name='IBEA')
		self.final_pop, self.hall_of_fame, self.logs, self.hist = optimisation.run(int(self.max_evaluation),cp_frequency=int(self.max_evaluation))
		os.system("ipcluster stop")
		#except Exception:
		"""os.system("ipcluster stop")
		print("*****************Single Run : IBEA *******************")
		optimisation = bpop.optimisations.DEAPOptimisation(evaluator=DeapEvaluator(self.params,self.deapfun,self.feats_and_weights,self.min_max,self.number_of_traces),seed=self.seed,offspring_size = int(self.pop_size),selector_name='IBEA')
		self.final_pop, self.hall_of_fame, self.logs, self.hist = optimisation.run(int(self.max_evaluation))"""	
		

	def SetBoundaries(self,bounds):
		"""
		Stores the bounds of the parameters and creates a ``bounder`` object which bounds
		every parameter into the range of 0-1 since the algorithms are using normalized values.

		:param bounds: ``list`` containing the minimum and maximum values.

		"""
		self.min_max=bounds
		self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
		
	def get_feat_names(self,feats):
		f_m={"MSE": "calc_ase",
						"Spike count": "calc_spike",
						"MSE (excl. spikes)": "calc_spike_ase",
						"Spike count (stim.)": "spike_rate",
						"ISI differences": "isi_differ",
						"Latency to 1st spike": "first_spike",
						"AP amplitude": "AP_overshoot",
						"AHP depth": "AHP_depth",
						"AP width": "AP_width",
						"Derivative difference" : "calc_grad_dif",
						"PPTD" : "pyelectro_pptd"}
		self.ffun_mapper=dict((v,k) for k,v in list(f_m.items()))
		if self.option_obj.type[-1]!="features":
			feat_names=[self.ffun_mapper[x.__name__] for x in feats[0][1]]
		else:
			feat_names=[x for x in feats[0][1]]
		return [feat_names,feats[1]]


class Nondominated_Sorted_Bluepyopt(oldBaseOptimizer):


	def __init__(self,reader_obj,model_obj,option_obj):
		self.fit_obj=fF(reader_obj,model_obj,option_obj)
		self.SetFFun(option_obj)
		self.option_obj=option_obj
		self.seed=option_obj.seed
		self.directory = str(option_obj.base_dir)
		self.pop_size=option_obj.pop_size
		self.max_evaluation=option_obj.max_evaluation
		self.num_params=option_obj.num_params
		self.number_of_cpu=option_obj.number_of_cpu
		self.SetBoundaries(option_obj.boundaries)
		self.param_names=self.option_obj.GetObjTOOpt()
		if self.option_obj.type[-1]!="features":
			self.number_of_traces=reader_obj.number_of_traces()
		else:
			self.number_of_traces=len(reader_obj.features_data["stim_amp"])
		feats=self.get_feat_names(self.option_obj.GetFitnessParam())
		self.feats_and_weights=[x for x in zip(feats[0],feats[1])]
		self.params=zip(self.param_names,self.min_max[0],self.min_max[1])
		



	def Optimize(self):
		#try:
		from ipyparallel import Client
		print("******************PARALLEL RUN : NSGA2 *******************")
		os.system("ipcluster start -n "+str(int(self.number_of_cpu))+" &")
		time.sleep(60)
		c = Client(timeout=60)
		view = c.load_balanced_view()
		view.map_sync(os.chdir, [str(os.path.dirname(os.path.realpath(__file__)))]*int(self.number_of_cpu))
		map_function=view.map_sync
		optimisation = bpop.optimisations.DEAPOptimisation(evaluator=DeapEvaluator(self.params,self.deapfun,self.feats_and_weights,self.min_max,self.number_of_traces),seed=self.seed,offspring_size = int(self.pop_size),map_function=map_function,selector_name='NSGA2')
		self.final_pop, self.hall_of_fame, self.logs, self.hist = optimisation.run(int(self.max_evaluation),cp_filename = 'checkpoint.pkl',cp_frequency=int(self.max_evaluation))
		os.system("ipcluster stop")
		#except Exception:
		"""os.system("ipcluster stop")
		print("*****************Single Run : NSGA2 *******************")
		optimisation = bpop.optimisations.DEAPOptimisation(evaluator=DeapEvaluator(self.params,self.deapfun,self.feats_and_weights,self.min_max,self.number_of_traces),seed=self.seed,offspring_size = int(self.pop_size),selector_name='NSGA2')
		self.final_pop, self.hall_of_fame, self.logs, self.hist = optimisation.run(int(self.max_evaluation))"""	
			

	def SetBoundaries(self,bounds):
		"""
		Stores the bounds of the parameters and creates a ``bounder`` object which bounds
		every parameter into the range of 0-1 since the algorithms are using normalized values.

		:param bounds: ``list`` containing the minimum and maximum values.

		"""
		self.min_max=bounds
		self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
		
	def get_feat_names(self,feats):
		f_m={"MSE": "calc_ase",
						"Spike count": "calc_spike",
						"MSE (excl. spikes)": "calc_spike_ase",
						"Spike count (stim.)": "spike_rate",
						"ISI differences": "isi_differ",
						"Latency to 1st spike": "first_spike",
						"AP amplitude": "AP_overshoot",
						"AHP depth": "AHP_depth",
						"AP width": "AP_width",
						"Derivative difference" : "calc_grad_dif",
						"PPTD" : "pyelectro_pptd"}
		self.ffun_mapper=dict((v,k) for k,v in list(f_m.items()))
		if self.option_obj.type[-1]!="features":
			feat_names=[self.ffun_mapper[x.__name__] for x in feats[0][1]]
		else:
			feat_names=[x for x in feats[0][1]]
		return [feat_names,feats[1]]


class DeapEvaluator(bpop.evaluators.Evaluator):
	
	def __init__(self,param,ffun,feats,min_max,number_of_traces):

		super(DeapEvaluator,self).__init__()
		self.ffun=ffun
		self.min_max=min_max
		self.params = [bpop.parameters.Parameter(p_name, bounds=(min_b,max_b)) for p_name,min_b,max_b in param]
		self.param_names = [param.name for param in self.params]
		self.objectives = [bpop.objectives.Objective(name=name) for name,value in feats*number_of_traces]


	def evaluate_with_lists(self, param_values):
		err=self.ffun(normalize(param_values,self))
		return err



