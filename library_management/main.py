# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:50:53 2021

@author: HP
"""
import sys
import os
for root, dirs, files in os.walk(sys.path[0]):
    sys.path.append(root) #* 完成路径的添加，路径包括：该文件所在路径，该文件所在文件夹的所有子文件夹的路径（子文件夹的子文件夹也会添加)
import GUI
import Data_class
import pandas as pd
from PyQt5.QtWidgets import QApplication,QMainWindow


app=QApplication(sys.argv)
win1=GUI.User_GUI()
sys.exit(app.exec())

