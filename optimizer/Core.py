from traceHandler import *
from modelHandler import *
from optimizerHandler import *
from optionHandler import optionHandler
from scipy.interpolate import interp1d
from scipy import linspace
import time
import numpy

class coreModul():
	"""
	This class is responsible to carry out the main steps of the optimization process by
	interacting with the other modules. The main attributes are the following:

	:attr: data_handler:

		performs input operations and handles input data

	:attr: option_handler:

		stores the settings

	:attr: model_handler:

		handles the model and runs the simulations and carries out other model related tasks

	:attr: optimizer:

		carries out the optimization process

	:attr: optimal_params:

		contains the resulting parameters

	:attr: ffun_calc_list:

		contains the list of available fitness functions in a dictionary

	"""
	def __init__(self):
		self.data_handler=DATA()
		self.option_handler=optionHandler()
		self.model_handler=None
		self.optimizer=None
		self.wfits = []
		self.wfits2 = []
		self.minind = 0
		self.moo_var = False
		self.deap_var = False
		self.brain_var = False
		f_m={"MSE": "calc_ase",
						"Spike count": "calc_spike",
						"MSE (excl. spikes)": "calc_spike_ase",
						"Spike count (stim.)": "spike_rate",
						"ISI differences": "isi_differ",
						"Latency to 1st spike": "first_spike",
						"AP amplitude": "AP_overshoot",
						"AHP depth": "AHP_depth",
						"AP width": "AP_width",
						"Derivative difference" : "calc_grad_dif"}
						#"PPTD" : "pyelectro_pptd"}
		self.ffun_mapper=dict((v,k) for k,v in list(f_m.items()))
		self.ffun_calc_list=["MSE",
						"MSE (excl. spikes)",
						"Spike count",
						"Spike count (stim.)",
						"ISI differences",
						"Latency to 1st spike",
						"AP amplitude",
						"AHP depth",
						"AP width",
						"Derivative difference"]
						#"PPTD"]
		self.grid_result=None

	def htmlStrBold(self,inp):
		return "<b>"+str(inp)+"</b>"

	def htmlStr(self,inp):
		return "<p>"+str(inp)+"</p>"

	def htmlUnderline(self):
		return "text-decoration:underline"

	def htmlResize(self,size):
		return "font-size:"+str(int(size))+"%"

	def htmlAlign(self,align_to):
		if align_to not in ["left","right","center"]:
			raise ValueError
		return  "text-align:"+align_to

	def htmlStyle(self,inp,*args):
		tmp_str="<span style=\""
		for n in args:
			tmp_str+=n+";"
		tmp_str+="\">"+str(inp)+"</span>"
		return tmp_str

	def htmlTable(self,header_list,data):
		tmp_str="<table border=\"1\" align=\"center\">"
		for h in header_list:
			tmp_str+="\n<th>"+str(h)+"</th>"

		for r in data:
			tmp_str+="\n<tr>"
			for c in r:
				tmp_str+="\n<td>"+str(c)+"</td>"
			tmp_str+="\n</tr>"

		tmp_str+="\n</table>"
		return tmp_str

	def htmlPciture(self,inp):
		return "<p align=\"center\"><img style=\"border:none;\" src=\""+inp+"\" ></p>"


	def Print(self):
		print([self.option_handler.GetFileOption(),
			   self.option_handler.GetInputOptions(),
			   self.option_handler.GetModelOptions(),
			   self.option_handler.GetModelStim(),
			   self.option_handler.GetModelStimParam(),
			   self.option_handler.GetObjTOOpt(),
			   self.option_handler.GetOptParam(),
			   self.option_handler.GetFitnessParam(),
			   self.option_handler.GetOptimizerOptions()])
		print("\n")

	def FirstStep(self,args):
		"""
		Stores the location of the input, and the base directory in the ``option_handler`` object
		and reads the data from the file into the ``data_handler`` object.

		:param args: dictionary with keys "file" and "input"

		"""
		self.option_handler.SetFileOptions(args.get("file"))
		self.option_handler.SetInputOptions(args.get("input"))

		self.data_handler.Read([self.option_handler.input_dir],self.option_handler.input_size,self.option_handler.input_scale,self.option_handler.input_length,self.option_handler.input_freq,self.option_handler.type[-1])


		if self.option_handler.type[-1]=='features':
			self.option_handler.input_size= len(self.data_handler.features_data['stim_amp'])

	def LoadModel(self,args):
		"""
		Stores the type of the simulator as well as the optional parameters passed to it.
		Creates the ``model_handler`` objects which can be either ``modelHandlerNeuron`` or ``externalHandler``.
		If the ``externalHandler`` is selected then the number of parameters subject to optimization is also set.

		:param args: dictionary with keys "simulator" and "sim_command"

		"""
		print(args)
		self.model_handler=None
		self.option_handler.SetSimParam([args.get("simulator","Neuron"),args.get("sim_command"),None])
		if self.option_handler.GetSimParam()[0]=="Neuron":
			self.option_handler.SetModelOptions(args.get("model"))
			self.model_handler=modelHandlerNeuron(self.option_handler.model_path,self.option_handler.model_spec_dir,self.option_handler.base_dir)
		else:
			self.model_handler=externalHandler(self.option_handler.GetSimParam()[1])
			self.model_handler.SetNParams(self.option_handler)
			self.option_handler.SetModelStimParam([[0]*self.data_handler.number_of_traces(),0,0])
	def ReturnSections(self):
		"""

		:return: the sections found in the model including "None" in a ``string`` ``list``.

		"""
		temp=self.model_handler.GetParameters()
		sections=[]
		for n in temp:
			sections.append(n[0])
		sections=list(set(sections))
		sections.append("None")
		return sections

	def ReturnMorphology(self):
		"""

		:return: the morphological parameters found in the model including "None" in a ``string`` ``list``.

		"""
		temp=self.model_handler.GetParameters()
		morphs=(str.split(temp[0][1], ", "))
		morphs=list(set(morphs))
		morphs.append("None")
		return morphs

	def ReturnChannels(self,section):
		"""
		Collects the channels from the given section.

		:param section: the name of the section

		:return: the channels in the given section including "None" in a ``string`` ``list``.

		"""
		temp=self.model_handler.GetParameters()
		channels=[]
		for n in temp:
			if n[0]==section:
				for k in str.split(n[2]," "):
						if k!="":
							for s in str.split(n[3]," "):
								if str.count(k,s)==1 and s!="":
									channels.append(s)


		channels=list(set(channels))
		channels.append("None")
		return channels

	def get_moo_var(self):
		return self.moo_var

	def get_deap_var(self):
		return self.deap_var

	def get_brain_var(self):
		return self.brain_var

	def ReturnChParams(self,channel):
		"""
		Collects channel parameters from the given channel

		:param channel: the name of the channel mechanism
		:return: the channel parameters in the given channel including "None" in a ``string`` ``list``.

		.. note::
			This function returns everything from the channel object not only the parameters.

		"""
		temp=self.model_handler.GetParameters()
		ch_param=[]
		for n in temp:
			if str.find(n[3],channel)!=-1:
				for p in n[2].split():
					if str.find(p,channel)!=-1:
						ch_param.append(p)
		ch_param=list(set(ch_param))
		ch_param.append("None")

		return ch_param

	#not in use
	def SetModel(self,args):

		if args.get("channel")!="None":
			self.model_handler.SetChannelParameters(args.get("section"), args.get("segment"), args.get("channel"), args.get("params"), args.get("values"))
		else:
			self.model_handler.SetMorphParameters(args.get("section"), args.get("morph"), args.get("values"))

	def SetModel2(self,args):
		"""
		Stores the selected parameter as subject to optimization in the ``option_handler`` object.
		For future use it offers a way to store initial value (not in use at the moment).

		:param args: must be a string-string dictionary containing the following keys:

				* section
				* channel
				* params
				* value

			or:

				* section
				* morph
				* values

		"""
		if args.get("channel")!="None":
			self.option_handler.SetObjTOOpt(args.get("section")+" "+args.get("segment")+" "+args.get("channel")+" "+args.get("params"))
			self.option_handler.SetOptParam(args.get("values"))
		else:
			self.option_handler.SetObjTOOpt(args.get("section")+" "+args.get("morph"))
			self.option_handler.SetOptParam(args.get("values"))

	def SecondStep(self,args):
		"""
		Stores the stimulation settings in the option object.

		:param args: must be a dictionary with the following keys:

			* stim
				must hold a ``list`` as value, which contains:
				   * stimulus type as ``string``, must be either "IClamp" or "VClamp"
				   * position of stimulus inside the section as of real value (0-1)
				   * name of stimulated section as ``string``
			* stimparam
				must hold a ``list`` as value which contains:
				   * stimulus amplitudes as a ``list`` of real values
				   * delay of stimulus as real value
				   * duration of stimulus as real value

		"""
		self.option_handler.SetModelStim(args.get("stim"))
		self.option_handler.SetModelStimParam(args.get("stimparam"))


	def ThirdStep(self,args):
		"""
		Stores the parameters in the ``option_handler`` object regarding the optimization process.
		If the sampling rate of the simulation is higher than the sampling rate of the input trace,
		then it re-samples the input using linear interpolation to create more points.
		Currently running a simulation with lower sampling rate than the input trace is not supported!
		After storing the necessary settings the ``optimizer`` object is initialized and the optimization is performed.
		The raw results are stored in the ``final_pop`` variable in the ``optimizer`` object.

		:param args: a dictionary containing the following keys:

			* runparam
				must be a list containing the following values:
					* length of simulation as real value
					* integration step as real value
					* parameter to record as ``string``
					* name of the section where the recording takes place as ``string``
					* position inside the section as real value (0-1)
					* initial voltage as a real value
			* feat
				must be a ``list`` with the names of the selected fitness functions
			* weights
				must be a list of real values
			* algo_options
				must be a dictionary containing options related to the optimization algorithm

				mandatory parameters:
					* seed
					* evo_strat
					* pop_size
					* num_params
					* boundaries

				optional parameters belonging to the different algorithms (see the optimizerHandler module for more)
					* max_evaluation
					* mutation_rate
					* cooling_rate
					* m_gauss
					* std_gauss
					* schedule
					* init_temp
					* final_temp
					* acc
					* dwell
					* x_tol
					* f_tol
			* inertia
			* social_rate
			* cognitive_rate
			* neighoborhood_size
				optional parameter shared by every algorithm
					* starting_points
		"""
		self.grid_result=None
		if args!=None:
			self.option_handler.SetModelRun(args.get("runparam"))
			fit_par=[]
			#fit_par.append(args.get("ffun",[]))
			fit_par.append(args.get("feat",[]))
			fit_par.append(args.get("weights",[]))
			self.option_handler.SetFitnesParam(fit_par)
			tmp=args.get("algo_options")
			"""
			if self.option_handler.type[-1]=='features':
				tmp.update({"num_params" : len(self.data_handler.features_data['stim_amp'])})
			"""
			if len(tmp.get("boundaries")[0])<1:
				raise sizeError("No boundaries were given!")
			#tmp.append(args.get("starting_points"))
			self.option_handler.SetOptimizerOptions(tmp)

		if self.option_handler.type[-1]!='features':
			if self.option_handler.run_controll_dt<self.data_handler.data.step:
				print("re-sampling because integration step is smaller then data step")
				print((self.option_handler.run_controll_dt,self.data_handler.data.step))
				#we have to resample the input trace so it would match the model output
				#will use lin interpolation
				x=linspace(0,self.option_handler.run_controll_tstop,int(self.option_handler.run_controll_tstop*(1/self.data_handler.data.step)))#x axis of data points

				tmp=[]
				for i in range(self.data_handler.number_of_traces()):
					y=self.data_handler.data.GetTrace(i)#y axis, the values from the input traces, corresponding to x
					f=interp1d(x,y)
					#we have the continuous trace, we could re-sample it now
					new_x=linspace(0,self.option_handler.run_controll_tstop,int(self.option_handler.run_controll_tstop/self.option_handler.run_controll_dt))
					#self.trace_reader.SetColumn(i,f(new_x)) the resampled vector replaces the original in the trace reader object
					tmp.append(f(new_x))
				self.data_handler.data.t_length=len(tmp[0])
				self.data_handler.data.freq=self.option_handler.run_controll_tstop/self.option_handler.run_controll_dt
				self.data_handler.data.step=self.option_handler.run_controll_dt
				transp=list(map(list,list(zip(*tmp))))
				self.data_handler.data.data=[]
				for n in transp:
					self.data_handler.data.SetTrace(n)
			#running simulation with smaller resolution is not supported
			if self.option_handler.run_controll_dt>self.data_handler.data.step:
				self.option_handler.run_controll_dt=self.data_handler.data.step

		import re 
		algo_str=re.sub('_+',"_",re.sub("[\(\[].*?[\)\]]", "", self.option_handler.evo_strat).replace("-","_").replace(" ","_"))
		exec("self.optimizer="+algo_str+"(self.data_handler,self.option_handler)")
		

		f_handler=open(self.option_handler.GetFileOption()+"/"+self.option_handler.GetFileOption().split("/")[-1]+"_settings.xml", 'w')
		f_handler.write(self.option_handler.dump(self.ffun_mapper))
		f_handler.close()

		if self.option_handler.type[-1]!= 'features':
			self.feat_str=", ".join([self.ffun_mapper[x.__name__] for x in self.option_handler.feats])
		else:
			self.feat_str=", ".join(self.option_handler.feats)

			
		try:
			if(self.option_handler.simulator == 'Neuron'):
				del self.model_handler
		except:
			"no model yet"

		start_time=time.time()
		self.optimizer.Optimize()
		stop_time=time.time()

		self.cands,self.fits = [],[]

		if self.option_handler.evo_strat.split(" ")[-1] == "Bluepyopt":
			self.cands=[list(normalize(hof,self.optimizer)) for hof in self.optimizer.hall_of_fame]
			self.fits=[x.fitness.values for x in self.optimizer.hall_of_fame]
			popsize=int(self.option_handler.pop_size)
			self.allfits=[self.optimizer.hist.genealogy_history[x].fitness.values for x in self.optimizer.hist.genealogy_history]
			self.allpop=[self.optimizer.hist.genealogy_history[x] for x in self.optimizer.hist.genealogy_history]
			if self.option_handler.type[-1]!="features":
				number_of_traces=self.data_handler.number_of_traces()
			else:
				number_of_traces=len(self.data_handler.features_data["stim_amp"])
			allgens=[]
			minfits=[]
			maxfits=[]
			medfits=[]
			cumminfits=[]
			with open(self.option_handler.base_dir + "/bpopt_stats.txt" , "w") as out_handler:
				out_handler.write("Gen \t Min \t \t Max \t \t Median \t  Cumulative Min \n")
				for idx in range(0,int(self.option_handler.max_evaluation*2),2):
					current_gen=self.allfits[idx*popsize:(idx+1)*popsize]
					weighted_sum=numpy.dot(current_gen,self.option_handler.weights*int(number_of_traces))
					min_e=numpy.min(weighted_sum)
					max_e=numpy.max(weighted_sum)
					med_e=numpy.median(weighted_sum)
					minfits.append(min_e)
					maxfits.append(max_e)
					medfits.append(med_e)
					if cumminfits:
						cumminfits.append(cumminfits[-1]) if min_e>cumminfits[-1] else cumminfits.append(min_e)
					else:
						cumminfits.append(minfits[-1])
					out_handler.write(str(int(idx/2+1))+","+str(min_e)+","+str(max_e)+","+str(med_e)+","+str(cumminfits[-1])+"\n")
			
			with open(self.option_handler.base_dir + "/bpopt_pop.txt" , "w") as out_handler:
				out_handler.write("Gen \t Parameters \t \t Fitnesses \n")
				for idx in range(0,int(self.option_handler.max_evaluation*2),2):
					current_fits=self.allfits[idx*popsize:(idx+1)*popsize]
					current_gen=self.allpop[idx*popsize:(idx+1)*popsize]
					for gen,fit in zip(current_gen,current_fits):
						out_handler.write(str(int(idx/2+1))+":"+str(gen)+":"+str(fit)+"\n")
		elif(self.option_handler.evo_strat.split(" ")[-1] == "Pygmo"):
			'''
			Currently only the best individual with its fitness is passed
			'''
			self.cands = [self.optimizer.best]
			self.fits = [self.optimizer.best_fitness]
			print((self.cands, "CANDS"))
			print((self.fits, "FITS"))
		elif(self.option_handler.evo_strat.split(" ")[-1] == "Base"):
			'''
			Currently only the best individual with its fitness is passed
			'''
			self.cands = [x.candidate[0] for x in reversed(self.optimizer.final_pop)]
			self.fits = [x.fitness[0] for x in reversed(self.optimizer.final_pop)]
			print((self.cands[0], "CANDS"))
			print((self.fits[0], "FITS"))
		else:
			self.optimizer.final_pop.sort(reverse=True)
			for i in range(len(self.optimizer.final_pop)):
				self.cands.append(self.optimizer.final_pop[i].candidate[0:len(self.option_handler.adjusted_params)])
				self.fits.append(self.optimizer.final_pop[i].fitness)

		print(("Optimization lasted for ", stop_time-start_time, " s"))	
		self.optimal_params=self.optimizer.fit_obj.ReNormalize(self.cands[0])
		
		

	def FourthStep(self,args={}):
		"""
		Renormalizes the output of the ``optimizer`` (see optimizerHandler module for more), and runs
		a simulation with the optimal parameters to receive an optimal trace.
		The components of the fitness value is calculated on this optimal trace.
		Settings of the entire work flow are saved into a configuration file named "model name"_settings.xml.
		A report of the results is generated in the form of a html document.

		:param args: currently not in use
		"""
		self.final_result=[]
		self.error_comps=[]
		self.last_fitness=self.optimizer.fit_obj.combineFeatures([self.optimal_params],delete_model=False)
		print((self.optimal_params,"fitness: ",self.last_fitness))
		#calculate the error components
		if self.option_handler.type[-1]!= 'features':
			k_range=self.data_handler.number_of_traces()
		else:
			k_range=len(self.data_handler.features_data["stim_amp"])
			
		for k in range(k_range):
			self.error_comps.append(self.optimizer.fit_obj.getErrorComponents(k, self.optimizer.fit_obj.model.record[0]))
			trace_handler=open("result_trace"+str(k)+".txt","w")
			for l in self.optimizer.fit_obj.model.record[0]:
				trace_handler.write(str(l))
				trace_handler.write("\n")
			trace_handler.close()
			self.final_result.extend(self.optimizer.fit_obj.model.record)

		if isinstance(self.optimizer.fit_obj.model, externalHandler):
			self.optimizer.fit_obj.model.record[0]=[]

		name=self.option_handler.model_path.split("/")[-1].split(".")[0]
		f_handler=open(name+"_results.html","w")
		tmp_str="<!DOCTYPE html>\n<html>\n<body>\n"
		tmp_str+=self.htmlStr(str(time.asctime( time.localtime(time.time()) )))+"\n"
		tmp_str+="<p>"+self.htmlStyle("Optimization of <b>"+name+".hoc</b> based on: "+self.option_handler.input_dir,self.htmlAlign("center"))+"</p>\n"
		tmp_list=[]
		#tmp_fit=self.optimizer.fit_obj.ReNormalize(self.optimizer.final_pop[0].candidate[0:len(self.option_handler.adjusted_params)])
		tmp_fit=self.optimal_params
		for name,mmin,mmax,f in zip(self.option_handler.GetObjTOOpt(),self.option_handler.boundaries[0],self.option_handler.boundaries[1],tmp_fit):
			tmp_list.append([str(name),str(mmin),str(mmax),str(f)])
		tmp_str+="<center><p>"+self.htmlStyle("Results",self.htmlUnderline(),self.htmlResize(200))+"</p></center>\n"
		tmp_str+=self.htmlTable(["Parameter Name","Minimum","Maximum","Optimum"], tmp_list)+"\n"
		tmp_str+="<center><p>"+self.htmlStrBold("Fitness: ")
		#tmp_str+=self.htmlStrBold(str(self.optimizer.final_pop[0].fitness))+"</p></center>\n"
		tmp_str+=self.htmlStrBold(str(self.last_fitness))+"</p></center>\n"
		tmp_str+=self.htmlPciture("result_trace.png")+"\n"
		for k in list(self.option_handler.GetOptimizerOptions().keys()):
			tmp_str+="<p><b>"+k+" =</b> "+str(self.option_handler.GetOptimizerOptions()[k])+"</p>\n"

		tmp_str+="<p><b>feats =</b> "+self.feat_str +"</p>\n"
		tmp_str+="<p><b>weights =</b> "+ str(self.option_handler.weights)+"</p>\n"
		tmp_str+="<p><b>user function =</b></p>\n"
		for l in (self.option_handler.u_fun_string.split("\n")[4:-1]):
			tmp_str+="<p>"+l+"</p>"
		tmp_str+="</body>\n</html>\n"

		#error components
		tmp_str+="<p><b>Fitness Components:</b></p>\n"
		tmp_w_sum=0
		tmp_list=[]
		for t in self.error_comps:
			for c in t:
				if self.option_handler.type[-1]!='features':
				#tmp_str.append( "*".join([str(c[0]),c[1].__name__]))
					tmp_list.append([self.ffun_mapper[c[1].__name__],
										str(c[2]),
										str(c[0]),
										str(c[0]*c[2]),""])
					tmp_w_sum +=c[0]*c[2]
				else:
					tmp_list.append([c[1],
										str(c[2]),
										str(c[0]),
										str(c[0]*c[2]),""])
					tmp_w_sum +=c[0]*c[2]
			tmp_list.append(["","","","",tmp_w_sum])
			tmp_w_sum=0
		#print tmp_list
		tmp_str+=self.htmlTable(["Name","Value","Weight","Weighted Value","Weighted Sum"], tmp_list)+"\n"
		#print tmp_str
		#transpose the error comps
		tmp_list=[]
		for c in zip(*self.error_comps):
			tmp=[0]*4

			for t_idx in range(len(c)):
				#print c[t_idx]
				tmp[1]+=c[t_idx][2]
				tmp[2]=c[t_idx][0]
				tmp[3]+=c[t_idx][2]*c[t_idx][0]

			if self.option_handler.type[-1]!='features':
				tmp[0]=self.ffun_mapper[c[t_idx][1].__name__]
			else:
				tmp[0]=(c[t_idx][1])
			tmp=list(map(str,tmp))
			tmp_list.append(tmp)

		#print tmp_list
		tmp_str+=self.htmlTable(["Name","Value","Weight","Weighted Value"], tmp_list)+"\n"
		#tmp_str+="<center><p><b>weighted sum = "+(str(tmp_w_sum)[0:5])+"</b></p></centered>"
		#print tmp_str
		f_handler.write(tmp_str)
		f_handler.close()


	def callGrid(self,resolution):
		"""
		Calculates fitness values on a defined grid (see optimizerHandler module for more).
		This tool is purely for analyzing results, and we do not recommend to use it to obtain parameter values.
		"""
		import copy
		self.prev_result=copy.copy(self.optimizer.final_pop)
		self.optimizer=grid(self.data_handler,self.optimizer.fit_obj.model,self.option_handler,resolution)
		self.optimizer.Optimize(self.optimal_params)
		self.grid_result=copy.copy(self.optimizer.final_pop)
		self.optimizer.final_pop=self.prev_result
