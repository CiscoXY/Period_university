# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:44:42 2021

@author: HP
"""
import os
import sys
for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))):
    sys.path.append(root) #* 完成路径的添加，路径包括：该文件所在路径，该文件所在文件夹的所有子文件夹的路径（子文件夹的子文件夹也会添加）
from PyQt5.QtGui import QIntValidator
import Ui_login_window as MUI
import Ui_AD_window as AUI
import Ui_RD_window as RUI
import Data_class as Data
import copy
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class MAIN_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MAIN_UI,self).__init__()
        self.ui = MUI.Ui_MainWindow()
        self.ui.setupUi(self)# 建立界面
        
        
class AD_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(AD_UI,self).__init__()
        self.ui= AUI.Ui_ADWindow()
        self.ui.setupUi(self)# 建立界面
        
        self.singlebook=Data.book()# 完成单个书籍导入的信息创建
        self.singlereader=Data.reader()# 完成单个读者导入的信息创建
        self.PLbookinsert_path=""# 完成批量导入图书的路径创建
        self.PLreaderinsert_path=""# 完成批量导入读者的路径创建

        self.booksearchList=[]
        self.readersearchList=[]
        
        self.PLbookList=[]
        self.PLreaderList=[]

        INTVALIDATER=QIntValidator(self)
        INTVALIDATER.setRange(0,10000)#*设置输入上下限，下限为1 上限为10000
        self.ui.bookuncheckoutinput.setValidator(INTVALIDATER)#*设置校验器
        self.ui.bookcheckoutinput.setValidator(INTVALIDATER)#*设置校验器
        
        
        self.ui.mess_show.setReadOnly(True)#设定为只读模式，这样不会出现用户访问遗漏


        self.ui.bookIDinput.textChanged['QString'].connect(self.book_ID_set)#*图书部分的UI的信号与槽的连接
        self.ui.bookNameinput.textChanged['QString'].connect(self.book_Name_set)
        self.ui.bookISBNinput.textChanged['QString'].connect(self.book_ISBN_set)
        self.ui.bookpublishinginput.textChanged['QString'].connect(self.book_publishing_set)
        self.ui.bookpub_yearinput.textChanged['QString'].connect(self.book_pub_year_set)
        self.ui.bookauthorinput.textChanged['QString'].connect(self.book_author_set)
        self.ui.booklabelinput.textChanged['QString'].connect(self.book_label_set)
        self.ui.bookuncheckoutinput.textChanged['QString'].connect(self.book_uncheckout_num_set)
        self.ui.bookcheckoutinput.textChanged['QString'].connect(self.book_checkout_num_set)
        
        self.ui.readerIDinput.textChanged['QString'].connect(self.reader_ID_set)#*读者部分的UI的信号与槽的连接
        self.ui.readerNameinput.textChanged['QString'].connect(self.reader_Name_set)
        self.ui.reader_typeinput.currentIndexChanged.connect(self.reader_reader_type_set)
        self.ui.phoneinput.textChanged['QString'].connect(self.reader_Phone_set)
        
        self.ui.model_choose1.currentIndexChanged.connect(self.model_choose_emit1)#*完成图书的模式选择的槽的绑定
        self.ui.model_choose2.currentIndexChanged.connect(self.model_choose_emit2)#*完成读者的模式选择的槽的绑定
        
        #!self.ui.verifyButton_1.clicked.connect(lambda:self.message_show(self.singlebook.textreturn()))#*图书信息确认的槽的绑定
        self.ui.clearButton_1.clicked.connect(self.book_information_clear) #*图书信息清除的槽的绑定
        #!self.ui.verifyButton_4.clicked.connect(lambda:self.message_show(self.singlereader.textreturn()))#*读者信息确认的槽的绑定
        self.ui.clearButton_4.clicked.connect(self.reader_information_clear)#*读者信息清除的槽的绑定
        #下面完成批量导入模块的槽的绑定
        self.ui.verifyButton_2.clicked.connect(self.PLbookinsert_emit)
        self.ui.verifyButton_3.clicked.connect(self.PLreaderinsert_emit)
        self.ui.clearButton_2.clicked.connect(self.PLbookinsert_clear)
        self.ui.clearButton_3.clicked.connect(self.PLreaderinsert_clear)

    #*接下来是单个图书输入的槽
    def book_ID_set(self,text): 
        self.singlebook.ID=text
    def book_Name_set(self,text):
        self.singlebook.Name=text
    def book_ISBN_set(self,text):
        self.singlebook.ISBN=text
    def book_publishing_set(self,text):
        self.singlebook.publishing=text
    def book_pub_year_set(self,text):
        self.singlebook.pub_year=text
    def book_author_set(self,text):
        self.singlebook.author=text
    def book_label_set(self,text):
        self.singlebook.label=text
    def book_uncheckout_num_set(self,text):
        self.singlebook.uncheckout_num=text
    def book_checkout_num_set(self,text):
        self.singlebook.checkout_num=text
    ## 到此为止
    def book_information_show(self): #* 没啥用了 图书信息的print
        print(self.singlebook)
    def book_information_clear(self):#* 图书信息的清除
        self.ui.bookIDinput.setText("");self.ui.bookNameinput.setText("");self.ui.bookISBNinput.setText("");
        self.ui.bookpublishinginput.setText("");self.ui.bookpub_yearinput.setText("");self.ui.bookauthorinput.setText("");
        self.ui.booklabelinput.setText("");self.ui.bookuncheckoutinput.setText("");self.ui.bookcheckoutinput.setText("");
        
    #*接下来是单个读者输入的槽
    def reader_ID_set(self,text):
        self.singlereader.ID=text
    def reader_Name_set(self,text):
        self.singlereader.Name=text
    def reader_reader_type_set(self,i):
        text=self.ui.reader_typeinput.currentText()
        self.singlereader.reader_type=text
    def reader_Phone_set(self,text):
        self.singlereader.phone=text
    ##到此为止
    def reader_information_show(self): #读者信息显示
        print(self.singlereader)
    def reader_information_clear(self):# 完成读者信息的重置
        self.ui.readerIDinput.setText("")
        self.ui.readerNameinput.setText("");
        self.ui.reader_typeinput.setCurrentIndex(0);# 设置索引为0 既跳转到索引为0的选项
        self.ui.phoneinput.setText("");
    # 对应第一个模块选择，如果是选择了导入，那么下面的完成导入可以点击，完成修改不能点击，反之同理
    def model_choose_emit1(self,i): 
        text=self.ui.model_choose1.currentText()
        if(text=="导入"):
            self.ui.insert_1.setEnabled(False)
            self.ui.modify_1.setEnabled(False)
            self.ui.verifyButton_1.setEnabled(True)
            self.ui.checkBox_1.setEnabled(False)
        if(text=="编辑"):
            self.ui.modify_1.setEnabled(False)
            self.ui.insert_1.setEnabled(False)
            self.ui.verifyButton_1.setEnabled(False)
            self.ui.checkBox_1.setEnabled(True)
        if(text=="搜索"):
            self.ui.insert_1.setEnabled(False)
            self.ui.modify_1.setEnabled(False)
            self.ui.verifyButton_1.setEnabled(False)
            self.ui.checkBox_1.setEnabled(False)
        if(text=="删除"):
            self.ui.modify_1.setEnabled(False)
            self.ui.insert_1.setEnabled(False)
            self.ui.verifyButton_1.setEnabled(False)
            self.ui.checkBox_1.setEnabled(True)
    # 对应第二个模块选择，如果是选择了导入，那么下面的完成导入可以点击，完成修改不能点击，反之同理
    def model_choose_emit2(self,i): 
        text=self.ui.model_choose2.currentText()
        if(text=="导入"):
            self.ui.insert_2.setEnabled(False)
            self.ui.modify_2.setEnabled(False)
            self.ui.verifyButton_4.setEnabled(True)
            self.ui.checkBox_2.setEnabled(False)
        if(text=="编辑"):
            self.ui.modify_2.setEnabled(False)
            self.ui.insert_2.setEnabled(False)
            self.ui.verifyButton_4.setEnabled(False)
            self.ui.checkBox_2.setEnabled(True)
        if(text=="搜索"):
            self.ui.insert_2.setEnabled(False)
            self.ui.modify_2.setEnabled(False)
            self.ui.verifyButton_4.setEnabled(False)
            self.ui.checkBox_2.setEnabled(False)
        if(text=="删除"):
            self.ui.modify_2.setEnabled(False)
            self.ui.insert_2.setEnabled(False)
            self.ui.verifyButton_4.setEnabled(False)
            self.ui.checkBox_2.setEnabled(True)
    #下面是批量导入模块对应的槽的方法
    def PLbookinsert_emit(self):
        self.PLbookinsert_path=self.ui.booklist_insert.text() #获取lineedit里的文本信息
        if(self.PLbookinsert_path==""):
            self.ui.mess_show.setText("输入路径为空,请重新输入")
        else:
            try:
                os.startfile(self.PLbookinsert_path)
            except FileNotFoundError:
                self.ui.mess_show.setText("没有找到对应的文档,请仔细检查输入是否有误")
            else:
                self.ui.mess_show.setText("成功找到该文件,并成功打开,请仔细核验内容是否正确")
                self.ui.PLinsert_1.setEnabled(True)
    def PLreaderinsert_emit(self):
        self.PLreaderinsert_path=self.ui.readerlist_insert.text() #获取lineedit里的文本信息
        if(self.PLreaderinsert_path==""):
            self.ui.mess_show.setText("输入路径为空,请重新输入")
        else:
            try:
                os.startfile(self.PLreaderinsert_path)
            except FileNotFoundError:
                self.ui.mess_show.setText("没有找到对应的文档,请仔细检查输入是否有误")
            else:
                self.ui.mess_show.setText("成功找到该文件,并成功打开,请仔细核验内容是否正确")
                self.ui.PLinsert_2.setEnabled(True)
    def PLbookinsert_clear(self):
        self.ui.booklist_insert.setText("")
    def PLreaderinsert_clear(self):
        self.ui.readerlist_insert.setText("")
    
    
    
    #上述完成-----------------------
    def message_show(self,mes):#*信息显示
        self.ui.mess_show.setPlainText(str(mes))
#!工具函数
    def bookinput_isNone(self):
        """
        #*用来判断输入栏是否有空槽
        #*但凡有一个是空槽，便返回false
        """
        part1=self.ui.bookIDinput.text()==""
        part2=self.ui.bookNameinput.text()==""
        part3=self.ui.bookISBNinput.text()==""
        part4=self.ui.bookpublishinginput.text()==""
        part5=self.ui.bookpub_yearinput.text()==""
        part6=self.ui.bookauthorinput.text()==""
        part7=self.ui.booklabelinput.text()==""
        part8=self.ui.bookuncheckoutinput.text()==""
        part9=self.ui.bookcheckoutinput.text()==""
        return part1 or part2 or part3 or part4 or part5 or part6 or part7 or part8 or part9
    def readerinput_isNone(self):
        """
        #*用来判断输入栏是否有空槽
        #*但凡有一个是空槽，便返回false
        """
        part1=self.ui.readerIDinput.text()==""
        part2=self.ui.readerNameinput.text()==""
        part4=self.ui.phoneinput.text()==""
        return part1 or part2 or part4
class RD_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(RD_UI,self).__init__()
        self.ui= RUI.Ui_RDWindow()
        self.ui.setupUi(self)# 建立界面
        self.singlebook=Data.book()
        self.singlereader=Data.reader()
        self.booksearchList=[]
        self.readersearchList=[]
        self.borrowedbooksearchList=[]
        self.historysearchList=[]
    #* 图书信息搜索的信号与槽的绑定
        self.ui.bookNameinput.textChanged['QString'].connect(self.book_Name_set)
        self.ui.bookISBNinput.textChanged['QString'].connect(self.book_ISBN_set)
        self.ui.bookpublishinginput.textChanged['QString'].connect(self.book_publishing_set)
        self.ui.bookpub_yearinput.textChanged['QString'].connect(self.book_pub_year_set)
        self.ui.bookauthorinput.textChanged['QString'].connect(self.book_author_set)
        self.ui.booklabelinput.textChanged['QString'].connect(self.book_label_set)
    #* 读者信息搜搜的信号与槽的绑定
        self.ui.readerNameinput.textChanged['QString'].connect(self.reader_Name_set)
        self.ui.phoneinput.textChanged['QString'].connect(self.reader_phone_set)
    #* 清除按钮的信号与槽的绑定
        self.ui.clearButton_1.clicked.connect(self.bookinf_clear)
        self.ui.clearButton_2.clicked.connect(self.readerinf_clear)
#* 图书信息的输入槽
    def book_Name_set(self,text):
        self.singlebook.Name=text
    def book_ISBN_set(self,text):
        self.singlebook.ISBN=text
    def book_publishing_set(self,text):
        self.singlebook.publishing=text
    def book_pub_year_set(self,text):
        self.singlebook.pub_year=text
    def book_author_set(self,text):
        self.singlebook.author=text
    def book_label_set(self,text):
        self.singlebook.label=text
#* 读者信息的输入槽
    def reader_Name_set(self,text):
        self.singlereader.Name=text
    def reader_phone_set(self,text):
        self.singlereader.phone=text
#* 清除槽
    def bookinf_clear(self):
        self.ui.bookNameinput.setText("")
        self.ui.bookISBNinput.setText("")
        self.ui.bookpublishinginput.setText("")
        self.ui.bookpub_yearinput.setText("")
        self.ui.bookauthorinput.setText("")
        self.ui.booklabelinput.setText("")
    def readerinf_clear(self):
        self.ui.readerNameinput.setText("")
        self.ui.phoneinput.setText("")
#!----------------------------------------------------------------
#!----------------------------------------------------------------
#!----------------------------------------------------------------
#!----------------------------------------------------------------
class User_GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(User_GUI,self).__init__()
        self.main=MAIN_UI()
        self.AD=AD_UI()
        self.RD=RD_UI()
        self.road1="books_data.xlsx"
        self.road2="readers_data.xlsx"
        self.road3="history_of_borrowed.xlsx"
        self.road4="borrowing_list.xlsx"
        self.booklist=Data.Books_data_read(self.road1)
        self.readerlist=Data.Readers_data_read(self.road2)
        self.historylist=Data.History_data_read(self.readerlist,self.road3) #*历史记录的读取
        self.borrowList=Data.History_data_read(self.readerlist,self.road4) #*现存借书数据的读取
        #* 读者界面显示的初始化
        ##接下来是界面切换的信号和槽的绑定
        
#*1:主界面的信号与槽绑定
        self.main.ui.QuitButton.clicked.connect(self.MUI_close)
        self.main.ui.AdminBotton.clicked.connect(self.switch_to_AD_UI)# 初始化信号和槽
        self.main.ui.ReaderBotton.clicked.connect(self.switch_to_RD_UI)# 初始化信号和槽
        
        self.AD.ui.BacktoMainButton.clicked.connect(self.AD_to_MAIN_UI)# 返回主页面的信号与槽的绑定
        self.RD.ui.BacktoMainButton.clicked.connect(self.RD_to_MAIN_UI)# 绑定返回到主界面的信号和槽
        #*完成主界面绑定



#*接下来是管理员界面控件的绑定                

    #*模式选择的信号与槽的绑定
        self.AD.ui.model_choose1.currentIndexChanged.connect(self.AD_booksearch_edit)
        self.AD.ui.model_choose2.currentIndexChanged.connect(self.AD_readersearch_edit)

    #*所有图书信息的显示
        self.AD.ui.totalbooks_show.clicked.connect(self.totalbook_information_show)
    #*所有读者信息的显示
        self.AD.ui.totalreaders_show.clicked.connect(self.totalreader_information_show)

    #*批量导入的信号和槽绑定
        self.AD.ui.PLinsert_1.clicked.connect(self.AD_PLinsert1)
        self.AD.ui.PLinsert_2.clicked.connect(self.AD_PLinsert2)
            
    #*图书导入栏的绑定
        self.AD.ui.insert_1.clicked.connect(self.singlebook_insert)
        self.AD.ui.verifyButton_1.clicked.connect(self.insert_1_abled)
    #*读者导入栏的绑定
        self.AD.ui.insert_2.clicked.connect(self.singlereader_insert)
        self.AD.ui.verifyButton_4.clicked.connect(self.insert_2_abled)

    #*图书信息输入栏的绑定
        self.AD.ui.bookIDinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookNameinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookISBNinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookpublishinginput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookpub_yearinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookauthorinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.booklabelinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookuncheckoutinput.textChanged['QString'].connect(self.AD_booksearch_edit)
        self.AD.ui.bookcheckoutinput.textChanged['QString'].connect(self.AD_booksearch_edit)
    #*读者信息输入栏的绑定
        self.AD.ui.readerIDinput.textChanged['QString'].connect(self.AD_readersearch_edit)
        self.AD.ui.readerNameinput.textChanged['QString'].connect(self.AD_readersearch_edit)
        self.AD.ui.reader_typeinput.currentIndexChanged.connect(self.AD_readersearch_edit)
        self.AD.ui.phoneinput.textChanged['QString'].connect(self.AD_readersearch_edit)
    #*图书编辑栏的绑定
        self.AD.ui.modify_1.clicked.connect(self.AD_book_mess_edit)
        self.AD.ui.checkBox_1.stateChanged.connect(self.AD_booksearch_edit)
        
    #*读者编辑栏的绑定
        self.AD.ui.modify_2.clicked.connect(self.AD_reader_mess_edit)
        self.AD.ui.checkBox_2.stateChanged.connect(self.AD_readersearch_edit)
#*接下来是读者界面控件的绑定
        #*----------------------------------------------------------------
        self.RD.ui.bookNameinput.textChanged['QString'].connect(self.RD_book_mess_show)
        self.RD.ui.bookISBNinput.textChanged['QString'].connect(self.RD_book_mess_show)
        self.RD.ui.bookpublishinginput.textChanged['QString'].connect(self.RD_book_mess_show)
        self.RD.ui.bookpub_yearinput.textChanged['QString'].connect(self.RD_book_mess_show)
        #*----------------------------------------------------------------
        self.RD.ui.bookNameinput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        self.RD.ui.bookISBNinput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        self.RD.ui.bookpublishinginput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        self.RD.ui.bookpub_yearinput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        self.RD.ui.readerNameinput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        self.RD.ui.phoneinput.textChanged['QString'].connect(self.RD_reader_relative_inf_show)
        #*----------------------------------------------------------------
        self.RD.ui.returnBT.clicked.connect(self.restore)
        self.RD.ui.borrowBT.clicked.connect(self.borrow)
#*主界面显示，必须放到最后 
        self.main.show()## 最最最最后也是最重要的一句 完成界面的显示 
#*1:主界面的绑定
    def MUI_close(self):
        self.main.close()
        #*下面是文件输出
        Data.booklist_output(self.road1,self.booklist)
        Data.readerlist_output(self.road2,self.readerlist)
        Data.historylist_output(self.road3,self.historylist)
        Data.borrowlist_output(self.road4,self.borrowList)
    def switch_to_AD_UI(self): #定义槽 为切换到管理员界面
        self.AD.ui.mess_show.setText(
            "现存的图书数据\n"+Data.Books_massage_return(self.booklist)+
            "\n现存的读者数据\n"+Data.Readers_massage_return(self.readerlist)
            ) #*完成现存的图书数据和读者数据的显示
        self.AD.show()
        self.main.hide()
    def switch_to_RD_UI(self): #定义槽 为切换到读者界面
        self.RD_book_mess_show(1)#*触发一下，完成读者界面的初始化信息显示
        self.RD_reader_relative_inf_show(1)#*出发一下，完成读者界面的初始化信息显示
        self.RD.show()
        self.main.hide()
#*2:管理员界面的绑定
    def AD_to_MAIN_UI(self):#定义槽 为切换到主界面
        self.main.show()
        self.AD.hide()
        
#*3:读者界面的绑定 
    def RD_to_MAIN_UI(self):#定义槽 为切换到主界面
        self.main.show()
        self.RD.hide()
#!----------------------------------------------------------------
#* 管理员界面的槽

#* 所有图书信息显示的槽
    def totalbook_information_show(self):
        self.AD.ui.mess_show.setText("现存的图书数据\n"+Data.Books_massage_return(self.booklist))
#* 所有读者信息显示的槽
    def totalreader_information_show(self):
        self.AD.ui.mess_show.setText("现存的读者数据\n"+Data.Readers_massage_return(self.readerlist))


#*单个导入图书的槽
    def insert_1_abled(self):
        if(self.AD.bookinput_isNone()):
            self.AD.ui.mess_show.append("当仅当输入信息栏不存在空时可以导入")
        else:
            self.AD.ui.insert_1.setEnabled(True)
    def singlebook_insert(self):
        text="未导入时的图书数据\n"+Data.Books_massage_return(self.booklist)
        text+="\n\n导入的图书数据为\n"+self.AD.singlebook.textreturn()+"\n\n"
        for i in self.booklist:
            if(self.AD.singlebook==i):
                text+="存在相同的书目信息，现在已经合并\n"
                break
        temp=copy.deepcopy(self.AD.singlebook)
        Data.Books_list_extend(self.booklist,[temp])
        text+="导入后的图书数据为\n"+Data.Books_massage_return(self.booklist)
        self.AD.ui.mess_show.setText(text) #*将上述的信息放到内容显示的窗口上去
        self.AD.ui.insert_1.setEnabled(False)
#*单个导入读者的槽
    def insert_2_abled(self):
        if(self.AD.readerinput_isNone()):
            self.AD.ui.mess_show.append("当仅当输入信息栏不存在空时可以导入")
        else:
            self.AD.ui.insert_2.setEnabled(True)
    def singlereader_insert(self):
        text="未导入时的读者数据\n"+Data.Readers_massage_return(self.readerlist)
        text+="\n\n导入的读者数据为\n"+self.AD.singlereader.textreturn()+"\n\n"
        for i in self.readerlist:
            if(self.AD.singlereader==i):
                text+="存在相同的读者信息，跳过\n"
                break
        temp=copy.deepcopy(self.AD.singlereader)
        Data.Books_list_extend(self.readerlist,[temp])
        text+="导入后的读者数据为\n"+Data.Readers_massage_return(self.readerlist)
        self.AD.ui.mess_show.setText(text) #*将上述的信息放到内容显示的窗口上去
        self.AD.ui.insert_2.setEnabled(False)
#*批量导入图书的槽
    def AD_PLinsert1(self):
        self.AD.ui.PLinsert_1.setEnabled(False)
        if(len(self.AD.PLbookinsert_path)>5 and self.AD.PLbookinsert_path[len(self.AD.PLbookinsert_path)-5:]!=".xlsx"):
            print("文件并非xlsx类型，无法导入，请重新输入")
        else:
            self.AD.PLbookList=Data.Books_data_read(self.AD.PLbookinsert_path)
            Data.Books_list_extend(self.booklist,self.AD.PLbookList)
            self.AD.ui.mess_show.setText(
                "导入的图书数据为:\n"+Data.Books_massage_return(self.AD.PLbookList)+
                "\n\n现存的图书数据\n"+Data.Books_massage_return(self.booklist)
            )
#*批量导入读者的槽
    def AD_PLinsert2(self):
        self.AD.ui.PLinsert_2.setEnabled(False)
        if(len(self.AD.PLreaderinsert_path)>5 and self.AD.PLreaderinsert_path[len(self.AD.PLreaderinsert_path)-5:]!=".xlsx"):
            print("文件并非xlsx类型，无法导入，请重新输入")
        else:
            self.AD.PLreaderList=Data.Readers_data_read(self.AD.PLreaderinsert_path)
            Data.Readers_list_extend(self.readerlist,self.AD.PLreaderList)
            self.AD.ui.mess_show.setText(
                "导入的读者数据为:\n"+Data.Books_massage_return(self.AD.PLreaderList)+
                "\n\n现存的读者书数据\n"+Data.Books_massage_return(self.readerlist)
            )

#*图书搜索编辑槽
    def AD_booksearch_edit(self,text):  
        '''
        #*text屁用没有，就是单纯的为了参数传递正确罢了
        '''
        if(self.AD.ui.model_choose1.currentText() == "导入"):
            self.AD.ui.mess_show.setText(
                "现存的图书数据\n"+Data.Books_massage_return(self.booklist)+
                "\n即将导入的书籍信息为:"+self.AD.singlebook.textreturn()
                )
            if(self.AD.bookinput_isNone()):self.AD.ui.insert_1.setEnabled(False)
        elif(self.AD.ui.model_choose1.currentText() == "搜索"):
            #*创建搜索表
            self.AD.booksearchList=Data.Books_searching(self.AD.singlebook,self.booklist)
            #*搜索模块的结束
            self.AD.ui.mess_show.setText("搜索到的图书为:\n"+Data.Books_massage_return(self.AD.booksearchList))

        elif(self.AD.ui.model_choose1.currentText() == "编辑"):
            if(not self.AD.ui.checkBox_1.isChecked()): #*如果没有被锁定
                self.AD.singlebook.ID=self.AD.ui.bookIDinput.text()
                self.AD.singlebook.Name=self.AD.ui.bookNameinput.text()
                self.AD.singlebook.ISBN=self.AD.ui.bookISBNinput.text()
                self.AD.singlebook.publishing=self.AD.ui.bookpublishinginput.text()
                self.AD.singlebook.pub_year=self.AD.ui.bookpub_yearinput.text()
                self.AD.singlebook.author=self.AD.ui.bookauthorinput.text()
                self.AD.singlebook.label=self.AD.ui.booklabelinput.text()
                self.AD.singlebook.uncheckout_num=self.AD.ui.bookuncheckoutinput.text()
                self.AD.singlebook.checkout_num=self.AD.ui.bookcheckoutinput.text()
                self.AD.booksearchList=Data.Books_searching(self.AD.singlebook,self.booklist)
            #*搜索模块的结束
                self.AD.ui.mess_show.setText(
                    "搜索到的图书为:\n"+Data.Books_massage_return(self.AD.booksearchList)+"\n\n"
                    +"即将改换成:\n"+self.AD.singlebook.textreturn()+"\n注：当仅当搜索到的书籍为一本时可以进行更改"
                )
                if(len(self.AD.booksearchList)==1):
                    '''
                    #*当仅当搜索的书单栏只有一本书是才可以点击锁定
                    '''
                    self.AD.ui.modify_1.setEnabled(False)
                    self.AD.ui.checkBox_1.setEnabled(True)
                else:
                    self.AD.ui.modify_1.setEnabled(False)
                    self.AD.ui.checkBox_1.setEnabled(False)
            else:#*如果被锁定了
                message="现锁定的书籍信息为:\n"+Data.Books_massage_return(self.AD.booksearchList)+"\n\n"
                self.AD.ui.mess_show.setText(message+"即将改换成:\n"+self.AD.singlebook.textreturn())
                if(self.AD.bookinput_isNone()):
                    #*当且仅当输入栏没有空槽时，才可以使用“确定“按钮
                    self.AD.ui.mess_show.append("编辑后的信息不能有'空'")
                    self.AD.ui.modify_1.setEnabled(False)
                else:
                    self.AD.ui.modify_1.setEnabled(True)
                    
                    
        elif(self.AD.ui.model_choose1.currentText() == "删除"):
            if(not self.AD.ui.checkBox_1.isChecked()): #*如果没有被锁定
                self.AD.singlebook.ID=self.AD.ui.bookIDinput.text()
                self.AD.singlebook.Name=self.AD.ui.bookNameinput.text()
                self.AD.singlebook.ISBN=self.AD.ui.bookISBNinput.text()
                self.AD.singlebook.publishing=self.AD.ui.bookpublishinginput.text()
                self.AD.singlebook.pub_year=self.AD.ui.bookpub_yearinput.text()
                self.AD.singlebook.author=self.AD.ui.bookauthorinput.text()
                self.AD.singlebook.label=self.AD.ui.booklabelinput.text()
                self.AD.singlebook.uncheckout_num=self.AD.ui.bookuncheckoutinput.text()
                self.AD.singlebook.checkout_num=self.AD.ui.bookcheckoutinput.text()
                self.AD.booksearchList=Data.Books_searching(self.AD.singlebook,self.booklist)
            #*搜索模块的结束
                self.AD.ui.mess_show.setText(
                    "搜索到的图书为:\n"+Data.Books_massage_return(self.AD.booksearchList)+"\n\n"
                    "\n注：当仅当搜索到的书籍为一本且在库与借出数量均为0时可以进行删除！！"+"\n注：当仅当搜索到的书籍为一本时且在库与借出数量均为0可以进行删除！！"
                )
                if(len(self.AD.booksearchList)==1 and self.AD.booksearchList[0].uncheckout_num=="0" and self.AD.booksearchList[0].checkout_num=="0"):
                    '''
                    #*当仅当搜索的书单栏只有一本书且在库与借出数量均为0时才可以点击锁定
                    '''
                    self.AD.ui.modify_1.setEnabled(False)
                    self.AD.ui.checkBox_1.setEnabled(True)
                else:
                    self.AD.ui.modify_1.setEnabled(False)
                    self.AD.ui.checkBox_1.setEnabled(False)
            else:#*如果被锁定了
                message="即将删除的书籍信息为:\n"+Data.Books_massage_return(self.AD.booksearchList)
                self.AD.ui.mess_show.setText(message)
                self.AD.ui.modify_1.setEnabled(True)
#*读者搜索编辑槽
    def AD_readersearch_edit(self,text):
        '''
        #*text屁用没有，就是单纯的为了参数传递正确罢了
        '''
        if(self.AD.ui.model_choose2.currentText() == "导入"):
            self.AD.ui.mess_show.setText(
                "现存的读者数据\n"+Data.Books_massage_return(self.readerlist)+
                "\n即将导入的读者信息为:"+self.AD.singlereader.textreturn()
                )
            if(self.AD.readerinput_isNone()):self.AD.ui.insert_2.setEnabled(False)
            
        elif(self.AD.ui.model_choose2.currentText() == "搜索"):
            self.AD.readersearchList=Data.Readers_searching(self.AD.singlereader,self.readerlist)
            #*搜索模块的结束
            self.AD.ui.mess_show.setText("搜索到的读者为:\n"+Data.Books_massage_return(self.AD.readersearchList))
            
        elif(self.AD.ui.model_choose2.currentText() == "编辑"):
            if(not self.AD.ui.checkBox_2.isChecked()): #*如果没有被锁定
                self.AD.singlereader.ID = self.AD.ui.readerIDinput.text()
                self.AD.singlereader.Name = self.AD.ui.readerNameinput.text()
                self.AD.singlereader.reader_type = self.AD.ui.reader_typeinput.currentText()
                self.AD.singlereader.phone = self.AD.ui.phoneinput.text()
                self.AD.readersearchList=Data.Readers_searching(self.AD.singlereader,self.readerlist)
            #*搜索模块的结束
                self.AD.ui.mess_show.setText(
                    "搜索到的读者信息为:\n"+Data.Readers_massage_return(self.AD.readersearchList)+"\n\n"
                    +"即将改换成:\n"+self.AD.singlereader.textreturn()+"\n注：当仅当搜索到的读者为一人时可以进行更改"
                )
                if(len(self.AD.readersearchList)==1):
                    '''
                    #*当仅当搜索的读者栏只有一个人时才可以点击锁定
                    '''
                    self.AD.ui.modify_2.setEnabled(False)
                    self.AD.ui.checkBox_2.setEnabled(True)
                else:
                    self.AD.ui.modify_2.setEnabled(False)
                    self.AD.ui.checkBox_2.setEnabled(False)
            else:#*如果被锁定了
                message="现锁定的读者信息为:\n"+Data.Readers_massage_return(self.AD.readersearchList)+"\n\n"
                self.AD.ui.mess_show.setText(message+"即将改换成:\n"+self.AD.singlereader.textreturn())
                if(self.AD.readerinput_isNone()):
                    #*当且仅当输入栏没有空槽时，才可以使用“确定“按钮
                    self.AD.ui.mess_show.append("编辑后的信息不能有'空'")
                    self.AD.ui.modify_2.setEnabled(False)
                else:
                    self.AD.ui.modify_2.setEnabled(True)
        elif(self.AD.ui.model_choose2.currentText() == "删除"):
            if(not self.AD.ui.checkBox_2.isChecked()): #*如果没有被锁定
                self.AD.singlereader.ID = self.AD.ui.readerIDinput.text()
                self.AD.singlereader.Name = self.AD.ui.readerNameinput.text()
                self.AD.singlereader.reader_type = self.AD.ui.reader_typeinput.currentText()
                self.AD.singlereader.phone = self.AD.ui.phoneinput.text()
                self.AD.readersearchList=Data.Readers_searching(self.AD.singlereader,self.readerlist)
            #*搜索模块的结束
                self.AD.ui.mess_show.setText(
                    "搜索到的读者信息为:\n"+Data.Readers_massage_return(self.AD.readersearchList)+"\n\n"
                    "\n注：当仅当搜索到的读者为一人时可以进行删除操作！！！"+"\n注：当仅当搜索到的读者为一人时可以进行删除操作！！！"
                )
                if(len(self.AD.readersearchList)==1):
                    '''
                    #*当仅当搜索的读者栏只有一个人时才可以点击锁定
                    '''
                    self.AD.ui.modify_2.setEnabled(False)
                    self.AD.ui.checkBox_2.setEnabled(True)
                else:
                    self.AD.ui.modify_2.setEnabled(False)
                    self.AD.ui.checkBox_2.setEnabled(False)
            else:#*如果被锁定了
                message="即将删除的读者信息为:\n"+Data.Readers_massage_return(self.AD.readersearchList)+"\n\n"
                self.AD.ui.mess_show.setText(message)
                self.AD.ui.modify_2.setEnabled(True)
#*图书信息编辑的槽
    def AD_book_mess_edit(self):
        """
        #*编辑单个书籍
        """
        #*当满足搜索列表只存在一本书的时候，从整体的书单中搜索到这本书，并且将这本书的信息重置为self.AD.singlebook的数据
        if(self.AD.ui.model_choose1.currentText() == "编辑"):
            for index,i in enumerate(self.booklist): 
                if(self.AD.booksearchList[0]== i):
                    temp=copy.deepcopy(self.AD.singlebook)
                    print(temp)
                    self.booklist.pop(index)
                    Data.Books_list_extend(self.booklist,[temp])
                    break
            self.AD.ui.modify_1.setEnabled(False)
            self.AD.ui.checkBox_1.setChecked(False)
        elif(self.AD.ui.model_choose1.currentText() == "删除"):
            for index,i in enumerate(self.booklist):
                if(self.AD.booksearchList[0]== i):
                    self.booklist.pop(index)
            self.AD.ui.modify_1.setEnabled(False)
            self.AD.ui.checkBox_1.setChecked(False)
#*读者信息编辑的槽
    def AD_reader_mess_edit(self):
        """
        #*编辑单个读者
        """
        #*当满足搜索列表只存在一本书的时候，从整体的书单中搜索到这本书，并且将这本书的信息重置为self.AD.singlebook的数据
        if(self.AD.ui.model_choose2.currentText() == "编辑"):
            for index,i in enumerate(self.readerlist): 
                if(self.AD.readersearchList[0]== i):
                    temp=copy.deepcopy(self.AD.singlereader)
                    print(temp)
                    self.readerlist.pop(index)
                    Data.Readers_list_extend(self.readerlist,[temp])
                    break
            self.AD.ui.modify_2.setEnabled(False)
            self.AD.ui.checkBox_2.setChecked(False)
        #*如果为删除 那么找到这个元素并且出栈
        elif(self.AD.ui.model_choose2.currentText() == "删除"):
            for index,i in enumerate(self.readerlist):
                if(self.AD.readersearchList[0]== i):
                    self.readerlist.pop(index)
            self.AD.ui.modify_2.setEnabled(False)
            self.AD.ui.checkBox_2.setChecked(False)
#!----------------------------------------------------------------
#* 下面是读者界面的槽
#* 搜索槽
    def RD_book_mess_show(self,text):
        """
        #*text纯粹是垃圾，不用管
        """
        self.RD.booksearchList=Data.Books_searching(self.RD.singlebook,self.booklist)
        self.RD.ui.books_inf_show.setText("搜索到的书籍信息为:\n"+Data.Books_massage_return_simplify(self.RD.booksearchList))
        if(len(self.RD.booksearchList)==1 and len(self.RD.readersearchList)==1):
            if(int(self.RD.booksearchList[0].uncheckout_num)>0):
                self.RD.ui.books_inf_show.append(
                    "\n当前书籍库存数量为:"+self.RD.booksearchList[0].uncheckout_num+"\n可借"
                    )
                self.RD.ui.borrowBT.setEnabled(True)
            else:
                self.RD.ui.books_inf_show.append("\n在库数量不足，不能借出")
                self.RD.ui.borrowBT.setEnabled(False)
        else:
            self.RD.ui.books_inf_show.append("当仅当搜索到一本书且搜索到一个人时可以借出")
            self.RD.ui.borrowBT.setEnabled(False)
            
    def RD_reader_relative_inf_show(self,text):
        self.RD.readersearchList=Data.Readers_searching(self.RD.singlereader,self.readerlist)
        self.RD.ui.readers_inf_show.setText("搜索到的读者信息为:\n"+Data.Readers_massage_return(self.RD.readersearchList))
        self.RD_book_mess_show(1)#*触发一下
        self.RD.historysearchList=Data.History_search(self.historylist,r=self.RD.singlereader)
        self.RD.borrowedbooksearchList=Data.History_search(self.borrowList,r=self.RD.singlereader,b=self.RD.singlebook)
        if(len(self.RD.borrowedbooksearchList) > 0): self.RD.ui.returnBT.setEnabled(True) #*可以按了
        else: self.RD.ui.returnBT.setEnabled(False)
        #*显示信息
        self.RD.ui.borrow_history_show.setText(Data.History_message_return(self.RD.historysearchList))
        self.RD.ui.borrowed_books_show.setText(Data.History_message_return(self.RD.borrowedbooksearchList))
    def restore(self):
        for tuple in self.RD.borrowedbooksearchList:
            k=0
            length=len(self.booklist)
            for book in self.booklist: 
                if(tuple.book == book): #*如果现在存储的书的列表中存在和借出书籍相同书籍信息的，那么库存数量+1，借出数量-1
                    book.uncheckout_num = str(int(book.uncheckout_num)+1)
                    book.checkout_num = str(int(book.checkout_num)-1)
                    break
                k+=1
            if(k == length):#* 如果遍历了所有的书单发现并没有找到相同信息的书籍，那么就在书单中新建一个书籍信息，并且归还该书籍
                temp=copy.deepcopy(tuple.book)
                temp.uncheckout_num="1"
                temp.checkout_num="0"
                self.booklist.append(temp)
            for index,i in enumerate(self.borrowList):
                if(tuple == i):
                    self.borrowList.pop(index)
        self.RD.ui.returnBT.setEnabled(False) #*取消按键
        self.RD_reader_relative_inf_show(1)#* 再刷新显示一下
    def borrow(self):
        temp_book=copy.deepcopy(self.RD.booksearchList[0])
        temp_reader=copy.deepcopy(self.RD.readersearchList[0])
        for i in self.booklist:
            if (temp_book==i):
                i.uncheckout_num=str(int(i.uncheckout_num)-1)
                i.checkout_num=str(int(i.checkout_num)+1)
                break
        temp=Data.history_tuple(reader_1=temp_reader,book_1=temp_book)
        self.borrowList.append(temp)
        self.historylist.append(temp)
        self.RD.ui.borrowBT.setEnabled(False) #*取消按键
        self.RD_reader_relative_inf_show(1)#* 再刷新显示一下
#!接下来都是工具函数
    
if __name__=="__main__":
    # app=QApplication(sys.argv)
    # win1=User_GUI()
    # sys.exit(app.exec())
    pass