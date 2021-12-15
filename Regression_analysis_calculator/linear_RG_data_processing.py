from pandas import DataFrame, read_csv
import numpy as np
from scipy.optimize import curve_fit
#*----------------------------------------------------------------功能型函数
def data_read(path="data\data.txt",sep="\t",head=0):
    """
    #*用pandas读取txt文件，间隔默认为'\t',默认没有表头
    """
    df=read_csv(path,sep=sep,header=head,dtype=np.float64)
    df=df.values.transpose()
    return df


def data_write(data,path="data\data.txt",sep='\t'):
    df=DataFrame(data.transpose(),columns=['x','y'])
    df.to_csv(path,sep=sep,index=False)

def parameters_write(data,path="data/result.txt",sep="\t"):
    """
    #* 利用pandas将data写到文件中去
    """
    p=["参数"]
    p.extend(data[0])#* data[0]中存储的是参数数据
    p=DataFrame(p)
    p.to_csv(path,sep=sep,index=False,header=False)
    print(data[1:])
    df=np.array([["Var(y):","Mean(y):","RSS:","sigma^2的LS:","决定系数R^2:"],data[1:]])
    df=DataFrame(df.transpose())
    df.to_csv(path,sep=sep,index=False,header=False,mode='a')

def data_form(sep=0.1):
    """
    #*产生测试数据
    """
    start=sep
    x=np.arange(start,10,sep)
    length_x=len(x)
    np.random.seed(4)
    epsilon= 0.1*np.random.normal(2, 1, size=length_x)
    y=func_log(x,0.5,3.3,2.3) 
    y=y + epsilon
    return np.array([x,y])
def RSS_relative_analysis(y,y_predict):
    """
    #* 返回一个顺序为：RSS残差平方和,sigma^2:均值为0的正太分布的方差的最小二乘estimate,R^2:决定系数  的np数组
    Args:
        y ([type]): 原始y的数据
        y_predict ([type]): 拟合后y的数据
    """
    RSS= np.sum((y-y_predict)**2)
    SS_y=len(y)*np.var(y)
    R_2=(SS_y-RSS)/SS_y
    sigma_2 = RSS/(len(y)-1)
    return np.array([RSS,sigma_2,R_2])
def func_pow(x,a,b,c):
    """
    #*幂函数，返回a*x^c + b
    """
    return a * x ** c + b
def func_exp(x,a,b,c):
    """
    #*指数函数，返回a*exp(cx) + b
    """
    return a * np.exp(c*x) + b
def func_log(x,a,b,c):
    """
    #*对数函数，返回a*log(x+c) + b
    """
    return a * np.log(x+c) + b

#*--------------------------------------------------------主要函数
#! 多项式回归(包含简单线性回归)
def simple_linear(x=None,y=None,degree=1):
    """
    #* 支持2维数据的拟合，简单线性拟合，并且返回一个参数列表
    #* 刑如array[array[里面是各阶的参数,包括常数项b^2的最小二乘估计],RSS残差平方和,sigma^2:均值为0的正太分布的方差的最小二乘estimate,R^2:决定系数]
    #*Args:
        #*x (一维数组): 作为采样的x. Defaults to None.
        #*y (一维数组): 作为采样的y. Defaults to None.
        #*degree(拟合的阶数):      Defaults to 1.
    """
    length_x=len(x)
    ploy=np.polyfit(x,y,degree,full = True,cov = False)
    RSS=ploy[1][0]
    sigma_2 = RSS/(length_x-1)#* sigma^2的最小二乘估计 为RSS/(n-p) p=rank(X)
    SS_y=length_x*np.var(y)#* R^2
    R_2=(SS_y-RSS)/SS_y
    result=[ploy[0],RSS,sigma_2,R_2]
    return result
def simple_linear_predict(x=None,coe=None):
    """
    #* x为待预测的自变量（可以是单个值也可以是一维数组） coe为参数数组，对应的阶数参数从高到低
    Args:
        x ([type], optional): Defaults to None.
        coe ([type], optional): Defaults to None.
    """
    coe_l=len(coe)
    y=np.zeros(len(x))
    for i in range(0,coe_l):
        y += coe[i]*x**(coe_l-1-i) #* 例如coe[0]表示最高次项系数 coe[len(coe)-1]表示常数项系数
    return y #* 完成predict


#! 幂回归(特指y=ax^c + b)
def pow_regression(x=None,y=None):
    popt, pcov = curve_fit(func_pow, x, y,maxfev = 10000)
    return popt
def pow_predict(x,a,b,c):
    """
    #* 传入三个参数，一般为对应的LS估计，并返回对应的值或者数组
    """
    y_predict=func_pow(x,a,b,c)
    return y_predict


#! 指数回归(特指y=ae^x + b)
def exp_regression(x=None,y=None):
    popt, pcov = curve_fit(func_exp, x, y,maxfev = 10000)
    return popt
def exp_predict(x,a,b,c):
    """
    #* 传入三个参数，一般为对应的LS估计，并返回对应的值或者数组
    """
    y_predict=func_exp(x,a,b,c)
    return y_predict


#! 对数回归(特指y=alog(x+c) + b)
def log_regression(x=None,y=None):
    popt, pcov = curve_fit(func_log, x, y,maxfev = 10000)
    return popt


def log_predict(x,a,b,c):
    """
    #* 传入三个参数，一般为对应的LS估计，并返回对应的值或者数组
    """
    y_predict=func_log(x,a,b,c)
    return y_predict
if  __name__== "__main__" :
    test_data=data_form()
    result=pow_regression(x=test_data[0],y=test_data[1])
    print(result)
    data_write(test_data)