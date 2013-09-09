import wx
#import wx.lib.scrolledpanel as scroll
import sys
import matplotlib
from inspyred.ec import analysis
from inspyred.ec.analysis import generation_plot, allele_plot
import inspyred
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import os
from string import count,split,strip
from copy import copy
import Core


#input file settings
#"multiple input files" option not available yet
#surrogate generation not available yet
#base directory settings
class firstLayer(wx.Frame):
    def __init__(self,parent,ID,size,title,core,path):
        
        wx.Frame.__init__(self,parent,ID,title=title,size=size)
        self.Bind(wx.EVT_CLOSE, self.my_close)
        self.core=core
        self.path=path
        self.layer=None
        self.panel=wx.Panel(self)
        self.Center()
        self.ToolbarCreator()
        self.Design()
        self.Text()
        self.Buttons()
        
        
        
        self.Show(True)
        
        
    def Buttons(self):
        
        browser1=wx.Button(self.panel,label="Browse...", pos=(350,85))
        browser1.Bind(wx.EVT_BUTTON,self.BrowseFile)
        browser2=wx.Button(self.panel,label="Browse...", pos=(350,165))
        browser2.Bind(wx.EVT_BUTTON,self.BrowseDir)
        self.load=wx.Button(self.panel,label="Load trace", pos=(10,445))
        self.load.Disable()
        self.load.Bind(wx.EVT_BUTTON,self.Load)
        self.time_checker=wx.CheckBox(self.panel,wx.ID_ANY,label="Contains time",pos=(20,115))
        self.dropdown=wx.Choice(self.panel,wx.ID_ANY,(150,245))
        self.dropdown.SetSize((100,30))
        self.dropdown.AppendItems(Core.scales.keys())
        self.dropdown.Select(1)
        
    def ToolbarCreator(self):
        
        self.toolbar=self.CreateToolBar()
        button_toolbar_fward=self.toolbar.AddLabelTool(887,'NextLayer',wx.Bitmap(self.path+"/2rightarrow.png"))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
        self.toolbar.EnableTool(button_toolbar_fward.GetId(),False)
        
        
    
    def Text(self):
        
        self.input_file_controll=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,85),size=(300,30),name="Input Location")
        self.input_file_controll.WriteText(os.getcwd())
        self.base_dir_controll=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,165),size=(300,30),name="Base Location")
        self.base_dir_controll.WriteText(os.getcwd())
        self.size_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,245),size=(100,30),name="NO traces")
        self.length_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,325),size=(100,30),name="Length")
        self.freq_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,405),size=(100,30),name="Frequency")
        
    def Design(self):
        
        heading = wx.StaticText(self.panel, label='File Options', pos=(10, 15))
        heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
        wx.StaticLine(self.panel, pos=(1, 215), size=(self.Size[0],1))
        decr1 = wx.StaticText(self.panel, label='Input File', pos=(10, 65))
        descr2 = wx.StaticText(self.panel, label='Base Directory', pos=(10, 145))
        descr3 = wx.StaticText(self.panel, label='Number of traces', pos=(10, 220))
        descr4 = wx.StaticText(self.panel, label='Length of traces (ms)', pos=(10, 300))
        descr5 = wx.StaticText(self.panel, label='Sampling frequency (Hz)', pos=(10, 380))
        descr6 = wx.StaticText(self.panel, label='Unit of the data', pos=(150, 220))


#event functions
    def Next(self,e):
        
            self.core.Print()
            self.Hide()
            
            try:
                self.layer.Show()
            except AttributeError:
                self.layer=secondLayer(self,1,self.Size,"Model & Parameter Selection",self.core,self.path)
                self.layer.Show()
            
            
        
                    
    def BrowseFile(self,e):

        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_file_controll.Clear()
            self.input_file = dlg.GetDirectory()+"/"+dlg.GetFilename()
            self.input_file_controll.WriteText(self.input_file)
            self.base_dir_controll.Clear()
            self.base_dir_controll.WriteText(dlg.GetDirectory())
        dlg.Destroy()
        self.load.Enable()
        
        
    def BrowseDir(self,e):
        dlg = wx.DirDialog(self, "Choose a directory", defaultPath=os.getcwd(), style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.base_dir_controll.Clear()
            self.base_dir = dlg.GetPath()
            self.base_dir_controll.WriteText(self.input_file)
        dlg.Destroy()
#        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.FD_CHANGE_DIR)
#        if dlg.ShowModal() == wx.ID_OK:
#            self.base_dir_controll.Clear()
#            self.input_file = dlg.GetDirectory()
#            self.base_dir_controll.WriteText(self.input_file)
#        dlg.Destroy()
    
    def my_close(self,e):
        wx.Exit()
        
    def Load(self,e):
        self.toolbar.EnableTool(887,True)
        try:
            
            kwargs={"file" : str(self.base_dir_controll.GetValue()),"input" : [str(self.input_file_controll.GetValue()),int(self.size_ctrl.GetValue()),str(self.dropdown.GetItems()[self.dropdown.GetCurrentSelection()]),int(self.length_ctrl.GetValue()),int(self.freq_ctrl.GetValue()),self.time_checker.IsChecked()]}
            self.core.FirstStep(kwargs)
                
            canvas=wx.Panel(self.panel,pos=(300,220),size=(self.GetSize()[0],self.GetSize()[1]))
            figure = Figure(figsize=(6,4))
            axes = figure.add_subplot(111)
            f=int(self.freq_ctrl.GetValue())
            t=int(self.length_ctrl.GetValue())
            axes.set_xticks([n for n in range(0,f/1000*t,int(float(f/1000*t)/5))])
            axes.set_xticklabels([n for n in range(0,t,int(float(t)/5))])
            axes.set_xlabel("time [ms]")
            axes.set_ylabel("voltage ["+str(self.dropdown.GetItems()[self.dropdown.GetCurrentSelection()])+"]" )
            canv = FigureCanvas(canvas, -1, figure)
            self.panel.Fit()
            self.Show()
            canvas.Show()
            exp_data=[]
            for n in range(len(self.core.trace_reader.data[0])):
                exp_data.extend(self.core.trace_reader.GetTrace(n))
            axes.plot( range(0,len(exp_data)),exp_data)
            
        except ValueError:
            wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK|wx.ICON_ERROR)

           


        
