import wx
import sys
from traceHandler import sizeError
try:
	import matplotlib
	matplotlib.use('WXAgg')
	from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
	from matplotlib.figure import Figure
except RuntimeError as re:
	print(re)
	sys.exit()
#from inspyred.ec import analysis
from inspyred.ec.analysis import generation_plot
import inspyred
import matplotlib.pyplot as plt
#from wxPython._controls import wxTextCtrl
import os
from copy import copy
import Core
import numpy


from deap.benchmarks.tools import diversity, convergence, hypervolume
from deap import tools


class boundarywindow(wx.Frame):
	def __init__(self, par):

		wx.Frame.__init__(self,par, wx.ID_PROPERTIES, "Boundaries", size=(600, 700))
		panel = wx.Panel(self)
		#self.Bind(wx.EVT_CLOSE, self.my_close)
		self.par = par
		hstep = 400
		vstep = 35
		hoffset = 10
		voffset = 15
		self.min = []
		self.max = []

		for l in range(len(self.par.core.option_handler.GetObjTOOpt())):
			param=self.par.core.option_handler.GetObjTOOpt()[l].split()
			if len(param)==4:
				label=param[0] + " " + param[1] + " " + param[3]
			else:
				if param[0]!=param[-1]:
					label=param[0] + " " + param[-1]
				else:
					label=param[-1]
			#wx.StaticText(panel, label=self.par.core.option_handler.GetObjTOOpt()[l].split()[-1], pos=(hoffset, voffset + l * vstep))
			wx.StaticText(panel, label=label, pos=(hoffset, voffset + l * vstep))
			tmp_min = wx.TextCtrl(panel, id=l, pos=(hstep, voffset + l * vstep), size=(75, 30))
			self.min.append(tmp_min)
			tmp_max = wx.TextCtrl(panel, id=l + len(self.par.core.option_handler.GetOptParam()), pos=(hstep / 4 + hstep, voffset + l * vstep), size=(75, 30))
			self.max.append(tmp_max)
			if len(self.par.core.option_handler.boundaries[1]) == len(self.par.core.option_handler.GetObjTOOpt()):
				tmp_min.SetValue(str(self.par.core.option_handler.boundaries[0][l]))
				tmp_max.SetValue(str(self.par.core.option_handler.boundaries[1][l]))
		Setbutton = wx.Button(panel, label="Set", pos=(hstep, 250))
		Setbutton.Bind(wx.EVT_BUTTON, self.Set)
		Savebutton = wx.Button(panel, label="Save", pos=(100, 250))
		Savebutton.Bind(wx.EVT_BUTTON, self.Save)
		Loadbutton = wx.Button(panel, label="Load", pos=(300, 250))
		Loadbutton.Bind(wx.EVT_BUTTON, self.Load)
		self.Show()
		self.save_file_name="boundaries.txt"

	def Set(self, e):
		try:
			self.par.core.option_handler.boundaries[0] = [float(n.GetValue()) for n in self.min]
			self.par.core.option_handler.boundaries[1] = [float(n.GetValue()) for n in self.max]
		except ValueError as ve:
			wx.MessageBox(str(ve), "Invalid Value", wx.OK | wx.ICON_ERROR)

		else:
			for i in range(len(self.par.core.option_handler.boundaries[0])):
				if self.par.core.option_handler.boundaries[0][i] >= self.par.core.option_handler.boundaries[1][i] :
					wx.MessageBox("Min boundary must be lower than max", "Invalid Values", wx.OK | wx.ICON_ERROR)
					break

			#self.boundaries_window.Destroy()
		self.Close()

	def Save(self,e):
		dlg = wx.FileDialog(self, "Type a filename", os.getcwd(), "", "*.*", style=wx.FD_SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.save_file_name=dlg.GetFilename()
			f=open(self.save_file_name,"w")
			for _min,_max in zip(self.min,self.max):
				f.write(str(_min.GetValue()))
				f.write("\t")
				f.write(str(_max.GetValue()))
				f.write("\n")
			dlg.Destroy()

	def Load(self,e):
		dlg = wx.FileDialog(self, "Select a file", os.getcwd(), "", "*.*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			load_file_name=dlg.GetDirectory()+"/"+dlg.GetFilename()
			#print load_file_name
			try:
				f=open(load_file_name,"r")
				for idx,l in enumerate(f):
					bounds=l.split()
					self.min[idx].SetValue(bounds[0])
					self.max[idx].SetValue(bounds[1])
			except IOError:
				wx.MessageBox('Error reading the file', 'Error', wx.OK | wx.ICON_ERROR)
			dlg.Destroy()


	def my_close(self, e):
		wx.Exit()

class gridwindow(wx.Frame):
	def __init__(self, par):

		wx.Frame.__init__(self,par, wx.ID_PROPERTIES, "Grid Boundaries", size=(400, 700))
		panel = wx.Panel(self)
		#self.Bind(wx.EVT_CLOSE, self.my_close)
		self.par = par
		hstep = 200
		vstep = 35
		hoffset = 10
		voffset = 15
		self.min = []
		self.max = []

		for l in range(len(self.par.core.option_handler.GetObjTOOpt())):
			wx.StaticText(panel, label=self.par.core.option_handler.GetObjTOOpt()[l].split()[-1], pos=(hoffset, voffset + l * vstep))
			tmp_min = wx.TextCtrl(panel, id=l, pos=(hstep, voffset + l * vstep), size=(75, 30))
			self.min.append(tmp_min)
			tmp_max = wx.TextCtrl(panel, id=l + len(self.par.core.option_handler.GetOptParam()), pos=(hstep / 2 + hstep, voffset + l * vstep), size=(75, 30))
			self.max.append(tmp_max)
			if len(self.par.core.option_handler.boundaries[1]) == len(self.par.core.option_handler.GetObjTOOpt()):
				tmp_min.SetValue(str(self.par.core.option_handler.boundaries[0][l]))
				tmp_max.SetValue(str(self.par.core.option_handler.boundaries[1][l]))

		wx.StaticText(panel,label="Resolution:", pos=(hoffset,600))
		self.resolution_ctrl=wx.TextCtrl(panel,id=wx.ID_ANY,pos=(hstep,600),size=(75,30))
		self.resolution_ctrl.SetValue(str(self.par.resolution))
		Setbutton = wx.Button(panel, label="Set", pos=(hstep, 650))
		Setbutton.Bind(wx.EVT_BUTTON, self.Set)


	def Set(self, e):
		try:
			self.par.core.option_handler.boundaries[0] = [float(n.GetValue()) for n in self.min]
			self.par.core.option_handler.boundaries[1] = [float(n.GetValue()) for n in self.max]
			self.par.resolution=int(self.resolution_ctrl.GetValue())
		except ValueError as ve:
			wx.MessageBox(str(ve), "Invalid Value", wx.OK | wx.ICON_ERROR)
			#self.boundaries_window.Destroy()
		self.par.DisplayGrid()


	def my_close(self, e):
		wx.Exit()

class stimuliwindow2(wx.Frame):
	def __init__(self, par):
		self.container=[]

class stimuliwindow(wx.Frame):
	def __init__(self, par, core):
		self.core =core
		self.stimuli_window = wx.Frame(par.panel, wx.ID_ANY, "Set Amplitude(s)", size=(400, 500))
		self.panel = wx.Panel(self.stimuli_window)
		self.par = par
		self.container = []
		wx.StaticText(self.panel, label="Number of stimuli:", pos=(10, 10))
		self.generate = wx.Button(self.panel, label="Create", pos=(250, 10))
		self.generate.Bind(wx.EVT_BUTTON, self.Set)
		#self.load_waveform = wx.Button(self.panel, label="Time Varying\nStimulus", pos=(250, 50))
		#self.load_waveform.Bind(wx.EVT_BUTTON, self.Load)
		self.number = wx.TextCtrl(self.panel, id=wx.ID_ANY, pos=(150, 10), size=(50, 30))
		self.accept = wx.Button(self.panel, label="Accept", pos=(200, 450))
		self.accept.Disable()
		self.accept.Bind(wx.EVT_BUTTON, self.Accept)
		if self.core.option_handler.type[-1]=="features":
			self.number.SetValue((str(len(self.core.data_handler.features_data["stim_amp"]))))
			self.Set(self)
		self.stimuli_window.Show()

	def Set(self, e):
		self.temp = []
		hstep = 200
		vstep = 35
		hoffset = 10
		voffset = 50
		unit="nA" if self.par.dd_type.GetSelection()==0 else "mV"
		for l in range(min(10, int(self.number.GetValue()))):
			wx.StaticText(self.panel, label="Amplitude" + str(l+1) + " ("+unit+"):", pos=(hoffset, voffset + l * vstep))
			tmp_obj = wx.TextCtrl(self.panel, id=l, pos=(hstep / 2+25, voffset + l * vstep), size=(75, 30))
			if self.core.option_handler.type[-1]=="features":
				tmp_obj.SetValue(str(self.core.data_handler.features_data["stim_amp"][l]))

			self.temp.append(tmp_obj)
		self.accept.Enable()
		self.stimuli_window.Show()


	def Accept(self, e):
		for n in range(len(self.temp)):
			self.container.append(float(self.temp[n].GetValue()))
		self.stimuli_window.Hide()

	#def Load(self, e):


	def my_close(self, e):
		wx.Exit()

class ErrorDialog(wx.Frame):
	def __init__(self, par):
		wx.Frame.__init__(self,par, wx.ID_PROPERTIES, "Detailed Error", size=(700, 400))
		panel = wx.Panel(self)
		self.parent = par
		self.error_comp_table = wx.ListCtrl(panel,pos=(10,10),size=(600,300),style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.error_comp_table.InsertColumn(0, 'Error Function', width=200)
		self.error_comp_table.InsertColumn(1, 'Value', width=200)
		self.error_comp_table.InsertColumn(2, 'Weight', width=200)
		self.error_comp_table.InsertColumn(3, 'Weighted Value', width=200)

		tmp_w_sum=0
		c_idx=0
		for t in self.parent.core.error_comps:
			for c in t:
				#tmp_str.append( "*".join([str(c[0]),c[1].__name__]))
				if self.parent.core.option_handler.type[-1]!="features":
					idx=self.error_comp_table.InsertStringItem(c_idx,self.parent.core.ffun_mapper[c[1].__name__])
				else:
					idx=self.error_comp_table.InsertStringItem(c_idx,c[1])
				self.error_comp_table.SetStringItem(idx,1,str(c[2]))
				self.error_comp_table.SetStringItem(idx,2,str(c[0]))
				self.error_comp_table.SetStringItem(idx,3,str(c[0]*c[2]))
				c_idx+=1
				tmp_w_sum +=c[0]*c[2]
			c_idx+=1
			idx=self.error_comp_table.InsertStringItem(c_idx,"Weighted Sum")
			self.error_comp_table.SetStringItem(idx,1,"-")
			self.error_comp_table.SetStringItem(idx,2,"-")
			self.error_comp_table.SetStringItem(idx,3,str(tmp_w_sum))
			#print str(tmp_w_sum)
			tmp_w_sum=0


class MyDialog(wx.Dialog):
	def __init__(self, parent, *args, **kw):
		super(MyDialog, self).__init__(*args, **kw)
		self.parent = parent
		#panel=wx.Panel(self,size=(300,250))
		#wx.StaticText(self,label="#Please define your function below!\n#The first uncommented line should contain\neither the word python or hoc.\n#This would tell the compiler \nwhich language do you use.",id=wx.ID_ANY,pos=(465,10),style=wx.TE_MULTILINE)
		self.string = wx.TextCtrl(self, id=wx.ID_ANY, pos=(10, 10), size=(450, 400), style=wx.TE_MULTILINE | wx.TE_AUTO_URL | wx.TE_PROCESS_TAB)
		self.string.SetValue("#Please define your function below in the template!\n"+
							 "#You may choose an arbitrary name for your function,\n"+
							 "#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\n"+
							 "#In the next lines you may specify the names of the parameters in separate comments.\n"+
							 "def usr_fun(self,v):")
		okButton = wx.Button(self, label='Ok', pos=(50, 420))
		closeButton = wx.Button(self, label='Close', pos=(200, 420))
		okButton.Bind(wx.EVT_BUTTON, self.OnOk)
		closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
		loadButton = wx.Button(self, label="Load", pos=(470, 20))
		loadButton.Bind(wx.EVT_BUTTON, self.OnLoad)




	def OnOk(self, e):
		try:
			#print self.string.GetValue()
			self.parent.core.option_handler.u_fun_string = str(self.string.GetValue())
			self.parent.core.option_handler.adjusted_params=[]
			self.parent.model.DeleteAllItems()
			text = ""
			text = list(map(strip, str(self.string.GetValue()).split("\n")))[4:-1]
			#print text
			variables = []
			variables = list(map(strip, str(text[0][text[0].index("(") + 1:text[0].index(")")]).split(",")))
			#print variables
			var_len = int(text[1].lstrip("#"))
			#print var_len
			i=0
			var_names=[]
			while text[i+2][0]=="#" and i<var_len:
				var_names.append(text[i+2].lstrip("#"))
				i+=1
			if len(var_names)!=var_len and len(var_names)!=0:
				raise SyntaxError("Number of parameter names must equal to number of parameters")
			if var_names==[]:
				var_names=None
			for i in range(var_len):
				self.parent.core.option_handler.SetOptParam(0.1)
				if var_names != None:
					self.parent.core.option_handler.SetObjTOOpt(var_names[i])
				else:
					self.parent.core.option_handler.SetObjTOOpt("Vector" + "[" + str(i) + "]")
			#print variables, variables[0]
			if variables[0] == '':
				raise ValueError
			compile(self.string.GetValue(), '<string>', 'exec')
			self.parent.toolbar.EnableTool(888, True)
			self.Destroy()
		except ValueError as val_err:
			print(val_err)
			wx.MessageBox("Your function doesn't have any input parameters!", "Error", wx.OK | wx.ICON_ERROR)
		except SyntaxError as syn_err:
			wx.MessageBox(str(syn_err), "Syntax Error", wx.OK | wx.ICON_ERROR)




	def OnClose(self, e):

		self.Destroy()

	def OnLoad(self, e):
		dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			fun_file_path = dlg.GetDirectory() + "/" + dlg.GetFilename()
		dlg.Destroy()
		f = open(fun_file_path, "r")
		fun =   ("#Please define your function below in the template!\n"+
				"#You may choose an arbitrary name for your function,\n"+
				"#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\n"+
				"#In the second line you may specify the names of the parameters in a comment, separated by spaces.\n")
		for l in f:
			fun = fun + l
		self.string.SetValue(fun)

class MyDialog2(wx.Dialog):
	def __init__(self,parent,*args,**kwargs):

		super(MyDialog2,self).__init__(parent,title="Starting Points")
		self.parent = parent
		self.Bind(wx.EVT_CLOSE,self.OnClose)
		n_o_params=args[0]
		self.container=[]
		self.vals=args[1]
		self.SetSize((500,min(150*n_o_params+1,600)))
		_sizer=wx.GridSizer(n_o_params+1,2,20,200)
#        row_sizer=wx.BoxSizer(wx.HORIZONTAL)
#        col_sizer1=wx.BoxSizer(wx.VERTICAL)
#        col_sizer2=wx.BoxSizer(wx.VERTICAL)
		for n in range(n_o_params):
			param=self.parent.core.option_handler.GetObjTOOpt()[n].split()
			if len(param)==4:
				p_name=param[0] + " " + param[1] + " " + param[3]
			else:
				if param[0]!=param[-1]:
					p_name=param[0] + " " + param[-1]
				else:
					p_name=param[-1]
			#p_name=self.parent.core.option_handler.GetObjTOOpt()[n].split()[-1]
			p_name_txt=wx.StaticText(self,label=p_name)
			ctrl=wx.TextCtrl(self,wx.ID_ANY,size=(100,30))
			self.container.append(ctrl)
			#col_sizer1.Add(p_name_txt,flag=wx.UP,border=15)
			#col_sizer2.Add(ctrl,flag=wx.UP,border=15)
			_sizer.Add(p_name_txt,flag=wx.LEFT | wx.UP,border=5)
			_sizer.Add(ctrl,flag=wx.LEFT | wx.UP,border=5)

		b_ok=wx.Button(self,label="Ok")
		b_close=wx.Button(self,label="Cancel")
		b_ok.Bind(wx.EVT_BUTTON, self.OnOk)
		b_close.Bind(wx.EVT_BUTTON, self.OnClose)
		b_load=wx.Button(self,label="Load Point")
		b_load.Bind(wx.EVT_BUTTON, self.OnLoad)
		b_load_pop=wx.Button(self,label="Load Population")
		b_load_pop.Bind(wx.EVT_BUTTON, self.OnLoadPop)
#        col_sizer1.Add(b_ok,flag=wx.UP,border=15)
#        col_sizer2.Add(b_close,flag=wx.UP,border=15)
#        row_sizer.Add(col_sizer1,flag=wx.LEFT,border=20)
#        row_sizer.Add(col_sizer2,flag=wx.LEFT,border=50)
#        self.SetSizer(row_sizer)

		_sizer.Add(b_ok,flag=wx.LEFT | wx.UP,border=5)
		_sizer.Add(b_close,flag=wx.LEFT | wx.UP,border=5)
		_sizer.Add(b_load,flag=wx.LEFT | wx.UP,border=5)
		_sizer.Add(b_load_pop,flag=wx.LEFT | wx.UP,border=5)
		self.SetSizer(_sizer)


	def OnOk(self,e):
		try:
			for n in self.container:
				self.vals.append(float(n.GetValue()))
			self.Destroy()
		except ValueError:
			wx.MessageBox("You must give every parameter an initial value!", "Error", wx.OK | wx.ICON_ERROR)


	def OnClose(self,e):
		self.vals=None
		self.Destroy()

	def OnLoad(self, e):
		file_path = ""
		dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			file_path = dlg.GetDirectory() + "/" + dlg.GetFilename()
		dlg.Destroy()
		f = open(file_path, "r")
		for idx, l in enumerate(f):
			self.container[idx].SetValue(str(l))

	def OnLoadPop(self, e):
		self.size_of_pop = 0
		file_path = ""
		dlg1 = wx.MessageDialog(self, "This function is only supported by the algorithms from inspyred!", style=wx.OK | wx.CANCEL)
		if dlg1.ShowModal() == wx.ID_OK:
			dlg2 = wx.TextEntryDialog(self, "Enter size of population", caption="Replace this with an arbitrary number", style=wx.OK | wx.CANCEL)
			if dlg2.ShowModal() == wx.ID_OK:
				self.size_of_pop = int(dlg2.GetValue())
				dlg3 = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
				if dlg3.ShowModal() == wx.ID_OK:
					file_path = dlg3.GetDirectory() + "/" + dlg3.GetFilename()
					dlg3.Destroy()
				dlg2.Destroy()
				dlg1.Destroy()
			else:
				dlg2.Destroy()
				dlg1.Destroy()
		else:
			dlg1.Destroy()

		def lastlines(hugefile, n, bsize=2048):
			import errno
			hfile = open(hugefile, 'rU')
			if not hfile.readline():
				return
			sep = hfile.newlines
			hfile.close()

			hfile = open(hugefile, 'rb')
			hfile.seek(0, os.SEEK_END)
			linecount = 0
			pos = 0

			while linecount <= n:

				try:
					hfile.seek(-bsize, os.SEEK_CUR)
					linecount += hfile.read(bsize).count(sep)
					hfile.seek(-bsize, os.SEEK_CUR)
				except IOError as e:
					if e.errno == errno.EINVAL:
						# Attempted to seek past the start, can't go further
						bsize = hfile.tell()
						hfile.seek(0, os.SEEK_SET)
						linecount += hfile.read(bsize).count(sep)
				pos = hfile.tell()

			hfile.close()
			hfile = open(hugefile, 'r')
			hfile.seek(pos, os.SEEK_SET)  # our file position from above


			for line in hfile:
			# We've located n lines *or more*, so skip if needed
				if linecount > n:
					linecount -= 1
					continue
			# The rest we yield
				yield line

		for l in lastlines(file_path, self.size_of_pop, 1):
			s=l.strip()
			#print s
			params = [float(x.lstrip("[").rstrip("]")) for x in s.split(", ")][3:-1]
			params = params[0:len(params) / 2 + 1]
			self.vals.append(params)
		self.Destroy()



class inputLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path):

		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.core = core

		#this will need to be wrapped in a try statement later:
		import optimizer
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		self.layer = None
		self.panel = wx.Panel(self)
		self.Center()
		self.ToolbarCreator()
		self.Design()
		self.Show(True)



	def ToolbarCreator(self):

		self.toolbar = self.CreateToolBar()
		button_toolbar_fward = self.toolbar.AddLabelTool(887, 'NextLayer', wx.Bitmap(self.path + "/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.toolbar.EnableTool(button_toolbar_fward.GetId(), False)


	def Design(self):
		self.horizontal_box1 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box2 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box3 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box4 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box5 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box6 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box7 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box8 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box9 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box10 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box11 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box12 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box13 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box14 = wx.BoxSizer(wx.HORIZONTAL)
		#self.horizontal_box15 = wx.BoxSizer(wx.HORIZONTAL)
		self.vertical_box1 = wx.BoxSizer(wx.VERTICAL)
		self.vertical_box2 = wx.BoxSizer(wx.VERTICAL)

		heading = wx.StaticText(self.panel, label='File Options')
		heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.horizontal_box1.Add(heading, flag=wx.BOTTOM, border=10)
#        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
#        wx.StaticLine(self.panel, pos=(1, 215), size=(self.Size[0],1))

		descr1 = wx.StaticText(self.panel, label='Input File')
		self.horizontal_box2.Add(descr1)

		self.input_file_controll = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(300, 30), name="Input Location")
		self.input_file_controll.SetHelpText("Location of input trace")
		self.horizontal_box3.Add(self.input_file_controll)

		browser1 = wx.Button(self.panel, label="Browse...")
		browser1.Bind(wx.EVT_BUTTON, self.BrowseFile)
		self.horizontal_box3.Add(browser1, flag=wx.LEFT, border=10)

		self.time_checker = wx.CheckBox(self.panel, wx.ID_ANY, label="Contains time")
		self.horizontal_box3.Add(self.time_checker, flag=wx.LEFT, border=10)

		self.type_selector = wx.Choice(self.panel, wx.ID_ANY)
		#enable this later
		#self.type_selector.AppendItems(["Voltage trace", "Current trace", "Spike times", "Other"])
		self.type_selector.AppendItems(["Voltage trace", "Current trace", "Features", "Other"])
		self.type_selector.SetSelection(0)
		self.type_selector.Bind(wx.EVT_CHOICE, self.typeChanged)
		self.horizontal_box3.Add(self.type_selector, flag=wx.LEFT, border=10)

		descr2 = wx.StaticText(self.panel, label='Base Directory')
		self.horizontal_box4.Add(descr2)

		self.input_file_controll.WriteText(os.getcwd())
		self.base_dir_controll = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(300, 30), name="Base Location")
		self.horizontal_box5.Add(self.base_dir_controll)
		self.base_dir_controll.WriteText(os.getcwd())

		browser2 = wx.Button(self.panel, label="Browse...")
		browser2.Bind(wx.EVT_BUTTON, self.BrowseDir)
		self.horizontal_box5.Add(browser2, flag=wx.LEFT, border=10)

		self.input_tree=wx.TreeCtrl(self.panel,wx.ID_ANY,pos=(425,155),size=(250,100),style=wx.TR_HAS_BUTTONS | wx.TR_EXTENDED)
		self.troot=self.input_tree.AddRoot("Input data")
		self.tvoltage=None
		self.tcurrent=None
		self.tspike_t=None
		self.tother=None
		self.tfeatures=None
		#enable this later
		self.loaded_input_types=[self.tvoltage ,
								 self.tcurrent ,
#                                 self.tspike_t ,
#                                 self.tother,
								  self.tfeatures]


		descr3 = wx.StaticText(self.panel, label='Number of traces')
		self.horizontal_box6.Add(descr3, flag=wx.UP, border=30)

		descr6 = wx.StaticText(self.panel, label='Units')
		self.horizontal_box6.Add(descr6, flag=wx.UP | wx.LEFT, border=30)

		self.size_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, pos=(10, 245), size=(100, 30), name="NO traces")
		self.horizontal_box7.Add(self.size_ctrl)

		self.dropdown = wx.Choice(self.panel, wx.ID_ANY, (150, 245))
		self.dropdown.SetSize((100, 30))
		self.dropdown.AppendItems(list(Core.scales[str(self.type_selector.GetItems()[self.type_selector.GetCurrentSelection()]).split()[0].lower()].keys()))
		self.dropdown.Select(1)
		self.horizontal_box7.Add(self.dropdown, flag=wx.LEFT, border=50)

		descr4 = wx.StaticText(self.panel, label='Length of traces (ms)')
		self.horizontal_box8.Add(descr4)

		self.length_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, pos=(10, 325), size=(100, 30), name="Length")
		self.horizontal_box9.Add(self.length_ctrl)

		descr5 = wx.StaticText(self.panel, label='Sampling frequency (Hz)')
		self.horizontal_box10.Add(descr5)

		self.freq_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, pos=(10, 405), size=(100, 30), name="Frequency")
		self.horizontal_box11.Add(self.freq_ctrl)


		self.load = wx.Button(self.panel, label="Load trace", pos=(10, 445))
		self.load.Disable()
		self.load.Bind(wx.EVT_BUTTON, self.Load)
		self.horizontal_box12.Add(self.load)




		self.vertical_box1.Add(self.horizontal_box1, flag=wx.ALL, border=10)
		self.vertical_box1.Add(self.horizontal_box2, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box3, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box4, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box5, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box6, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box7, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box8, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box9, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box10, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box11, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box12, flag=wx.ALL, border=5)
		self.vertical_box1.Add(self.horizontal_box13, flag=wx.ALL, border=5)
		self.vertical_box2.Add(self.vertical_box1, flag=wx.ALL, border=10)
		self.panel.SetSizer(self.vertical_box2)


