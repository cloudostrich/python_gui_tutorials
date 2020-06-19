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

MA1 = 10
MA2 = 30

def sma(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows

highs = [11,12,13,15,17]
lows = [1,2,3,4,5]
##h_l = list(map(high_minus_low, highs, lows))
##print(h_l)

def bytespdate2num(fmt,encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter #(strconverter)

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((6,1),(0,0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1),(1,0), rowspan=4, colspan=1)
##    plt.xlabel('Date') # wasted space?
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1)
    plt.ylabel('SMA')
    
    ''' try modify with quandl and pandas'''
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()#'utf-8')
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[:500]:
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

    ma1 = sma(closep, MA1)
    ma2 = sma(closep, MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date, h_l, '-')
    ax1.grid(True)
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='lower')) 
##    ax1.plot(date,closep, label='close')
##    ax1.plot(date,openp, label='open')
    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')
    
    
    ax2.grid(True)

    # Annotate Last Price
    bbox_props = dict(boxstyle='larrow', fc='w',ec='k', lw=1)
    ax2.annotate(str(closep[1]), (date[1], closep[1]),
                 xytext= (date[1]+5, closep[1]),
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

    print(len(date), len(ma1))
    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)
    ax3.grid(True)
    
    ax3.fill_between(date[-start:], ma2[-start:],
                     ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r', edgecolor='r', alpha=0.5)
    ax3.fill_between(date[-start:], ma2[-start:],
                     ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y)%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
##    ax3.set_yticks([0,10,20,30,40,50])

    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.16, right=0.94, top=0.9, wspace=0.2, hspace=0)
    plt.show()

graph_data('AAPL')