#model options
#files, parameters, stimuli, etc
#model viewer not completed
#surrogate generation not available yet
#multiple stimuli not available yet        
class secondLayer(wx.Frame):
    def __init__(self,parent,ID,size,title,core,path):
        
        wx.Frame.__init__(self,parent,ID,title=title,size=size)
        self.Bind(wx.EVT_CLOSE, self.my_close)
        self.panel=wx.Panel(self)
        self.parent=parent
        self.core=core
        self.layer=None
        self.path=path
        self.Center()
        self.ToolbarCreator()
        self.Design()
        self.Text()
        self.Buttons()
        
        #self.Show()

        
    def Buttons(self):
        
        browser1=wx.Button(self.panel,label="Browse...", pos=(315,75))
        browser1.Bind(wx.EVT_BUTTON,self.BrowseFile)
        browser2=wx.Button(self.panel,label="Browse...", pos=(315,125))
        browser2.Bind(wx.EVT_BUTTON,self.BrowseDir)
        stimuli=wx.Button(self.panel,label="Amplitude(s)",pos=(675,75))
        stimuli.Bind(wx.EVT_BUTTON,self.Stimuli)
        load=wx.Button(self.panel,label="Load", pos=(315,25))
        load.Bind(wx.EVT_BUTTON, self.Load)
        user_function=wx.Button(self.panel,label="Define Function",pos=(175,25))
        user_function.Bind(wx.EVT_BUTTON,self.UF)
        setter=wx.Button(self.panel,label="Set",pos=(650,385))
        setter.Bind(wx.EVT_BUTTON,self.Set)
        self.remover=wx.Button(self.panel,label="Remove",pos=(650,445))
        self.remover.Bind(wx.EVT_BUTTON,self.Remove)
        self.remover.Disable()
        self.to_opt=wx.CheckBox(self.panel,wx.ID_ANY,label="To optimization",pos=(650,415))
        self.to_opt.SetValue(True)
        self.dd_sec1=wx.Choice(self.panel,wx.ID_ANY,(415,125),size=(150,30))
        self.dd_type=wx.Choice(self.panel,wx.ID_ANY,(415,75),size=(150,30))
        self.dd_type.AppendItems(["IClamp","VClamp"])
        self.dd_type.Select(0)
        
        #self.dd_sec2=wx.Choice(self.panel,wx.ID_ANY,(415,285),size=(150,30))
        #self.dd_chan=wx.Choice(self.panel,wx.ID_ANY,(415,335),size=(150,30))
        #self.dd_param=wx.Choice(self.panel,wx.ID_ANY,(415,385),size=(150,30))
        #self.dd_morph=wx.Choice(self.panel,wx.ID_ANY,(415,435),size=(150,30))
#        self.dd_record=wx.Choice(self.panel,wx.ID_ANY,(650,385),size=(100,30))
#        self.dd_record.AppendItems(["v","i"])
#        self.dd_record.Select(0)
        #self.dd_chan.Disable()
        #self.dd_morph.Disable()
        #self.dd_param.Disable()
#        self.dropdown.SetSize((100,30))
#        self.dropdown.AppendItems(Core.scales.keys())
#        self.dropdown.Select(0)
        
    def ToolbarCreator(self):
        
        self.toolbar=self.CreateToolBar()
        button_toolbar_bward=self.toolbar.AddLabelTool(wx.ID_ANY,'PrevLayer',wx.Bitmap(self.path+"/2leftarrow.png"))
        button_toolbar_fward=self.toolbar.AddLabelTool(888,'NextLayer',wx.Bitmap(self.path+"/2rightarrow.png"))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
        self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
        self.toolbar.EnableTool(button_toolbar_fward.GetId(),False)
        
    def Text(self):
        
        self.model_file_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,75),size=(300,30),name="Model File")
        self.model_file_ctrl.WriteText(os.getcwd())
        self.spec_file_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(10,125),size=(300,30),name="Special File Location")
        self.spec_file_ctrl.WriteText(os.getcwd())
        self.model_file=self.model_file_ctrl.GetValue()
        self.spec_file=self.spec_file_ctrl.GetValue()
        self.value_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(650,490),size=(100,30),name="Value")