#event functions
	def Next(self, e):
			if self.core.option_handler.output_level=="1":
				self.core.Print()
			try:
				self.layer.Show()
			except AttributeError:
				self.layer = modelLayer(self, 1, self.Size, "Model & Parameter Selection", self.core, self.path)
				self.layer.Show()
			self.Hide()


	def typeChanged(self,e):
		self.dropdown.Clear()
		self.dropdown.AppendItems(list(Core.scales[str(self.type_selector.GetItems()[self.type_selector.GetCurrentSelection()]).split()[0].lower()].keys()))
		self.dropdown.Select(1)

	def BrowseFile(self, e):

		dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.input_file_controll.Clear()
			self.input_file = dlg.GetDirectory() + "/" + dlg.GetFilename()
			self.input_file_controll.WriteText(self.input_file)
			self.base_dir_controll.Clear()
			self.base_dir_controll.WriteText(dlg.GetDirectory())
		dlg.Destroy()
		self.load.Enable()


	def BrowseDir(self, e):
		dlg = wx.DirDialog(self, "Choose a directory", defaultPath=self.base_dir_controll.GetValue(), style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			self.base_dir_controll.Clear()
			self.base_dir = dlg.GetPath()
			self.base_dir_controll.WriteText(self.base_dir)
		dlg.Destroy()


	def my_close(self, e):
		wx.Exit()

	def Load(self, e):
		self.toolbar.EnableTool(887, True)

		if (str(self.type_selector.GetItems()[self.type_selector.GetCurrentSelection()]).split()[0].lower() == 'features'):
			try:

				kwargs = {"file" : str(self.base_dir_controll.GetValue()),
						"input" : [str(self.input_file_controll.GetValue()),
								   None,
								   str(self.dropdown.GetItems()[self.dropdown.GetCurrentSelection()]),
								   None,
								   None,
								   None,
								   str(self.type_selector.GetItems()[self.type_selector.GetCurrentSelection()]).split()[0].lower()]}
			except ValueError as ve:
				wx.MessageBox('The input file or the type is missing. Please give them', 'Error', wx.OK | wx.ICON_ERROR)
				print(ve)

		else:
			try:

				kwargs = {"file" : str(self.base_dir_controll.GetValue()),
						"input" : [str(self.input_file_controll.GetValue()),
								   int(self.size_ctrl.GetValue()),
								   str(self.dropdown.GetItems()[self.dropdown.GetCurrentSelection()]),
								   int(self.length_ctrl.GetValue()),
								   int(self.freq_ctrl.GetValue()),
								   self.time_checker.IsChecked(),
								   str(self.type_selector.GetItems()[self.type_selector.GetCurrentSelection()]).split()[0].lower()]}
			except ValueError as ve:
				wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK | wx.ICON_ERROR)
				print(ve)

		self.core.FirstStep(kwargs)
		if self.type_selector.GetSelection()==0 or self.type_selector.GetSelection()==1 or self.type_selector.GetSelection()==3:
			canvas = wx.Panel(self.panel, pos=(300, 270), size=(400, self.GetSize()[1]))
			figure = Figure(figsize=(5, 3))
			axes = figure.add_axes([0.15, 0.15, 0.8, 0.8])
			FigureCanvas(canvas,-1, figure)
			#self.panel.Fit()
			self.Show()
			#this part is not working yet
			f = self.core.option_handler.input_freq
			t = self.core.option_handler.input_length
			no_traces=self.core.option_handler.input_size
			axes.set_xticks([n for n in range(0, int((t*no_traces)/(1000.0/f)), int((t*no_traces)/(1000.0/f)/5.0)) ])
			axes.set_xticklabels([str(n) for n in range(0, t*no_traces, (t*no_traces)/5)])
			axes.set_xlabel("time [ms]")
			_type="voltage" if self.type_selector.GetSelection()==0 else "current" if self.type_selector.GetSelection()==1 else "unkown"
			#unit="V" if self.type_selector.GetSelection()==0 else "A" if self.type_selector.GetSelection()==1 else ""
			axes.set_ylabel(_type+" [" + self.core.option_handler.input_scale + "]")
			canvas.Fit()
			canvas.Show()
			exp_data = []
			for k in range(self.core.data_handler.number_of_traces()):
				exp_data.extend(self.core.data_handler.data.GetTrace(k))
			axes.plot(list(range(0, len(exp_data))), exp_data)

			if self.type_selector.GetSelection()==0:
				for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
					self.input_tree.Delete(n[1])
					self.loaded_input_types[n[0]]=None
				self.tvoltage=self.input_tree.AppendItem(self.troot,"Voltage trace")
				self.loaded_input_types[0]=self.tvoltage
				self.input_tree.AppendItem(self.tvoltage,self.input_file_controll.GetValue().split("/")[-1])
			elif self.type_selector.GetSelection()==1:
				for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
					self.input_tree.Delete(n[1])
					self.loaded_input_types[n[0]]=None
				self.tcurrent=self.input_tree.AppendItem(self.troot,"Current trace")
				self.loaded_input_types[1]=self.tcurrent
				self.input_tree.AppendItem(self.tcurrent,self.input_file_controll.GetValue().split("/")[-1])

			'''
			elif self.type_selector.GetSelection()==3:
				try:
					self.input_tree.Delete(self.tspike_t)
				except ValueError:
					pass
				self.tspike_t=self.input_tree.AppendItem(self.troot,"Spike times")
				self.input_tree.AppendItem(self.tspike_t,self.input_file_controll.GetValue().split("/")[-1])
				'''

		elif self.type_selector.GetSelection()==2:
			for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
				self.input_tree.Delete(n[1])
				self.loaded_input_types[n[0]]=None
			self.tfeatures=self.input_tree.AppendItem(self.troot,"Features")
			self.loaded_input_types[2]=self.tfeatures
			features_file=self.input_tree.AppendItem(self.tfeatures,self.input_file_controll.GetValue().split("/")[-1])
			self.add_data_dict(self.core.data_handler.features_dict, features_file)

		else:
			pass

	def add_data_dict(self,data_dict, root):
		stack = list(data_dict.items())
		while stack:
			key, value = stack.pop()
			if isinstance(value, dict):
				self.input_tree.AppendItem(root, "{0} : ".format(key))
				stack.extend(iter(value.items()))
			else:
				self.input_tree.AppendItem(root, "  {0} : {1}".format(key, value))



class modelLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path):

		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.panel = wx.Panel(self)
		self.parent = parent
		self.core = core
		self.layer = None

		#this will need to be wrapped in a try statement later:
		import optimizer
		#print optimizer.__file__
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		#print "path",self.path
		self.Center()
		self.ToolbarCreator()
		self.Design()
		#self.is_loaded=False


	def ToolbarCreator(self):

		self.toolbar = self.CreateToolBar()
		button_toolbar_bward = self.toolbar.AddLabelTool(wx.ID_ANY, 'PrevLayer', wx.Bitmap(self.path + "/2leftarrow.png"))
		button_toolbar_fward = self.toolbar.AddLabelTool(888, 'NextLayer', wx.Bitmap(self.path + "/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
		self.toolbar.EnableTool(button_toolbar_fward.GetId(), False)

	def Design(self):

		self.horizontal_box1 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box2 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box3 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box4 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box5 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box6 = wx.BoxSizer(wx.HORIZONTAL)
		self.horizontal_box7 = wx.BoxSizer(wx.HORIZONTAL)


		self.vertical_box1 = wx.BoxSizer(wx.VERTICAL)
		self.vertical_box2 = wx.BoxSizer(wx.VERTICAL)
		self.vertical_box3 = wx.BoxSizer(wx.VERTICAL)


		heading = wx.StaticText(self.panel, label='Model Options')
		heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.horizontal_box1.Add(heading)
#        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
#        wx.StaticLine(self.panel, pos=(400, 215), size=(self.Size[0],1))
#        wx.StaticLine(self.panel, pos=(1, 175), size=(self.Size[0]/2,1))
#        wx.StaticLine(self.panel, pos=(400, 0), size=(1,215),style=wx.LI_VERTICAL)

		descr1 = wx.StaticText(self.panel, label='Model File')
		self.horizontal_box2.Add(descr1)

		self.model_file_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(300, 30), name="Model File")
		self.model_file_ctrl.WriteText(self.core.option_handler.base_dir)
		self.browser1 = wx.Button(self.panel, label="Browse...")
		self.browser1.Bind(wx.EVT_BUTTON, self.BrowseFile)
		self.dd_type = wx.Choice(self.panel, wx.ID_ANY, size=(150, 30))
		self.dd_type.AppendItems(["Neuron", "external"])
		self.dd_type.Select(0)
		self.dd_type.Bind(wx.EVT_CHOICE, self.selectType)
		self.load = wx.Button(self.panel, label="Load")
		self.load.Bind(wx.EVT_BUTTON, self.Load)
		self.horizontal_box3.Add(self.model_file_ctrl, flag=wx.RIGHT, border=50)
		self.horizontal_box3.Add(self.browser1, flag=wx.RIGHT, border=15)
		self.horizontal_box3.Add(self.load, flag=wx.RIGHT, border=15)
		self.horizontal_box3.Add(self.dd_type, flag=wx.RIGHT, border=15)

		descr2 = wx.StaticText(self.panel, label='Special File Location')
		self.horizontal_box4.Add(descr2)
		descr3 = wx.StaticText(self.panel, label='Command to external simulator')
		self.horizontal_box4.Add(descr3, flag=wx.LEFT, border=315)

		self.spec_file_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(300, 30), name="Special File Location")
		self.spec_file_ctrl.WriteText(self.core.option_handler.base_dir)
		self.browser2 = wx.Button(self.panel, label="Browse...")
		self.browser2.Bind(wx.EVT_BUTTON, self.BrowseDir)
		self.sim_path = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(250, 30), name="External simulator path")
		self.sim_path.Disable()
		self.horizontal_box5.Add(self.spec_file_ctrl, flag=wx.RIGHT, border=50)
		self.horizontal_box5.Add(self.browser2, flag=wx.RIGHT, border=15)
		self.horizontal_box5.Add(self.sim_path, flag=wx.RIGHT, border=15)




		self.model_file = self.model_file_ctrl.GetValue()
		self.spec_file = self.spec_file_ctrl.GetValue()


		self.vertical_box1.Add(self.horizontal_box1, flag=wx.BOTTOM, border=15)
		self.vertical_box1.Add(self.horizontal_box2, flag=wx.BOTTOM, border=5)
		self.vertical_box1.Add(self.horizontal_box3, flag=wx.BOTTOM, border=5)
		self.vertical_box1.Add(self.horizontal_box4, flag=wx.BOTTOM, border=5)
		self.vertical_box1.Add(self.horizontal_box5, flag=wx.BOTTOM, border=15)
		self.vertical_box1.Add(self.horizontal_box6, flag=wx.BOTTOM, border=5)



		descr4 = wx.StaticText(self.panel, label='Model & Parameter adjustment', pos=(10, 185))
		descr4.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.horizontal_box6.Add(descr4)

		self.model = wx.ListCtrl(self.panel, pos=(20, 220), size=(600, 300), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.model.InsertColumn(0, 'Section', width=125)
		self.model.InsertColumn(1, 'Segment', width=100)
		self.model.InsertColumn(2, 'Mechanism', width=150)
		self.model.InsertColumn(3, 'Parameter', width=200)
		self.horizontal_box7.Add(self.model)

		self.user_function = wx.Button(self.panel, label="Define Function", pos=(175, 25))
		self.user_function.Bind(wx.EVT_BUTTON, self.UF)
		self.setter = wx.Button(self.panel, label="Set", pos=(650, 385))
		self.setter.Bind(wx.EVT_BUTTON, self.Set)
		self.remover = wx.Button(self.panel, label="Remove", pos=(650, 445))
		self.remover.Bind(wx.EVT_BUTTON, self.Remove)
		self.remover.Disable()
		self.vertical_box2.Add(self.user_function, flag=wx.BOTTOM, border=50)
		self.vertical_box2.Add(self.setter, flag=wx.BOTTOM, border=10)
		self.vertical_box2.Add(self.remover, flag=wx.BOTTOM, border=15)

		self.horizontal_box7.Add(self.vertical_box2, flag=wx.LEFT, border=25)

		self.vertical_box1.Add(self.horizontal_box7)
		self.vertical_box3.Add(self.vertical_box1, flag=wx.ALL, border=10)
		self.panel.SetSizer(self.vertical_box3)


#event functions
	def Next(self, e):

		try:

			#self.core.SecondStep({"stim" : [str(self.dd_type.GetItems()[self.dd_type.GetCurrentSelection()]),float(self.pos_ctrl.GetValue()),str(self.dd_sec1.GetItems()[self.dd_sec1.GetCurrentSelection()])],"stimparam" : [self.stim_window.container,float(self.del_ctrl.GetValue()),float(self.dur_ctrl.GetValue())]})
			self.Hide()
			self.layer.Show()

		except ValueError:
			wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK | wx.ICON_ERROR)
			self.Show()
			self.layer.Hide()
			#layer.Destroy()
		except AttributeError:
