# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:25:03 2021

@author: HP
"""
import pandas as pd
import copy
# 图书类和读者类的定义module

#*图书类的定义------------------------------------------------------------------------------------------------
class book(object):
    def __init__(self, ID="", Name="", ISBN="", publishing="", pub_year="", author="", label="", uncheckout_num="", checkout_num=""):
        self.ID = ID  # 书的ID
        self.Name = Name  # 书名
        self.ISBN = ISBN  # 书的ISBN 数据类型为str
        self.publishing = publishing  # 出版社
        self.pub_year = pub_year  # 出版年月
        self.author = author  # 作者
        self.label = label  # 标签
        self.uncheckout_num = uncheckout_num  # 未借出书的数量
        self.checkout_num = checkout_num  # 借出书的数量

    def __str__(self):
        return "ID:{:<7} Name:{:<9} ISBN:{:<15} 出版社:{:<9} 出版年月:{:<8}\t作者:{:<12} 标签:{:<6} 在库数量:{:<3} 借出数量:{:<3}".format(self.ID, self.Name, self.ISBN, self.publishing, self.pub_year, self.author, self.label, self.uncheckout_num, self.checkout_num)

    def textreturn(self):
        return "ID:{:<7} Name:{:<9} ISBN:{:<15} 出版社:{:<9} 出版年月:{:<8}\t作者:{:<12} 标签:{:<6} 在库数量:{:<3} 借出数量:{:<3}".format(self.ID, self.Name, self.ISBN, self.publishing, self.pub_year, self.author, self.label, self.uncheckout_num, self.checkout_num)
    def textreturn_simplify(self):
        return "书名:{:<9}\tISBN:{:<15} 出版社:{:<9} 出版年月:{:<8}\t作者:{:<12} 标签:{:<6}".format(self.Name, self.ISBN, self.publishing, self.pub_year, self.author, self.label)
    

    def __eq__(self, other):
        #*意思为如果这两者的ID不相等且都不为空 那么返回False 即这两个组件不相等 反之相等
        if(self.ID != other.ID or self.ID == "" or other.ID == ""):
            return False
        else:
            if(self.Name != other.Name or self.Name == "" or other.Name == ""):
                return False
            else:
                if(self.ISBN != other.ISBN or self.ISBN == "" or other.ISBN == ""):
                    return False
                else:
                    if(self.publishing != other.publishing or self.publishing == "" or other.publishing == ""):
                        return False
                    else:
                        if(self.pub_year != other.pub_year or self.pub_year == "" or other.pub_year == ""):
                            return False
                        else:
                            if(self.author != other.author or self.author == "" or other.author == ""):
                                return False
                            else:
                                if(self.label!= other.label or self.label == "" or other.label == ""):
                                    return False
                                else:
                                    return True  #*表明上述检验全部通过 那么这两个元素的基本信息相等
#! 下面是图书类基本函数
def Books_data_read(r):
    df1 = pd.read_excel(r, header=0)
    # 'C:/Users/HP/Desktop/大三上计算机课程学习资料/面向对象编程/上机实验1/books_data.xlsx'
    df1 = df1.values  # 默认有9行
    books_list = []
    for j in df1:
        temp = book()  # 实例化
        try:
            temp.ID = str(j[0]) #*注意，因为所有数据都是以str形式保存并且参与运算的，所以这里必须要加上一个强制转换步骤
            temp.Name = str(j[1])
            temp.ISBN = str(j[2])
            temp.publishing = str(j[3])
            temp.pub_year = str(j[4])
            temp.author = str(j[5])
            temp.label = str(j[6])
            temp.uncheckout_num = str(j[7])
            temp.checkout_num = str(j[8])
        except IndexError:
            print("初始数据读取错误\n路径名为:"+r+"\n的初始数据的列数错误，请返回原始数据进行查看和修改")
            exit(1)
        books_list.append(temp)
    return books_list
def Books_massage_return(bookList):
    '''
    #*返回传入的图书列表所含信息的一个长字符串
    '''
    text = ""
    for i in bookList:
        temp = i.textreturn()+"\n"
        text += temp
    return text
def Books_massage_return_simplify(bookList):
    '''
    #*返回传入的图书列表所含信息的精简版
    '''
    text=""
    for i in bookList:
        temp = i.textreturn_simplify()+"\n"
        text += temp
    return text
def Books_list_extend(bookList_1, bookList_2):
    '''
    #*把第二个bookList的书籍信息加入到第一个booklist当中，如果出现重复的书籍信息，那么合并两个的入库和借出数量
    '''
    for i in bookList_2:
        lens=len(bookList_1)
        temp=copy.deepcopy(i)
        for index,j in enumerate(bookList_1):
            if (temp == j):
                if(temp.uncheckout_num=="" and j.uncheckout_num==""):
                    break#*什么也不做
                elif(temp.uncheckout_num=="" and j.uncheckout_num!=""):
                    j.uncheckout_num=temp.uncheckout_num
                    break
                elif(temp.uncheckout_num!="" and j.uncheckout_num==""):
                    break#*什么也不做
                else:
                    j.uncheckout_num = str(
                        int(j.uncheckout_num)+int(temp.uncheckout_num))
                    j.checkout_num = str(int(j.checkout_num)+int(temp.checkout_num))
                    break
                # 完成信息合并
            else:
                if(index== lens-1):
                    bookList_1.append(temp)
                    break
def Books_compare(b_1, b_2):
    '''
    #*判断book1是否在book2中
    '''
    step_1 = b_1.ID == "" or (b_1.ID in b_2.ID)
    step_2 = b_1.Name == "" or (b_1.Name in b_2.Name)
    step_3 = b_1.ISBN == "" or (b_1.ISBN in b_2.ISBN)
    step_4 = b_1.publishing == "" or (b_1.publishing in b_2.publishing)
    step_5 = b_1.pub_year == "" or (b_1.pub_year in b_2.pub_year)
    step_6 = b_1.author == "" or (b_1.author in b_2.author)
    step_7 = b_1.label == "" or (b_1.label in b_2.label)
    step_8 = b_1.uncheckout_num == "" or (b_1.uncheckout_num in b_2.uncheckout_num)
    step_9 = b_1.checkout_num == "" or (b_1.checkout_num in b_2.checkout_num)

    return step_9 and step_8 and step_7 and step_6 and step_5 and step_4 and step_3 and step_2 and step_1
def Books_searching(b,booklist):
    '''
    #*b为待搜索对象，booklist为搜索集，
    #*从booklist当中筛选对象添加到searchedlist当中，
    #*最后searchedlist为搜索完成后的书单
    '''
    searchedlist=[]
    for i in booklist:
        if(Books_compare(b,i)):
            temp=copy.deepcopy(i)
            searchedlist.append(temp)
    return searchedlist

#* 读者类的定义------------------------------------------------------------------------------------------------

class reader(object):
    def __init__(self, ID="", Name="", reader_type="", phone=""):
        self.ID = ID  # 读者ID
        self.Name = Name  # 读者姓名
        self.reader_type = reader_type  # vip 和 normal
        self.phone = phone  # 读者电话

    def __str__(self):
        return "ID:{:<6} Name:{:<7} 类型:{:<6} 电话:{:<11}".format(self.ID, self.Name, self.reader_type, self.phone)

    def textreturn(self):
        return "ID:{:<6} Name:{:<7} 类型:{:<6} 电话:{:<11}".format(self.ID, self.Name, self.reader_type, self.phone)

    def __eq__(self, other):
        if(self.ID != other.ID or self.ID=="" or other.ID==""):
            return False
        else:
            if(self.Name!=other.Name or self.Name=="" or other.Name==""):
                return False
            else:
                if(self.reader_type!=other.reader_type or self.reader_type == "" or other.reader_type == ""):
                    return False
                else:
                    if(self.phone!= other.phone or self.phone == "" or other.phone == ""):
                        return False
                    else:
                        return True #*表明上述检验全部通过 那么这两个元素的基本信息相等
    def get_borrow_list(self):
        return self.borrow_list
    def __lt__(self, other):
        step_1 = self.ID == "" or (self.ID in other.ID)
        step_2 = self.Name == "" or (self.Name in other.Name)
        step_3 = self.reader_type == "" or (self.reader_type in other.reader_type)
        step_4 = self.phone == "" or (self.phone in other.phone)
        return step_1 and step_2 and step_3 and step_4
#! 下面是读者类基本函数
def Readers_data_read(r):
    """
    #* 读取路径为r 返回一个读取完的list 注意这里并不会读取读者的借读书目和借书历史
    """
    df1 = pd.read_excel(r, header=0)
    df1 = df1.values  # 默认有9列
    readers_list = []
    for j in df1:
        temp = reader()  # 实例化
        try:
            temp.ID = str(j[0]) #*注意，因为所有数据都是以str形式保存并且参与运算的，所以这里必须要加上一个强制转换步骤
            temp.Name = str(j[1])
            temp.reader_type= str(j[2])
            temp.phone = str(j[3])
        except IndexError:
            print("初始数据读取错误\n路径名为:"+r+"\n的初始数据的列数错误，请返回原始数据进行查看和修改")
            exit(1)
        readers_list.append(temp)
    return readers_list
def Readers_massage_return(readerList):
    '''
    #*返回传入的图书列表所含信息的一个长字符串
    '''
    text = ""
    for i in readerList:
        temp = i.textreturn()+"\n"
        text += temp
    return text
def Readers_list_extend(readerList_1, readerList_2):
    '''
    #*把第二个readerList的书籍信息加入到第一个readerList当中，如果出现重复的书籍信息，那么跳过
    '''
    for i in readerList_2:
        lens=len(readerList_1)
        temp=copy.deepcopy(i)
        for index,j in enumerate(readerList_1):
            if (temp == j):#* 如果相等的话，那么跳过这个人信息的导入
                break
            else:
                if(index== lens-1):
                    readerList_1.append(temp)
                    break
def Readers_compare(r_1, r_2):
    '''
    #*判断reader1是否在reader2中
    '''
    step_1 = r_1.ID == "" or (r_1.ID in r_2.ID)
    step_2 = r_1.Name == "" or (r_1.Name in r_2.Name)
    step_3 = r_1.reader_type == "" or (r_1.reader_type in r_2.reader_type)
    step_4 = r_1.phone == "" or (r_1.phone in r_2.phone)
    return step_1 and step_2 and step_3 and step_4
def Readers_searching(r,readerlist):
    '''
    #*r为待搜索对象，readerlist为搜索集，
    #*从readerlist当中筛选对象添加到searchedlist当中，
    #*最后searchedlist为搜索完成后的读者名单
    '''
    searchedlist=[]
    for i in readerlist:
        if(Readers_compare(r,i)):
            temp=copy.deepcopy(i)
            searchedlist.append(temp)
    return searchedlist
#! 下面是借阅历史的类的定义
class history_tuple(object):
    def __init__(self,reader_1="",book_1=""):
        if(type(reader_1)==str):
            self.reader=reader()
        else:
            self.reader=copy.deepcopy(reader_1)
            self.reader.borrow_list=[]
        if(type(book_1)==str):
            self.book=book()
        else:
            self.book=copy.deepcopy(book_1)
    def __str__(self):
        return "借书人姓名:{:<6} 图书ID:{:<9} 书名:{:<9}\tISBN:{:<15} 出版社:{:<9} 出版年月:{:<8}\t作者:{:<12} 标签:{:<6}".format(
            self.reader.Name,self.book.ID,self.book.Name,self.book.ISBN,self.book.publishing,self.book.pub_year,self.book.author,self.book.label
            )
    def __eq__(self,other):
        if((self.book==other.book) and (self.reader==other.reader)):
            return True
        else:
            return False
def History_data_read(readerlist,road):
    """
    #* 读取路径为r 输入一个读者名单从中获取读者信息 
    #* 因为源文件只包含读者ID 最后返回一个借阅历史的列表
    """
    df = pd.read_excel(road, header=0)
    df = df.values  # 默认有9列
    listofhistory=[]
    k=len(readerlist) #* 整体长度
    for j in df: 
        temp = history_tuple()  # 实例化
        temp.book.ID=str(j[1])
        temp.book.Name=str(j[2])
        temp.book.ISBN=str(j[3])
        temp.book.publishing=str(j[4])
        temp.book.pub_year=str(j[5])
        temp.book.author=str(j[6])
        temp.book.label=str(j[7])
        index=0  #*标记
        for reader in readerlist:
            if(reader.ID==str(j[0])):
                temp.reader=copy.deepcopy(reader)
                listofhistory.append(temp)
                break
            else:
                index += 1
        if(index == k):
            index=0
            temp.reader.ID=str(j[0])
            listofhistory.append(temp)
    return listofhistory
def History_message_return(historylist):
    text=""
    for i in historylist:
        text+= str(i)+"\n"
    return text
def History_search(historylist,r=reader(),b=book()):
    """[summary]:
    #*输入比较条件，默认为空，如果比较条件均满足，那么返回一个从historylist中搜索到的list
    Args:
        r (reader): 待比较的reader
        b (book): 待比较的book
        historylist (list of history_tuple): 从这个list当中筛选对应的数据
    """
    history_searched_list=[]
    for i in historylist:
        if((r < i.reader) and Books_compare(b,i.book)):
            history_searched_list.append(i)
    return history_searched_list

#! 下面是输出到xlsx的函数
def booklist_output(road,booklist):
    """
    #* 将booklist里的内容按行输出到road代表的路径当中 .xlsx
    Args:
        road : 要写入的文件路径
        booklist : 待写入的书单
    """
    df_value=[]
    for i in booklist:
        temp=[i.ID,i.Name,i.ISBN,i.publishing,i.pub_year,i.author,i.label,i.uncheckout_num,i.checkout_num]
        df_value.append(temp)
    df=pd.DataFrame(df_value,columns=['ID','Name','ISBN','publishing','pub_year','author','label','uncheckout_num','checkout_num'],dtype=str)
    df.to_excel(road,index=False,header=True)
def readerlist_output(road,readerlist):
    """
    #* 将readerlist里的内容按行输出到road代表的路径当中 .xlsx
    Args:
        road : 要写入的文件路径
        readerlist : 待写入的读者名单
    """
    df_value=[]
    for i in readerlist:
        temp=[i.ID,i.Name,i.reader_type,i.phone]
        df_value.append(temp)
    df=pd.DataFrame(df_value,columns=['ID','Name','reader_type','phone'],dtype=str)
    df.to_excel(road,index=False,header=True)
def historylist_output(road,historylist):
    """
    #* 将historylist里的内容按行输出到road代表的路径当中 .xlsx
    Args:
        road : 要写入的文件路径
        historylist : 待写入的借书历史单
    """
    df_value=[]
    for i in historylist:
        temp=[i.reader.ID, i.book.ID, i.book.Name, i.book.ISBN, i.book.publishing, i.book.pub_year, i.book.author, i.book.label]
        df_value.append(temp)
    df=pd.DataFrame(df_value,columns=['reader\'s ID','ID','Name','ISBN','publishing','pub_year','author','label'],dtype=str)
    df.to_excel(road,index=False,header=True)
def borrowlist_output(road,borrowlist):
    """
    #* 将borrowlist里的内容按行输出到road代表的路径当中 .xlsx
    Args:
        road : 要写入的文件路径
        borrowlist : 待写入的借书历史单
    """
    df_value=[]
    for i in borrowlist:
        temp=[i.reader.ID, i.book.ID, i.book.Name, i.book.ISBN, i.book.publishing, i.book.pub_year, i.book.author, i.book.label]
        df_value.append(temp)
    df=pd.DataFrame(df_value,columns=['reader\'s ID','ID','Name','ISBN','publishing','pub_year','author','label'],dtype=str)
    df.to_excel(road,index=False,header=True)
#! 下面是测试程序
if __name__ == "__main__":
    # road3=r"C:\Users\HP\Desktop\大三上计算机课程学习资料\面向对象编程\数据备份\readers_data.xlsx"
    # readerList=Readers_data_read(road3)
    # for i in readerList:
    #     print(i)
    # print("\n\n\n\n")
    # road5=r"C:\Users\HP\Desktop\大三上计算机课程学习资料\面向对象编程\上机实验1\history_of_borrowed.xlsx"
    # historyList=History_data_read(readerList,road5)
    # for i in historyList:
    #     print(i)
    # road1 = "C:/Users/HP/Desktop/大三上计算机课程学习资料/面向对象编程/上机实验1/books_data.xlsx"
    # bookList = Books_data_read(road1)
    # for i in bookList:
    #     print(i)
    # road2 = r"C:\Users\HP\Desktop\大三上计算机课程学习资料\面向对象编程\上机实验1\批量导入书籍的测试数据.xlsx"
    # print("\n\n\n\n")
    # bookListInsert = Books_data_read(road2)
    # print("第一次塞")
    # Books_list_extend(bookList, bookListInsert)
    # for i in bookList:
    #     print(i)
    # print("\n\n\n\n")
    # Books_list_extend(bookList, bookListInsert)
    # print("第二次塞")
    # for i in bookList:
    #     print(i)
    # print("\n\n\n\n")
    # road3=r"C:\Users\HP\Desktop\大三上计算机课程学习资料\面向对象编程\数据备份\readers_data.xlsx"
    # readerList=Readers_data_read(road3)
    # for i in readerList:
    #     print(i)    
    # print("\n\n")
    # road4=r"C:\Users\HP\Desktop\大三上计算机课程学习资料\面向对象编程\数据备份\批量导入读者的测试数据.xlsx"
    # readerListInsert=Readers_data_read(road4)
    # Readers_list_extend(readerList,readerListInsert)
    # print("第一次塞")
    # for i in readerList:
    #     print(i)
    # print("第二次塞")
    # Readers_list_extend(readerList,readerListInsert)
    # for i in readerList:
    #     print(i)
    pass
    