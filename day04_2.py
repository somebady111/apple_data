# _*_coding:utf-8_*_
'''
1.用python读文件
2.绘制k线图
3.计算均值
4.求数据标准差*
'''
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 读取数据
def dmy2ymd(s):
    dmy = str(s,encoding='utf-8')
    time = dt.datetime.strptime(dmy,'%d-%m-%Y')
    ymd = time.date().strftime('%Y-%m-%d')
    return ymd

dates,opening_prices,highest_prices,lowest_prices,closing_prices,volums = np.loadtxt(
    '../da_data/aapl.csv',unpack=True,delimiter=',',usecols=(1,3,4,5,6,7),dtype='M8[D],f8,f8,f8,f8,f8',converters={1:dmy2ymd}
    )
print(dates,sep='\n')

# 求出closing_prices的标准差
std1 = np.std(closing_prices)
std2 = np.std(closing_prices,ddof=1)
print(std1,std2,sep='\n')

# 手动计算
m = np.mean(closing_prices) # 均值
m1 = closing_prices.mean() # 或者
d = closing_prices - m # 离差
q = d**2 # 离差方
v = sum(q)/len(q) # 总体方差
v1 = sum(q)/(len(q)-1) # 样本方差
s = np.sqrt(v) # 样本标准差
s1 = np.sqrt(v1)
print(m,m1,d,q,v,v1,s,s1,sep='\n')