#        self.run_controll_tstop = options[0]
#        self.run_controll_dt = options[1]
#        self.run_controll_record = options[2]
#        self.run_controll_sec = options[3]
#        self.run_controll_pos = options[4]
#        self.run_controll_vrest = options[5]

			if self.core.option_handler.type[-1]!="features":
				self.kwargs={"runparam" : [self.core.data_handler.data.t_length,
										   self.core.data_handler.data.step,
										   "record",
										   "sec",
										   "pos",
										   "vrest"]
							}
			else:
				self.kwargs={"runparam" : [self.core.data_handler.features_data["stim_delay"] + self.core.data_handler.features_data["stim_duration"]+100,
										   0.05,
										   "record",
										   "sec",
										   "pos",
										   "vrest"]
							}

			if self.dd_type.GetSelection() == 1:
				self.layer = ffunctionLayer(self, 4, self.Size, "Select Fitness Function", self.core, self.path, self.kwargs)
			else:
				self.layer = stimuliLayer(self, 2, self.Size, "Stimuli & Recording Settings", self.core, self.path)
			self.Hide()
			self.layer.Show()
		if self.core.option_handler.output_level=="1":
			self.core.Print()

	def Prev(self, e):

		self.Hide()
		self.parent.Show()

	def BrowseFile(self, e):

		dlg = wx.FileDialog(self, "Choose a file", self.core.option_handler.base_dir, "", "*.hoc*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.model_file_ctrl.Clear()
			self.model_file = dlg.GetDirectory() + "/" + dlg.GetFilename()
			self.model_file_ctrl.WriteText(self.model_file)
			self.spec_file = dlg.GetDirectory()
			self.spec_file_ctrl.Clear()
			self.spec_file_ctrl.WriteText(self.spec_file)
		dlg.Destroy()

	def BrowseDir(self, e):

		dlg = wx.DirDialog(self, "Choose a directory", self.core.option_handler.base_dir, style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			self.spec_file_ctrl.Clear()
			self.spec_file = dlg.GetPath()
			self.spec_file_ctrl.WriteText(self.spec_file)
		dlg.Destroy()

	def Set(self, e):
		item_selected = self.model.GetFirstSelected()
		if item_selected != -1:
			self.remover.Enable()
			#try to use the table for selection

			section = str(self.model.GetItem(item_selected, 0).GetText())
			#
			segment = str(self.model.GetItem(item_selected, 1).GetText())
			chan = str(self.model.GetItem(item_selected, 2).GetText())
			morph=""
			par = str(self.model.GetItem(item_selected, 3).GetText())
			if chan == "morphology":
				chan = "None"
				par= "None"
				morph = str(self.model.GetItem(item_selected, 3).GetText())



			kwargs = {"section" : section,
					"segment" : segment,
					"channel" : chan,
					"morph" : morph,
					"params" : par,
					"values" : 0}

			searchValue = [kwargs["section"], kwargs["segment"], kwargs["params"], kwargs["morph"]]


			if True:

				for idx in range(self.model.GetItemCount()):
					item = self.model.GetItem(idx, 3)
					item1 = self.model.GetItem(idx, 1)
					item2 = self.model.GetItem(idx, 2)
					item0 = self.model.GetItem(idx, 0)
					if (item0.GetText() == searchValue[0] and item1.GetText() == searchValue[1])and(item.GetText() == searchValue[2] or item2.GetText() == searchValue[3]):
						self.model.SetItemBackgroundColour(idx, "red")


				self.core.SetModel2(kwargs)
			else:
				for idx in range(self.model.GetItemCount()):
					item = self.model.GetItem(idx, 3)
					item1 = self.model.GetItem(idx, 1)
					item2 = self.model.GetItem(idx, 2)
					item0 = self.model.GetItem(idx, 0)
					if (item0.GetText() == searchValue[0] and item1.GetText() == searchValue[1])and(item.GetText() == searchValue[2] or item2.GetText() == searchValue[3]):

						self.model.SetItemBackgroundColour(idx, "green")

				self.core.SetModel(kwargs)

			self.toolbar.EnableTool(888, True)

	def Remove(self, e):
		item_selected = self.model.GetFirstSelected()
		if item_selected != -1:
			#try to use the table for selection

			section = str(self.model.GetItem(item_selected, 0).GetText())
			#
			segment = str(self.model.GetItem(item_selected, 1).GetText())
			chan = str(self.model.GetItem(item_selected, 2).GetText())
			morph=""
			par = str(self.model.GetItem(item_selected, 3).GetText())
			if chan == "morphology":
				chan= "None"
				par= "None"
				morph = str(self.model.GetItem(item_selected, 3).GetText())

			kwargs = {"section" : section,
					"segment" : segment,
					"channel" : chan,
					"morph" : morph,
					"params" : par}

			if kwargs["channel"] == "None":
				temp = kwargs["section"] + " " + kwargs["morph"]
			else:
				temp = kwargs["section"] + " " + kwargs["segment"] +  " " + kwargs["channel"] + " " + kwargs["params"]
			self.core.option_handler.param_vals.pop(self.core.option_handler.GetObjTOOpt().index(temp))
			self.core.option_handler.adjusted_params.remove(temp)
			if len(self.core.option_handler.GetObjTOOpt()) == 0:
				self.remover.Disable()
			searchValue = [kwargs["section"], kwargs["segment"], kwargs["params"], kwargs["morph"]]
			for idx in range(self.model.GetItemCount()):
				item = self.model.GetItem(idx, 3)
				item1 = self.model.GetItem(idx, 1)
				item2 = self.model.GetItem(idx, 2)
				item0 = self.model.GetItem(idx, 0)
				if (item0.GetText() == searchValue[0] and item1.GetText() == searchValue[1])and(item.GetText() == searchValue[2] or item2.GetText() == searchValue[3]):

					self.model.SetItemBackgroundColour(idx, "white")


	def Load(self, e):


		self.model.DeleteAllItems()
		try:
			self.core.LoadModel({"model" : [self.model_file, self.spec_file],
								 "simulator" : self.dd_type.GetItems()[self.dd_type.GetSelection()],
								 "sim_command" : self.sim_path.GetValue()})
			self.core.model_handler.load_neuron()
			temp = self.core.model_handler.GetParameters()
			#print temp
			if temp!=None:
				out = open("model.txt", 'w')

				for i in temp:
					out.write(str(i))
					out.write("\n")

				index = 0
				for row in temp:
					#self.model.InsertStringItem(index,row[0])
					#print row[1]
					for k in (row[1]):
						if k != []:
							#.model.InsertStringItem(index, row[0])
							#self.model.SetStringItem(index, 2, k[0])
							for s in (k[2]):
								self.model.InsertStringItem(index, row[0])
								self.model.SetStringItem(index, 1, str(k[0]))
								self.model.SetStringItem(index, 2, k[1])
								self.model.SetStringItem(index, 3, s)

								index += 1
			else:
				self.toolbar.EnableTool(888, True)
		except OSError:
			wx.MessageBox('Path error! Please use absolute path!', 'Error', wx.OK | wx.ICON_ERROR)


	def selectType(self, e):
		#edit number according the number of options in the construction of dd_type
		if self.dd_type.GetSelection() == 1:
			self.spec_file_ctrl.Disable()
			self.model_file_ctrl.Disable()
			#self.load.Disable()
			self.browser1.Disable()
			self.browser2.Disable()
			self.user_function.Disable()
			self.setter.Disable()
			self.sim_path.Enable()
			self.load.SetLabel("Set")

		else:
			self.spec_file_ctrl.Enable()
			self.model_file_ctrl.Enable()
			#self.load.Enable()
			self.browser1.Enable()
			self.browser2.Enable()
			self.user_function.Enable()
			self.setter.Enable()
			self.sim_path.Disable()
			self.load.SetLabel("Load")


	def UF(self, e):

		dlg = MyDialog(self, self.parent, size=(600, 450), title="User Defined Function")
		dlg.ShowModal()

	def my_close(self, e):
		wx.Exit()

class stimuliLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path):
		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.core = core
		self.panel = wx.Panel(self)
		self.parent = parent

		#this will need to be wrapped in a try statement later:
		import optimizer
		#print optimizer.__file__
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		#print "path",self.path
		self.Center()
		self.ToolbarCreator()
		self.Design()
		self.seed = None

		self.toolbar.EnableTool(wx.ID_FORWARD, True)
		self.layer = None

	def ToolbarCreator(self):
		self.toolbar = self.CreateToolBar()
		button_toolbar_bward = self.toolbar.AddLabelTool(wx.ID_ANY, 'PrevLayer', wx.Bitmap(self.path + "/2leftarrow.png"))
		button_toolbar_fward = self.toolbar.AddLabelTool(wx.ID_FORWARD, 'NextLayer', wx.Bitmap(self.path + "/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
		self.toolbar.EnableTool(wx.ID_FORWARD, False)

	def Design(self):
		self.column1 = wx.BoxSizer(wx.VERTICAL)
		self.column2 = wx.BoxSizer(wx.VERTICAL)
		self.final_sizer = wx.BoxSizer(wx.HORIZONTAL)

		descr3 = wx.StaticText(self.panel, label='Stimulation Settings')
		descr3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.column1.Add(descr3)


		descr5 = wx.StaticText(self.panel, label='Stimulation protocol')
		self.dd_type = wx.Choice(self.panel, wx.ID_ANY, size=(150, 30))
		self.dd_type.AppendItems(["IClamp", "VClamp"])
		self.dd_type.Select(0)
		self.dd_type.Bind(wx.EVT_CHOICE, self.protocolSelection)
		self.column1.Add(descr5, flag=wx.UP, border=15)
		self.column1.Add(self.dd_type, flag=wx.UP, border=5)



		self.stimuli_type=wx.Choice(self.panel,wx.ID_ANY,size=(150,30))
		self.stimuli_type.AppendItems(["Step Protocol", "Custom Waveform"])
		self.stimuli_type.Bind(wx.EVT_CHOICE, self.typeChange)
		self.stimuli_type.Select(0)
		descr7 = wx.StaticText(self.panel, label='Stimulus Type')
		self.column1.Add(descr7, flag=wx.UP, border=15)
		self.column1.Add(self.stimuli_type, flag=wx.UP, border=5)

		#remove this label
		#descr7 = wx.StaticText(self.panel, label='Amplitude')
		self.stimuli = wx.Button(self.panel, label="Amplitude(s)")
		self.stimuli.Bind(wx.EVT_BUTTON, self.Stimuli)


		tmp_sizer2=wx.BoxSizer(wx.HORIZONTAL)
		tmp_sizer2.Add(self.stimuli)
		self.stimuli2 = wx.Button(self.panel, label="Load Waveform")
		self.stimuli2.Bind(wx.EVT_BUTTON, self.Stimuli2)
		self.stimuli2.Disable()
		self.stimuli2.Hide()
		tmp_sizer2.Add(self.stimuli2)
		self.column1.Add(tmp_sizer2, flag=wx.UP, border=15)

		descr8 = wx.StaticText(self.panel, label='Delay (ms)')
		self.del_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="Value")
		self.column1.Add(descr8, flag=wx.UP, border=15)
		self.column1.Add(self.del_ctrl, flag=wx.UP, border=5)
		if self.core.option_handler.type[-1]=="features":
			self.del_ctrl.SetValue(str(self.core.data_handler.features_data["stim_delay"]))


		descr9 = wx.StaticText(self.panel, label='Duration (ms)')
		self.dur_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="Value")
		self.column1.Add(descr9, flag=wx.UP, border=15)
		self.column1.Add(self.dur_ctrl, flag=wx.UP, border=5)
		if self.core.option_handler.type[-1]=="features":
			self.dur_ctrl.SetValue(str(self.core.data_handler.features_data["stim_duration"]))

		descr6 = wx.StaticText(self.panel, label='Section')
		self.dd_sec1 = wx.Choice(self.panel, wx.ID_ANY, size=(150, 30))
		self.dd_sec1.Bind(wx.EVT_CHOICE, self.secChange)
		tmp=self.core.ReturnSections()
		self.dd_sec1.AppendItems(tmp)
		try:
			self.dd_sec1.Select(tmp.index("Soma"))
		except ValueError:
			try:
				self.dd_sec1.Select(tmp.index("soma"))
			except ValueError:
				self.dd_sec1.Select(0)

		self.column1.Add(descr6, flag=wx.UP, border=15)
		self.column1.Add(self.dd_sec1, flag=wx.UP, border=5)

		descr10 = wx.StaticText(self.panel, label='Position inside the section')
		self.pos_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="Value")
		self.pos_ctrl.SetValue("0.5")
		self.pos_ctrl.Bind(wx.EVT_TEXT, self.posChange)
		self.column1.Add(descr10, flag=wx.UP, border=15)
		self.column1.Add(self.pos_ctrl, flag=wx.UP, border=5)

		self.final_sizer.Add(self.column1, flag=wx.LEFT, border=15)


		descr7 = wx.StaticText(self.panel, label='Parameter to record')
		self.dd_record = wx.Choice(self.panel, wx.ID_ANY, size=(100, 30))
		self.dd_record.AppendItems(["v", "i"])
		self.dd_record.Select(0)
		self.column2.Add(descr7, flag=wx.UP, border=35)
		self.column2.Add(self.dd_record, flag=wx.UP, border=5)


		descr6 = wx.StaticText(self.panel, label='Position')
		self.pos_ctrl2 = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="pos")
		self.pos_ctrl2.SetValue("0.5")

		descr8 = wx.StaticText(self.panel, label='Section')
		self.dd_sec = wx.Choice(self.panel, wx.ID_ANY, size=(100, 30))
		self.dd_sec.AppendItems(tmp)

		try:
			self.dd_sec.Select(tmp.index("Soma"))
		except ValueError:
			try:
				self.dd_sec.Select(tmp.index("soma"))
			except ValueError:
				self.dd_sec.Select(0)
		self.column2.Add(descr8, flag=wx.UP, border=15)
		self.column2.Add(self.dd_sec, flag=wx.UP, border=5)
		self.column2.Add(descr6, flag=wx.UP, border=15)
		self.column2.Add(self.pos_ctrl2, flag=wx.UP, border=5)



		descr1 = wx.StaticText(self.panel, label='Run Control')
		descr1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.column2.Add(descr1,flag=wx.UP, border=25)

		descr3 = wx.StaticText(self.panel, label='Initial Voltage (mV)')
		self.vrest_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="vrest")
		self.vrest_ctrl.SetValue("-65")
		self.column2.Add(descr3, flag=wx.UP, border=15)
		self.column2.Add(self.vrest_ctrl, flag=wx.UP, border=5)


		descr4 = wx.StaticText(self.panel, label='tstop (ms)')
		self.tstop_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="tstop")
		if self.core.option_handler.type[-1]!="features":
			self.tstop_ctrl.SetValue(str(self.core.data_handler.data.t_length))
		else:
			self.tstop_ctrl.SetValue(str(self.core.data_handler.features_data["stim_delay"] + self.core.data_handler.features_data["stim_duration"]+100))
		self.column2.Add(descr4, flag=wx.UP, border=15)
		self.column2.Add(self.tstop_ctrl, flag=wx.UP, border=5)

		descr5 = wx.StaticText(self.panel, label='dt')
		self.dt_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(100, 30), name="dt")
		self.dt_ctrl.SetValue(str(0.05))
		self.column2.Add(descr5, flag=wx.UP, border=15)
		self.column2.Add(self.dt_ctrl, flag=wx.UP, border=5)




		self.final_sizer.Add(self.column2, flag=wx.LEFT, border=75)






		self.panel.SetSizer(self.final_sizer)



	def typeChange(self,e):
		if self.stimuli_type.GetSelection()==0:#step prot
			self.stimuli.Enable()
			self.stimuli2.Disable()
			self.del_ctrl.Enable()
			self.dur_ctrl.Enable()
			self.stimuli2.Hide()
			self.stimuli.Show()
			self.final_sizer.Layout()
			#hide wave button
		if self.stimuli_type.GetSelection()==1:#wave prot
			self.stimuli2.Enable()
			self.stimuli.Disable()
			self.del_ctrl.Disable()
			self.del_ctrl.SetValue("0")
			self.dur_ctrl.Disable()
			self.dur_ctrl.SetValue("1e9")
			self.stimuli.Hide()
			self.stimuli2.Show()
			self.final_sizer.Layout()
			#hide step button

	def protocolSelection(self,e):
		if self.dd_type.GetSelection()==1:
			self.dd_sec.Disable()
			self.pos_ctrl2.Disable()
			self.dd_record.SetSelection(1)
		else:
			self.dd_sec.Enable()
			self.pos_ctrl2.Enable()

	def secChange(self,e):
		if self.dd_type.GetSelection()==1:
			self.dd_sec.SetSelection(self.dd_sec1.GetSelection())

	def posChange(self,e):
		if self.dd_type.GetSelection()==1:
			self.pos_ctrl2.SetValue(self.pos_ctrl.GetValue())

	def Stimuli(self, e):
		self.stim_window = stimuliwindow(self, self.core)

	def Stimuli2(self,e):
		self.stim_window = stimuliwindow2(self)
		dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			input_file = dlg.GetDirectory() + "/" + dlg.GetFilename()
		dlg.Destroy()
		self.stim_window.container.append(input_file)
