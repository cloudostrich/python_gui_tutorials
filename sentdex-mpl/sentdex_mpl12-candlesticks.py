import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np
import urllib


def bytespdate2num(fmt,encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter #(strconverter)

def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    
    
    ''' try modify with quandl and pandas'''
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()#'utf-8')
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'Date' not in line:
                stock_data.append(line)
        

    date, closep, highp, lowp, openp,settlep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year
                                                          # %y = part year
                                                          # %m = month
                                                          # %d = day
                                                          # %H = hr
                                                          # %M = minute
                                                          # %S = seconds
                                                          converters={0: bytespdate2num('%Y-%m-%d')})
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y)%m-%d'))
    ax1.grid(True) 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()

graph_data('AAPL')
