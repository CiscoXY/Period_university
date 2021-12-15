# -*- coding: utf-8 -*-
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
        plt.savefig("data\原始数据.png")
        #*连接信号与槽
        self.ui.path_verify.clicked.connect(self.path_input_abled)
        self.ui.path_input.clicked.connect(self.data_load)
        self.ui.path_clear.clicked.connect(self.clear)
        self.ui.btDraw.clicked.connect(self.draw_links)
        self.ui.path_output.clicked.connect(self.Para_output)
        self.pattern_preview(1)
        self.ui.modual_choose.currentIndexChanged.connect(self.pattern_preview)
#!----------------------------------------------------------------杂项函数
    def data_load(self):
        if(self.ui.data_path.text() == ""):
            self.data=DP.data_read()
        else:
            self.data=DP.data_read(path=self.ui.data_path.text())
        x_text="X:\n"
        for i in self.data[0]:
            x_text += (str(i) + "\n")
        self.ui.x_preview.setText(x_text)
        y_text="Y:\n"
        for i in self.data[1]:
            y_text += (str(i) + "\n")
        self.ui.y_preview.setText(y_text)
        self.ui.path_input.setEnabled(False)
    def png_path_T_or_F(self):
        """
        #* 判断保存图片路径的函数
        """
        text=self.ui.png_name.text()
        if(text == "" or (text[-4:] != ".png")):
            return False
        else: 
            return True
    def txt_path_T_or_F(self):
        """
        #* 判断读取数据路径的函数
        """
        text=self.ui.data_path.text()
        if(text == "" or (text[-4:] != ".txt")):
            return False
        else:
            return True
    def path_input_abled(self):
        if(self.txt_path_T_or_F()):
            self.ui.path_input.setEnabled(True)
        else:
            self.ui.modual_preview.setText("路径有误，请重新输入")
            self.ui.coe_show.setText("路径有误，请重新输入")
    def clear(self):
        self.ui.data_path.clear()
    def get_degree(self):
        """
        #*获取拟合的阶数
        """
        if (self.ui.degree_input.text()==""):
            return 1
        else:
            return int(self.ui.degree_input.text())
    def regression(self):
        """
        #*根据具体的combobox的选项选择具体的回归
        """
        if(self.ui.modual_choose.currentText() == "幂拟合"):
            self.Parameter=DP.pow_regression(self.data[0],self.data[1])
            self.y_predict=DP.pow_predict(self.data[0],*self.Parameter)
        elif(self.ui.modual_choose.currentText() == "指数拟合"):
            self.Parameter=DP.exp_regression(x=self.data[0],y=self.data[1])
            self.y_predict=DP.exp_predict(self.data[0],*self.Parameter)
        elif(self.ui.modual_choose.currentText() == "对数拟合"):
            self.Parameter=DP.log_regression(x=self.data[0],y=self.data[1])
            self.y_predict=DP.log_predict(self.data[0],*self.Parameter)
    def p_show(self):
        text="从左到右为a,b,c……\n"
        if(self.ui.modual_choose.currentText() == "幂拟合"):
            self.ui.coe_show.setText("幂拟合系数:"+text+str(self.Parameter))
        elif(self.ui.modual_choose.currentText() == "指数拟合"):
            self.ui.coe_show.setText("指数拟合系数:"+text+str(self.Parameter))
        elif(self.ui.modual_choose.currentText() == "对数拟合"):
            self.ui.coe_show.setText("对数拟合系数:"+text+str(self.Parameter))
    def pattern_preview(self,text):
        if (self.ui.modual_choose.currentText() == "简单线性回归"):
            self.ui.modual_preview.setText("y=ax + b")
        elif(self.ui.modual_choose.currentText() == "多项式拟合"):
            self.ui.modual_preview.setText("y=P(x)\n注:P(x)为x的多项式")
        elif(self.ui.modual_choose.currentText() == "幂拟合"):
            self.ui.modual_preview.setText("y= a x ^ c + b")
        elif(self.ui.modual_choose.currentText() == "指数拟合"):
            self.ui.modual_preview.setText("y= a e ^ (cx) + b")
        elif(self.ui.modual_choose.currentText() == "对数拟合"):
            self.ui.modual_preview.setText("y= a log(x + c) + b")
    def RSS_analysis(self):
        """
        #* 有关参数分析的部分的打包函数,并且显示
        """
        RSS_analysis=DP.RSS_relative_analysis(self.data[1],self.y_predict)
        self.ui.Var_show.setText(str(np.var(self.data[1])))
        self.ui.Mean_show.setText(str(np.average(self.data[1])))
        self.ui.RSS_show.setText(str(RSS_analysis[0]))
        self.ui.sigma_show.setText(str(RSS_analysis[1]))
        self.ui.R_show.setText(str(RSS_analysis[2]))
        
        self.totalparaments=[self.Parameter,
                             np.var(self.data[1]),
                             np.average(self.data[1]),
                             RSS_analysis[0],
                             RSS_analysis[1],
                             RSS_analysis[2]]
    def Para_output(self):
        """
        #*参数和参数分析的导出
        """
        if(self.ui.output_path.text()!=""):
            outpath=self.ui.output_path.text()
            DP.parameters_write(data=self.totalparaments,path=outpath)
        else:
            DP.parameters_write(data=self.totalparaments)
        self.ui.path_output.setEnabled(False)
