import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib

style.use('seaborn-notebook')
print(plt.style.available)
print(plt.__file__)

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

##    ax1.plot(date,closep, label='close')
##    ax1.plot(date,openp, label='open')
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y)%m-%d'))
    ax1.grid(True)

    # Annotate Last Price
    bbox_props = dict(boxstyle='larrow', fc='w',ec='k', lw=1)
    ax1.annotate(str(closep[1]), (date[1], closep[1]),
                 xytext= (date[1]+20, closep[1]),
                 bbox = bbox_props)

##    # Annotate with arrow
##    ax1.annotate('Big News!', (date[20], highp[20]),
##                 xytext=(0.8, 0.9), textcoords='axes fraction',
##                 arrowprops = dict(facecolor='grey', color='grey'))
##    
##    # Placing Text with font-dict
##    font_dict = {'family':'serif',
##                 'color': 'darkred',
##                 'size':15}
##    ax1.text(date[10], closep[10], 'wat de frag', fontdict=font_dict)

    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()

graph_data('AAPL')