#        self.vrest_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(650,435),size=(100,30),name="Value")
#        self.vrest_ctrl.SetValue("-65")
        #self.amp_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(675,75),size=(100,30),name="Value")
        self.del_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(675,125),size=(100,30),name="Value")
        self.dur_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(675,175),size=(100,30),name="Value")
        self.pos_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(415,175),size=(100,30),name="Value")
        self.pos_ctrl.SetValue("0.5")
        self.model=wx.ListCtrl(self.panel,pos=(20,220),size=(600,300),style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        #self.model.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnClick)
        self.model.InsertColumn(0, 'Section',width=125)
        self.model.InsertColumn(1, 'Morphology',width=100)
        self.model.InsertColumn(2, 'Channel',width=150)
        self.model.InsertColumn(3, 'Channel Parameter',width=200)
        
        
    def Design(self):
        
        heading = wx.StaticText(self.panel, label='Model Options', pos=(10, 15))
        heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
        wx.StaticLine(self.panel, pos=(400, 215), size=(self.Size[0],1))
        wx.StaticLine(self.panel, pos=(1, 175), size=(self.Size[0]/2,1))
        wx.StaticLine(self.panel, pos=(400, 0), size=(1,215),style=wx.LI_VERTICAL)
        
        decr1 = wx.StaticText(self.panel, label='Model File', pos=(10, 55))
        descr2 = wx.StaticText(self.panel, label='Special File Location', pos=(10, 105))
        
        descr3 = wx.StaticText(self.panel, label='Stimulation Settings', pos=(415, 15))
        descr3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
        descr4 = wx.StaticText(self.panel, label='Model & Parameter adjustment', pos=(10, 185))
        descr4.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
        descr5 = wx.StaticText(self.panel, label='Stimulation type', pos=(415, 55))
        descr6 = wx.StaticText(self.panel, label='Section', pos=(415, 105))
        descr7 = wx.StaticText(self.panel, label='Amplitude', pos=(675,55))
        descr8 = wx.StaticText(self.panel, label='Delay', pos=(675, 105))
        descr9 = wx.StaticText(self.panel, label='Duration', pos=(675, 155))
        descr10 = wx.StaticText(self.panel, label='Position inside the section', pos=(415, 155))
        
#        descr15 = wx.StaticText(self.panel, label='Parameter adjustment', pos=(415, 220))
#        descr15.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
#        descr11 = wx.StaticText(self.panel, label='Section', pos=(415, 265))
#        descr12 = wx.StaticText(self.panel, label='Channel', pos=(415, 315))
#        descr13 = wx.StaticText(self.panel, label='Parameter', pos=(415, 365))
#        descr16 = wx.StaticText(self.panel, label='Morph', pos=(415, 415))
        descr14 = wx.StaticText(self.panel, label='Value', pos=(415, 465))
        #descr17 = wx.StaticText(self.panel, label='Vrest', pos=(650, 415))
        #descr18 = wx.StaticText(self.panel, label='Parameter to Record', pos=(650, 365))

        
        
#event functions    
    def Next(self,e):
        
        
        
        try:
            
            self.core.SecondStep({"stim" : [str(self.dd_type.GetItems()[self.dd_type.GetCurrentSelection()]),float(self.pos_ctrl.GetValue()),str(self.dd_sec1.GetItems()[self.dd_sec1.GetCurrentSelection()])],"stimparam" : [self.stim_window.container,float(self.del_ctrl.GetValue()),float(self.dur_ctrl.GetValue())]})
            self.Hide()
            self.layer.Show()
            
        except ValueError:
            wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK|wx.ICON_ERROR)
            self.Show()
            self.layer.Hide()
            #layer.Destroy()
        except AttributeError:
            self.layer=thirdLayer(self,2,self.Size,"Optimalization & Recording Settings",self.core,self.path)
            self.layer.Show()
        
        self.core.Print()
    
    def Prev(self,e):
       
        self.Hide()
        self.parent.Show()
        
    def BrowseFile(self,e):

        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.hoc*", style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.model_file_ctrl.Clear()
            self.model_file = dlg.GetDirectory()+"/"+dlg.GetFilename()
            self.model_file_ctrl.WriteText(self.model_file)
            self.spec_file=dlg.GetDirectory()
            self.spec_file_ctrl.Clear()
            self.spec_file_ctrl.WriteText(self.spec_file)
        dlg.Destroy()
        
    def BrowseDir(self,e):
        
        dlg = wx.DirDialog(self, "Choose a directory", defaultPath=os.getcwd(), style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.spec_file_ctrl.Clear()
            self.spec_file = dlg.GetPath()
            self.spec_file_ctrl.WriteText(self.spec_file)
        dlg.Destroy()
        
    def Set(self,e):
        item_selected=self.model.GetFirstSelected()
        if item_selected!=-1:
            self.remover.Enable()
            #try to use the table for selection
            
            section=str(self.model.GetItem(item_selected,0).GetText())
            #
            chan=str(self.model.GetItem(item_selected,2).GetText())
            if chan=="-":
                chan="None"
            morph=str(self.model.GetItem(item_selected,1).GetText())
            if morph=="-":
                morph="None"
            par=str(self.model.GetItem(item_selected,3).GetText())
            if par=="-":
                par="None"
    
            try:
                val=float( self.value_ctrl.GetValue())
            except ValueError:
                val=0.1
            
              
            kwargs={"section" : self.model.GetItem(item_selected,0).GetText(),
                    "channel" : chan,
                    "morph" : morph,
                    "params" : par,
                    "values" : val}
            
            searchValue=[kwargs["section"],kwargs["params"],kwargs["morph"]]
            
        
            if self.to_opt.GetValue():
                
                for idx in range(self.model.GetItemCount()): 
                    item = self.model.GetItem(idx, 3)
                    item2=self.model.GetItem(idx, 1)
                    item0=self.model.GetItem(idx,0)
                    if (item0.GetText()==searchValue[0])and(item.GetText() == searchValue[1] or item2.GetText()==searchValue[2]):
                        self.model.SetItemBackgroundColour(idx,"red")
                         
                        
                self.core.SetModel2(kwargs)
            else:
                for idx in range(self.model.GetItemCount()): 
                    item = self.model.GetItem(idx, 3)
                    item2=self.model.GetItem(idx, 1)
                    item0=self.model.GetItem(idx,0)
                    if (item0.GetText()==searchValue[0])and(item.GetText() == searchValue[1] or item2.GetText()==searchValue[2]):
                        
                        self.model.SetItemBackgroundColour(idx,"green") 
                    
                self.core.SetModel(kwargs)
            
            self.toolbar.EnableTool(888,True)
        
    def Remove(self,e):
        item_selected=self.model.GetFirstSelected()
        if item_selected!=-1:
            #try to use the table for selection
            
            section=str(self.model.GetItem(item_selected,0).GetText())
            #
            chan=str(self.model.GetItem(item_selected,2).GetText())
            if chan=="-":
                chan="None"
            morph=str(self.model.GetItem(item_selected,1).GetText())
            if morph=="-":
                morph="None"
            par=str(self.model.GetItem(item_selected,3).GetText())
            if par=="-":
                par="None"
              
            kwargs={"section" : self.model.GetItem(item_selected,0).GetText(),
                "channel" : chan,
                "morph" : morph,
                "params" : par,
                }
            if kwargs["channel"]=="None":
                temp=kwargs["section"]+" "+kwargs["morph"]
            else:
                temp=kwargs["section"]+" "+kwargs["channel"]+" "+kwargs["params"]
            print self.core.option_handler.GetObjTOOpt()
            self.core.option_handler.param_vals.pop(self.core.option_handler.GetObjTOOpt().index(temp))
            self.core.option_handler.adjusted_params.remove(temp)
            print self.core.option_handler.GetObjTOOpt()
            if len(self.core.option_handler.GetObjTOOpt())==0:
                self.remover.Disable()
            searchValue=[kwargs["section"],kwargs["params"],kwargs["morph"]]
            for idx in range(self.model.GetItemCount()): 
                item = self.model.GetItem(idx, 3)
                item2=self.model.GetItem(idx, 1)
                item0=self.model.GetItem(idx,0)
                if (item0.GetText()==searchValue[0])and(item.GetText() == searchValue[1] or item2.GetText()==searchValue[2]):
                    
                    self.model.SetItemBackgroundColour(idx,"white") 
        
                
                        
        
        
    
    
#    def SelectSec(self,e):
#        self.dd_chan.Enable()
#        self.dd_morph.Enable()
#        self.dd_chan.Clear()
#        self.dd_morph.Clear()
#        self.dd_chan.AppendItems(self.core.ReturnChannels(self.dd_sec2.GetItems()[self.dd_sec2.GetCurrentSelection()]))
#        self.dd_morph.AppendItems(self.core.ReturnMorphology())
#
#        self.dd_chan.Select(self.dd_chan.GetItems().index("None"))
#        self.dd_morph.Select(self.dd_morph.GetItems().index("None"))
#        
#    def SelectChan(self,e):
#        if self.dd_chan.GetItems()[self.dd_chan.GetSelection()]=="None":
#            self.dd_morph.Enable()
#            try:
#                self.dd_param.Select(self.dd_param.GetItems().index("None"))
#            except:
#                pass
#            self.dd_param.Disable()
#        else:
#            self.dd_param.Enable()
#            self.dd_param.Clear()
#            self.dd_param.AppendItems(self.core.ReturnChParams(self.dd_chan.GetItems()[self.dd_chan.GetCurrentSelection()]))
#            self.dd_morph.Select(self.dd_morph.GetItems().index("None"))
#            self.dd_morph.Disable()
#        
#    def SelectMorph(self,e):
#        if self.dd_morph.GetItems()[self.dd_morph.GetSelection()]=="None":
#            self.dd_chan.Enable()
#            self.dd_param.Disable()
#        else:
#            self.dd_chan.Select(self.dd_chan.GetItems().index("None"))
#            try:
#                self.dd_param.Select(self.dd_param.GetItems().index("None"))
#            except ValueError:
#                pass
#            self.dd_param.Disable()
#            self.dd_chan.Disable()
#
        
                
    def Load(self,e):
        
        
            
        self.core.LoadModel({"model" : [self.model_file,self.spec_file]})
        self.dd_sec1.Clear()
        #self.dd_sec2.Clear()
        #self.model.DeleteAllColumns()
        self.model.DeleteAllItems()
        #self.model=wx.StaticText(self.panel,wx.ID_ANY,"",pos=(20,200))
        self.dd_sec1.AppendItems(self.core.ReturnSections())
        #self.dd_sec2.AppendItems(self.core.ReturnSections())
        
#        self.dd_sec2.Bind(wx.EVT_CHOICE, self.SelectSec)
#        self.dd_chan.Bind(wx.EVT_CHOICE, self.SelectChan)
#        self.dd_morph.Bind(wx.EVT_CHOICE, self.SelectMorph)
#        
#        self.dd_chan.Clear()
#        self.dd_morph.Clear()
        

        temp=self.core.model_handler.GetParameters()
        out=open("model.txt",'w')
        
        for i in temp:
            out.write(str(i))
            out.write("\n")
            
        #print temp
#        model=""
#        for row in temp:
#            model=model+"--"+row[0]+"\n"+"  -"+row[1]+"\n"+"    -"+row[3]+"\n"+"      -"+row[2][0:rfind(row[2][0:int(3*floor(len(row[2])/4))]," ")]+"\n\t"+"  "+row[2][rfind(row[2][0:int(floor(len(row[2])/2))]," "):len(row[2])-1]+"\n"
#            for col in row:
#                print col+"\n"
        index=0
        for row in temp:
            #self.model.InsertStringItem(index,row[0])
            for k in split(row[1],", "):
                self.model.InsertStringItem(index,row[0])
                self.model.SetStringItem(index,1,k)
                self.model.SetStringItem(index,2,"-")
                self.model.SetStringItem(index,3,"-")
                index+=1
                
            #index+=1
            for k in split(row[2]," "):
                if k!="":
                    self.model.InsertStringItem(index,row[0])
                    self.model.SetStringItem(index,3,k)
                    for s in split(row[3]," "):
                        if count(k,s)==1 and s!="":
                            self.model.SetStringItem(index,2,s)
                            self.model.SetStringItem(index,1,"-")
                    index+=1
                    
                    
            
            
        #self.model=wx.StaticText(self.panel,wx.ID_ANY,str(model),pos=(20,200))
        
    def Stimuli(self,e):
        #start=float(self.del_ctrl.GetValue())
        #dur=float(self.dur_ctrl.GetValue())
        self.stim_window=stimuliwindow(self)
        
    def UF(self,e):
        
        dlg=MyDialog(self,self.parent,size=(600, 450),title="User Defined Function")
        dlg.ShowModal()
            
    def my_close(self,e):
        wx.Exit()
        
        
#optimizer settings
#fittnes function settings
#might need new interface        
class thirdLayer(wx.Frame):
    def __init__(self,parent,ID,size,title,core,path):
        wx.Frame.__init__(self,parent,ID,title=title,size=size)
        self.Bind(wx.EVT_CLOSE, self.my_close)
        self.core=core
        self.panel=wx.Panel(self)
        self.parent=parent
        self.core=core
        self.path=path
        self.Center()
        self.ToolbarCreator()
        self.Design()
        self.Text()
        self.Buttons()
        self.seed=None
        
        
        #self.Show()
        self.layer=None

    def ToolbarCreator(self):
        self.toolbar=self.CreateToolBar()
        button_toolbar_bward=self.toolbar.AddLabelTool(wx.ID_ANY,'PrevLayer',wx.Bitmap(self.path+"/2leftarrow.png"))
        button_toolbar_fward=self.toolbar.AddLabelTool(wx.ID_FORWARD,'NextLayer',wx.Bitmap(self.path+"/2rightarrow.png"))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
        self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
        self.toolbar.EnableTool(wx.ID_FORWARD,False)
    
    def Design(self):
        wx.StaticLine(self.panel, pos=(400, 0), size=(1,self.Size[1]),style=wx.LI_VERTICAL)
        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
        
        descr1 = wx.StaticText(self.panel, label='Run Controll', pos=(10, 15))
        descr1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        descr2 = wx.StaticText(self.panel, label='Optimizer Settings', pos=(415, 15))
        descr2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
        descr3 = wx.StaticText(self.panel, label='Resting Voltage', pos=(10, 130))
        descr4 = wx.StaticText(self.panel, label='tstop', pos=(10, 180))
        descr5 = wx.StaticText(self.panel, label='dt', pos=(10, 230))
        descr6 = wx.StaticText(self.panel, label='position', pos=(10, 280))
        descr7 = wx.StaticText(self.panel, label='Parameter to record', pos=(10, 30))
        descr8 = wx.StaticText(self.panel, label='Section', pos=(10, 80))
        
        descr9 = wx.StaticText(self.panel, label='Minimum in input trace:', pos=(410, 40))
        descr10 = wx.StaticText(self.panel, label='Maximum in input trace:', pos=(410, 70))
        descr11 = wx.StaticText(self.panel, label='Mean of input trace:', pos=(410, 100))
        descr12 = wx.StaticText(self.panel, label='Std deviation of input:', pos=(410, 130))
        
        
        
        temp=self.core.thresHint()
        descr13 = wx.StaticText(self.panel, label=str(temp[0]), pos=(600, 40))
        descr14 = wx.StaticText(self.panel, label=str(temp[1]), pos=(600, 70))
        descr15 = wx.StaticText(self.panel, label=str(temp[2]), pos=(600, 100))
        descr16 = wx.StaticText(self.panel, label=str(temp[3]), pos=(600, 130))
        
        descr17 = wx.StaticText(self.panel, label='Spike detection thres.:', pos=(410, 170))
        descr18 = wx.StaticText(self.panel, label='Random seed:', pos=(410, 200))
        descr19 = wx.StaticText(self.panel, label='Size of population:', pos=(410, 230))
        descr20 = wx.StaticText(self.panel, label='Number of generations:', pos=(410, 260))
        descr21 = wx.StaticText(self.panel, label='Mutation rate:', pos=(410, 290))
        descr22 = wx.StaticText(self.panel, label='Algorithm:', pos=(410, 320))
        descr23 = wx.StaticText(self.panel, label='Fitness function:', pos=(410, 350))
        descr24 = wx.StaticText(self.panel, label='Number of parameters to optimize:'+str(len(self.core.option_handler.GetObjTOOpt())), pos=(410, 385))

    def Text(self):
        
        
        self.vrest_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(15,150),size=(100,30),name="vrest")
        self.vrest_ctrl.SetValue("-65")
        self.tstop_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(15,200),size=(100,30),name="tstop")
        self.tstop_ctrl.SetValue(str(self.core.option_handler.GetInputOptions()[3]))
        self.dt_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(15,250),size=(100,30),name="dt")
        self.dt_ctrl.SetValue(str(float(self.core.trace_reader.step)))
        self.pos_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(15,300),size=(100,30),name="pos")
        self.pos_ctrl.SetValue("0.5")
        self.thres_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(600,160),size=(100,30),name="thres")
        self.thres_ctrl.SetValue("0.0")
        self.seed_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(600,190),size=(100,30),name="seed")
        self.seed_ctrl.SetValue("1234")
        self.pop_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(600,220),size=(100,30),name="population")
        self.pop_ctrl.SetValue("100")
        self.eval_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(600,250),size=(100,30),name="evaluation")
        self.eval_ctrl.SetValue(self.pop_ctrl.GetValue())
        self.mutrat_ctrl=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(600,280),size=(100,30),name="mutation rate")
        self.mutrat_ctrl.SetValue("0.25")



    def Buttons(self):
        self.dd_record=wx.Choice(self.panel,wx.ID_ANY,(15,50),size=(100,30))
        self.dd_record.AppendItems(["v","i"])
        self.dd_record.Select(0)
        self.dd_sec=wx.Choice(self.panel,wx.ID_ANY,(15,100),size=(100,30))
        self.dd_sec.AppendItems(self.core.ReturnSections())
        self.starting_points=wx.Button(self.panel,label="Starting Points",pos=(600,130))
        self.starting_points.Bind(wx.EVT_BUTTON, self.Seed)
        self.dd_evo=wx.Choice(self.panel,wx.ID_ANY,(600,310),size=(175,30))
        self.dd_evo.Append("Classical EO")
        self.dd_evo.Append("Simulated Annealing")
        #self.dd_evo.Append("COBYLA")
        self.dd_evo.Append("SA Scipy")
        self.dd_evo.Append("Nelder-Mead")
        self.dd_evo.Append("L-BFGS-B")
        self.dd_ffun=wx.Choice(self.panel,wx.ID_ANY,(600,340),size=(175,30))
        self.dd_ffun.AppendItems(self.core.ffun_list)
        self.dd_ffun.Select(1)
        self.run=wx.Button(self.panel,label="Run",pos=(700,450))
        self.run.Disable()
        self.run.Bind(wx.EVT_BUTTON, self.Run)
        self.boundaries=wx.Button(self.panel,label="Boundaries",pos=(450,450))
        self.boundaries.Bind(wx.EVT_BUTTON, self.Boundaries)
    
    def Seed(self,e):
        dlg=wx.TextEntryDialog(self,"Insert initial values in the appropriate order, separated by commas!")
        seeds=[]
        if dlg.ShowModal()==wx.ID_OK:
            seeds=map(float,dlg.GetValue().split(","))
            dlg.Destroy()
