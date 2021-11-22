# -*- coding: utf-8 -*-
from os import walk
from os import path as os_path
from sys import path,argv,exit
for root, dirs, files in walk(os_path.dirname(os_path.dirname(os_path.realpath(__file__)))):
    path.append(root) #* 完成路径的添加，路径包括：该文件所在路径，该文件所在文件夹的所有子文件夹的路径（子文件夹的子文件夹也会添加）
import linear_RG_data_processing as DP
import Ui_Mwd as MUI
import matplotlib as mpl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np
#*----------------------------------------------------------------
mpl.rcParams['font.sans-serif'] = ['SimHei']##允许显示中文
plt.rcParams['axes.unicode_minus']=False##允许显示坐标轴负数
#*----------------------------------------------------------------
class MAIN_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MAIN_UI,self).__init__()
        self.ui = MUI.Ui_Mainwindow()
        self.ui.setupUi(self)# 建立界面
        self.show()
        
        
        #*连接信号与槽
        self.ui.btDraw.clicked.connect(self.Draw)
        
    def Draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        plt.title("测试")
        data=DP.data_form(sep=0.01)
        plt.scatter(data[0],data[1],s=5,c="black",alpha=0.2) #* 绘制散点图
        ploy=DP.simple_linear(x=data[0],y=data[1],degree=2) #* 放入数据set进行学习
        y_predict=DP.simple_linear_predict(x=data[0],coe=ploy[0]) #* 进行预测
        plt.plot(data[0],y_predict) #* 绘制折线图
		#*画图
        self.ui.figure_layout.itemAt(0).widget().deleteLater() #*删除图片（对应的控件）
        self.canvas = FigureCanvas(self.figure)#* 刷新对象
        self.ui.figure_layout.addWidget(self.canvas)#* 并且添加
        self.canvas.draw()
        #*参数显示:
        self.ui.Var_show.setText(str(np.var(data[1])))
        self.ui.Mean_show.setText(str(np.average(data[1])))
        self.ui.R_show.setText(str(ploy[3]))
        self.ui.RSS_show.setText(str(ploy[1]))
        self.ui.sigma_show.setText(str(ploy[2]))
        #*保存画出来的图片
        plt.savefig('1.jpg')
if __name__=="__main__":
    app=QApplication(argv)
    win1=MAIN_UI()
    exit(app.exec())