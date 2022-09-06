# Script for ColonySelectorGui
# Go to https://github.com/SydShafferLab/ColonySelector/wiki for more details.

# Variables:

#   paths_to_data = path/to/pkl_folder/*.pkl  #XY columns 

#     output_path = path/to/output_folder/ 


# paths_to_images = "path/to/images/"  #images have to be .jpg or .tif
#                   image and name of pkl file must be the same!
#                   "" leave empty if you don't want to use images.

#   is_tif_or_jpg = ".jpg" or ".tif" # is the image in ".jpg" or ".tif" format




import os
import glob
import numpy as np
import pandas as pd
import pyqtgraph as pg
import random

import scipy as sp
import scipy.spatial
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import pdist

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget

from sklearn import mixture
from matplotlib.path import Path
from PIL import Image , ImageEnhance, ImageOps
Image.MAX_IMAGE_PIXELS = 1000000000

#__________________________________________________________________________
#_________________________User defined Paths:______________________________

paths_to_data = "/Users/raul/Documents/GitHub/ColonySelector/test_data/*.pkl"

output_path = "/Users/raul/Documents/GitHub/ColonySelector/example_output/"

# image and name of pkl file must be the same or leave empty ""
paths_to_images = ""#"/Users/raul/Documents/GitHub/ColonySelector/test_data/" # 

is_tif_or_jpg = ".jpg" # is the image in ".jpg" or ".tif" format




#__________________________________________________________________________
#_________________Checking whether folder/directory exists_________________


#define funtion to determine if folder exist
def does_folder_exist(path_to_folder):
    if not os.path.exists(path_to_folder):
        os.mkdir(path_to_folder)
    # else:
    #     raise Exception("folder {} already exists".format(path_to_folder))

does_folder_exist(output_path)




#__________________________________________________________________________
#__________________________________________________________________________