#        if dlg.ShowModal()==wx.ID_CANCEL:
#            print "cancel"
#            seeds=None
#            dlg.Destroy()
        self.seed=seeds
            

    def Run(self,e):
        #try:    
            kwargs={"runparam":[float(self.tstop_ctrl.GetValue()),
                                float(self.dt_ctrl.GetValue()),
                                str(self.dd_record.GetItems()[self.dd_record.GetCurrentSelection()]),
                                str(self.dd_sec.GetItems()[self.dd_sec.GetCurrentSelection()]),
                                float(self.pos_ctrl.GetValue()),
                                float(self.vrest_ctrl.GetValue())],
                    "ffun":[float(self.thres_ctrl.GetValue()),str(self.dd_ffun.GetItems()[self.dd_ffun.GetCurrentSelection()])],
                    "algo_options":[float(self.seed_ctrl.GetValue()),
                                    str(self.dd_evo.GetItems()[self.dd_evo.GetCurrentSelection()]),
                                    float(self.pop_ctrl.GetValue()),
                                    int(self.eval_ctrl.GetValue()),
                                    float(self.mutrat_ctrl.GetValue()),
                                    len(self.core.option_handler.GetObjTOOpt()),
                                    self.core.option_handler.boundaries 
                                    ]
                    }
#            if self.seed!=None:
            print "graphic",self.seed
            kwargs.update({"starting_points" : self.seed})
            
            if str(self.dd_ffun.GetItems()[self.dd_ffun.GetCurrentSelection()])=="Combinations":
                #create new window
                #ask for selected functions and weights
                #return them in "feat", "weights"
                self.combine=combinewindow(self,kwargs)
            else:        
                msg="Optimization will start after you pressed ok, after that please wait.."
                dlg=wx.MessageBox(msg,"Starting",wx.OK | wx.ICON_EXCLAMATION)
                self.core.ThirdStep(kwargs)

                wx.MessageBox('Optimization finished. Press the Next button for the results', 'Done', wx.OK|wx.ICON_EXCLAMATION)
    
                self.core.Print()
                self.toolbar.EnableTool(wx.ID_FORWARD,True)
            self.seed=None
            #except ValueError:
            #wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK|wx.ICON_ERROR)
            
            
            
    def Boundaries(self,e):
        boundarywindow(self)
        #self.run.Enable()           
           
    def Next(self,e):
        self.Hide()
        try:
            self.layer.Show()
            self.layer.Design()
        except AttributeError:
            self.layer=fourthLayer(self,4,self.Size,"Results",self.core,self.path)
            self.layer.Show()
            self.layer.Design()
        
    def Prev(self,e):
        self.Hide()
        self.parent.Show()
        
    def my_close(self,e):
        wx.Exit()
        