#        self.del_ctrl.SetValue("0")
#        self.del_ctrl.Disable()
#        self.dur_ctrl.SetValue("0")
#        self.dur_ctrl.Disable()

	def Next(self, e):
		try:
			self.core.SecondStep({"stim" : [str(self.dd_type.GetItems()[self.dd_type.GetCurrentSelection()]), float(self.pos_ctrl.GetValue()), str(self.dd_sec1.GetItems()[self.dd_sec1.GetCurrentSelection()])],
								  "stimparam" : [self.stim_window.container, float(self.del_ctrl.GetValue()), float(self.dur_ctrl.GetValue())]})
			self.kwargs = {"runparam":[float(self.tstop_ctrl.GetValue()),
									float(self.dt_ctrl.GetValue()),
									str(self.dd_record.GetItems()[self.dd_record.GetCurrentSelection()]),
									str(self.dd_sec.GetItems()[self.dd_sec.GetCurrentSelection()]),
									float(self.pos_ctrl2.GetValue()),
									float(self.vrest_ctrl.GetValue())]}
			if self.core.option_handler.output_level=="1":
				print({"stim" : [str(self.dd_type.GetItems()[self.dd_type.GetCurrentSelection()]), float(self.pos_ctrl.GetValue()), str(self.dd_sec1.GetItems()[self.dd_sec1.GetCurrentSelection()])],
					   "stimparam" : [self.stim_window.container, float(self.del_ctrl.GetValue()), float(self.dur_ctrl.GetValue())]})
				print(self.kwargs)
		except AttributeError:
			wx.MessageBox("No stimulus amplitude was selected!","Error", wx.OK | wx.ICON_ERROR)
		except ValueError:
			wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK | wx.ICON_ERROR)
		try:
			#self.layer.Design()
			self.layer.Show()
			self.layer.kwargs=self.kwargs
		except AttributeError:
			#self.layer = algorithmLayer(self, 4, self.Size, "Select Algorithm", self.core, self.path, self.kwargs)
			self.layer = ffunctionLayer(self, 4, self.Size, "Fitness Function Selection", self.core, self.path, self.kwargs)
			#self.layer.Design()
			self.layer.Show()
		self.Hide()

	def Prev(self, e):
		self.Hide()
		self.parent.Show()

	def my_close(self, e):
		wx.Exit()







#optimizer settings
#fittnes function settings
#might need new interface
class ffunctionLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path, kwargs):
		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.core = core
		self.panel = wx.Panel(self)
		self.parent = parent

		#this will need to be wrapped in a try statement later:
		import optimizer
		#print optimizer.__file__
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		self.Center()
		self.ToolbarCreator()
		self.Design()
		self.seed = None
		self.kwargs = kwargs

		#print "ffun",kwargs
		self.layer = None

	def ToolbarCreator(self):
		self.toolbar = self.CreateToolBar()
		button_toolbar_bward = self.toolbar.AddLabelTool(wx.ID_ANY, 'PrevLayer', wx.Bitmap(self.path + "/2leftarrow.png"))
		button_toolbar_fward = self.toolbar.AddLabelTool(wx.ID_FORWARD, 'NextLayer', wx.Bitmap(self.path + "/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
		self.toolbar.EnableTool(wx.ID_FORWARD, True)

	def Design(self):

		self.column1 = wx.BoxSizer(wx.VERTICAL)
		self.column2 = wx.BoxSizer(wx.VERTICAL)
		self.row0 = wx.BoxSizer(wx.HORIZONTAL)

		descr0 = wx.StaticText(self.panel, label='Fitness Functions')
		descr0.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))

		descr1 = wx.StaticText(self.panel, label='Weights')

		self.row0.Add(descr1)

		#descr2 = wx.StaticText(self.panel, label='Normalized Weights')


		#self.row0.Add(descr2, flag=wx.LEFT, border=10)

		descr3 = wx.StaticText(self.panel, label='Function Parameters')
		descr3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))

		self.row0.Add(descr3, flag=wx.LEFT, border=10)
		self.column2.Add(self.row0, flag=wx.BOTTOM, border=8)

		if self.core.option_handler.type[-1]!="features":
			self.my_list = copy(self.core.ffun_calc_list)
			#self.my_list=["ffun1","ffun","ffun3"]
		else:
			self.my_list=list(self.core.data_handler.features_data.keys())[3:-1]
		self.param_list = [[]] * len(self.my_list)
		if self.core.option_handler.type[-1]!="features":
			self.param_list[2] = [("Spike Detection Thres. (mv)",0.0)]
			self.param_list[1] = [("Spike Detection Thres. (mv)",0.0), ("Spike Window (ms)",1.0)]
		else:
			self.param_list[0] = [("Spike Detection Thres. (mv)",0.0)]
		self.param_list_container = []
		self.weights = []
		#self.norm_weights = []
		tmp = []
		#for f in self.param_list:
		for i, f in enumerate(self.param_list):
			self.row1 = wx.BoxSizer(wx.HORIZONTAL)
			tmp_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(50, 25))
			if self.core.option_handler.type[-1]=="features":
				tmp_ctrl.SetValue(str(self.core.data_handler.features_data[self.my_list[i]]["weight"]))
			tmp_ctrl.Disable()
			self.weights.append(tmp_ctrl)
			self.row1.Add(tmp_ctrl)