#!----------------------------------------------------------------主体画图函数
    def draw_links(self):
        self.ui.path_output.setEnabled(True)
        if (self.ui.modual_choose.currentText() == "简单线性回归"):
            self.ui.degree_input.setText("")
            self.simple_draw()
        elif(self.ui.modual_choose.currentText() == "多项式拟合"):
            self.simple_draw()
        elif(self.ui.modual_choose.currentText() == "幂拟合" or 
             self.ui.modual_choose.currentText() == "指数拟合" or 
             self.ui.modual_choose.currentText() == "对数拟合"):
            self.complex_draw()
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
        plt.legend(["原始数据"])
    def simple_draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        if(self.ui.modual_choose.currentText() == "简单线性回归"):
            plt.title("简单线性回归")
        else:
            plt.title("多项式回归")
        # self.data=DP.data_form(sep=0.01)
        plt.scatter(self.data[0],self.data[1],s=5,c="black",alpha=0.2,label="原始数据") #* 绘制散点图
        ploy=DP.simple_linear(x=self.data[0],y=self.data[1],degree=self.get_degree()) #* 放入数据set进行学习
        self.y_predict=DP.simple_linear_predict(x=self.data[0],coe=ploy[0]) #* 进行预测
        plt.plot(self.data[0],self.y_predict,c="red",alpha=0.5,label="回归曲线") #* 绘制折线图
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
        #* 总参数构建
        self.totalparaments=[ploy[0],
                             np.var(self.data[1]),
                             np.average(self.data[1]),
                             ploy[1],
                             ploy[2],
                             ploy[3]]
        #* 系数的显示
        self.ui.coe_show.setText("依次为n,n-1,n-2……2,1,0阶系数\n"+str(ploy[0]))
        #*保存画出来的图片
        if(self.png_path_T_or_F()==False):
            global picture_num
            save_name="data/"+str(picture_num)+".png"
            picture_num += 1
            plt.savefig(save_name)
        else:
            plt.savefig(self.ui.png_name.text())
    def complex_draw(self):
        self.figure=plt.figure(figsize=(10,10),dpi=150)
        plt.title(self.ui.modual_choose.currentText())
        plt.scatter(self.data[0],self.data[1],s=5,c="black",alpha=0.2,label="原始数据") #* 绘制散点图
        self.regression()
        self.p_show()
        plt.plot(self.data[0],self.y_predict,c="red",alpha=0.5,label="回归曲线") #* 绘制折线图
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
        self.RSS_analysis() #* 应用上放的"RSS_analysis方法"
        #*保存画出来的图片
        if(self.png_path_T_or_F()==False):
            global picture_num
            save_name="data/"+str(picture_num)+".png"
            picture_num += 1
            plt.savefig(save_name)
        else:
            plt.savefig(self.ui.png_name.text())
if __name__=="__main__":
    app=QApplication(argv)
    win1=MAIN_UI()
    exit(app.exec())