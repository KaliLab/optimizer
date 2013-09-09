from random import Random
#from time import time
from inspyred import ec
from inspyred.ec import terminators
from inspyred.ec import variators
from inspyred.ec import observers
from fitnessFunctions import fF
#from fitnessFunctions import *
import sys
import inspyred
import logging
from scipy import optimize, array, ndarray
from numpy import random
import copy
#from math import exp

#from inspyred.ec.terminators import max_evaluations

# to generate a new set of parameters
class baseOptimizer():
    def __init__(self):
        pass
    def SetFFun(self,option_obj):
        try:
            self.ffun=self.fit_obj.fun_dict["Combinations"]
        except KeyError:
            sys.exit("Unknown fitness function!")
        try:
            option_obj.feats=map(lambda x:self.fit_obj.calc_dict[x],option_obj.feats)
        except KeyError:
            pass
        
    

def normalize(v,args):
    c=copy.copy(v)
    for i in range(len(v)):
        c[i]=(v[i]-args.min_max[0][i])/(args.min_max[1][i]-args.min_max[0][i])
    return c
                


def uniform(random,args):
    size=args.get("num_inputs")
    bounds=args.get("_ec",args.get("self")).bounder
    candidate=[]
    for n in range(size):
        candidate.append(random.uniform(bounds.lower_bound[n],bounds.upper_bound[n]))
    print "uni",candidate
    return candidate

class my_candidate():
    def __init__(self,vals, fitn=-1):
        self.candidate=ndarray.tolist(vals)
        self.candidate.extend(vals)
        self.fitness=fitn
       
       

class annealing(baseOptimizer):
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=Random()
        self.seed=option_obj.seed
        self.rand.seed(self.seed)
        self.evo_strat=ec.SA(self.rand)
        self.evo_strat.terminator=terminators.evaluation_termination
#        self.evo_strat.selector=inspyred.ec.selectors.default_selection
#        self.evo_strat.replacer=inspyred.ec.replacers.simulated_annealing_replacement
#        self.evo_strat.variator=[variators.gaussian_mutation,
#                                 variators.blend_crossover]
        self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)####!!!!!!!!!!!!!!!!!!!!!!!!!!!!probably should place it into the Optimize()!!!!!!!!!###########xx
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})),self)]
        try:
            self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        print "optimizer",self.starting_points
        
#    def wrapper(self,candidates,args):
#        tmp=ndarray.tolist(candidates)
#        c=[]
#        for n in tmp:
#            c.append(n[0])
#        #c=self.bounder(c,args)
#        print [c] 
#        return self.ffun([c],args)[0]
        
    def Optimize(self):
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
                                             num_inputs=self.num_inputs, 
                                             maximize=self.maximize, 
                                             bounder=self.bounder,
                                             seeds=self.starting_points,
#                                             cooling_rate=0.01,
#                                             gaussian_mean=0,
#                                             gaussian_stdev=1,
                                             boundaries=self.min_max,
                                             statistics_file=self.stat_file,
                                             individuals_file=self.ind_file,
                                             gaussian_stdev=0.5)
#                                             cooling_rate=0.3)
        
        
    def SetBoundaries(self,bounds):
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
            
        
         

            
            
        
class scipy_anneal(baseOptimizer):
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.rand=random
        self.seed=option_obj.seed
        self.rand.seed([self.seed])
        self.init_temp=option_obj.init_temp
        self.final_temp=option_obj.final_temp
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.schedule={'1' : 'fast', '2' : 'cauchy', '3' : 'boltzmann'}[str(int(option_obj.schedule))]
        self.dwell=option_obj.dwell
        self.feps=option_obj.acc
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)
        try:
            self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
        print "optimizer",self.starting_points
        

    def wrapper(self,candidates,args):
        tmp=ndarray.tolist(candidates)
        candidates=self.bounder(tmp,args) 
        return self.ffun([candidates],args)[0]
    
        
        
    def Optimize(self):
        self.result=optimize.anneal(self.wrapper, 
                                      x0=ndarray((self.num_inputs,),buffer=array(self.starting_points),offset=0,dtype=float), 
                                      args=[[]],  
                                      maxiter= self.max_evaluation,
                                      schedule= self.schedule, 
                                      T0= self.init_temp,
                                      Tf= self.final_temp, 
                                      learn_rate= self.mutation_rate,
                                      feps= self.feps,
                                      dwell= self.dwell,
                                      lower= [0]*len(self.min_max[0]),
                                      upper= [1]*len(self.min_max[0])
                                      )
        print self.result[-1]
        self.final_pop=[my_candidate(self.result[0],self.result[1])]
        
    def SetBoundaries(self,bounds):
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        
        