class fourthLayer(wx.Frame):
    def __init__(self,parent,ID,size,title,core,path):
        wx.Frame.__init__(self,parent,ID,title=title,size=size)
        self.Bind(wx.EVT_CLOSE, self.my_close)
        self.core=core
        self.layer=None
        self.path=path
        self.panel=wx.Panel(self)
        self.parent=parent
        self.core.FourthStep()
        self.Center()
        self.ToolbarCreator()
        self.Design()
        

        
    def Design(self):
        heading = wx.StaticText(self.panel, label='Final Result', pos=(10, 15))
        heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        text="Results:"
        for n,k in zip(self.core.option_handler.GetObjTOOpt(),self.core.optimizer.fit_obj.ReNormalize(self.core.optimizer.final_pop[0].candidate[0:len(self.core.option_handler.adjusted_params)])):
            
            text+="\n"+": ".join([n.split()[0],n.split()[-1]])+"\n"+"\t"+str(k)
        text+="\n"+"fitness:\n"+"\t"+str(self.core.optimizer.final_pop[0].fitness)
        wx.StaticText(self.panel, label=text, pos=(10, 40))
        wx.StaticLine(self.panel, pos=(1, 0), size=(self.Size[0],1))
        wx.StaticLine(self.panel,pos=(200,0),size=(1,self.GetSize()[1]),style=wx.LI_VERTICAL)
        canvas=wx.Panel(self.panel,pos=(210,10),size=(550,self.GetSize()[1]))
        figure = Figure(figsize=(7,6))
        axes = figure.add_subplot(111)
        canv = FigureCanvas(canvas, -1, figure)
        self.panel.Fit()
        self.Show()
        canvas.Show()
        f=self.core.option_handler.input_freq
        t=self.core.option_handler.input_length
        axes.set_xticks([n for n in range(0,f/1000*t,int(float(f/1000*t)/5))])
        axes.set_xticklabels([n for n in range(0,t,int(float(t)/5.0))])
        axes.set_xlabel("time [ms]")
        axes.set_ylabel("voltage ["+self.core.option_handler.input_scale+"]")
        exp_data=[]
        model_data=[]
        for n in range(self.core.trace_reader.no_traces):
            exp_data.extend(self.core.trace_reader.GetTrace(n))
            model_data.extend(self.core.final_result[n])
        axes.plot( range(0,len(exp_data)),exp_data)
        axes.plot(range(0,len(model_data)),model_data,'r')
        axes.legend(["target","model"])
        figure.savefig("result_trace.png", dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1)

        
        
    def ToolbarCreator(self):
        self.toolbar=self.CreateToolBar()
        button_toolbar_bward=self.toolbar.AddLabelTool(wx.ID_ANY,'PrevLayer',wx.Bitmap(self.path+"/2leftarrow.png"))
        button_toolbar_fward=self.toolbar.AddLabelTool(wx.ID_FORWARD,'NextLayer',wx.Bitmap(self.path+"/2rightarrow.png"))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.Next, button_toolbar_fward)
        self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
        #self.toolbar.EnableTool(wx.ID_FORWARD,False)
    
    
    def Prev(self,e):
        self.Destroy()
        self.parent.Show()
        
    def Next(self,e):
        self.Hide()
        try:
            self.layer.Design()
            self.layer.Show()
        except AttributeError:
            self.layer=fifthLayer(self,5,self.Size,"Analysis",self.core,self.path)
            self.layer.Design()
            self.layer.Show()
            
        
    def my_close(self,e):
        wx.Exit()
        
     
     