#            tmp_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(50, 25))
#            tmp_ctrl.Disable()
#            self.norm_weights.append(tmp_ctrl)
#            self.row1.Add(tmp_ctrl, flag=wx.LEFT, border=15)
			for p in f:
				tmp_ctrl = wx.TextCtrl(self.panel, id=wx.ID_ANY, size=(50, 25))
				tmp_ctrl.SetValue(str(p[1]))
				if self.core.option_handler.type[-1]!="features":
					tmp_ctrl.Disable()
				tmp.append(tmp_ctrl)
				descr4 = wx.StaticText(self.panel, label=p[0])
				self.row1.Add(descr4, flag=wx.LEFT, border=20)
				self.row1.Add(tmp_ctrl, flag=wx.LEFT, border=2)
			self.param_list_container.append(tmp)
			self.column2.Add(self.row1, flag=wx.UP, border=1)
			tmp = []
		self.listbox = wx.CheckListBox(self.panel, wx.ID_ANY,size=(250,30*len(self.my_list)),choices=self.my_list)
		#lb_size=self.listbox.GetSize()

		#self.listbox.SetSize((200,lb_size[1]))
		self.listbox.SetFont(wx.Font(12,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))
		self.listbox.Bind(wx.EVT_CHECKLISTBOX, self.FunSelect)
		self.listbox.GetChecked()
		self.column1.Add(descr0)
		self.column1.Add(self.listbox, flag=wx.ALL, border=10)
		self.normalize = wx.Button(self.panel, label="Normalize")
		self.normalize.Bind(wx.EVT_BUTTON, self.Normalize)
		self.row3 = wx.BoxSizer(wx.HORIZONTAL)
		self.row3.Add(self.normalize, flag=wx.LEFT, border=10)
		self.column2.Add(self.row3, flag=wx.UP, border=50)
		self.final_sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.final_sizer.Add(self.column1, flag=wx.LEFT, border=10)
		self.final_sizer.Add(self.column2, flag=wx.LEFT, border=10)

		self.SetSizer(self.final_sizer)


	def Normalize(self, e):
		is_enabled = [x for x in enumerate(self.weights) if x[1].IsEnabled()]
		tmp = []
		for n in is_enabled:
			try:
				tmp.append(float(n[1].GetValue()))
			except ValueError:
				continue
		sum_o_weights = sum(tmp)
		for n in is_enabled:
			try:
				self.weights[n[0]].SetValue(str(float(n[1].GetValue()) / float(sum_o_weights)))
			except ValueError:
				continue

	def FunSelect(self, e):

		for i, n in enumerate(self.listbox.GetItems()):
			if i in self.listbox.Checked:
				try:
					if self.core.option_handler.type[-1]!="features":
						for p in self.param_list_container[i]:
							p.Enable()
					self.weights[i].Enable()
					#self.norm_weights[i].Enable()
				except IndexError:
					break
			else:
				try:
					if self.core.option_handler.type[-1]!="features":
						for p in self.param_list_container[i]:
							p.Disable()
					self.weights[i].Disable()
					#self.norm_weights[i].Disable()
				except IndexError:
					break



	def Next(self, e):

		tmp_dict = {}
		for fun, fun_name in zip(self.param_list_container, self.param_list):
			for f, f_n in zip(fun, fun_name):
				if f.IsEnabled():
					tmp_dict.update({f_n[0] : float(f.GetValue())})
		#print tmp_dict
		if self.core.option_handler.type[-1]!="features":
			self.kwargs.update({"feat":
								[tmp_dict,
								 [self.core.ffun_calc_list[fun[0]] for fun in [x for x in enumerate(self.weights) if x[1].IsEnabled()]]]
								})
			self.kwargs.update({"weights" : [float(w.GetValue()) for w in [x for x in self.weights if x.IsEnabled()]]})
		else:
			#self.my_list=self.core.data_handler.features_data.keys()[3:-1]
			self.kwargs.update({"feat":
								[tmp_dict,
								 [self.my_list[fun[0]] for fun in [x for x in enumerate(self.weights) if x[1].IsEnabled()]]]
								})
			self.kwargs.update({"weights" : [float(w.GetValue()) for w in [x for x in self.weights if x.IsEnabled()]]})

		if not(0.99<sum(self.kwargs["weights"])<=1.01):
			dlg = wx.MessageDialog(self, "You did not normalize your weights!\nDo you want to continue?",'Warning', wx.YES_NO | wx.ICON_QUESTION)
			b_id=dlg.ShowModal()
			if  b_id== wx.ID_YES:
				dlg.Destroy()
				#print "yes"
			if b_id == wx.ID_NO:
				#print "no"
				dlg.Destroy()
				return
		try:
			self.layer.Show()
			self.layer.Design()
			self.layer.kwargs=self.kwargs
		except AttributeError:
			#self.layer = resultsLayer(self, 4, self.Size, "Results", self.core, self.path)
			self.layer = algorithmLayer(self, 4, self.Size, "Select Algorithm", self.core, self.path, self.kwargs)
			self.layer.Show()
			self.layer.Design()
		self.Hide()

	def Prev(self, e):
#        self.Hide()
#        tmp=self.parent
#        grandparent=self.parent.parent
#        grandparent.layer=algorithmLayer(grandparent, 4, self.Size, "Select Algorithm", self.core, self.path, self.kwargs)
#        self.parent=grandparent.layer
#        self.parent.Design()
#        tmp.Destroy()
#        self.parent.Show()
		self.parent.Show()
		self.Hide()
		self.Destroy()


	def my_close(self, e):
		wx.Exit()

