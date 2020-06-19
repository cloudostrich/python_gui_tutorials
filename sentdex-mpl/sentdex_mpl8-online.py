import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt,encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter #(strconverter)

def graph_data(stock):
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
                        
    plt.plot_date(date, closep,'-', label='Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('main title')
    plt.legend()
    plt.show()

graph_data('AAPL')
