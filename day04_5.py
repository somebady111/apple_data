# _*_coding:utf-8_*_
'''
1.用python读文件
2.绘制k线图
3.计算均值
4.绘制均线*
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
print(dates)

# 绘制折线图
mp.figure('Closeing Prices',facecolor='lightgray')
mp.title('Closeing Prices',fontsize=14)
mp.xlabel('Date',fontsize=12)
mp.ylabel('Closeing Prices',fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)

# 设置刻度
# 获取到当前坐标轴
ax = mp.gca()
# 设置主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# 设置刻度格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
# 设置时间刻度
ax.xaxis.set_minor_locator(md.DayLocator())

# 将dates转换为matplotlib识别的Datetime类型
dates = dates.astype(md.datetime.datetime)
mp.plot(dates,closing_prices,c='dodgerblue',linewidth=2,linestyle='--',label='Closeing Prices',alpha=0.6)

# 绘制k线图
# 实体高度
rise = closing_prices <= opening_prices

# 整理填充色,三目运算符
color = np.array([('white' if x else 'green') for x in rise])

# 整理边缘色
edgecolor = np.array([('red' if x else 'green') for x in rise])

# 绘制影线,lowest_prices最低价，hightest最高价
mp.vlines(dates,lowest_prices,highest_prices,color=edgecolor)

# 绘制实体，宽度0.8,opening_prices开始绘制位置,edgecolor边缘色
mp.bar(dates,closing_prices-opening_prices,0.8,opening_prices,color=color,edgecolor=edgecolor,zorder=3)

# 绘制均值线
m = np.mean(closing_prices)
mp.hlines(m,dates[0],dates[-1],color='red',label='AVG(cp)')

# 绘制交易量加权均线
vwap = np.average(closing_prices,weights=volums)
mp.hlines(vwap,dates[0],dates[-1],color='blue',label='AVG(wap)')

# 评估apl的股票波动性
max_v = np.max(highest_prices)
min_v = np.min(lowest_prices)
print(max_v,min_v)

# 查看apl的最大最小的日期
max_i = np.argmax(highest_prices)
min_i = np.argmin(lowest_prices)
print('max date',dates[max_i])
print('min date',dates[min_i])

# 中位数
closing_prices = np.msort(closing_prices)
median = np.median(closing_prices)
mp.hlines(median,dates[0],dates[-1],color='black',label='Median')

# 绘制均线
sma5 = np.zeros(closing_prices.size -4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i+10].mean()
mp.plot(dates[4:],sma5,c='purple',label='SMA-5')

# 卷积绘制均线
kernel = np.ones(10)/10
sma10_2 = np.convolve(closing_prices,kernel,'valid')
mp.plot(dates[9:],sma10_2,c = 'violet',linewidth=2,label='SMA-10')

# 加权卷积绘制均线
kernel = np.exp(np.linspace(-1, 0, 5))[::-1]
kernel /= kernel.sum() # 保证权重相加等于1
sma5_1 = np.convolve(closing_prices, kernel, 'valid')
mp.plot(dates[4:], sma5_1, c='yellow',
        label='SMA-5_1')

mp.legend()
# 设置x轴的日期可视化
mp.gcf().autofmt_xdate()
mp.tight_layout()
mp.show()
