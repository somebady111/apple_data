# _*_coding:utf-8_*_
'''
1.用python读文件
2.绘制k线图
3.计算均值
4.求数据标准差
5.处理时间的实例应用*
'''
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 读取数据
def dmywday(s):
    dmy = str(s,encoding='utf-8')
    time = dt.datetime.strptime(dmy,'%d-%m-%Y')
    wdays = time.date().weekday() # 转换为周几,并返回
    return wdays

wdays,closing_prices = np.loadtxt(
    '../da_data/aapl.csv',unpack=True,delimiter=',',usecols=(1,6),dtype='f8,f8',converters={1:dmywday}
    )

# 返回数值中0代表周一
avg_prices = np.zeros(5)
for wday in range(avg_prices.size):
    avg_prices[wday] = closing_prices[wdays == wday].mean() # 算出的均值存入到数组中

# 双列表遍历
for wday,avg_prices in zip(['Mon','Tue','Wed','Thu','Fri'],avg_prices):
    print(wday,':',avg_prices)

