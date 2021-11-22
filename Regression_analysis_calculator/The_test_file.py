import numpy as np
x=np.arange(0,10,0.1)
length_x=len(x)
epsilon= np.random.normal(2, 1, size=length_x)
y=x**2+x+epsilon #*产生测试数据
ploy=np.polyfit(x,y,2,rcond = None,full = True,w = None,cov = False )
print(ploy)
sigma_2 = (ploy[1])[0]/(length_x-1)#* sigma^2的最小二乘估计 为RSS/(n-p) p=rank(X)
print(sigma_2)
RSS=ploy[1][0]
SS_y=length_x*np.var(y)#* R^2
R_2=(SS_y-RSS)/SS_y
print(R_2)