class Ui_MainWindow(object):

    def __init__(self, paths_to_data, output_path):

        self.paths_to_data = glob.glob(paths_to_data)

        self.numberpath = 0
        self.output_path = output_path
        self.filename = self.paths_to_data[self.numberpath].split('/')[-1]


        self.filename_image = paths_to_images + self.filename.split('.')[0] + is_tif_or_jpg#tif"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Count Ya Colonies!")
        if paths_to_images != "":
            MainWindow.resize(1899, 1036)
        else:
            MainWindow.resize(970, 1036)

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
        self.label_7.setGeometry(QtCore.QRect(550, 820, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 900, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 850, 31, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 850, 71, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 840, 281, 20))
        self.label_4.setObjectName("label_4")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 900, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 820, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 900, 71, 24))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 850, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(840, 850, 101, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(840, 900, 101, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(690, 900, 100, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 900, 311, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 860, 200, 20))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(700, 850, 81, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 970, 460, 20))
        self.label_12.setObjectName("label_12")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(275, 990, 441, 20))
        self.label_22.setObjectName("label_22")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 0, 921, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")







        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(960, 0, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 920, 211, 20))
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 850, 120, 20))
        self.label_10.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1899, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        if paths_to_images != "":
            self.graphicsView_2 = PlotWidget(self.centralwidget)
            self.graphicsView_2.setGeometry(QtCore.QRect(960, 20, 921, 791))
            self.graphicsView_2.setObjectName("graphicsView_2")

            self.Flipim = QtWidgets.QPushButton(self.centralwidget)
            self.Flipim.setGeometry(QtCore.QRect(1010, 850, 91, 31))
            self.Flipim.setObjectName("Flipim")
            self.label_11 = QtWidgets.QLabel(self.centralwidget)
            self.label_11.setGeometry(QtCore.QRect(970, 820, 191, 16))
            font = QtGui.QFont()
            font.setPointSize(18)
            self.label_11.setFont(font)
            self.label_11.setObjectName("label_11")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(1120, 850, 281, 20))
            self.label_6.setObjectName("label_6")
            self.label_16 = QtWidgets.QLabel(self.centralwidget)
            self.label_16.setGeometry(QtCore.QRect(1010, 910, 481, 20))
            self.label_16.setObjectName("label_16")
            self.label_17 = QtWidgets.QLabel(self.centralwidget)
            self.label_17.setGeometry(QtCore.QRect(1010, 940, 481, 20))
            self.label_17.setObjectName("label_17")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




        #remove x and y axis
        self.graphicsView.getPlotItem().hideAxis('bottom')
        self.graphicsView.getPlotItem().hideAxis('left')
        self.graphicsView.setAspectLocked(True)

        # Initialize
        self.lineEdit.setText('6')
        self.lineEdit_2.setText('2')
        self.lineEdit_3.setText('40')
        self.pushButton.setEnabled(False)
        self.keep_points = []
        self.mouse_x = []
        self.mouse_y = []

        if paths_to_images != "":
            self.graphicsView_2.getPlotItem().hideAxis('bottom')
            self.graphicsView_2.getPlotItem().hideAxis('left')
            self.graphicsView_2.setAspectLocked(True)
            self.graphicsView_2.setYLink(self.graphicsView)
            self.graphicsView_2.setXLink(self.graphicsView)

            # Img
            im = Image.open(self.filename_image)

            # differnt way to contrast image
            #scale_value=50
            #im = ImageEnhance.Contrast(im).enhance(scale_value)
            self.im = im


            pixvals = np.asarray(im)
            minval = np.percentile(pixvals, 2)
            maxval = np.percentile(pixvals, 90)
            pixvals = np.clip(pixvals, minval, maxval)
            pixvals = ((pixvals - minval) / (maxval - minval)) * 255
            img_x,img_y = pixvals.shape

            im = pg.ImageItem(pixvals)
            im.setZValue(-100)
            self.graphicsView_2.addItem(im)
            
            

            r1 = pg.ROI([0,0], [img_x,img_y], resizable=False, removable=True)
            r1.addRotateHandle([1,0], [0.5, 0.5])
            r1.addRotateHandle([0,1], [0.5, 0.5])
            im.setParentItem(r1)
            self.graphicsView_2.addItem(r1)
            self.r1 = r1
            self.flip_num = 0
            self.flip_next = 0

        self.new_color_tracker = 0 

        # Set up data
        data   = pd.read_pickle(self.paths_to_data[self.numberpath])

        if len(data.columns) < 3:
            self.X = data.to_numpy()

            self.labels = [0]*len(self.X[:,0])
            self.colonyID = [0]*len(self.X[:,0])
        else:
            self.X = data.to_numpy()
            
            self.labels = self.X[:,2]
            self.colonyID = self.X[:,3]
            self.X = self.X[:,0:2]

        # First plot
        self.PLOT = self.graphicsView.plot(self.X[:,0], self.X[:,1] ,pen=None, symbol='o', symbolPen=None, symbolSize=5)

        # Use this plot for all the x y coord
        self.proxy = pg.SignalProxy(self.PLOT.scene().sigMouseMoved, rateLimit=60, slot=self.mouse_position)

        # determine distance 
        self.lineEdit.setText(str(np.floor(np.mean(pdist(self.X, 'euclid'))/100 ) ) )

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

        self.shortcutW = QtWidgets.QShortcut(QtGui.QKeySequence('W'), MainWindow)
        self.shortcutR = QtWidgets.QShortcut(QtGui.QKeySequence('R'), MainWindow)
        self.shortcutW.activated.connect(lambda shortcut_key=self.shortcutA.key().toString(): self.displayKeysW(shortcut_key))
        self.shortcutR.activated.connect(lambda shortcut_key=self.shortcutD.key().toString(): self.displayKeysR(shortcut_key))


        if paths_to_images != "":
            # Flip image
            self.Flipim.clicked.connect(lambda:self.fun_flip())


    def fun_flip(self):

        
        if self.flip_next != 1:
            self.flip_num = self.flip_num + 1

        if np.mod(self.flip_num,2) == 1:
            self.graphicsView_2.clear()

            self.im = ImageOps.flip(self.im)
            pixvals = np.asarray(self.im )
            minval = np.percentile(pixvals, 2)
            maxval = np.percentile(pixvals, 90)
            pixvals = np.clip(pixvals, minval, maxval)
            pixvals = ((pixvals - minval) / (maxval - minval)) * 255
            img_x,img_y = pixvals.shape
            im = pg.ImageItem(pixvals)


            im.setZValue(-100)


            self.graphicsView_2.addItem(im)
            im.setParentItem(self.r1)

        else:
            self.graphicsView_2.clear()

            pixvals = np.asarray(self.im)
            minval = np.percentile(pixvals, 2)
            maxval = np.percentile(pixvals, 90)
            pixvals = np.clip(pixvals, minval, maxval)
            pixvals = ((pixvals - minval) / (maxval - minval)) * 255
            img_x,img_y = pixvals.shape
            im = pg.ImageItem(pixvals)

            im.setZValue(-100)

            self.graphicsView_2.addItem(im)
            im.setParentItem(self.r1)

        self.graphicsView_2.addItem(self.r1)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.label_7.setText(_translate("MainWindow", "Step 2: Cluster colonies"))
        self.pushButton_4.setText(_translate("MainWindow", "Clean"))
        self.label_2.setText(_translate("MainWindow", "eps:"))
        self.label_4.setText(_translate("MainWindow", "Maximum distance between"))
        self.label_3.setText(_translate("MainWindow", "weight:"))
        self.label.setText(_translate("MainWindow", "Step 1: Clean"))
        self.pushButton_3.setText(_translate("MainWindow", "Plot"))
        self.pushButton_6.setText(_translate("MainWindow", "Plot colonies"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.pushButton_9.setText(_translate("MainWindow", "Predict #"))
        self.label_8.setText(_translate("MainWindow", "The number of points in"))
        self.label_9.setText(_translate("MainWindow", "two samples (euclidean distance)"))
        self.label_12.setText(_translate("MainWindow", "Hotkeys: Step 1    Shift = Circle colony        W = keep                 R = Remove"))
        self.label_22.setText(_translate("MainWindow", "         Step 2    Shift = Circle colony        A = Accept colony        D = Delete"))
        self.label_13.setText(_translate("MainWindow", "File name"))
        self.label_15.setText(_translate("MainWindow", "an area (includes tho point itself)"))
        self.label_10.setText(_translate("MainWindow", "Number of colonies:"))
        self.label_13.setText(_translate("MainWindow", self.filename))

        if paths_to_images != "":
            self.label_14.setText(_translate("MainWindow", "Image"))
            self.Flipim.setText(_translate("MainWindow", "Flip image"))
            self.label_11.setText(_translate("MainWindow", "Image orientation:"))
            self.label_6.setText(_translate("MainWindow", "Flip the image by taking the ~mirror image~"))
            self.label_16.setText(_translate("MainWindow", "How to align the XY axis? Hover over the image, click and drag it around."))
            self.label_17.setText(_translate("MainWindow", "How to rotate the image? Click and drag the top left or bottom right corner. "))




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

        self.filename_image = paths_to_images + self.filename.split('.')[0] + is_tif_or_jpg#tif"

        if paths_to_images != "":
            # Im
            self.im = Image.open(self.filename_image)

            tr = QtGui.QTransform()  # prepare ImageItem transformation:
            tr.rotate(0)       # Rotates the coordinate system counterclockwise by the given angle
            tr.translate(0, 0) # move 3x3 image to locate center at axis origin

            self.flip_next = 1
            self.fun_flip()
            self.flip_next = 0


    def Next(self):

        if self.numberpath != len(self.paths_to_data)-1:
            self.pushButton.setEnabled(True)

            # Set up next data
            self.numberpath = self.numberpath + 1
            data   = pd.read_pickle(self.paths_to_data[self.numberpath])
            self.X = data.to_numpy()
            self.graphicsView.clear()
            self.graphicsView.plot(self.X[:,0], self.X[:,1],pen=None, symbol='o', symbolPen=None, symbolSize=5)

        if self.numberpath == len(self.paths_to_data)-1:
            self.pushButton_2.setEnabled(False)

        self.filename = self.paths_to_data[self.numberpath].split('/')[-1]
        _translate = QtCore.QCoreApplication.translate
        self.label_13.setText(_translate("MainWindow", self.filename))




        self.filename_image = paths_to_images + self.filename.split('.')[0] + is_tif_or_jpg#tif"

        if paths_to_images != "":
            # Im
            self.im = Image.open(self.filename_image)



            self.flip_next = 1
            self.fun_flip()
            self.flip_next = 0




    #---------- Step1 ------------

    def Refresh(self):

        self.graphicsView.clear()

        clustering = DBSCAN(eps=float(self.lineEdit.text()), min_samples=int(self.lineEdit_2.text())).fit(self.X)
        self.labels = clustering.labels_
        self.colonyID = clustering.labels_
        


        new_label = []
        for label in self.labels:
            if label > 0:
                new_label.append('w')
            else:
                new_label.append('r')
        self.labels = new_label

        self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        self.scatter_plot_item.clear()
        self.scatter_plot_item.setData(pos=self.X, brush=self.labels)


        self.graphicsView.clear()
        self.graphicsView.addItem(self.scatter_plot_item)

    def Clean(self):

        self.X_clean = []
        self.Y_clean = []

        for i,l in enumerate(self.labels):
            if l == 'w':
                self.X_clean.append(self.X[i,0])
                self.Y_clean.append(self.X[i,1])

        d = {'x': self.X_clean, 'y': self.Y_clean}
        data = pd.DataFrame(data=d)
        self.X = data.to_numpy()
        self.labels = ['w']*len(self.X_clean)

        self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        self.scatter_plot_item.clear()
        self.scatter_plot_item.setData(pos=self.X, brush=self.labels)

        self.graphicsView.clear()
        self.graphicsView.addItem(self.scatter_plot_item)

    #---------- Step2 ------------

    def Estimate(self):

        self.lineEdit_3.clear()
        clustering = DBSCAN(eps=float(self.lineEdit.text()), min_samples=int(self.lineEdit_2.text())).fit(self.X)
        self.lineEdit_3.setText(str(max(np.unique(clustering.labels_))))

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

        # self.graphicsView.clear()

        # clustering = DBSCAN(eps=float(self.lineEdit_3.text()), min_samples=int(self.lineEdit_4.text())).fit(self.X)
        # self.labels = clustering.labels_
        # self.colonyID = clustering.labels_


        # #random color for new label
        # #new_color = pg.mkColor(random.choice(['w','#E6DAA6','#06C2AC','#6E750E','#FF7F50','#054907','#380282','#C79FEF','#FF4500','#069AF3','#ADD8E6','#90EE90']))
        

        # new_label = []
        # for label in self.labels:
        #     # new_color = pg.mkColor(random.choice(['w','#E6DAA6','#06C2AC','#6E750E','#FF7F50','#054907','#380282','#C79FEF','#FF4500','#069AF3','#ADD8E6','#90EE90']))
        #     # new_label.append(new_color )
        #     new_label.append(pg.intColor(label,np.floor(np.max(self.labels)/10)  ))
        # self.labels = new_label

        # self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        # self.scatter_plot_item.clear()
        # self.scatter_plot_item.setData(pos=self.X, brush=self.labels)


        # self.graphicsView.clear()
        # self.graphicsView.addItem(self.scatter_plot_item)


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

    def displayKeysW(self,mapping):
        self.newLab = 'w'
        self.clean_colonies()

    def displayKeysR(self,mapping):
        self.newLab  = 'r'
        self.clean_colonies()

    def clean_colonies(self):

        points = np.vstack((self.X[:,0], self.X[:,1])).T
        lasso  = np.vstack((self.mouse_x, self.mouse_y)).T
        p = Path(lasso) # make a polygon
        grid = p.contains_points(points)

        for i,m in enumerate(grid):
            if m == True:
                self.labels[i] = self.newLab 

        self.scatter_plot_item = pg.ScatterPlotItem(size=5, pen=pg.mkPen(None))
        self.scatter_plot_item.clear()
        self.scatter_plot_item.setData(pos=self.X, brush=self.labels)
        self.graphicsView.clear()
        self.graphicsView.addItem(self.scatter_plot_item)

        self.mouse_x = []
        self.mouse_y = [] 

    def define_colonies(self):

        points = np.vstack((self.X[:,0], self.X[:,1])).T
        lasso  = np.vstack((self.mouse_x, self.mouse_y)).T
        p = Path(lasso) # make a polygon
        grid = p.contains_points(points)

        #random color for new label
        #new_color = pg.mkColor(random.choice(['w','#E6DAA6','#06C2AC','#6E750E','#FF7F50','#054907','#380282','#C79FEF','#FF4500','#069AF3','#ADD8E6','#90EE90']))
        
        handpicked_colors = ['w','#E6DAA6','#06C2AC','#6E750E','#FF7F50','#054907','#380282','#C79FEF','#FF4500','#069AF3','#ADD8E6','#90EE90']

        self.new_color_tracker = self.new_color_tracker + 1
        self.new_color_tracker = np.mod(self.new_color_tracker,len(handpicked_colors))
        new_color = pg.mkColor(handpicked_colors[self.new_color_tracker])

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




#Extra code

# pyuic5 -x mainwindow.ui -o updated_gui_Final.py
# import pyqtgraph.examples
# pyqtgraph.examples.run()

# tr = QtGui.QTransform()  # prepare ImageItem transformation:
# tr.rotate(np.degrees(self.r1.angle()))       # Rotates the coordinate system counterclockwise by the given angle
# tr.translate(int(self.r1.pos()[0]), int(self.r1.pos()[1])) # move 3x3 image to locate center at axis origin
# im.setTransform(tr)



# pixvals = np.asarray(im)
# minval = np.percentile(pixvals, 2)
# maxval = np.percentile(pixvals, 90)
# pixvals = np.clip(pixvals, minval, maxval)
# pixvals = ((pixvals - minval) / (maxval - minval)) * 255

# im = pg.ImageItem(pixvals)
# im.setZValue(-100)
# self.graphicsView_2.clear()

# self.graphicsView_2.addItem(im)
