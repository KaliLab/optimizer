  
import wx
import sys
from traceHandler import sizeError
from inspyred.ec.analysis import generation_plot
import inspyred
import matplotlib.pyplot as plt
#from wxPython._controls import wxTextCtrl
import os
from copy import copy
from Core import *
import numpy


from deap.benchmarks.tools import diversity, convergence, hypervolume
from deap import tools


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog , QTableWidgetItem
from PyQt5.QtGui import *
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def popup(message):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)
    msg.setText(message)
    msg.setInformativeText("")
    msg.setWindowTitle("Warning")
    msg.exec()


class Ui_Optimizer(object):
    def setupUi(self, Optimizer):
        Optimizer.setObjectName("Optimizer")
        Optimizer.resize(771, 589)
        self.centralwidget = QtWidgets.QWidget(Optimizer)
        self.centralwidget.setObjectName("centralwidget")
        self.tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabwidget.setGeometry(QtCore.QRect(0, 0, 771, 551))
        self.tabwidget.setObjectName("tabwidget")
                #filetab 2
        self.filetab = QtWidgets.QWidget()
        self.filetab.setObjectName("filetab")
        self.label_3 = QtWidgets.QLabel(self.filetab)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.freq_ctrl = QtWidgets.QLineEdit(self.filetab)
        self.freq_ctrl.setGeometry(QtCore.QRect(10, 330, 221, 22))
        self.freq_ctrl.setObjectName("freq_ctrl")
        self.label_4 = QtWidgets.QLabel(self.filetab)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.length_ctrl = QtWidgets.QLineEdit(self.filetab)
        self.length_ctrl.setGeometry(QtCore.QRect(10, 280, 221, 22))
        self.length_ctrl.setObjectName("length_ctrl")
        self.label_5 = QtWidgets.QLabel(self.filetab)
        self.label_5.setGeometry(QtCore.QRect(10, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.filetab)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.filetab)
        self.label_7.setGeometry(QtCore.QRect(250, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.size_ctrl = QtWidgets.QLineEdit(self.filetab)
        self.size_ctrl.setGeometry(QtCore.QRect(10, 230, 221, 22))
        self.size_ctrl.setObjectName("size_ctrl")
        self.pushButton_3 = QtWidgets.QPushButton(self.filetab)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 400, 80, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.filetab)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.base_dir_controll = QtWidgets.QPushButton(self.filetab)
        self.base_dir_controll.setGeometry(QtCore.QRect(240, 150, 80, 22))
        self.base_dir_controll.setObjectName("base_dir_controll")
        self.label_6 = QtWidgets.QLabel(self.filetab)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_folder = QtWidgets.QLineEdit(self.filetab)
        self.lineEdit_folder.setGeometry(QtCore.QRect(10, 150, 221, 22))
        self.lineEdit_folder.setObjectName("lineEdit_2")
        self.type_selector = QtWidgets.QComboBox(self.filetab)
        self.type_selector.setGeometry(QtCore.QRect(500, 100, 120, 22))
        self.type_selector.setObjectName("type_selector")
        self.type_selector.addItem("")
        self.type_selector.addItem("")
        self.type_selector.addItem("")
        self.type_selector.addItem("")
        self.input_file_controll = QtWidgets.QPushButton(self.filetab)
        self.input_file_controll.setGeometry(QtCore.QRect(240, 100, 80, 22))
        self.input_file_controll.setObjectName("pushButton")
        self.time_checker = QtWidgets.QCheckBox(self.filetab)
        self.time_checker.setGeometry(QtCore.QRect(340, 100, 121, 20))
        self.time_checker.setObjectName("time_checker")
        self.dropdown = QtWidgets.QComboBox(self.filetab)
        self.dropdown.setGeometry(QtCore.QRect(240, 230, 61, 22))
        self.dropdown.setObjectName("dropdown")
        self.dropdown.addItem("uV")
        self.dropdown.addItem("mV")
        self.dropdown.addItem("V")
        self.lineEdit_file = QtWidgets.QLineEdit(self.filetab)
        self.lineEdit_file.setGeometry(QtCore.QRect(10, 100, 221, 22))
        self.lineEdit_file.setObjectName("lineEdit")
        self.input_tree=QtWidgets.QTreeView(self.filetab)
        self.input_tree.setGeometry(QtCore.QRect(370, 130, 250, 100))
        self.model = QStandardItemModel(0, 1)
        self.widget = QtWidgets.QWidget(self.filetab)
        self.widget.setGeometry(QtCore.QRect(290, 270, 331, 200))
        self.widget.setObjectName("widget")


        #model tab 
        self.tabwidget.addTab(self.filetab, "")
        self.modeltab = QtWidgets.QWidget()
        self.modeltab.setObjectName("modeltab")
        self.label_23 = QtWidgets.QLabel(self.modeltab)
        self.label_23.setGeometry(QtCore.QRect(10, 130, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.modeltab)
        self.label_24.setGeometry(QtCore.QRect(10, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_13 = QtWidgets.QPushButton(self.modeltab)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 100, 80, 22))
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_file2 = QtWidgets.QLineEdit(self.modeltab)
        self.lineEdit_file2.setGeometry(QtCore.QRect(10, 100, 221, 22))
        self.lineEdit_file2.setText("")
        self.lineEdit_file2.setObjectName("lineEdit_file2")
        self.modellist = QtWidgets.QTableWidget(self.modeltab)
        self.modellist.setGeometry(QtCore.QRect(10, 200, 441, 261))
        self.modellist.setObjectName("modellist")
        self.pushButton_14 = QtWidgets.QPushButton(self.modeltab)
        self.pushButton_14.setGeometry(QtCore.QRect(240, 150, 80, 22))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.modeltab)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 100, 80, 22))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.modeltab)
        self.pushButton_16.setGeometry(QtCore.QRect(460, 200, 111, 22))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_25 = QtWidgets.QLabel(self.modeltab)
        self.label_25.setGeometry(QtCore.QRect(10, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.modeltab)
        self.label_26.setGeometry(QtCore.QRect(370, 130, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.modeltab)
        self.label_27.setGeometry(QtCore.QRect(10, 180, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.dd_type = QtWidgets.QComboBox(self.modeltab)
        self.dd_type.setGeometry(QtCore.QRect(480, 100, 121, 23))
        self.dd_type.setObjectName("dd_type")
        self.dd_type.addItem("Neuron")
        self.dd_type.addItem("external")
        self.dd_type.currentIndexChanged.connect(self.sim_plat)
        self.lineEdit_folder2 = QtWidgets.QLineEdit(self.modeltab)
        self.lineEdit_folder2.setGeometry(QtCore.QRect(10, 150, 221, 22))
        self.lineEdit_folder2.setText("")
        self.lineEdit_folder2.setObjectName("lineEdit_folder2")
        self.sim_path = QtWidgets.QLineEdit(self.modeltab)
        self.sim_path.setGeometry(QtCore.QRect(360, 150, 241, 22))
        self.sim_path.setObjectName("sim_path")
        self.sim_path.setEnabled(False)
        self.setter = QtWidgets.QPushButton(self.modeltab)
        self.setter.setGeometry(QtCore.QRect(460, 250, 80, 22))
        self.setter.setObjectName("setter")
        self.remover = QtWidgets.QPushButton(self.modeltab)
        self.remover.setGeometry(QtCore.QRect(460, 280, 80, 22))
        self.remover.setObjectName("remover")
        self.remover.setEnabled(False)
        

        

        #sim tab 3
        self.tabwidget.addTab(self.modeltab, "")
        self.simtab = QtWidgets.QWidget()
        self.simtab.setObjectName("simtab")
        self.spinBox_15 = QtWidgets.QComboBox((self.simtab))
        self.spinBox_15.setGeometry(QtCore.QRect(220, 100, 121, 23))
        self.spinBox_15.setObjectName("parameter to record")
        self.label_44 = QtWidgets.QLabel(self.simtab)
        self.label_44.setGeometry(QtCore.QRect(10, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_66 = QtWidgets.QLabel(self.simtab)
        self.label_66.setGeometry(QtCore.QRect(220, 260, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.simtab)
        self.label_67.setGeometry(QtCore.QRect(220, 310, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.label_45 = QtWidgets.QLabel(self.simtab)
        self.label_45.setGeometry(QtCore.QRect(10, 320, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.lineEdit_pos = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_pos.setGeometry(QtCore.QRect(220, 200, 113, 22))
        self.lineEdit_pos.setObjectName("position")
        self.spinBox_9 = QtWidgets.QComboBox(self.simtab)
        self.spinBox_9.setGeometry(QtCore.QRect(10, 340, 121, 23))
        self.spinBox_9.setObjectName("section dur")
        self.label_46 = QtWidgets.QLabel(self.simtab)
        self.label_46.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.stimprot = QtWidgets.QComboBox(self.simtab)
        self.stimprot.setGeometry(QtCore.QRect(10, 100, 121, 23))
        self.stimprot.setObjectName("stimprot")
        self.spinBox_11 = QtWidgets.QComboBox(self.simtab)
        self.spinBox_11.setGeometry(QtCore.QRect(10, 150, 121, 23))
        self.spinBox_11.setObjectName("stimulus type")
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_71 = QtWidgets.QLabel(self.simtab)
        self.label_71.setGeometry(QtCore.QRect(10, 370, 160, 16))
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.lineEdit_posins = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_posins.setGeometry(QtCore.QRect(10, 390, 113, 22))
        self.lineEdit_posins.setObjectName("posinside")
        self.lineEdit_duration = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_duration.setGeometry(QtCore.QRect(10, 290, 113, 22))
        self.lineEdit_duration.setObjectName("duration")
        self.label_47 = QtWidgets.QLabel(self.simtab)
        self.label_47.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.base_dir_controll9 = QtWidgets.QPushButton(self.simtab)
        self.base_dir_controll9.setGeometry(QtCore.QRect(10, 180, 91, 22))
        self.base_dir_controll9.setObjectName("base_dir_controll9")
        self.label_48 = QtWidgets.QLabel(self.simtab)
        self.label_48.setGeometry(QtCore.QRect(220, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.lineEdit_tstop = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_tstop.setGeometry(QtCore.QRect(220, 330, 113, 22))
        self.lineEdit_tstop.setObjectName("tstop")
        self.label_49 = QtWidgets.QLabel(self.simtab)
        self.label_49.setGeometry(QtCore.QRect(10, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_68 = QtWidgets.QLabel(self.simtab)
        self.label_68.setGeometry(QtCore.QRect(220, 360, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.label_50 = QtWidgets.QLabel(self.simtab)
        self.label_50.setGeometry(QtCore.QRect(220, 240, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.lineEdit_delay = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_delay.setGeometry(QtCore.QRect(10, 240, 113, 22))
        self.lineEdit_delay.setObjectName("Delay")
        self.label_51 = QtWidgets.QLabel(self.simtab)
        self.label_51.setGeometry(QtCore.QRect(220, 180, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.simtab)
        self.label_52.setGeometry(QtCore.QRect(220, 80, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.lineEdit_dt = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_dt.setGeometry(QtCore.QRect(220, 380, 113, 22))
        self.lineEdit_dt.setObjectName("lineEdit_dt")
        self.spinBox_16 = QtWidgets.QComboBox(self.simtab)
        self.spinBox_16.setGeometry(QtCore.QRect(220, 150, 121, 23))
        self.spinBox_16.setObjectName("section")
        self.lineEdit_initv = QtWidgets.QLineEdit(self.simtab)
        self.lineEdit_initv.setGeometry(QtCore.QRect(220, 280, 113, 22))
        self.lineEdit_initv.setObjectName("initv")
        self.label_55 = QtWidgets.QLabel(self.simtab)
        self.label_55.setGeometry(QtCore.QRect(10, 80, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        

        #fit tab 4
        self.tabwidget.addTab(self.simtab, "")
        self.fittab = QtWidgets.QWidget()
        self.fittab.setObjectName("fittab")
        self.label_56 = QtWidgets.QLabel(self.fittab)
        self.label_56.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.fitlist = QtWidgets.QTableWidget(self.fittab)
        self.fitlist.setGeometry(QtCore.QRect(10, 80, 301, 401))
        self.fitlist.setObjectName("fitlist")
        self.spike_tresh = QtWidgets.QLineEdit(self.fittab)
        self.spike_tresh.setGeometry(QtCore.QRect(370,110, 113, 22))
        self.spike_tresh.setObjectName("spike_tresh")
        self.spike_window = QtWidgets.QLineEdit(self.fittab)
        self.spike_window.setGeometry(QtCore.QRect(570, 110, 113, 22))
        self.spike_window.setObjectName("spike_window")
        self.label_69 = QtWidgets.QLabel(self.fittab)
        self.label_69.setGeometry(QtCore.QRect(330, 90, 201, 16))
        self.spike_tresh.setText("0.0")
        self.spike_window.setText("1.0")
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.fittab)
        self.label_70.setGeometry(QtCore.QRect(560, 90, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.pushButton_normalize = QtWidgets.QPushButton(self.fittab)
        self.pushButton_normalize.setGeometry(QtCore.QRect(220, 50, 80, 22))
        self.pushButton_normalize.setObjectName("pushButton_normalize")
        self.pushButton_normalize.setText("Normalize")

        

        #run tab 5
        self.tabwidget.addTab(self.fittab, "")
        self.runtab = QtWidgets.QWidget()
        self.runtab.setObjectName("runtab")
        self.pushButton_30 = QtWidgets.QPushButton(self.runtab)
        self.pushButton_30.setGeometry(QtCore.QRect(630, 460, 80, 22))
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_57 = QtWidgets.QLabel(self.runtab)
        self.label_57.setGeometry(QtCore.QRect(10, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.pushButton_31 = QtWidgets.QPushButton(self.runtab)
        self.pushButton_31.setGeometry(QtCore.QRect(110, 460, 111, 22))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.runtab)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 460, 80, 22))
        self.pushButton_32.setObjectName("pushButton_32")
        self.label_59 = QtWidgets.QLabel(self.runtab)
        self.label_59.setGeometry(QtCore.QRect(10, 70, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.algolist = QtWidgets.QTableWidget(self.runtab)
        self.algolist.setGeometry(QtCore.QRect(10, 90, 441, 351))
        self.algolist.setObjectName("algolist")
        self.aspectlist = QtWidgets.QTableWidget(self.runtab)
        self.aspectlist.setGeometry(QtCore.QRect(470, 90, 241, 351))
        self.aspectlist.setObjectName("aspectlist")
        self.label_60 = QtWidgets.QLabel(self.runtab)
        self.label_60.setGeometry(QtCore.QRect(470, 70, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.tabwidget.addTab(self.runtab, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        #eval tab 6
        self.tabwidget.addTab(self.tab_7, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")


        #plot tab 7
        self.tabwidget.addTab(self.tab_4, "")
        Optimizer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Optimizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 19))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        Optimizer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Optimizer)
        self.statusbar.setObjectName("statusbar")
        Optimizer.setStatusBar(self.statusbar)
        self.actionMultiple_Optimization = QtWidgets.QAction(Optimizer)
        self.actionMultiple_Optimization.setObjectName("actionMultiple_Optimization")
        self.menuMenu.addAction(self.actionMultiple_Optimization)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(Optimizer)
        QtCore.QMetaObject.connectSlotsByName(Optimizer)
        self.tabwidget.setCurrentIndex(0)

    def retranslateUi(self, Optimizer):
        _translate = QtCore.QCoreApplication.translate
        Optimizer.setWindowTitle(_translate("Optimizer", "Optimizer"))
        #self.tabwidget.currentChanged.connect(self.onChange)
        #modeltab 1
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.filetab), _translate("Optimizer", "File Tab"))
        self.label_23.setText(_translate("Optimizer", "Special File location"))
        self.label_24.setText(_translate("Optimizer", "Model File"))
        self.pushButton_13.setText(_translate("Optimizer", "Load"))
        self.pushButton_13.clicked.connect(self.Load2)
        self.pushButton_14.setText(_translate("Optimizer", "Browse..."))
        self.pushButton_14.clicked.connect(self.openFolderNameDialog2)
        self.pushButton_15.setText(_translate("Optimizer", "Browse..."))
        self.pushButton_15.clicked.connect(self.openFileNameDialog2)
        self.pushButton_16.setText(_translate("Optimizer", "Define function"))
        self.pushButton_16.clicked.connect(self.UF)
        self.label_25.setText(_translate("Optimizer", "Model Options"))
        self.label_26.setText(_translate("Optimizer", "Command to external simulator"))
        self.label_27.setText(_translate("Optimizer", "Model   Parameter  adjustment"))
        self.setter.setText(_translate("Optimizer", "Set"))
        self.setter.clicked.connect(self.Set)
        self.remover.setText(_translate("Optimizer", "Remove"))
        self.remover.clicked.connect(self.Remove)
        self.modellist.setColumnCount(4)
        self.modellist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.modellist.setHorizontalHeaderLabels(("Section;Segment;Mechanism;Parameter").split(";"))
        #self.modellist.resizeColumnsToContents()
        self.modellist.horizontalHeader().setStretchLastSection(True)
        self.modellist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.modellist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


        #filetab 2
        self.label_3.setText(_translate("Optimizer", "Base Directory"))
        self.label_4.setText(_translate("Optimizer", "Length of traces (ms)"))
        self.label_5.setText(_translate("Optimizer", "Number of traces"))
        self.label.setText(_translate("Optimizer", "File Options"))
        self.label_7.setText(_translate("Optimizer", "Units"))
        self.pushButton_3.setText(_translate("Optimizer", "Load trace"))
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.Load)
        self.label_2.setText(_translate("Optimizer", "Input File"))
        self.base_dir_controll.setText(_translate("Optimizer", "Browse..."))
        self.base_dir_controll.clicked.connect(self.openFolderNameDialog)
        self.label_6.setText(_translate("Optimizer", "Sampling frequency (Hz)"))
        self.type_selector.setItemText(0, _translate("Optimizer", "Voltage trace"))
        self.type_selector.setItemText(1, _translate("Optimizer", "Current trace"))
        self.type_selector.setItemText(2, _translate("Optimizer", "Features"))
        self.type_selector.setItemText(3, _translate("Optimizer", "Other"))
        self.type_selector.currentTextChanged.connect(self.unitchange)
        self.input_file_controll.setText(_translate("Optimizer", "Browse..."))
        self.input_file_controll.clicked.connect(self.openFileNameDialog)
        self.time_checker.setText(_translate("Optimizer", "Contains time"))
        self.dropdown.setItemText(0, _translate("Optimizer", "uV"))
        self.dropdown.setItemText(1, _translate("Optimizer", "mV"))
        self.dropdown.setItemText(2, _translate("Optimizer", "V"))
        self.dropdown.setCurrentIndex(1)

        self.tvoltage=None
        self.tcurrent=None
        self.tspike_t=None
        self.tother=None
        self.tfeatures=None
        #self.vbox.setItemText(_translate("Optimizer", "Vbox"))
        self.figure = plt.figure(figsize=(4,1.75), dpi=80)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.widget)
        #enable this later
        self.loaded_input_types=[self.tvoltage ,
                                 self.tcurrent ,
#                                 self.tspike_t ,
#                                 self.tother,
                                  self.tfeatures]
        self.core=Core.coreModul()

        #optiontab 3
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.modeltab), _translate("Optimizer", "Model Tab"))
        self.label_44.setText(_translate("Optimizer", "Delay (ms)"))
        self.label_66.setText(_translate("Optimizer", "Initial Voltage (mV)"))
        self.label_67.setText(_translate("Optimizer", "tstop (ms)"))
        self.label_45.setText(_translate("Optimizer", "Section"))
        self.label_46.setText(_translate("Optimizer", "Duration (ms)"))
        self.label_47.setText(_translate("Optimizer", "Simulation Settings"))
        self.base_dir_controll9.setText(_translate("Optimizer", "Amplitude(s)"))
        self.base_dir_controll9.clicked.connect(self.amplitudes_fun)
        self.label_48.setText(_translate("Optimizer", "Section"))
        self.label_49.setText(_translate("Optimizer", "Stimulus Type"))
        self.label_68.setText(_translate("Optimizer", "dt"))
        self.label_50.setText(_translate("Optimizer", "Run Control"))
        self.label_51.setText(_translate("Optimizer", "Position"))
        self.label_52.setText(_translate("Optimizer", "Parameter to record"))
        self.label_55.setText(_translate("Optimizer", "Simulation protocol"))
        self.label_71.setText(_translate("Optimizer", "Position inside the section"))
        self.lineEdit_pos.setText("0.5")
        self.lineEdit_posins.setText("0.5")
        self.lineEdit_initv.setText("-65")
        self.lineEdit_dt.setText("0.05")
        
        self.stimprot.addItems(["IClamp","VClamp"])
        self.spinBox_11.addItems(["Step Protocol","Custom Waveform"])
        self.spinBox_15.addItems(["v","i"])
        #self.stimprot.setItemText(0, _translate("Optimizer", "IClamp"))
        #self.stimprot.setItemText(1, _translate("Optimizer", "VClamp"))



        #fittab 4
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.simtab), _translate("Optimizer", "Options Tab"))
        self.label_56.setText(_translate("Optimizer", "Fitness Functions"))
        self.fitlist.setColumnCount(2)
        #self.fitlist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #self.flist.setHorizontalHeaderLabels(("Section;Segment;Mechanism;Parameter").split(";"))
        #self.modellist.resizeColumnsToContents()
        
        #self.fitlist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fitlist.setHorizontalHeaderLabels(["Fitness Functions","Weights"])
        #self.fitlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fitlist.setColumnWidth(0,200)
        self.fitlist.setColumnWidth(1,101)
        self.fitlist.itemSelectionChanged.connect(self.fitselect)
        self.fitlist.horizontalHeader().setStretchLastSection(True)
        self.fitset=set()
        self.label_69.setText(_translate("Optimizer", "Spike Detection Tresh. (mv)"))
        self.label_70.setText(_translate("Optimizer", "Spike Window (ms)"))
        self.pushButton_normalize.clicked.connect(self.Normalize)

        #runtab 5
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.fittab), _translate("Optimizer", "Fitness Tab"))
        self.pushButton_30.setText(_translate("Optimizer", "Run"))
        self.pushButton_30.clicked.connect(self.runsim)
        self.label_57.setText(_translate("Optimizer", "Optimizer Settings"))
        self.pushButton_31.setText(_translate("Optimizer", "Starting Points"))
        self.pushButton_31.clicked.connect(self.startingpoints)
        self.pushButton_32.setText(_translate("Optimizer", "Boundaries"))
        self.pushButton_32.clicked.connect(self.boundarywindow)
        self.label_59.setText(_translate("Optimizer", "Algorithms"))
        self.label_60.setText(_translate("Optimizer", "Parameters"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.runtab), _translate("Optimizer", "Run Tab"))
        self.algolist.setColumnCount(3)
        self.algolist.horizontalHeader().setStretchLastSection(True)
        self.algolist.setHorizontalHeaderLabels(["Algorithms","Package","Description"])
        self.algolist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.algolist.setColumnWidth(0,200)
        self.algolist.clicked.connect(self.algoselect)
        self.algolist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.aspectlist.setColumnCount(2)
        self.aspectlist.horizontalHeader().setStretchLastSection(True)
        self.aspectlist.setHorizontalHeaderLabels(["Aspects","Num"])
        self.aspectlist.cellChanged.connect(self.aspect_changed)
        self.seed=None

        inspyredalgos=["Classical EO","Particle Swarm","Differential Evolution","Random Search","Nondominated Sorted(NSGAII)","Pareto Archived(PAES)"]
        scipyalgos=["Simulated Annealing","Basinhopping","Nelder-Mead","L-BFGS-B"]
        deapalgos=["Nondominated Sorted(NSGAII)","Strength Pareto(SPEA2)","Indicator Based(IBEA)"]
        pybrainalgos=["Natural Esvolution Strategies"]
        pygmoalgos=["Differential Evolution","Self-adaptive DE","Particle Swarm"]
        algos=inspyredalgos+scipyalgos+deapalgos+pybrainalgos+pygmoalgos
        self.algolist.setRowCount(len(algos))
        for index,item in enumerate(algos):        
            self.algolist.setItem(index, 0, QTableWidgetItem(item))

        descr19 = {'Size of Population:':100}
        descr20 = {'Number of Generations:':100}
        descr21 = {'Mutation Rate:':0.25}
        descr22 = {'Cooling Rate:':0.5}
        descr23 = {'Mean of Gaussian:':0}
        descr24 = {'Std. Deviation of Gaussian:':1}
        descr26 = {'Initial Temperature:':1.2}
        descr28 = {'Accuracy:':1e-06}
        descr25 = {'Update Frequency:':50}
        descr27 = {'Temperature:':0.1}
        descr29 = {'Step Size:':0.1}
        descr32 = {'Number of Iterations:':100}
        descr33 = {'Number of Repetition:':100}
        descr30 = {'Error Tolerance for x:':0.0001}
        descr31 = {'Error Tolerance for f:':0.0001}
        descr34 = {'Inertia:': 0.5}
        descr35 = {'Cognitive Rate:': 2.1}
        descr36 = {'Social Rate:':2.1}
        descr37 = {'Neighborhood Size:': 5}
        descr38 = {'Topology:':0}
        descr39 = {'Crossover Rate:':1}
        descr40 = {'Number of CPU:':1}

        self.algo_dict={
            "Classical EO": [descr19.copy(),descr20.copy(),descr21.copy(),descr40],
            "Simulated Annealing": [descr20.copy(),descr21.copy(),descr22.copy(),descr23.copy(),descr24.copy(),descr26.copy(),descr40],
            "Particle Swarm": [descr19.copy(),descr20.copy(),descr34.copy(),descr35.copy(),descr36.copy(),descr40],
            "Basinhopping": [descr32.copy(),descr33.copy(),descr25.copy(),descr27.copy(),descr29],
            "Nelder-Mead": [descr20.copy(),descr30.copy(),descr31],
            "L-BFGS-B": [descr20.copy(),descr28],
            "Differential Evolution": [descr19.copy(),descr20.copy(),descr21.copy(),descr39.copy(),descr40],
            "Random Search": [descr19.copy(),descr40],
            "Nondominated Sorted(NSGAII)": [descr19.copy(),descr20.copy(),descr21.copy(),descr40],
            "Pareto Archived(PAES)": [descr19.copy(),descr20.copy(),descr40],
            "Strength Pareto(SPEA2)": [descr19.copy(),descr20.copy(),descr40],
            "Indicator Based(IBEA)": [descr19.copy(),descr20.copy(),descr40],
            "Natural Esvolution Strategies": [descr19.copy(),descr20.copy(),descr40]
        }
        


        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_7), _translate("Optimizer", "Evaluation Tab"))


        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_4), _translate("Optimizer", "Plot Tab"))
        self.menuMenu.setTitle(_translate("Optimizer", "Menu"))
        self.actionMultiple_Optimization.setText(_translate("Optimizer", "Multiple Optimization"))
        #self.tabwidget.setTabEnabled(1,False)
        #self.tabwidget.setTabEnabled(2,False)
        #self.tabwidget.setTabEnabled(3,False)
        #self.tabwidget.setTabEnabled(4,False)
        self.tabwidget.setTabEnabled(5,False)
        self.tabwidget.setTabEnabled(6,False)
    
                

    def openFileNameDialog(self):    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Data files (*.dat);;All Files (*);;", options=options)
        if fileName:
            self.lineEdit_file.setText(fileName)
            self.lineEdit_folder.setText(os.path.dirname(os.path.realpath(fileName)))
            self.pushButton_3.setEnabled(True)

    def openFolderNameDialog2(self):  
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        folderName= QFileDialog.getExistingDirectory(None, options=options)
        if folderName:
            self.lineEdit_folder2.setText(folderName)

    def openFileNameDialog2(self):    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Hoc Files (*.hoc);;All Files (*);;", options=options)
        if fileName:
            self.lineEdit_file2.setText(fileName)
            self.lineEdit_folder2.setText(os.path.dirname(os.path.realpath(fileName)))
            self.pushButton_3.setEnabled(True)

    def openFolderNameDialog(self):  
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        folderName= QFileDialog.getExistingDirectory(None, options=options)
        if folderName:
            self.lineEdit_folder.setText(folderName)

    def unitchange(self):
        self.dropdown.clear()
        if self.type_selector.currentIndex()==0:
            self.dropdown.addItems(["uV","mV","V"])
        elif self.type_selector.currentIndex()==1:
            self.dropdown.addItems(["pA","nA","uA"])
        elif self.type_selector.currentIndex()==2:
            self.dropdown.addItems(["uV","mV","V","pA","nA","uA"])
        else:
            self.dropdown.addItems(["none"])
        self.dropdown.setCurrentIndex(1)

        
    def add_data_dict(self,data_dict, root):
        stack = data_dict.items()
        while stack:
            key, value = stack.pop()
            if isinstance(value, dict):
                self.input_tree.AppendItem(root, "{0} : ".format(key))
                stack.extend(value.iteritems())
            else:
                self.input_tree.AppendItem(root, "  {0} : {1}".format(key, value))   
        

    def Load(self):

        if (self.type_selector.currentText() == 'Features'):
            try:

                kwargs = {"file" : str(self.lineEdit_folder.text()),
                        "input" : [str(self.lineEdit_file.text()),
                                   None,
                                   str(self.dropdown.currentText()),
                                   None,
                                   None,
                                   None,
                                   self.type_selector.currentText().split()[0].lower()]}
                
            except ValueError as ve:
                #wx.MessageBox('The input file or the type is missing. Please give them', 'Error', wx.OK | wx.ICON_ERROR)
                print(ve)

        else:
            try:

                kwargs = {"file" : str(self.lineEdit_folder.text()),
                        "input" : [str(self.lineEdit_file.text()),
                                   int(self.size_ctrl.text()),
                                   str(self.dropdown.currentText()),
                                   int(self.length_ctrl.text()),
                                   int(self.freq_ctrl.text()),
                                   self.time_checker.isChecked(),
                                   self.type_selector.currentText().split()[0].lower()]}
                
            except ValueError as ve:
                #wx.MessageBox('Some of the cells are empty. Please fill out all of them!', 'Error', wx.OK | wx.ICON_ERROR)
                print(ve)
        self.core.FirstStep(kwargs)
        self.tabwidget.setTabEnabled(1,True)
        if self.type_selector.currentIndex()==0 or self.type_selector.currentIndex()==1 or self.type_selector.currentIndex()==3:
            
            f = self.core.option_handler.input_freq
            t = self.core.option_handler.input_length
            no_traces=self.core.option_handler.input_size
            #self.graphicsView.set_xticks([n for n in range(0, int((t*no_traces)/(1000.0/f)), int((t*no_traces)/(1000.0/f)/5.0)) ])
            #self.graphicsView.set_xticklabels([str(n) for n in range(0, t*no_traces, (t*no_traces)/5)])
            #self.graphicsView.set_xlabel("time [ms]")
            _type="voltage" if self.type_selector.currentIndex==0 else "current" if self.type_selector.currentIndex==1 else "unkown"
            #unit="V" if self.type_selector.GetSelection()==0 else "A" if self.type_selector.GetSelection()==1 else ""
            #self.graphicsView.set_ylabel(_type+" [" + self.core.option_handler.input_scale + "]")
            exp_data = []
            
            for k in range(self.core.data_handler.number_of_traces()):
                exp_data.extend(self.core.data_handler.data.GetTrace(k))
            ax = self.figure.add_subplot(111)
            ax.hold(False)
            ax.plot(list(range(0, len(exp_data))), exp_data)
            self.canvas.draw()
            #self.graphicsView.set_title('PyQt Matplotlib Example')
            
            
            
            for k in range(self.core.data_handler.number_of_traces()):
                exp_data.extend(self.core.data_handler.data.GetTrace(k))
            #axes.plot(list(range(0, len(exp_data))), exp_data)
            self.model.insertRow(0)
            if self.type_selector.currentIndex()==0:
                for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
                    self.loaded_input_types[n[0]]=None
                #self.tvoltage=self.input_tree.AppendItem(self.troot,"Voltage trace")
                self.loaded_input_types[0]=self.tvoltage
                
                #self.model.setData(self.model.index(0), self.tvoltage,self.input_file_controll.GetValue().split("/")[-1])
                #self.input_tree.AppendItem(self.tvoltage,self.input_file_controll.GetValue().split("/")[-1])
            elif self.type_selector.currentIndex()==1:
                for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
                    #self.input_tree.Delete(n[1])
                    self.loaded_input_types[n[0]]=None
                #self.tcurrent=self.input_tree.AppendItem(self.troot,"Current trace")
                self.loaded_input_types[1]=self.tcurrent
                #self.model.setData(self.model.index(0),self.tcurrent,self.input_file_controll.GetValue().split("/")[-1])
                #self.input_tree.AppendItem(self.tcurrent,self.input_file_controll.GetValue().split("/")[-1])

            '''
            elif self.type_selector.GetSelection()==3:
                try:
                    self.input_tree.Delete(self.tspike_t)
                except ValueError:
                    pass
                self.tspike_t=self.input_tree.AppendItem(self.troot,"Spike times")
                self.input_tree.AppendItem(self.tspike_t,self.input_file_controll.GetValue().split("/")[-1])
                '''

        elif self.type_selector.currentIndex()==2:
            for n in [x for x in enumerate(self.loaded_input_types) if x[1]!=None and x[0]!=2]:
                #self.input_tree.Delete(n[1])
                self.loaded_input_types[n[0]]=None
            #self.tfeatures=self.input_tree.AppendItem(self.troot,"Features")
            #self.loaded_input_types[2]=self.tfeatures
            #features_file=self.model.setData(self.model.index(0, self.FROM),self.tfeatures,self.input_file_controll.GetValue().split("/")[-1])
            #features_file=self.input_tree.AppendItem(self.tfeatures,self.input_file_controll.GetValue().split("/")[-1])
            #self.add_data_dict(self.core.data_handler.features_dict, features_file)

        else:
            pass
    
        if self.core.option_handler.type[-1]!="features":
                self.my_list = copy(self.core.ffun_calc_list)
               
        else:
            self.my_list=list(self.core.data_handler.features_data.keys())[3:-1]
        self.param_list = [[]] * len(self.my_list)
        if self.core.option_handler.type[-1]!="features":
            self.param_list[2] = [("Spike Detection Thres. (mv)",0.0)]
            self.param_list[1] = [("Spike Detection Thres. (mv)",0.0), ("Spike Window (ms)",1.0)]
        else:
            self.param_list[0] = [("Spike Detection Thres. (mv)",0.0)]

        self.fitlist.setRowCount(len(self.my_list))
        for index,elems in enumerate(self.my_list):  
            item = QTableWidgetItem(elems)
            item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )      
            self.fitlist.setItem(index, 0, item)
            self.fitlist.setItem(index, 1, QTableWidgetItem("0"))

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
                                        "vrest"]}
        if self.core.option_handler.output_level=="1":
            self.core.Print()
        self.fit_container=[]
        if self.core.option_handler.type[-1]!="features":
            self.lineEdit_tstop.setText(str(self.core.data_handler.data.t_length))
        else:
            self.lineEdit_tstop.setText(str(self.core.data_handler.features_data["stim_delay"] + self.core.data_handler.features_data["stim_duration"]+100))
        self.fitlist.cellChanged.connect(self.fitchanged)
        
        
        
    def Set(self, e):
        items = self.modellist.selectionModel().selectedRows()
        self.remover.setEnabled(True)
        for item_selected in items:
                #try to use the table for selection

                section = str(self.modellist.item(item_selected.row(), 0).text())
                #
                segment = str(self.modellist.item(item_selected.row(), 1).text())
                chan = str(self.modellist.item(item_selected.row(), 2).text())
                morph=""
                par = str(self.modellist.item(item_selected.row(), 3).text())
                if chan == "morphology":
                    chan = "None"
                    par= "None"
                    morph = str(self.modellist.item(item_selected.row(), 3).text())



                kwargs = {"section" : section,
                        "segment" : segment,
                        "channel" : chan,
                        "morph" : morph,
                        "params" : par,
                        "values" : 0}

                searchValue = [kwargs["section"], kwargs["segment"], kwargs["params"], kwargs["morph"]]


                if True:

                    for idx in range(self.modellist.rowCount()):
                        item = self.modellist.item(idx, 3).text()
                        item1 = self.modellist.item(idx, 1).text()
                        item2 = self.modellist.item(idx, 2).text()
                        item0 = self.modellist.item(idx, 0).text()
                        
                        if (item0 == searchValue[0] and item1 == searchValue[1])and(item == searchValue[2] or item2 == searchValue[3]):
                            for j in range(4):
                                self.modellist.item(idx,j).setBackground(QtGui.QColor(255,0,0))


                    self.core.SetModel2(kwargs)
                else:
                    for idx in range(self.modellist.rowCount()):
                        item = self.modellist.item(idx, 3)
                        item1 = self.modellist.item(idx, 1)
                        item2 = self.modellist.item(idx, 2)
                        item0 = self.modellist.item(idx, 0)
                        if (item0 == searchValue[0] and item1 == searchValue[1])and(item == searchValue[2] or item2 == searchValue[3]):

                            for j in range(4):
                                self.modellist.item(idx,j).setBackground(QtGui.QColor(0,255,0))

                    self.core.SetModel(kwargs)
            

    def Remove(self, e):
        items = self.modellist.selectionModel().selectedRows()
        for item_selected in items:
                #try to use the table for selection

                section = str(self.modellist.item(item_selected.row(), 0).text())
                    #
                segment = str(self.modellist.item(item_selected.row(), 1).text())
                chan = str(self.modellist.item(item_selected.row(), 2).text())
                morph=""
                par = str(self.modellist.item(item_selected.row(), 3).text())
                if chan == "morphology":
                    chan = "None"
                    par= "None"
                    morph = str(self.modellist.item(item_selected.row(), 3).text())

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
                    self.remover.setEnabled(False )
                searchValue = [kwargs["section"], kwargs["segment"], kwargs["params"], kwargs["morph"]]
                for idx in range(self.modellist.rowCount()):
                    item = self.modellist.item(idx, 3).text()
                    item1 = self.modellist.item(idx, 1).text()
                    item2 = self.modellist.item(idx, 2).text()
                    item0 = self.modellist.item(idx, 0).text()
                    if (item0 == searchValue[0] and item1 == searchValue[1])and(item == searchValue[2] or item2 == searchValue[3]):
                        for j in range(4):
                                    self.modellist.item(idx,j).setBackground(QtGui.QColor(255,255,255))



    def sim_plat(self):
        if self.dd_type.currentIndex():
            self.sim_path.setEnabled(True)
            self.pushButton_13.setText(QtCore.QCoreApplication.translate("Optimizer", "Set"))
            self.pushButton_14.setEnabled(False)
            self.pushButton_15.setEnabled(False)
            self.pushButton_16.setEnabled(False)
            self.setter.setEnabled(False)
            self.remover.setEnabled(False)
            self.modellist.setEnabled(False)
            self.lineEdit_file2.setEnabled(False)
            self.lineEdit_folder2.setEnabled(False)
        else:
            self.pushButton_13.setText(QtCore.QCoreApplication.translate("Optimizer", "Load"))
            self.sim_path.setEnabled(False)
            self.pushButton_14.setEnabled(True)
            self.pushButton_15.setEnabled(True)
            self.pushButton_16.setEnabled(True)
            self.setter.setEnabled(True)
            self.remover.setEnabled(True)
            self.modellist.setEnabled(True)
            self.lineEdit_file2.setEnabled(True)
            self.lineEdit_folder2.setEnabled(True   )


    def Load2(self, e):

        self.model_file = self.lineEdit_file2.text()
        self.spec_file = self.lineEdit_folder2.text()
        try:
            self.core.LoadModel({"model" : [self.model_file, self.spec_file],
                                 "simulator" : self.dd_type.currentText(),
                                 "sim_command" : self.sim_path.text()})
            self.core.model_handler.load_neuron()
            temp = self.core.model_handler.GetParameters()
            
            if temp!=None:
                out = open("model.txt", 'w')

                for i in temp:
                    out.write(str(i))
                    out.write("\n")
                self.modellist.setRowCount(len(temp[0][1]))
                for row in temp:
                    #self.model.InsertStringItem(index,row[0])
                    #print row[1]
                    for k in (row[1]):
                        if k != []:
                            #.model.InsertStringItem(index, row[0])
                            #self.model.SetStringItem(index, 2, k[0])
                            for index,s in enumerate(k[2]):
                                self.modellist.setItem(index, 0, QTableWidgetItem(row[0]))
                                self.modellist.setItem(index, 1, QTableWidgetItem(str(k[0])))
                                self.modellist.setItem(index, 2, QTableWidgetItem(k[1]))
                                self.modellist.setItem(index, 3, QTableWidgetItem(s))
            else:
                pass

        except OSError as oe:
            print(oe)
        
        tmp=self.core.ReturnSections()
        self.spinBox_16.addItems(tmp)
        self.spinBox_9.addItems(tmp)



    def UF(self):
        self.SW = SecondWindow() 
        self.SW.setObjectName("Optimizer")
        self.SW.resize(500, 500)
        self.SW.show()

    def amplitudes_fun(self):
        self.SiW = StimuliWindow() 
        self.SiW.setObjectName("Optimizer")
        self.SiW.resize(400, 500)
        self.SiW.show()

    
    def fitselect(self):
        items = self.fitlist.selectionModel().selectedIndexes()
        for item_selected in items:
            if item_selected.column()==0:
                current_item=str(self.fitlist.item(item_selected.row(), 0).text())
                if current_item in self.fitset:
                    self.fitlist.item(item_selected.row(),0).setBackground(QtGui.QColor(255,255,255))
                    self.fitset.remove(current_item)
                else:
                    self.fitlist.item(item_selected.row(),0).setBackground(QtGui.QColor(0,255,0))
                    self.fitset.add(current_item)

    def fitchanged(self):
        self.weights=[]
        try:
            allRows = self.fitlist.rowCount()
            for row in range(0,allRows):
                current_fun=str(self.fitlist.item(row, 0).text())
                if current_fun in self.fitset:
                    current_weight=str(self.fitlist.item(row, 1).text())
                    self.weights.append(float(current_weight))
        except:
            self.fitlist.item(row, 1).setText("0")
        

    def Normalize(self, e):
        try:
            sum_o_weights = sum(self.weights)
            allRows = self.fitlist.rowCount()
            for row in range(0,allRows):
                current_fun=str(self.fitlist.item(row, 0).text())
                if current_fun in self.fitset:
                    current_weight=str(self.fitlist.item(row, 1).text())
                    try:
                        self.fitlist.item(row, 1).setText(str(float(current_weight) / sum_o_weights))
                    except ValueError:
                        continue
                else:
                    try:
                        self.fitlist.item(row, 1).setText("0")
                    except ValueError:
                        continue
        except:
            popup("Wrong values given")


    def algoselect(self):
        selected_algo = self.algolist.selectionModel().selectedRows()
        aspects=self.algo_dict.get(str(self.algolist.item(selected_algo[0].row(), 0).text()))
        self.aspectlist.setRowCount(len(aspects)+1)
        item = QTableWidgetItem('Seed')
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )      
        self.aspectlist.setItem(0, 0, item)
        item2 = QTableWidgetItem('1234')   
        self.aspectlist.setItem(0, 1, item2)
        for index,elems in enumerate(aspects):
            key=next(iter(elems))
            item = QTableWidgetItem(key)
            item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )      
            self.aspectlist.setItem(index+1, 0, item)
            item2 = QTableWidgetItem(str(elems.get(key)))   
            self.aspectlist.setItem(index+1, 1, item2)


    def aspect_changed(self):
        try:
            selected_algo = self.algolist.selectionModel().selectedRows()
            selected_asp = self.aspectlist.selectionModel().selectedIndexes()
            if selected_asp[0].row():
                self.algo_dict[str(self.algolist.item(selected_algo[0].row(), 0).text())][selected_asp[0].row()-1][str(self.aspectlist.item(selected_asp[0].row(), 0).text())]=float(self.aspectlist.item(selected_asp[0].row(), 1).text())#][str(self.aspectlist.item(asps.row(), 0).text())])
                self.aspectlist.clearSelection()
        except:
            "ok"


    def runsim(self): 
        err=[]
        errpop=[]
        try:
            self.core.SecondStep({"stim" : [str(self.stimprot.currentText()), float(self.lineEdit_pos.text()), str(self.spinBox_16.currentText())],
                                  "stimparam" : [self.SiW.container, float(self.lineEdit_delay.text()), float(self.lineEdit_duration.text())]})
            self.kwargs = {"runparam":[float(self.lineEdit_tstop.text()),
                                    float(self.lineEdit_dt.text()),
                                    str(self.spinBox_15.currentText()),
                                    str(self.spinBox_9.currentText()),
                                    float(self.lineEdit_posins.text()),
                                    float(self.lineEdit_initv.text())]}
        except AttributeError:
            err.append(2)
            errpop.append("No stimulus amplitude was selected!")
        except ValueError:
            errpop.append('Some of the cells are empty. Please fill out all of them!')
            err.append(2)
        except:
            err.append(2)
            errpop.append("Error")

        try:
            if self.core.option_handler.type[-1]!="features":
                self.kwargs.update({"feat":
                                    [{"Spike Detection Thres. (mv)": float(self.spike_tresh.text()), "Spike Window (ms)":float(self.spike_window.text())},
                                    [x for x in self.my_list if x in self.fitset]]
                                    })
                self.kwargs.update({"weights" : self.weights})
            else:
                self.my_list=self.core.data_handler.features_data.keys()[3:-1]
                self.kwargs.update({"feat":
                                    [{"Spike Detection Thres. (mv)": float(self.spike_tresh.text()), "Spike Window (ms)":float(self.spike_window.text())},
                                    [x for x in self.my_list if x in self.fitset]]
                                    })
                self.kwargs.update({"weights" : self.weights})
            if not(0.99<sum(self.kwargs["weights"])<=1.01):
                errpop.append("You did not normalize your weights!\nDo you want to continue?")
        except:
            err.append(3)
            errpop.append("Fitness Values not right")
        
        try:
            """
            allRows = self.aspectlist.rowCount()
            for row in range(0,allRows):
                print(self.aspectlist.item(row,1).text())
            """
            selected_algo = self.algolist.selectionModel().selectedRows()
            algo_name=str(self.algolist.item(selected_algo[0].row(), 0).text())
            tmp = {"seed" : int(self.aspectlist.item(0,1).text()),
                "evo_strat" : str(algo_name)
                }
            #for n in self.algo_param:
                #tmp.update({str(n[1]) : float(n[0].GetValue())})
            allRows = self.aspectlist.rowCount()
            for row in range(1,allRows):
                tmp.update({str(self.aspectlist.item(row,0).text()):float(self.aspectlist.item(row,1).text())})
            tmp.update({
                "num_params" : len(self.core.option_handler.GetObjTOOpt()),
                "boundaries" : self.BW.core.option_handler.boundaries ,
                "starting_points" : self.seed
                })
            self.kwargs.update({"algo_options":tmp})
        except:
            err.append(4)
            errpop.append("You forget to select an algorithm!")
            
        #try:
        self.core.ThirdStep(self.kwargs)
        #wx.MessageBox('Optimization finished. Press the Next button for the results!', 'Done', wx.OK | wx.ICON_EXCLAMATION)
        if self.core.option_handler.output_level=="1":
            self.core.Print()
        self.seed = None
        """except sizeError as sE:
            err.append(4)
            errpop.append("There was an error during the optimization: "+sE.m)
        except:
            err.append(4)
            errpop.append("There was an error:")"""
        if err:
            popup(errpop[0])
            self.tabwidget.setCurrentIndex(int(min(err)))


    def boundarywindow(self):
        self.BW = BoundaryWindow() 
        self.BW.setObjectName("Optimizer")
        self.BW.resize(400, 500)
        self.BW.show()

    def startingpoints(self):
        num_o_params=len(self.core.option_handler.GetObjTOOpt())
        seeds = []
        self.SPW = startingpoints(self,num_o_params,seeds) 
        self.SPW.setObjectName("Optimizer")
        self.SPW.resize(400, 500)
        self.SPW.show()
        self.seed = seeds

    
class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        super(SecondWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.core=Core.coreModul()
        self.plaintext = QtWidgets.QPlainTextEdit(self)
        self.plaintext.insertPlainText("#Please define your function below in the template!\n"+
                "#You may choose an arbitrary name for your function,\n"+
                "#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\n"+
                "#In the second line you may specify the names of the parameters in a comment, separated by spaces.\n")
        self.plaintext.move(10,10)
        self.plaintext.resize(350,400)
        self.pushButton_45 = QtWidgets.QPushButton(self)
        self.pushButton_45.setGeometry(QtCore.QRect(370, 30, 80, 22))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_45.setText(_translate("Ufun", "Load"))
        self.pushButton_45.clicked.connect(self.loaduserfun)
        self.pushButton_46 = QtWidgets.QPushButton(self)
        self.pushButton_46.setGeometry(QtCore.QRect(20, 440, 80, 22))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_46.setText(_translate("Ufun", "Ok"))
        self.pushButton_46.clicked.connect(self.OnOk)
        self.pushButton_47 = QtWidgets.QPushButton(self)
        self.pushButton_47.setGeometry(QtCore.QRect(120, 440, 80, 22))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_47.setText(_translate("Ufun", "Cancel"))
        self.pushButton_47.clicked.connect(self.close)
        


    def loaduserfun(self):    
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Text Files (*.txt);;All Files (*);;", options=options)
        if fileName:
            f = open(fileName, "r")
            fun =   ("#Please define your function below in the template!\n"+
                "#You may choose an arbitrary name for your function,\n"+
                "#but the input parameters must be self and a vector!In the first line of the function specify the length of the vector in a comment!\n"+
                "#In the second line you may specify the names of the parameters in a comment, separated by spaces.\n")
            for l in f:
                fun = fun + l
            self.plaintext.setPlainText(str(fun))
    
    def OnOk(self, e):
        try:
            #print self.string.GetValue()
            self.core.option_handler.u_fun_string = str(self.plaintext.toPlainText())
            self.core.option_handler.adjusted_params=[]
            ui.modellist.setRowCount(0)
            text = ""
            text = list(map(str.strip, str(self.plaintext.toPlainText()).split("\n")))[4:-1]
            variables = []
            variables = list(map(str.strip, str(text[0][text[0].index("(") + 1:text[0].index(")")]).split(",")))
            var_len = int(text[1].lstrip("#"))
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
                self.core.option_handler.SetOptParam(0.1)
                if var_names != None:
                    self.core.option_handler.SetObjTOOpt(var_names[i])
                else:
                    self.core.option_handler.SetObjTOOpt("Vector" + "[" + str(i) + "]")
            if variables[0] == '':
                raise ValueError
            compile(self.plaintext.toPlainText(), '<string>', 'exec')
            self.close()
        except ValueError as val_err:
            popup("Your function doesn't have any input parameters!")
        except SyntaxError as syn_err:
            popup(str(syn_err) +"Syntax Error")
    

class StimuliWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        super(StimuliWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.core=Core.coreModul()
        self.amplit_edit = QtWidgets.QLineEdit(self)
        self.amplit_edit.setGeometry(QtCore.QRect(120, 10, 61, 22))
        self.amplit_edit.setObjectName("amplit_edit")
        self.label_amplit = QtWidgets.QLabel(self)
        self.label_amplit.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.container = []
        self.label_amplit.setFont(font)
        self.label_amplit.setObjectName("label_amplit")
        self.label_amplit.setText(_translate("Optimizer", "Number of stimuli:"))
        self.pushButton_create = QtWidgets.QPushButton(self)
        self.pushButton_create.setGeometry(QtCore.QRect(250, 10, 61, 21))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_create.setText(_translate("Optimizer", "Create"))
        self.pushButton_create.clicked.connect(self.Set)
        self.pushButton_accept = QtWidgets.QPushButton(self)
        self.pushButton_accept.setGeometry(QtCore.QRect(200, 450, 61, 21))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_accept.setText(_translate("Optimizer", "Create"))
        self.pushButton_accept.clicked.connect(self.Accept)
        self.pushButton_accept.setEnabled(False)
        
        #if self.core.option_handler.type[-1]=="features":
        #    self.number.SetValue((str(len(self.core.data_handler.features_data["stim_amp"]))))
        #    self.Set(self) 

    def Set(self, e):
        try:
            self.temp = []
            hstep = 200
            vstep = 35
            hoffset = 10
            voffset = 50
            unit="nA" if ui.dd_type.currentText()==0 else "mV"
            for l in range(min(10, int(self.amplit_edit.text()))):
                label = QtWidgets.QLabel(self)
                label.setGeometry(QtCore.QRect(hoffset, voffset + l * vstep, 121, 16))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setPointSize(10)
                font.setBold(False)
                font.setWeight(50)
                label.setFont(font)
                label.setObjectName("label_amplit")
                label.setText(QtCore.QCoreApplication.translate("Optimizer", "Amplitude" + str(l+1) + " ("+unit+"):"))
                amplitude_edit = QtWidgets.QLineEdit(self)
                amplitude_edit.setGeometry(QtCore.QRect(hstep / 2+25, voffset + l * vstep, 61, 22))
                amplitude_edit.setObjectName("amplitude_edit")
                label.show()
                amplitude_edit.show()
                #wx.StaticText(self.panel, label="Amplitude" + str(l+1) + " ("+unit+"):", pos=(hoffset, voffset + l * vstep))
                #tmp_obj = wx.TextCtrl(self.panel, id=l, pos=(hstep / 2+25, voffset + l * vstep), size=(75, 30))
                #if self.core.option_handler.type[-1]=="features":
                #    amplitude_edit.setText(str(self.core.data_handler.features_data["stim_amp"][l]))

                self.temp.append(amplitude_edit)
            self.pushButton_accept.setEnabled(True)
        except:
            self.close()
        


    def Accept(self, e):
        for n in range(len(self.temp)):
            self.container.append(float(self.temp[n].text()))
        self.close()

    
class BoundaryWindow(QtWidgets.QMainWindow):
    def __init__(self): 
        super(BoundaryWindow, self).__init__()
        _translate = QtCore.QCoreApplication.translate
        self.core=Core.coreModul()
        hstep = 130
        vstep = 35
        hoffset = 10
        voffset = 15
        self.min = []
        self.max = []

        for l in range(len(ui.core.option_handler.GetObjTOOpt())):
            param=ui.core.option_handler.GetObjTOOpt()[l].split()
            if len(param)==4:
                label=param[0] + " " + param[1] + " " + param[3]
            else:
                if param[0]!=param[-1]:
                    label=param[0] + " " + param[-1]
                else:
                    label=param[-1]
           
            lbl = QtWidgets.QLabel(self)
            lbl.setGeometry(QtCore.QRect(hoffset, voffset + l * vstep, 121, 16))
            font = QtGui.QFont()
            font.setFamily("Ubuntu")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            lbl.setFont(font)
            lbl.setObjectName("tmp_min")
            lbl.setText(QtCore.QCoreApplication.translate("Optimizer", label))

            tmp_min = QtWidgets.QLineEdit(self)
            tmp_min.setGeometry(QtCore.QRect(hstep, voffset + l * vstep, 61, 22))
            tmp_min.setObjectName("tmp_min")
            tmp_max = QtWidgets.QLineEdit(self)
            tmp_max.setGeometry(QtCore.QRect(hstep + hstep/1.5, voffset + l * vstep, 61, 22))
            tmp_max.setObjectName("tmp_min")
            lbl.show()
            tmp_min.show()
            self.min.append(tmp_min)
            self.max.append(tmp_max)
            if len(ui.core.option_handler.boundaries[1]) == len(ui.core.option_handler.GetObjTOOpt()):
                tmp_min.SetValue(str(self.par.core.option_handler.boundaries[0][l]))
                tmp_max.SetValue(str(self.par.core.option_handler.boundaries[1][l]))
        
        Setbutton = QtWidgets.QPushButton(self)
        Setbutton.setGeometry(QtCore.QRect(10, 400, 80, 22))
        Setbutton.setObjectName("Setbutton")
        Setbutton.setText(_translate("Optimizer", "Set"))
        Setbutton.clicked.connect(self.Set)
        Savebutton = QtWidgets.QPushButton(self)
        Savebutton.setGeometry(QtCore.QRect(100, 400, 80, 22))
        Savebutton.setObjectName("Savebutton")
        Savebutton.setText(_translate("Optimizer", "Save"))
        Savebutton.clicked.connect(self.Save)
        Loadbutton = QtWidgets.QPushButton(self)
        Loadbutton.setGeometry(QtCore.QRect(190, 400, 80, 22))
        Loadbutton.setObjectName("Savebutton")
        Loadbutton.setText(_translate("Optimizer", "Load"))
        Loadbutton.clicked.connect(self.Load)
        self.save_file_name="boundaries.txt"

    def Set(self, e):
        try:
            self.core.option_handler.boundaries[0] = [float(n.text()) for n in self.min]
            self.core.option_handler.boundaries[1] = [float(n.text()) for n in self.max]
        except ValueError:
            
            
            popup("Invalid Value")
            

        else:
            for i in range(len(self.core.option_handler.boundaries[0])):
                if self.core.option_handler.boundaries[0][i] >= self.core.option_handler.boundaries[1][i] :
                    
                    
                    popup("""Min boundary must be lower than max
                                Invalid Values""")
                    
                    break
        self.close()

    def Save(self,e):
        try:    
            name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
            if name[0]:
                f = open(name,'w')
                for _min,_max in zip(self.min,self.max):
                    f.write(str(_min.text()))
                    f.write("\t")
                    f.write(str(_max.text()))
                    f.write("\n")
                f.close()
        except IOError:
            
            
            popup("Error writing the file!")
            

    def Load(self,e):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Text Files (*.txt);;All Files (*);;", options=options)
        if fileName:
            try:
                f = open(fileName, "r")
                for idx,l in enumerate(f):
                    bounds=l.split()
                    self.min[idx].setText(bounds[0])
                    self.max[idx].setText(bounds[1])
            except IOError:
                popup("Error reading the file!")
                


class startingpoints(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(startingpoints,self).__init__()
        _translate = QtCore.QCoreApplication.translate
        n_o_params=args[1]
        self.container=[]
        self.vals=args[2]
        hstep = 130
        vstep = 35
        hoffset = 10
        voffset = 15
        for n in range(n_o_params):
            param=ui.core.option_handler.GetObjTOOpt()[n].split()
            if len(param)==4:
                p_name=param[0] + " " + param[1] + " " + param[3]
            else:
                if param[0]!=param[-1]:
                    p_name=param[0] + " " + param[-1]
                else:
                    p_name=param[-1]
            #p_name=self.parent.core.option_handler.GetObjTOOpt()[n].split()[-1]
            lbl = QtWidgets.QLabel(self)
            lbl.setGeometry(QtCore.QRect(hoffset, voffset + n * vstep, 121, 16))
            font = QtGui.QFont()
            font.setFamily("Ubuntu")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            lbl.setFont(font)
            lbl.setObjectName("ctrl")
            lbl.setText(QtCore.QCoreApplication.translate("Optimizer", lbl))

            ctrl = QtWidgets.QLineEdit(self)
            ctrl.setGeometry(QtCore.QRect(hstep, voffset + n * vstep, 61, 22))
            ctrl.setObjectName("ctrl")
            lbl.show()
            ctrl.show()
            self.container.append(ctrl)

        Okbutton = QtWidgets.QPushButton(self)
        Okbutton.setGeometry(QtCore.QRect(10, 400, 80, 22))
        Okbutton.setObjectName("Okbutton")
        Okbutton.setText(_translate("Optimizer", "Ok"))
        Okbutton.clicked.connect(self.OnOk)
        Closebutton = QtWidgets.QPushButton(self)
        Closebutton.setGeometry(QtCore.QRect(100, 400, 80, 22))
        Closebutton.setObjectName("Closebutton")
        Closebutton.setText(_translate("Optimizer", "Cancel"))
        Closebutton.clicked.connect(self.close)
        Loadpopbutton = QtWidgets.QPushButton(self)
        Loadpopbutton.setGeometry(QtCore.QRect(280, 400, 80, 22))
        Loadpopbutton.setObjectName("Loadpopbutton")
        Loadpopbutton.setText(_translate("Optimizer", "Load Population"))
        Loadpopbutton.clicked.connect(self.OnLoadPop)
        Loadbutton = QtWidgets.QPushButton(self)
        Loadbutton.setGeometry(QtCore.QRect(190, 400, 80, 22))
        Loadbutton.setObjectName("Loadbutton")
        Loadbutton.setText(_translate("Optimizer", "Load Point"))
        Loadbutton.clicked.connect(self.OnLoad)

        

    def OnOk(self,e):
        try:
            for n in self.container:
                self.vals.append(float(n.text()))
        except ValueError:
            
            
            popup("""You must give every parameter an initial value!
                        Error""")
            

    def OnLoad(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Text Files (*.txt);;All Files (*);;", options=options)
        if fileName:
            try:
                f = open(fileName, "r")
                for idx, l in enumerate(f):
                    self.container[idx].SetValue(str(l))
            except IOError:
                
                
                popup("Error")
                
    
    def OnLoadPop(self,e):
        self.size_of_pop = 0
        file_path = ""
        popup("This function is only supported by the algorithms from inspyred!")
        
        text, ok = QInputDialog.getText(self, 'TLoad Population', 'Enter size of population:')
        if ok:
            self.size_of_pop = int(text)
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Text Files (*.txt);;All Files (*);;", options=options)
               

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
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Optimizer = QtWidgets.QMainWindow()
    ui = Ui_Optimizer()
    ui.setupUi(Optimizer)
    Optimizer.show()
    sys.exit(app.exec_())