class fifthLayer(wx.Frame):
    def __init__(self,parent,ID,size,title,core,path):
        wx.Frame.__init__(self,parent,ID,title=title,size=size)
        self.Bind(wx.EVT_CLOSE, self.my_close)
        self.panel=wx.Panel(self)
        self.parent=parent
        self.core=core
        self.path=path
        self.Center()
        self.ToolbarCreator()
        self.Design()
        #self.Text()
        self.Buttons()
        
    def Buttons(self):
        gen_plot=wx.Button(self.panel,label="Generation Plot",pos=(25,50))
        gen_plot.Bind(wx.EVT_BUTTON, self.PlotGen)
        allele_plot=wx.Button(self.panel,label="Allele Plot",pos=(25,100))
        allele_plot.Bind(wx.EVT_BUTTON, self.PlotAllele)
        grid_plot=wx.Button(self.panel,label="Grid Plot",pos=(25,150))
        grid_plot.Bind(wx.EVT_BUTTON, self.PlotGrid)
        
        
    def Design(self):
        heading = wx.StaticText(self.panel, label='Analysis', pos=(10, 15))
        heading.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        sub_title1=wx.StaticText(self.panel, label='Generation & Allele plot', pos=(10, 35))
        sub_title2=wx.StaticText(self.panel, label='Fitness statistics', pos=(410, 35))
        
        wx.StaticLine(self.panel, pos=(400, 0), size=(1,600),style=wx.LI_VERTICAL)
        
        
        stats = inspyred.ec.analysis.fitness_statistics(self.core.optimizer.final_pop)
        string="Best: "+str(stats['best'])+"\nWorst: "+str(stats['worst'])+"\nMean: "+str(stats['mean'])+"\nMedian: "+str(stats['median'])+"\nStd:"+str(stats['std'])
        wx.StaticText(self.panel, label=string, pos=(410, 55))
        
        
    def ToolbarCreator(self):
        self.toolbar=self.CreateToolBar()
        button_toolbar_bward=self.toolbar.AddLabelTool(wx.ID_ANY,'PrevLayer',wx.Bitmap(self.path+"/2leftarrow.png"))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.Prev, button_toolbar_bward)
    
    def PlotGen(self,e):
        generation_plot("stat_file.txt")
        self.Show()
        
    def PlotAllele(self,e):
        allele_plot("ind_file.txt")
        self.Show()
    def PlotGrid(self,e):
        boundarywindow(self)
        
        
        
    def Prev(self,e):
        self.Destroy()
        self.parent.Show()
        
    def my_close(self,e):
        wx.Exit()
     
     
