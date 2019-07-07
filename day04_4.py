# _*_coding:utf-8_*_
'''
1.用python读文件
2.绘制k线图
3.计算均值
4.求数据标准差
5.处理时间的实例应用
6.数据数组的轴向汇总
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

# 轴向汇总

# 获取所有元素下标
indices = np.arange(closing_prices.size)
mon_i = indices[wdays == 0]
tue_i = indices[wdays == 1]
wed_i = indices[wdays == 2]
thu_i = indices[wdays == 3]
fri_i = indices[wdays == 4]

# 补全缺失值,首位补0个数，末尾补2个数
mon_i = np.pad(mon_i,pad_width=(0,2),mode='constant',constant_values=0)
tue_i = np.pad(tue_i,pad_width=(0,1),mode='constant',constant_values=0)
wed_i = np.pad(wed_i,pad_width=(0,1),mode='constant',constant_values=0)
thu_i = np.pad(thu_i,pad_width=(0,1),mode='constant',constant_values=0)
fri_i = np.pad(fri_i,pad_width=(0,0),mode='constant',constant_values=0)

# 整理二维数组
data = np.array([mon_i,tue_i,wed_i,thu_i,fri_i])

# 轴向汇总
def func(row):
    # 掩码，在数组中放多个下标
    row = row[row != -1]
    return closing_prices[row].max(),closing_prices[row].min(),closing_prices[row].mean()

rep = np.apply_along_axis(func,1,data)

print(rep)