class fmin(baseOptimizer):
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
            self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
        print "optimizer",self.starting_points
        
        
        
    def wrapper(self,candidates,args):
        tmp=ndarray.tolist(candidates)
        candidates=self.bounder(tmp,args) 
        return self.ffun([candidates],args)[0]
    
    

        
        
    def Optimize(self):
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
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        


class L_BFGS_B(baseOptimizer):
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
            self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})
        print "optimizer",self.starting_points
        
        
    def wrapper(self,candidates,args):
        tmp=ndarray.tolist(candidates)
        candidates=self.bounder(tmp,args) 
        return self.ffun([candidates],args)[0]
    

        
        
    def Optimize(self):
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
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        
        
                
                
class grid(baseOptimizer):
    def __init__(self,reader_obj,model_obj,option_obj):
        self.fit_obj=fF(reader_obj,model_obj,option_obj)
        self.SetFFun(option_obj)
        self.num_inputs=option_obj.num_inputs
        #self.resolution=2000**(1.0/self.num_inputs)
        self.resolution=5
        print self.resolution
        self.SetBoundaries(option_obj.boundaries)
        

    
    
    def Optimize(self):
        #return result in self.final_pop
        #vals between self.bounder.lower_bound
        self.final_pop=[[],[]]
        import itertools
        f_r=map(lambda x:x/10.0,range(0,11,self.resolution))
        it=itertools.product(f_r,repeat=self.num_inputs)
        points=[]
        for c in it:
            points.append(list(c))
        fitness=self.ffun(points,{})
        fitness=map(lambda x: [x]*self.num_inputs,fitness)
        for p in range(len(points)):
            points[p]=self.fit_obj.ReNormalize(points[p])
        #transpose
        points=map(list,zip(*points))
        fitness=map(list,zip(*fitness))
        self.final_pop[0]=points
        self.final_pop[1]=fitness
            
        
    def SetBoundaries(self,bounds):
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
        
    

        
# simple EO algorithm
class simpleEO(baseOptimizer):
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
        self.evo_strat.observer=[observers.population_observer,observers.file_observer]
        self.pop_size=option_obj.pop_size
        self.max_evaluation=option_obj.max_evaluation
        self.mutation_rate=option_obj.mutation_rate
        self.num_inputs=option_obj.num_inputs
        self.SetBoundaries(option_obj.boundaries)####!!!!!!!!!!!!!!!!!!!!!!!!!!!!probably should place it into the Optimize()!!!!!!!!!###########xx
        self.maximize=False #hard wired, always minimize
        self.stat_file=open("stat_file.txt","w")
        self.ind_file=open("ind_file.txt","w")
        #inspyred needs sequence of seeds
        #self.starting_points=[normalize(args.get("starting_points",uniform(self.rand,{"num_inputs" : self.num_inputs,"self": self})),self)]
        try:
            self.starting_points=[normalize(option_obj.starting_points,self)]
        except TypeError:
            self.starting_points=None
        print "optimizer",self.starting_points
                
        # generator comes from the class
        # evaluator comes from fitnessFunctions
        # bounder comes from the class, should be callable
        
    def Optimize(self):
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
        self.min_max=bounds
        self.bounder=ec.Bounder([0]*len(self.min_max[0]),[1]*len(self.min_max[1]))
    
        


        
        