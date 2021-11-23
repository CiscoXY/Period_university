# -*- coding: utf-8 -*-
from inspect import Parameter
from os import walk
from os import path as os_path
from sys import path,argv,exit
for root, dirs, files in walk(os_path.dirname(os_path.dirname(os_path.realpath(__file__)))):
    path.append(root) #* 完成路径的添加，路径包括：该文件所在路径，该文件所在文件夹的所有子文件夹的路径（子文件夹的子文件夹也会添加）
import linear_RG_data_processing as DP
import Ui_Mwd as MUI
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MultipleLocator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIntValidator
import numpy as np

global picture_num #*作为图片名称的计数
picture_num = 1 
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
        #* 杂项设置
        INTVALIDATER=QIntValidator(self)
        INTVALIDATER.setRange(2,5)#*设置输入上下限，下限为1 上限为5
        self.ui.degree_input.setValidator(INTVALIDATER) #*设置校验器，这里仅允许输入1-5的整数作为最高次项阶数 因为再高阶数的计算量过大
        #* 原始数据的载入:
        self.data_load()
        #* 原始数据的图片绘制
        #*----------------------------------------------------------------
        self.original_draw()#* 先画个原始图
        self.canvas = FigureCanvas(self.figure)#* 建立对象
        self.ui.figure_layout.addWidget(self.canvas)#* 并且添加
        self.canvas.draw()
        plt.savefig("原始数据.png")
        #*连接信号与槽
        self.ui.btDraw.clicked.connect(self.draw_links)
#!----------------------------------------------------------------杂项函数
    def data_load(self):
        self.data=DP.data_read()
        x_text="X:\n"
        for i in self.data[0]:
            x_text += (str(i) + "\n")
        self.ui.x_preview.setText(x_text)
        y_text="Y:\n"
        for i in self.data[1]:
            y_text += (str(i) + "\n")
        self.ui.y_preview.setText(y_text)
    def png_path_T_or_F(self):
        """
        #* 判断保存图片路径的函数
        """
        text=self.ui.png_name.text()
        if(text == "" or (text[-4:] != ".png")):
            return False
        else: 
            return True
    def get_degree(self):
        """
        #*获取拟合的阶数
        """
        if (self.ui.degree_input.text()==""):
            return 1
        else:
            return int(self.ui.degree_input.text())
#!----------------------------------------------------------------主体画图函数
    def draw_links(self):
        if (self.ui.modual_choose.currentText() == "简单线性回归"):
            self.ui.degree_input.setText("")
            self.simple_draw()
        elif(self.ui.modual_choose.currentText() == "多项式拟合"):
            self.simple_draw()
        elif(self.ui.modual_choose.currentText() == "幂拟合"):
            self.pow_draw()
    def original_draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        plt.title("原始数据")
        # self.data=DP.data_form(sep=0.01)
        plt.scatter(self.data[0],self.data[1],s=5,c="black",alpha=0.2) #* 绘制散点图
        plt.xlabel("X",fontsize=15)
        plt.ylabel("Y",fontsize=15)
        ax=plt.gca()
        ax.xaxis.set_major_locator(MultipleLocator(int(max(self.data[0])-min(self.data[0]))/5))
        ax.yaxis.set_major_locator(MultipleLocator(int(max(self.data[1])-min(self.data[1]))/5))
        plt.legend(["数据点"])
    def simple_draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        if(self.ui.degree_input.text()==""):
            plt.title("简单线性回归")
        else:
            plt.title("多项式回归")
        # self.data=DP.data_form(sep=0.01)
        plt.scatter(self.data[0],self.data[1],s=5,c="black",alpha=0.2,label="原始数据") #* 绘制散点图
        ploy=DP.simple_linear(x=self.data[0],y=self.data[1],degree=self.get_degree()) #* 放入数据set进行学习
        y_predict=DP.simple_linear_predict(x=self.data[0],coe=ploy[0]) #* 进行预测
        plt.plot(self.data[0],y_predict,c="red",alpha=0.5,label="回归曲线") #* 绘制折线图
        #* 绘图美化部分:
        ax=plt.gca()
        plt.xlabel("X",fontsize=15)
        plt.ylabel("Y",fontsize=15)
        ax.xaxis.set_major_locator(MultipleLocator(int(max(self.data[0])-min(self.data[0]))/5))##设置主附坐标轴刻度间隔
        ax.yaxis.set_major_locator(MultipleLocator(int(max(self.data[1])-min(self.data[1]))/5))
        plt.legend()
		#*画图
        self.ui.figure_layout.itemAt(0).widget().deleteLater() #*删除图片（对应的控件）
        self.canvas = FigureCanvas(self.figure)#* 刷新对象
        self.ui.figure_layout.addWidget(self.canvas)#* 并且添加
        self.canvas.draw()
        #*参数显示:
        self.ui.Var_show.setText(str(np.var(self.data[1])))
        self.ui.Mean_show.setText(str(np.average(self.data[1])))
        self.ui.R_show.setText(str(ploy[3]))
        self.ui.RSS_show.setText(str(ploy[1]))
        self.ui.sigma_show.setText(str(ploy[2]))
        #*保存画出来的图片
        if(self.png_path_T_or_F()==False):
            global picture_num
            save_name=str(picture_num)+".png"
            picture_num += 1
            plt.savefig(save_name)
        else:
            plt.savefig(self.ui.png_name.text())
    def pow_draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        plt.title("幂回归(拟合)")
        plt.scatter(self.data[0],self.data[1],s=5,c="black",alpha=0.2,label="原始数据") #* 绘制散点图
        Parameter=DP.pow_regression(self.data[0],self.data[1])
        y_predict=DP.pow_predict(self.data[0],*Parameter)
        plt.plot(self.data[0],y_predict,c="red",alpha=0.5,label="回归曲线") #* 绘制折线图
        #* 绘图美化部分:
        ax=plt.gca()
        plt.xlabel("X",fontsize=15)
        plt.ylabel("Y",fontsize=15)
        ax.xaxis.set_major_locator(MultipleLocator(int(max(self.data[0])-min(self.data[0]))/5))##设置主附坐标轴刻度间隔
        ax.yaxis.set_major_locator(MultipleLocator(int(max(self.data[1])-min(self.data[1]))/5))
        plt.legend()
        #*画图
        self.ui.figure_layout.itemAt(0).widget().deleteLater() #*删除图片（对应的控件）
        self.canvas = FigureCanvas(self.figure)#* 刷新对象
        self.ui.figure_layout.addWidget(self.canvas)#* 并且添加
        self.canvas.draw()
        #* 参数分析部分:
        RSS_analysis=DP.RSS_relative_analysis(self.data[1],y_predict)
        self.ui.Var_show.setText(str(np.var(self.data[1])))
        self.ui.Mean_show.setText(str(np.average(self.data[1])))
        self.ui.RSS_show.setText(str(RSS_analysis[0]))
        self.ui.sigma_show.setText(str(RSS_analysis[1]))
        self.ui.R_show.setText(str(RSS_analysis[2]))
        #*保存画出来的图片
        if(self.png_path_T_or_F()==False):
            global picture_num
            save_name=str(picture_num)+".png"
            picture_num += 1
            plt.savefig(save_name)
        else:
            plt.savefig(self.ui.png_name.text())
if __name__=="__main__":
    app=QApplication(argv)
    win1=MAIN_UI()
    exit(app.exec())