class boundarywindow(wx.Frame):
    def __init__(self,par):
        self.boundaries_window=wx.Frame(par.panel,wx.ID_PROPERTIES,"Boundaries",size=(400,700))
        panel=wx.Panel(self.boundaries_window)

        self.par=par
        hstep=200
        vstep=35
        hoffset=10
        voffset=15
        self.min=[]
        self.max=[]
        
        for l in range(len(self.par.core.option_handler.GetObjTOOpt())):
            wx.StaticText(panel,label=self.par.core.option_handler.GetObjTOOpt()[l].split()[-1],pos=(hoffset,voffset+l*vstep))
            tmp_min=wx.TextCtrl(panel,id=l,pos=(hstep,voffset+l*vstep),size=(75,30))
            self.min.append(tmp_min)
            tmp_max=wx.TextCtrl(panel,id=l+len(self.par.core.option_handler.GetOptParam()),pos=(hstep/2+hstep,voffset+l*vstep),size=(75,30))
            self.max.append(tmp_max)
            if len(self.par.core.option_handler.boundaries[1])==len(self.par.core.option_handler.GetObjTOOpt()):
                tmp_min.SetValue(str(self.par.core.option_handler.boundaries[0][l]))
                tmp_max.SetValue(str(self.par.core.option_handler.boundaries[1][l]))
        Setbutton=wx.Button(panel,label="Set",pos=(hstep,650))
        Setbutton.Bind(wx.EVT_BUTTON,self.Set)    
        self.boundaries_window.Show()
        
    def Set(self,e):
            self.par.core.option_handler.boundaries[0]=[float(n.GetValue()) for n in self.min]
            self.par.core.option_handler.boundaries[1]=[float(n.GetValue()) for n in self.max]
            try:
                self.par.run.Enable()
            except AttributeError:
                tmp=self.par.core.option_handler.GetOptimizerOptions()
                tmp[1]="Grid"
                self.par.core.ThirdStep({"runparam" : self.par.core.option_handler.GetModelRun(),
                             "ffun" : [self.par.core.option_handler.spike_thres,self.par.core.option_handler.ffunction],
                             "feat" : self.par.core.option_handler.feats,
                             "weights" : self.par.core.option_handler.weights,
                             "algo_options" : tmp,
                             "starting_points" : None})
            self.boundaries_window.Destroy()
            
    def my_close(self,e):
        wx.Exit()
            
