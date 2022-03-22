import os
import glob
import numpy as np
import pandas as pd
import pyqtgraph as pg
import random

import scipy as sp
import scipy.spatial

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

from sklearn import mixture
from matplotlib.path import Path

#__________________________________________________________________________
#_________________________User defined Paths:______________________________
# 
# path_to_data = paths to the .pkl files created in Step0 and 
#                the * makes it so all .pkl files in the folder are grabed.
#
# output_path = path to output folder.

paths_to_data = "/Users/raul/Documents/GitHub/ColonySelector/test_data/*.pkl"
output_path = "/Users/raul/Documents/GitHub/ColonySelector/example_output/"


#__________________________________________________________________________
#__________________________________________________________________________



class Ui_MainWindow(object):

    def __init__(self, paths_to_data, output_path):
        
        self.paths_to_data = glob.glob(paths_to_data)
        self.numberpath = 0
        self.output_path = output_path
        self.filename = self.paths_to_data[self.numberpath].split('/')[-1]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(963, 1036)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 960, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 960, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 921, 791))
        self.graphicsView.setObjectName("graphicsView")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(470, 820, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 900, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 820, 71, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 850, 71, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 820, 141, 20))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 900, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 820, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 920, 161, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 840, 161, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 930, 71, 24))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 850, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(740, 860, 201, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(840, 910, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(470, 860, 130, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 900, 161, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(250, 860, 161, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 860, 81, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(470, 900, 251, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 920, 131, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 970, 441, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 0, 921, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        #remove x and y axis
        self.graphicsView.getPlotItem().hideAxis('bottom')
        self.graphicsView.getPlotItem().hideAxis('left')
        self.graphicsView.setAspectLocked(True)


        # Initialize 
        self.lineEdit.setText('7')
        self.lineEdit_2.setText('6')
        self.lineEdit_3.setText('42')
        self.pushButton.setEnabled(False)
        self.z = int(self.lineEdit_3.text())
        self.keep_points = []
        self.mouse_x = []
        self.mouse_y = []


        # Set up data
        data   = pd.read_pickle(self.paths_to_data[self.numberpath])
        self.X = data.to_numpy()
        self.labels = [0]*len(self.X[:,0])
        self.colonyID = [0]*len(self.X[:,0])

        # First plot
        self.PLOT = self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)
        
        # Use this plot for all the x y coord
        self.proxy = pg.SignalProxy(self.PLOT.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_position)


        # User actions
        self.pushButton.clicked.connect(lambda:self.Back())
        self.pushButton_2.clicked.connect(lambda:self.Next())
        
        self.pushButton_3.clicked.connect(lambda:self.Refresh())
        self.pushButton_4.clicked.connect(lambda:self.Clean())

        self.pushButton_6.clicked.connect(lambda:self.plot_predicted()) #plot predicted
        self.pushButton_9.clicked.connect(lambda:self.Estimate())


        self.pushButton_8.clicked.connect(lambda:self.Save())

        # basic Key shortcut
        self.shortcutA = QtWidgets.QShortcut(QtGui.QKeySequence('A'), MainWindow)
        self.shortcutD = QtWidgets.QShortcut(QtGui.QKeySequence('D'), MainWindow)
        self.shortcutA.activated.connect(lambda shortcut_key=self.shortcutA.key().toString(): self.displayKeysA(shortcut_key))
        self.shortcutD.activated.connect(lambda shortcut_key=self.shortcutD.key().toString(): self.displayKeysD(shortcut_key))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.label_7.setText(_translate("MainWindow", "Step 2: Cluster colonies"))
        self.pushButton_4.setText(_translate("MainWindow", "Clean"))
        self.label_2.setText(_translate("MainWindow", "Neighbors:"))
        self.label_4.setText(_translate("MainWindow", "How many neighboring"))
        self.label_3.setText(_translate("MainWindow", "Magnitude:"))
        self.label.setText(_translate("MainWindow", "Step 1: Clean"))
        self.label_5.setText(_translate("MainWindow", "(orders of magnitude)"))
        self.label_6.setText(_translate("MainWindow", "cells to calculate the "))
        self.pushButton_3.setText(_translate("MainWindow", "Plot"))
        self.pushButton_6.setText(_translate("MainWindow", "Plot predicted colonies"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.pushButton_9.setText(_translate("MainWindow", "Estimate colonies"))
        self.label_8.setText(_translate("MainWindow", "Threshold for the distance"))
        self.label_9.setText(_translate("MainWindow", "distance "))
        self.label_10.setText(_translate("MainWindow", "Automatically estimate colonies or "))
        self.label_11.setText(_translate("MainWindow", "write your own guess"))
        self.label_12.setText(_translate("MainWindow", "Hotkeys:    Shift = Circle colony        A = Accept colony        D = Delete"))
        self.label_13.setText(_translate("MainWindow", self.filename))



    #---------- Back/Next ------------

    def Back(self):

        if self.numberpath != 0:
            self.pushButton_2.setEnabled(True)
            
            # Set up previous data
            self.numberpath = self.numberpath - 1
            data   = pd.read_pickle(self.paths_to_data[self.numberpath])
            self.X = data.to_numpy()
            self.graphicsView.clear()
            self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)

        if self.numberpath == 0:
            self.pushButton.setEnabled(False)

        self.filename = self.paths_to_data[self.numberpath].split('/')[-1]
        _translate = QtCore.QCoreApplication.translate
        self.label_13.setText(_translate("MainWindow", self.filename))


    def Next(self):

        if self.numberpath != len(self.paths_to_data)-1:
            self.pushButton.setEnabled(True)

            # Set up next data
            self.numberpath = self.numberpath + 1
            print(self.numberpath)
            data   = pd.read_pickle(self.paths_to_data[self.numberpath])
            self.X = data.to_numpy()
            self.graphicsView.clear()
            self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)

        if self.numberpath == len(self.paths_to_data)-1:
            self.pushButton_2.setEnabled(False)

        self.filename = self.paths_to_data[self.numberpath].split('/')[-1]
        _translate = QtCore.QCoreApplication.translate
        self.label_13.setText(_translate("MainWindow", self.filename))


    #---------- Step1 ------------

    def Refresh(self):

        self.graphicsView.clear()
        self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)

        nearest_n  = int(self.lineEdit.text())#7 # how many neighboring cells to calculate distance
        threshhold = 1*10**int(self.lineEdit_2.text())#6 # squared sum ucledean distance

        points = self.X
        distances = sp.spatial.distance.cdist(points,points)

        # An element is not its own nearest neighbor
        np.fill_diagonal(distances, np.inf)

        # Find the index of each element's nearest neighbor
        mins = distances.argmin(0)

        idx = np.argpartition(distances, kth=nearest_n, axis=-1)
        distances_hold = np.take_along_axis(distances, idx, axis=-1)
        distances_hold = distances_hold[:,:nearest_n]
        dense_points   = points[np.sum(distances_hold**2, axis=1)<threshhold]

        
        self.X_clean = dense_points
        self.graphicsView.plot(self.X_clean[:,0], self.X_clean[:,1],pen=None, symbol='o', symbolPen='g', symbolSize=5)


    def Clean(self):
        self.graphicsView.clear()
        self.X = self.X_clean
        self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)


    #---------- Step2 ------------

    def Estimate(self):
        self.graphicsView.clear()
        self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)

        n_max = 100
        n = 0
        n_components = np.arange(0, n_max)
        models = []
        while n < n_max:
            n +=1
            if n > 3:
                if models[-2] > models[-1]:
                    models.append(mixture.GaussianMixture(n, covariance_type='full', random_state=0).fit(self.X).bic(self.X))
                else:
                    models.append(mixture.GaussianMixture(n, covariance_type='full', random_state=0).fit(self.X).bic(self.X))
                    if models[-2] < models[-1]:
                        break
            else:
                models.append(mixture.GaussianMixture(n, covariance_type='full', random_state=0).fit(self.X).bic(self.X))

        self.lineEdit_3.clear()
        self.lineEdit_3.setText(str(n_components[models.index(min(models))]))

    def plot_predicted(self):

        self.graphicsView.clear()
        self.z = int(self.lineEdit_3.text())


        gmm = mixture.GaussianMixture(n_components=self.z,random_state = 0)
        gmm.fit(self.X)
        self.labels = gmm.predict(self.X)
        self.colonyID = gmm.predict(self.X)



        new_label = []
        for label in self.labels:
            new_label.append(pg.intColor(label,self.z))
        self.labels = new_label

        self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        self.scatter_plot_item.clear()
        self.scatter_plot_item.setData(pos=self.X, brush=self.labels)


        self.graphicsView.clear()
        self.graphicsView.addItem(self.scatter_plot_item)

    def mouse_position(self,e):

        pos = e[0]
        mousePoint = self.graphicsView.getPlotItem().vb.mapSceneToView(pos)
        modifiers = QtWidgets.QApplication.keyboardModifiers()

        if modifiers == QtCore.Qt.ShiftModifier:
            self.mouse_x.append(mousePoint.x())
            self.mouse_y.append(mousePoint.y())
            self.graphicsView.plot(self.mouse_x, self.mouse_y)


    def displayKeysA(self,mapping):
        self.keep_points = 'Good'
        self.define_colonies()

    def displayKeysD(self,mapping):
        self.keep_points = 'Delete'
        self.define_colonies()

    def define_colonies(self):

        points = np.vstack((self.X[:,0], self.X[:,1])).T 
        lasso  = np.vstack((self.mouse_x, self.mouse_y)).T 
        p = Path(lasso) # make a polygon
        grid = p.contains_points(points)

        #random color for new label
        new_color = pg.mkColor(random.choice(['w','#E6DAA6','#06C2AC','#6E750E','#FF7F50','#054907','#380282','#C79FEF','#FF4500','#069AF3','#ADD8E6','#90EE90']))

        newID = 1 + np.max(self.colonyID)

        for i,m in enumerate(grid):
            if m == True:
                if self.keep_points == 'Good':
                    self.labels[i] = new_color
                    self.colonyID[i] = newID
                if self.keep_points == 'Delete':
                    self.labels[i] = pg.mkColor('#808080')
                    self.colonyID[i] = -1

        self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        self.scatter_plot_item.clear()
        self.scatter_plot_item.setData(pos=self.X, brush=self.labels)
        self.graphicsView.clear()
        self.graphicsView.addItem(self.scatter_plot_item)

        self.mouse_x = []
        self.mouse_y = []

    def Save(self):

        d = {'x':self.X[:,0],'y':self.X[:,1],'color':self.labels,'colonyID':self.colonyID}
        data_save = pd.DataFrame(data=d)
        data_save.to_pickle(self.output_path + "clean_" + self.filename)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow( paths_to_data, output_path)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