class algorithmLayer(wx.Frame):
	def __init__(self,parent,ID,size,title,core,path,kwargs):
		wx.Frame.__init__(self,parent,ID,title=title,size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.core=core
		self.panel=wx.Panel(self)
		#self.sub_panel=wx.Panel(self.panel,size=(300,300))
		self.parent=parent
		self.core=core
		self.path=path
		self.Center()
		self.ToolbarCreator()
		self.Design()
		self.seed=None
		self.num_of_ctrl=None
		self.kwargs=kwargs
		#print "algo",kwargs


		self.layer=None

	def ToolbarCreator(self):
		self.toolbar=self.CreateToolBar()
		button_toolbar_bward=self.toolbar.AddLabelTool(wx.ID_ANY,'PrevLayer',wx.Bitmap(self.path+"/2leftarrow.png"))
		button_toolbar_fward=self.toolbar.AddLabelTool(wx.ID_FORWARD,'NextLayer',wx.Bitmap(self.path+"/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
		self.toolbar.EnableTool(wx.ID_FORWARD,True)

	def Design(self):
		self.column1=wx.BoxSizer(wx.VERTICAL)
		self.column2=wx.BoxSizer(wx.VERTICAL)
		#self.column3=wx.BoxSizer(wx.VERTICAL)
		self.sub_row=wx.BoxSizer(wx.HORIZONTAL)
		self.sub_row2=wx.BoxSizer(wx.HORIZONTAL)
		self.final_sizer=wx.BoxSizer(wx.HORIZONTAL)

		descr2 = wx.StaticText(self.panel, label='Optimizer Settings')
		descr2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		self.column1.Add(descr2)


		descr18 = wx.StaticText(self.panel, label='Random seed:')
		self.seed_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,size=(100,30),name="seed")
		self.seed_ctrl.SetValue("1234")
		self.column1.Add(descr18,flag=wx.UP,border=15)
		self.column1.Add(self.seed_ctrl,flag=wx.UP,border=5)

		descr22 = wx.StaticText(self.panel, label='Algorithm:')
		self.dd_evo=wx.Choice(self.panel,wx.ID_ANY,size=(175,30))
		self.dd_evo.Append("Classical EO")
		self.dd_evo.Append("Simulated Annealing")
		self.dd_evo.Append("Particle Swarm")
		self.dd_evo.Append("Basinhopping")
		self.dd_evo.Append("Nelder-Mead")
		self.dd_evo.Append("L-BFGS-B")
		self.dd_evo.Append("Differential Evolution")
		self.dd_evo.Append("Random Search")
		self.dd_evo.Append("NSGAII")
		self.dd_evo.Append("PAES")
		self.dd_evo.Append("NSGAII-deap")
		self.dd_evo.Append("SPEA2")
		self.dd_evo.Append("IBEA")
		self.dd_evo.Append("NES")
		#self.dd_evo.Select(0)
		self.num_of_ctrl=3
		self.dd_evo.Bind(wx.EVT_CHOICE, self.Algo_Select)
		self.column1.Add(descr22,flag=wx.UP,border=15)
		self.column1.Add(self.dd_evo,flag=wx.UP,border=5)

		self.run = wx.Button(self.panel, label="Run")
		self.run.Disable()
		self.run.Bind(wx.EVT_BUTTON, self.Run)
		self.sub_row2.Add(self.run)

		self.boundaries=wx.Button(self.panel,label="Boundaries")
		self.boundaries.Bind(wx.EVT_BUTTON, self.Boundaries)
		self.sub_row.Add(self.boundaries)

		self.starting_points=wx.Button(self.panel,label="Starting Points")
		self.starting_points.Bind(wx.EVT_BUTTON, self.Seed)
		self.sub_row.Add(self.starting_points,flag=wx.LEFT,border=15)


		self.column1.Add(self.sub_row,flag=wx.UP,border=15)
		self.column1.Add(self.sub_row2,flag=wx.UP,border=15)

		descr24 = wx.StaticText(self.panel, label='Number of parameters to optimize:'+str(len(self.core.option_handler.GetObjTOOpt())))
		self.column1.Add(descr24,flag=wx.UP,border=15)

		#self.column2.Add(self.sub_panel,flag=wx.EXPAND)
		self.final_sizer.Add(self.column1,flag=wx.LEFT,border=5)

		self.SetSizer(self.final_sizer)
		self.final_sizer.Layout()


	def Algo_Select(self,e):
		descr19 = ('Size of Population:',100)
		descr20 = ('Number of Generations:',100)
		descr21 = ('Mutation Rate:',0.25)
		descr22 = ('Cooling Rate:',0.5)
		descr23 = ('Mean of Gaussian:',0)
		descr24 = ('Std. Deviation of Gaussian:',1)
		descr26 = ('Initial Temperature:',1.2)
		descr28 = ('Accuracy:',1e-06)
		descr25 = ('Update Frequency:',50)
		descr27 = ('Temperature:',0.1)
		descr29 = ('Step Size:', 0.1)
		descr32 = ('Number of Iterations:',100)
		descr33 = ('Number of Repetition:',100)
		descr30 = ('Error Tolerance for x:',0.0001)
		descr31 = ('Error Tolerance for f:',0.0001)
		descr34 = ('Inertia:', 0.5)
		descr35 = ('Cognitive Rate:', 2.1)
		descr36 = ("Social Rate:",2.1)
		descr37 = ('Neighborhood Size:', 5)
		descr38 = ('Topology:')
		descr39 = ('Crossover Rate:',1)
		descr40 = ('Number of CPU:',1)


		while(self.num_of_ctrl>0):
			self.column2.Hide(self.num_of_ctrl-1)
			self.column2.Remove(self.num_of_ctrl-1)
			self.num_of_ctrl-=1
			self.SetSizer(self.final_sizer)
			self.final_sizer.Layout()

		self.final_sizer.Hide(1)
		self.final_sizer.Remove(1)

		self.SetSizer(self.final_sizer)
		self.final_sizer.Layout()

		self.column2=wx.BoxSizer(wx.VERTICAL)
		selected_algo=self.dd_evo.GetItems()[self.dd_evo.GetSelection()]
		if selected_algo=="Classical EO":
			alg=[descr19,descr20,descr21,descr40]
		elif selected_algo=="Simulated Annealing":
			alg=[descr20,descr21,descr22,descr23,descr24,descr26,descr40]
		elif selected_algo=="Particle Swarm":
			alg=[descr19,descr20,descr34,descr35,descr36,descr40]
		elif selected_algo=="Basinhopping":
			alg=[descr32,descr33,descr25,descr27,descr29]
		elif selected_algo=="Nelder-Mead":
			alg=[descr20,descr30,descr31]
		elif selected_algo=="L-BFGS-B":
			alg=[descr20,descr28]
		elif selected_algo=="Differential Evolution":
			alg=[descr19,descr20,descr21,descr39,descr40]
		elif selected_algo=="Random Search":
			alg=[descr19,descr40]
		elif selected_algo=="NSGAII":
			alg=[descr19,descr20,descr21,descr40]
		elif selected_algo=="PAES":
			alg=[descr19,descr20,descr40]
		elif selected_algo=="NSGAII-deap":
			alg=[descr19,descr20,descr40]
		elif selected_algo=="SPEA2":
			alg=[descr19,descr20,descr40]
		elif selected_algo=="IBEA":
			alg=[descr19,descr20,descr40]
		elif selected_algo=="NES":
			alg=[descr19,descr20,descr40]


		self.algo_param=[]
		for i in range(len(alg)):
			if alg[i]==descr38:
				tmp=wx.Choice(self.panel,wx.ID_ANY,size=(100,30),choices=["Ring","Star"])

		else:
			tmp=wx.TextCtrl(self.panel,id=wx.ID_ANY,size=(100,30))
			tmp.SetValue(str(alg[i][1]))
			self.algo_param.append((tmp,alg[i][0]))
			self.column2.Add(wx.StaticText(self.panel,label=alg[i][0]),flag=wx.UP,border=15)
			self.column2.Add(tmp,flag=wx.UP,border=5)
			value=self.core.option_handler.GetOptimizerOptions().get(alg[i][0])
			if value!=None:
				tmp.SetValue(str(value))
			elif self.kwargs.get("algo_options",{}).get(alg[i][0],None)!=None:
				tmp.SetValue(str(self.kwargs.get("algo_options",{}).get(alg[i][0],None)))


		self.final_sizer.Add(self.column2,flag=wx.LEFT,border=100)
		self.SetSizer(self.final_sizer)
		self.final_sizer.Layout()
		self.run.Enable()



	def Seed(self, e):
		num_o_params=len(self.core.option_handler.GetObjTOOpt())
		seeds = []
		new_dialog_window=MyDialog2(self,num_o_params,seeds)
		new_dialog_window.ShowModal()
#        if dlg.ShowModal()==wx.ID_CANCEL:
#            print "cancel"
#            seeds=None
#            dlg.Destroy()
		#print len(seeds)
		#print seeds
		#if len(seeds)!=num_o_params or len(seeds[0])!=num_o_params:
		#   seeds=None
		self.seed = seeds
		#print self.seed




	def Boundaries(self, e):
		boundarywindow(self)
		#self.run.Enable()


	def Run(self, e):
		try:
			tmp = {"seed" : float(self.seed_ctrl.GetValue()),
				"evo_strat" : str(self.dd_evo.GetItems()[self.dd_evo.GetCurrentSelection()])
				}
			for n in self.algo_param:
				tmp.update({str(n[1]) : float(n[0].GetValue())})
			tmp.update({
				"num_params" : len(self.core.option_handler.GetObjTOOpt()),
				"boundaries" : self.core.option_handler.boundaries ,
				"starting_points" : self.seed
				})
			self.kwargs.update({"algo_options":tmp})
		except AttributeError:
			dlg = wx.MessageBox( "You forget to select an algorithm!",'Error', wx.OK | wx.ICON_ERROR)
			if dlg.ShowModal() == wx.ID_OK:
				dlg.Destroy()
		if self.core.option_handler.output_level=="1":
			self.core.Print()
		#[map(float,map(wxTextCtrl.GetValue,fun)) for fun in self.param_list_container]

		if self.core.option_handler.output_level=="1":
			print(self.kwargs)
		try:
			self.core.ThirdStep(self.kwargs)
			#wx.MessageBox('Optimization finished. Press the Next button for the results!', 'Done', wx.OK | wx.ICON_EXCLAMATION)
			if self.core.option_handler.output_level=="1":
				self.core.Print()
			self.toolbar.EnableTool(wx.ID_FORWARD, True)
			self.seed = None
			self.Next(None)
		except sizeError as sE:
			wx.MessageBox("There was an error during the optimization: "+sE.m, 'Error', wx.OK | wx.ICON_EXCLAMATION)


			#except ValueError:
			#wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK|wx.ICON_ERROR)


	def Next(self, e):
		try:
			self.layer.Show()
			self.layer.kwargs=self.kwargs
			self.layer.Design()
		except AttributeError:
			self.layer = resultsLayer(self, 4, self.Size, "Results", self.core, self.path,self.kwargs)
			#self.layer = ffunctionLayer(self, 4, self.Size, "Fitness Function Selection", self.core, self.path, self.kwargs)
			self.layer.Show()
			#self.layer.Design()
		self.Hide()

	def Prev(self, e):

		self.Hide()
		self.parent.Show()
		self.Destroy()

	def my_close(self, e):
		wx.Exit()



class resultsLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path,kwargs):
		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.core = core
		self.layer = None

		#this will need to be wrapped in a try statement later:
		import optimizer
		#print optimizer.__file__
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		self.panel = wx.Panel(self)
		self.parent = parent
		self.kwargs=kwargs
#        try:
#            self.core.FourthStep()
#            self.Center()
#            self.ToolbarCreator()
#            self.Design()
#        except AttributeError:
#            wx.MessageBox("No optimization result to display!","Error",wx.OK | wx.ICON_ERROR)
#            self.Prev(None)
		self.core.FourthStep()
		self.Center()
		self.ToolbarCreator()
		self.Design()




	def Design(self):
		heading = wx.StaticText(self.panel, label='Final Result', pos=(10, 15))
		heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		text = "Results:"
		#for n, k in zip(self.core.option_handler.GetObjTOOpt(), self.core.optimizer.fit_obj.ReNormalize(self.core.optimizer.final_pop[0].candidate[0:len(self.core.option_handler.adjusted_params)])):
		for n, k in zip(self.core.option_handler.GetObjTOOpt(), self.core.optimizer.fit_obj.ReNormalize(self.core.cands[0])):
			if n.split()[0]==n.split()[-1]:
				param=[n.split()[0], n.split()[-1]]
				text += "\n" + param[0] + "\n" + "\t" + str(k)
			else:
				param=[n.split()[0], "segment: " + n.split()[1], n.split()[-1]]
				#print param
				if n.split()[1]!=n.split()[-1]:
					text += "\n" + ": \n".join(param) + ":" + "\n" + "\t" + str(k)
				else:
					text += "\n" + param[0] + ": " + param[-1] + "\n" + "\t" + str(k)
		#text += "\n" + "fitness:\n" + "\t" + str(self.core.optimizer.final_pop[0].fitnes)
		text += "\n" + "fitness:\n" + "\t" + str(self.core.fits)

		wx.StaticText(self.panel, label=text, pos=(10, 40))
		wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0], 1))
		wx.StaticLine(self.panel, pos=(200, 0), size=(1, self.GetSize()[1]), style=wx.LI_VERTICAL)
		canvas = wx.Panel(self.panel, pos=(210, 10), size=(550, self.GetSize()[1]))
		figure = Figure(figsize=(7, 6))
		axes = figure.add_subplot(111)
		FigureCanvas(canvas, -1, figure)
		self.panel.Fit()
		self.Show()
		canvas.Show()
		exp_data = []
		model_data = []

		if self.core.option_handler.type[-1]!="features":
			for n in range(self.core.data_handler.number_of_traces()):
				exp_data.extend(self.core.data_handler.data.GetTrace(n))
				model_data.extend(self.core.final_result[n])
			no_traces=self.core.data_handler.number_of_traces()
			t = self.core.option_handler.input_length
			step = self.core.option_handler.run_controll_dt
			axes.set_xticks([n for n in range(0, int((t*no_traces)/(step)), int((t*no_traces)/(step)/5.0)) ])
			axes.set_xticklabels([str(n) for n in range(0, t*no_traces, (t*no_traces)/5)])

			axes.set_xlabel("time [ms]")
			_type=self.core.data_handler.data.type
			unit="mV" if _type=="voltage" else "nA" if _type=="current" else ""
			axes.set_ylabel(_type+" [" + unit + "]")
			axes.plot(list(range(0, len(exp_data))), exp_data)
			axes.plot(list(range(0, len(model_data))), model_data, 'r')
			axes.legend(["target", "model"])
			figure.savefig("result_trace.png", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches=None, pad_inches=0.1)
			figure.savefig("result_trace.eps", dpi=None, facecolor='w', edgecolor='w')
			figure.savefig("result_trace.svg", dpi=None, facecolor='w', edgecolor='w')
			param_save=wx.Button(self.panel,id=wx.ID_ANY,label="Save\nParameters",pos=(105,5),size=(90,50))
			param_save.Bind(wx.EVT_BUTTON,self.SaveParam)

		else:
			for n in range(len(self.core.data_handler.features_data["stim_amp"])):
				model_data.extend(self.core.final_result[n])
			no_traces=len(self.core.data_handler.features_data["stim_amp"])
			t = int(self.core.option_handler.run_controll_tstop)         # instead of input_length
			step = self.core.option_handler.run_controll_dt
			axes.set_xticks([n for n in range(0, int((t*no_traces)/(step)), int((t*no_traces)/(step)/5.0)) ])
			axes.set_xticklabels([str(n) for n in range(0, t*no_traces, (t*no_traces)/5)])

			axes.set_xlabel("time [ms]")
			_type=str(self.kwargs["runparam"][2])       #parameter to record
			_type_ = "Voltage" if _type =="v" else "Current" if _type=="c" else ""
			unit="mV" if _type=="v" else "nA" if _type=="c" else ""
			axes.set_ylabel(_type_+" [" + unit + "]")
			#axes.plot(range(0, len(exp_data)), exp_data)
			axes.plot(list(range(0, len(model_data))), model_data, 'r')
			axes.legend(["model"])
			figure.savefig("result_trace.png", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches=None, pad_inches=0.1)
			figure.savefig("result_trace.eps", dpi=None, facecolor='w', edgecolor='w')
			figure.savefig("result_trace.svg", dpi=None, facecolor='w', edgecolor='w')
			param_save=wx.Button(self.panel,id=wx.ID_ANY,label="Save\nParameters",pos=(105,5),size=(90,50))
			param_save.Bind(wx.EVT_BUTTON,self.SaveParam)


	def ToolbarCreator(self):
		self.toolbar = self.CreateToolBar()
		button_toolbar_bward = self.toolbar.AddLabelTool(wx.ID_ANY, 'PrevLayer', wx.Bitmap(self.path + "/2leftarrow.png"))
		button_toolbar_fward = self.toolbar.AddLabelTool(wx.ID_FORWARD, 'NextLayer', wx.Bitmap(self.path + "/2rightarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
		#self.toolbar.EnableTool(wx.ID_FORWARD,False)


	def Prev(self, e):
		self.Hide()
		tmp=self.parent
		grandparent=self.parent.parent
		grandparent.layer=algorithmLayer(grandparent, 4, self.Size, "Select Algorithm", self.core, self.path, self.kwargs)
		self.parent=grandparent.layer
		#self.parent.Design()
		tmp.Destroy()
		self.parent.Show()
#        self.Destroy()
#        self.parent.Show()

	def Next(self, e):
		self.Hide()
		try:
			self.layer.Design()
			self.layer.Show()
		except AttributeError:
			self.layer = analyzisLayer(self, 5, self.Size, "Analysis", self.core, self.path)
			self.layer.Design()
			self.layer.Show()

	def SaveParam(self, e):
		dlg = wx.FileDialog(self, "Type a filename", os.getcwd(), "", "*.*", style=wx.FD_SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.save_file_name=dlg.GetFilename()
			f=open(self.save_file_name,"w")
			#params=self.core.optimizer.fit_obj.ReNormalize(self.core.optimizer.final_pop[0].candidate[0:len(self.core.option_handler.adjusted_params)])
			params=self.core.optimizer.fit_obj.ReNormalize(self.core.cands[0])
			#params=self.core.optimizer.final_pop[0].candidate[0:len(self.core.option_handler.adjusted_params)]
			f.write("\n".join(map(str,params)))
			dlg.Destroy()

	def my_close(self, e):
		wx.Exit()



class analyzisLayer(wx.Frame):
	def __init__(self, parent, ID, size, title, core, path):
		wx.Frame.__init__(self, parent, ID, title=title, size=size)
		self.Bind(wx.EVT_CLOSE, self.my_close)
		self.panel = wx.Panel(self)
		self.parent = parent
		self.core = core
		self.flg = True
		#this will need to be wrapped in a try statement later:
		import optimizer
		#print optimizer.__file__
		path = os.path.dirname(optimizer.__file__)

		self.path = path
		self.Center()
		self.ToolbarCreator()
		self.Design()
		#self.Text()
		self.Buttons()

	def Buttons(self):
		gen_plot = wx.Button(self.panel, label="Generation Plot", pos=(200, 300))
		gen_plot.Bind(wx.EVT_BUTTON, self.PlotGen)
		grid_plot = wx.Button(self.panel, label="Grid Plot", pos=(200, 400))
		grid_plot.Bind(wx.EVT_BUTTON, self.PlotGrid)


	def Design(self):
		heading = wx.StaticText(self.panel, label='Analysis', pos=(10, 15))
		heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
		text = "Results:"
		#for n, k in zip(self.core.option_handler.GetObjTOOpt(), self.core.optimizer.fit_obj.ReNormalize(self.core.optimizer.final_pop[0].candidate[0:len(self.core.option_handler.adjusted_params)])):
		for n, k in zip(self.core.option_handler.GetObjTOOpt(), self.core.optimizer.fit_obj.ReNormalize(self.core.cands[0])):
			if n.split()[0]==n.split()[-1]:
				param=[n.split()[0], n.split()[-1]]
				text += "\n" + param[0] + "\n" + "\t" + str(k)
			else:
				param=[n.split()[0], "segment: " + n.split()[1], n.split()[-1]]
				#print param
				if n.split()[1]!=n.split()[-1]:
					text += "\n" + ": \n".join(param) + ":" + "\n" + "\t" + str(k)
				else:
					text += "\n" + param[0] + ": " + param[-1] + "\n" + "\t" + str(k)
		#text += "\n" + "fitness:\n" + "\t" + str(self.core.optimizer.final_pop[0].fitness)
		text += "\n" + "fitness:\n" + "\t" + str(self.core.fits[0])
		wx.StaticText(self.panel, label=text, pos=(10, 35))
		wx.StaticText(self.panel, label='Fitness statistics', pos=(410, 35))

		wx.StaticLine(self.panel, pos=(400, 0), size=(1, 600), style=wx.LI_VERTICAL)

		if self.core.moo_var:
			try:
				#print(self.core.optimizer.logbook)
				self.record=self.core.optimizer.logbook
				#for key, value in self.record.iteritems():
				#    print key, value
			except AttributeError:
				stats={'best' : "unkown",'worst' : "unkown",'mean' : "unkown",'median' : "unkown", 'std' : "unkown"}
			string = "Avg: " + str(self.record[-1]['avg']) + "\nStd: " + str(self.record[-1]['std']) + "\nMin: " + str(self.record[-1]['min']) + "\nMax: " + str(self.record[-1]['max'])
		else:
			try:
				stats = inspyred.ec.analysis.fitness_statistics(self.core.optimizer.final_pop)
			except AttributeError:
				stats={'best' : "unkown",'worst' : "unkown",'mean' : "unkown",'median' : "unkown", 'std' : "unkown"}
			#print 'type---------------------------------------------------------------'
			#print type(stats['best'])
			#if stats['best'] is tuple:
			#    stats['best']=sum(stats['best'])/len(stats['best'])
			#if stats['worst'] is tuple:
			#    stats['worst']=sum(stats['worst'])/len(stats['worst'])
			string = "Best: " + str(stats['best']) + "\nWorst: " + str(stats['worst']) + "\nMean: " + str(stats['mean']) + "\nMedian: " + str(stats['median']) + "\nStd:" + str(stats['std'])
		wx.StaticText(self.panel, label=string, pos=(410, 55))

		#insert table with error components: 410,200
		self.error_comp_table = wx.ListCtrl(self.panel, pos=(410, 200),size=(350,150),style=wx.LC_REPORT | wx.BORDER_SUNKEN)
		self.error_comp_table.InsertColumn(0, 'Error Function', width=200)
		self.error_comp_table.InsertColumn(1, 'Value', width=200)
		self.error_comp_table.InsertColumn(2, 'Weight', width=200)
		self.error_comp_table.InsertColumn(3, 'Weighted Value', width=200)

		#tmp_list=[]
		for c_idx,c in enumerate(zip(*self.core.error_comps)):
			tmp=[0]*4
			for t_idx in range(len(c)):
				#print c[t_idx]
				tmp[1]+=c[t_idx][2]
				tmp[2]=c[t_idx][0]
				tmp[3]+=c[t_idx][2]*c[t_idx][0]
			if self.core.option_handler.type[-1]!='features':
				tmp[0]=self.core.ffun_mapper[c[t_idx][1].__name__]
			else:
				tmp[0]=(c[t_idx][1])

			tmp=list(map(str,tmp))
			#tmp_list.append(tmp)
			self.error_comp_table.InsertStringItem(c_idx,tmp[0])
			self.error_comp_table.SetStringItem(c_idx,1,tmp[1])
			self.error_comp_table.SetStringItem(c_idx,2,tmp[2])
			self.error_comp_table.SetStringItem(c_idx,3,tmp[3])

		self.error_button=wx.Button(self.panel,pos=(410,410),label="Error Details")
		self.error_button.Bind(wx.EVT_BUTTON,self.ShowErrorDialog)



	def ToolbarCreator(self):
		self.toolbar = self.CreateToolBar()
		button_toolbar_bward = self.toolbar.AddLabelTool(wx.ID_ANY, 'PrevLayer', wx.Bitmap(self.path + "/2leftarrow.png"))
		self.toolbar.Realize()
		self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)

	def PlotGen(self, e):
		import os.path
		if self.core.moo_var and self.flg:
			with open("stat_file.txt","r") as f:
				textlines=""
				for line in f:
					if "(" not in line:
						break
					sums=0
					sums2=0
					i=0
					tups=line[line.index("(") + 1:line.index(")")]
					for word in tups.split(','):
						if word:
							sums+=float(word)*self.core.option_handler.weights[i]
						i+=1
					line=line.replace(tups,str(sums))
					tups2=line[line.rindex("(") + 1:line.rindex(")")]
					i=0
					for word in tups2.split(','):
						if word:
							sums2+=float(word)*self.core.option_handler.weights[i]
						i+=1
					line=line.replace(tups2,str(sums2))
					line=line.replace("(","")
					line=line.replace(")","")
					print(line)
					textlines+=line
			if textlines:
				statsd=open("stat_file.txt","w")
				statsd.write(textlines)
				statsd.close()
		if os.path.getmtime("stat_file.txt") <= self.core.option_handler.start_time_stamp:
			wx.MessageBox('Generation plot is not available for this algorithm.', 'Error', wx.OK | wx.ICON_ERROR)
		try:
			if self.core.moo_var:
				genarr=[]
				minarr=[]
				maxarr=[]
				avgarr=[]
				stdarr=[]
				for i in range(len(self.record)):
					genarr.append(int(self.record[i]['gen']))
					minarr.append(self.record[i]['min'])
					maxarr.append(self.record[i]['max'])
					avgarr.append(self.record[i]['avg'])
					stdarr.append(self.record[i]['std'])
				for i in range(len(maxarr)):
					maxn=0
					minn=0
					avgn=0
					stdn=0
					for j in range(len(maxarr[i])):
						maxn+=float(maxarr[i][j])*self.core.option_handler.weights[j]
						minn+=float(minarr[i][j])*self.core.option_handler.weights[j]
						avgn+=float(avgarr[i][j])*self.core.option_handler.weights[j]
						stdn+=float(stdarr[i][j])*self.core.option_handler.weights[j]
					maxarr[i]=maxn
					minarr[i]=minn
					avgarr[i]=avgn
					stdarr[i]=stdn
				plt.plot(genarr,minarr,label='Minimum')
				plt.plot(genarr,maxarr,label='Maximum')
				plt.plot(genarr,avgarr,label='Average')
				plt.plot(genarr,stdarr,label='Standard Deviation')
				legend = plt.legend(loc='upper center', shadow=True)
				frame = legend.get_frame()
				frame.set_facecolor('0.90')
				for label in legend.get_texts():
					label.set_fontsize('large')
				for label in legend.get_lines():
					label.set_linewidth(1.5)
				plt.show()
			else:
				generation_plot("stat_file.txt")
		except ValueError:
			stat_file=open("stat_file.txt","rb")
			generation_plot(stat_file)
		self.Show()

	def PlotGrid(self, e):
		self.prev_bounds=copy(self.core.option_handler.boundaries)
		self.resolution=10
		self.bw=gridwindow(self)
		self.bw.Show()

	def ShowErrorDialog(self,e):
		self.extra_error_dialog=ErrorDialog(self)
		self.extra_error_dialog.Show()

	def DisplayGrid(self):
		self.bw.Hide()
		from math import sqrt,ceil
		dlg=wx.MessageDialog(self,"Start calculating grid?\nThe calculation might take several minutes depending your machine's performance.",style=wx.OK|wx.CANCEL)
		if dlg.ShowModal()==wx.ID_OK:
			self.bw.Destroy()
			act_bounds=self.core.option_handler.boundaries
			if self.core.grid_result == None or act_bounds!=self.prev_bounds:
				self.core.callGrid(self.resolution)
			no_dims = int(ceil(sqrt(len(self.core.option_handler.GetObjTOOpt()))))
			import matplotlib.pyplot as plt
			f, axes = plt.subplots(no_dims, no_dims, squeeze=False)
			a = []
			for i in axes:
				for j in i:
					a.append(j)

			#,marker='o', color='r', ls=''
			for i in range(len(self.core.option_handler.GetObjTOOpt())):
				#for points, fitness in zip(self.core.optimizer.final_pop[0][i],self.core.optimizer.final_pop[1][i]):
				for points, fitness in zip(self.core.grid_result[0][i],self.core.grid_result[1][i]):
					a[i].plot(points[i],
										   fitness[0], marker='o', color='r', ls='')
				a[i].set_title(self.core.option_handler.GetObjTOOpt()[i].split()[-1])
				a[i].set_ylabel("Error Value")
				a[i].relim()
				a[i].autoscale(True,'both',False)

			#hide unused subplots
			for i in range(len(self.core.option_handler.GetObjTOOpt()),no_dims**2):
				a[i].axis('off')

			matplotlib.pyplot.show()




	def Prev(self, e):
		self.Destroy()
		self.parent.Show()

	def my_close(self, e):
		wx.Exit()


def main(param=None):
	app = wx.App(False)
	core = Core.coreModul()
	if param!=None:
		core.option_handler.output_level=param.lstrip("-v_level=")
	layer = inputLayer(None, 0, (800, 600), "Input Trace Selection", core, os.getcwd())
	#layer=modelLayer(None,0,(800,600),"Input Trace Selection",None,"/".join(os.getcwd().split("/")[0:-1]))
	#layer=stimuliLayer(None,0,(800,600),"Input Trace Selection",None,"/".join(os.getcwd().split("/")[0:-1]))
	#layer=algorithmLayer(None,0,(800,600),"Input Trace Selection",None,"/".join(os.getcwd().split("/")[0:-1]))
	#layer=ffunctionLayer(None,0,(800,600),"Input Trace Selection",None,os.getcwd(),{})
	#layer.Show()
	app.MainLoop()
	try:
		##core.model_handler.hoc_obj.quit()
		pass
	except AttributeError:
		pass
	sys.exit()

if __name__ == "__main__":
	main()
