from pandas import DataFrame, read_excel
import numpy as np
from sklearn import linear_model

def data_form(sep=0.1):
    """
    #*产生测试数据
    """
    x=np.arange(0,10,sep)
    length_x=len(x)
    epsilon= np.random.normal(2, 4, size=length_x)
    y=x**2+x+epsilon 
    return [x,y]
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
if  __name__== "__main__" :
    test_data=data_form()
    result=simple_linear(test_data[0],test_data[1],degree=2)
    print(result)