class stimuliwindow(wx.Frame):
    def __init__(self,par):
        self.stimuli_window=wx.Frame(par.panel,wx.ID_ANY,"Set Amplitude(s)",size=(400,500))
        self.panel=wx.Panel(self.stimuli_window)
        self.par=par
        self.container=[]
        wx.StaticText(self.panel,label="Number of stimuli:",pos=(10,10))
        self.generate=wx.Button(self.panel,label="Create",pos=(250,10))
        self.generate.Bind(wx.EVT_BUTTON, self.Set)
        self.load_waveform=wx.Button(self.panel,label="Time Varying\nStimulus",pos=(250,50))
        self.load_waveform.Bind(wx.EVT_BUTTON, self.Load)
        self.number=wx.TextCtrl(self.panel,id=wx.ID_ANY,pos=(150,10),size=(50,30))
        self.accept=wx.Button(self.panel,label="Accept",pos=(200,450))
        self.accept.Disable()
        self.accept.Bind(wx.EVT_BUTTON, self.Accept)
        self.stimuli_window.Show()
        
    def Set(self,e):
        self.temp=[]
        hstep=200
        vstep=35
        hoffset=10
        voffset=50
        for l in range(min(10,int(self.number.GetValue()))):
            wx.StaticText(self.panel,label="Amplitude"+str(l)+":",pos=(hoffset,voffset+l*vstep))
            tmp_obj=wx.TextCtrl(self.panel,id=l,pos=(hstep/2,voffset+l*vstep),size=(75,30))
            self.temp.append(tmp_obj)
        self.accept.Enable()
        self.stimuli_window.Show()
        
            
            
    def Accept(self,e):
        for n in range(len(self.temp)):
            self.container.append(float(self.temp[n].GetValue()))
        self.stimuli_window.Hide()
    
    def Load(self,e):
        dlg = wx.FileDialog(self.stimuli_window, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            input_file = dlg.GetDirectory()+"/"+dlg.GetFilename()
        dlg.Destroy()
        self.container.append(input_file)
        self.par.del_ctrl.SetValue("0")
        self.par.del_ctrl.Disable()
        self.par.dur_ctrl.SetValue("0")
        self.par.dur_ctrl.Disable()
        self.stimuli_window.Hide()
        
    def my_close(self,e):
        wx.Exit()
            
class MyDialog(wx.Dialog):
    
    def __init__(self,parent,*args,**kw):
        super(MyDialog,self).__init__(*args,**kw)
        self.parent=parent
        #panel=wx.Panel(self,size=(300,250))
        #wx.StaticText(self,label="#Please define your function below!\n#The first uncommented line should contain\neither the word python or hoc.\n#This would tell the compiler \nwhich language do you use.",id=wx.ID_ANY,pos=(465,10),style=wx.TE_MULTILINE)
        self.string=wx.TextCtrl(self,id=wx.ID_ANY,pos=(10,10),size=(450,400),style=wx.TE_MULTILINE | wx.TE_AUTO_URL | wx.TE_PROCESS_TAB )
        self.string.SetValue("#Please define your function below in the template!\n#You may choose an arbitrary name for your function,\n#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\ndef usr_fun(self,v):")
        okButton = wx.Button(self, label='Ok',pos=(50,420))
        closeButton = wx.Button(self, label='Close',pos=(200,420))
        okButton.Bind(wx.EVT_BUTTON, self.OnOk)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        loadButton=wx.Button(self,label="Load",pos=(470,20))
        loadButton.Bind(wx.EVT_BUTTON,self.OnLoad)
        
    
        
        
    def OnOk(self,e):
        try:
            #print self.string.GetValue()
            self.parent.core.option_handler.u_fun_string=str(self.string.GetValue())
            self.parent.model.DeleteAllItems()
            text=""
            text=map(strip,str(self.string.GetValue()).split("\n"))[3:-1]
            print text
            variables=[]
            variables=map(strip,str(text[0][text[0].index("(")+1:text[0].index(")")]).split(","))
            print variables
            var_len=int(text[1].lstrip("#"))
            print var_len
            for i in range(var_len):
                self.parent.core.option_handler.SetOptParam(0.1)
                self.parent.core.option_handler.SetObjTOOpt("Vector"+"["+str(i)+"]")
            print variables,variables[0]
            if variables[0]=='':
                raise ValueError
            compile(self.string.GetValue(),'<string>','exec')
            self.parent.toolbar.EnableTool(888,True)
        except ValueError as val_err:
            print val_err
            wx.MessageBox("Your function doesn't have any input parameters!","Error",wx.OK|wx.ICON_ERROR)
        except SyntaxError as syn_err:
            wx.MessageBox(str(syn_err),"Syntax Error",wx.OK|wx.ICON_ERROR)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!pas the user def function params to self.option_handler.SetOptParam(args.get("values"))
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!44 obtain name from self.option_handler.SetObjTOOpt() : vector[0], stb
            
        self.Destroy()
            
        
        
    def OnClose(self, e):
        
        self.Destroy()
        
    def OnLoad(self,e):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            fun_file_path = dlg.GetDirectory()+"/"+dlg.GetFilename()
        dlg.Destroy()
        f=open(fun_file_path,"r")
        fun="#Please define your function below in the template!\n#You may choose an arbitrary name for your function,\n#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\n"
        for l in f:
            fun=fun+l
        self.string.SetValue(fun)
        
        
class combinewindow(wx.Dialog):
    def __init__(self,par,kwargs):
        self.combine_window=wx.Frame(par.panel,wx.ID_ANY,"Functions & Weights",size=(400,500))
        self.panel=wx.Panel(self.combine_window)
        self.par=par
        self.kwargs=kwargs
        self.ok=wx.Button(self.panel,label="Ok",pos=(300,450))
        self.ok.Bind(wx.EVT_BUTTON,self.OnOk)
        wx.StaticText(self.panel,label="Put the weights into the panel above,\n separated by commas!",pos=(10,450))
        self.my_list=copy(self.par.core.ffun_calc_list)
        #self.my_list.remove("Combinations")
        self.listbox=wx.CheckListBox(self.panel,wx.ID_ANY,pos=(10,10),size=(380,400),choices=self.my_list)
        self.w=wx.TextCtrl(self.panel,wx.ID_ANY,pos=(10,410),size=(380,40))
        self.combine_window.Show()
        self.weights=[]
        self.feat=[]
        
    def OnOk(self,e):
        self.weights=map(float,self.w.GetValue().split(","))        
        self.feat=list(self.listbox.GetCheckedStrings())
        self.combine_window.Hide()
        msg="Optimization will start after you pressed ok, after that please wait.."
        dlg=wx.MessageBox(msg,"Starting",wx.OK | wx.ICON_EXCLAMATION)
        
        self.kwargs["feat"]=self.feat
        self.kwargs["weights"]=self.weights
        
        self.par.core.ThirdStep(self.kwargs)

        wx.MessageBox('Optimization finished. Press the Next button for the results', 'Done', wx.OK|wx.ICON_EXCLAMATION)

        self.par.core.Print()
        self.par.toolbar.EnableTool(wx.ID_FORWARD,True)
        
        
          

def main():         
    app=wx.App(False)  
    core=Core.coreModul()      
    layer=firstLayer(None,0,(800,600),"Input Trace Selection",core,"/".join(os.getcwd().split("/")[0:-1]))
    app.MainLoop()
    try:
        core.model_handler.hoc_obj.quit()
    except AttributeError:
        pass
    sys.exit()
    


if __name__=="__main__":
    main()
    sys.exit()
    

