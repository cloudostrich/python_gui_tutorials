import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
##from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc

import tkinter as tk
from tkinter import ttk

import urllib
import json
import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 8)
FUNNY_FONT = ("Comic Sans MS", 12)
style.use("ggplot")
# style.use("dark_background")

f = plt.figure()
##a = f.add_subplot(111)
exchange = "BTC-e"
DatCounter = 9000
programName = "btce"
resampleSize = "15Min"
dataPace = 'tick'
candleWidth = 0.008

topIndicator = 'none'
mainIndicator = 'none'
bottomIndicator = 'none'

darkColor = "#183A54"
lightColor="#00A3E0"
EMAs = []
SMAs=[]
chartLoad = True

paneCount = 1

def loadChart(run):
        global chartLoad
        if run =='start':
                chartLoad = True
        elif run == 'stop':
                chartLoad=False

def tutorial():
##        def leavemini(what):
##                what.destroy()
        def page2():
                tut.destroy()
                tut2 = tk.Tk()

                def page3():
                        tut2.destroy()
                        tut3 = tk.Tk()
                        tut3.wm_title('part 3')
                        label = ttk.Label(tut3, text='part 3', font=NORM_FONT)
                        label.pack(side='top', fill='x',pady=10)
                        B1 = ttk.Button(tut3, text='Done', command=tut3.destroy)
                        B1.pack()
                        tut3.mainloop()
                        
                tut2.wm_title('part 2')
                label = ttk.Label(tut2, text='part 2', font=NORM_FONT)
                label.pack(side='top', fill='x',pady=10)
                B1 = ttk.Button(tut2, text='Next', command=page3)
                B1.pack()
                tut2.mainloop()
        tut = tk.Tk()
        tut.wm_title('Tutorial')
        label = ttk.Label(tut, text='what you want?', font=NORM_FONT)
        label.pack(side='top', fill='x', pady=10)
        B1 = ttk.Button(tut, text='Overview', command=page2)
        B1.pack()
        B2 = ttk.Button(tut, text='how to trade', command=lambda:popupmsg('not yet ready'))
        B2.pack()
        B3 = ttk.Button(tut, text='how to indicator', command=lambda:popupmsg('not yet ready'))
        B3.pack()
        tut.mainloop()

def addMainindicator(what):
        global mainIndicator, DatCounter
        if dataPace =='tick':
                popupmsg('No indicators for ticks')
        if what !='none':
                if mainIndicator =='none':
                        if what =='sma':
                                midIQ = tk.Tk()
                                midIQ.wm_title('Periods?')
                                label = ttk.Label(midIQ, text='Choose periods.')
                                label.pack(side='top', fill='x', pady=10)
                                e = ttk.Entry(midIQ)
                                e.insert(0,10)
                                e.pack()
                                e.focus_set()

                                def callback():
                                        global mainIndicator, DatCounter
                                        mainIndicator = []
                                        periods = (e.get())
                                        group = []
                                        group.append('sma')
                                        group.append(int(periods))
                                        mainIndicator.append(group)
                                        DatCounter = 9000
                                        print('main indicator set to:', mainIndicator)
                                        midIQ.destroy()
                                b = ttk.Button(midIQ, text='submit', width=10, command=callback)
                                b.pack()
                                tk.mainloop()

                        if what =='ema':
                                midIQ = tk.Tk()
                                midIQ.wm_title('Periods?')
                                label = ttk.Label(midIQ, text='Choose periods.')
                                label.pack(side='top', fill='x', pady=10)
                                e = ttk.Entry(midIQ)
                                e.insert(0,10)
                                e.pack()
                                e.focus_set()

                                def callback():
                                        global mainIndicator, DatCounter
                                        mainIndicator = []
                                        periods = (e.get())
                                        group = []
                                        group.append('ema')
                                        group.append(int(periods))
                                        mainIndicator.append(group)
                                        DatCounter = 9000
                                        print('main indicator set to:', mainIndicator)
                                        midIQ.destroy()
                                b = ttk.Button(midIQ, text='submit', width=10, command=callback)
                                b.pack()
                                tk.mainloop()

                else:
                        if what =='sma':
                                midIQ = tk.Tk()
                                midIQ.wm_title('Periods?')
                                label = ttk.Label(midIQ, text='Choose periods.')
                                label.pack(side='top', fill='x', pady=10)
                                e = ttk.Entry(midIQ)
                                e.insert(0,10)
                                e.pack()
                                e.focus_set()

                                def callback():
                                        global mainIndicator, DatCounter
##                                        mainIndicator = []
                                        periods = (e.get())
                                        group = []
                                        group.append('sma')
                                        group.append(int(periods))
                                        mainIndicator.append(group)
                                        DatCounter = 9000
                                        print('main indicator set to:', mainIndicator)
                                        midIQ.destroy()
                                b = ttk.Button(midIQ, text='submit', width=10, command=callback)
                                b.pack()
                                tk.mainloop()

                        if what =='ema':
                                midIQ = tk.Tk()
                                midIQ.wm_title('Periods?')
                                label = ttk.Label(midIQ, text='Choose periods.')
                                label.pack(side='top', fill='x', pady=10)
                                e = ttk.Entry(midIQ)
                                e.insert(0,10)
                                e.pack()
                                e.focus_set()

                                def callback():
                                        global mainIndicator, DatCounter
##                                        mainIndicator = []
                                        periods = (e.get())
                                        group = []
                                        group.append('ema')
                                        group.append(int(periods))
                                        mainIndicator.append(group)
                                        DatCounter = 9000
                                        print('main indicator set to:', mainIndicator)
                                        midIQ.destroy()
                                b = ttk.Button(midIQ, text='submit', width=10, command=callback)
                                b.pack()
                                tk.mainloop()
        else:
                mainIndicator='none'
                
def addTopindicator(what):
        global topIndicator, DatCounter
        if dataPace == 'tick':
                popupmsg(' No indicators for ticks')
        elif what =='none':
                topIndicator=what
                datCounter=9000

        elif what=='rsi':
                rsiQ  = tk.Tk()
                rsiQ.wm_title('Periods?')
                label = ttk.Label(rsiQ, text='Choose periods')
                label.pack(side='top', fill='x', pady=10)

                e = ttk.Entry(rsiQ)
                e.insert(0,14)
                e.pack()
                e.focus_set()

                def callback():
                        global topIndicator, DatCounter
                        periods = (e.get())
                        group = []
                        group.append('rsi')
                        group.append(periods)
                        topIndicator=group
                        DatCounter=9000
                        print('set top indicator to',group)
                        rsiQ.destroy()

                b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

        elif what == 'macd':
##                global topIndicator, DatCounter
                topIndicator = 'macd'
                DatCounter = 9000

def addBottomindicator(what):
        global Bottomindicator, DatCounter
        if dataPace == 'tick':
                popupmsg(' No indicators for ticks')
        elif what =='none':
                Bottomindicator=what
                datCounter=9000

        elif what=='rsi':
                rsiQ  = tk.Tk()
                rsiQ.wm_title('Periods?')
                label = ttk.Label(rsiQ, text='Choose periods')
                label.pack(side='top', fill='x', pady=10)

                e = ttk.Entry(rsiQ)
                e.insert(0,14)
                e.pack()
                e.focus_set()

                def callback():
                        global Bottomindicator, DatCounter
                        periods = (e.get())
                        group = []
                        group.append('rsi')
                        group.append(periods)
                        Bottomindicator=group
                        DatCounter=9000
                        print('set bottom indicator to',group)
                        rsiQ.destroy()

                b = ttk.Button(rsiQ, text='Submit', width=10, command=callback)
                b.pack()
                tk.mainloop()

        elif what == 'macd':
##                global Bottomindicator, DatCounter
                Bottomindicator = 'macd'
                DatCounter = 9000
                
def changeTimeframe(tf):
        global dataPace, DatCounter
        if tf =="7d" and resampleSize =="1Min":
                popupmsg(" Too much data, I am not updated yet to handle it")
        else:
                dataPace = tf
                DatCounter = 9000

def changeSampleSize(size, width):
        global resampleSize, DatCounter, candleWidth
        if dataPace =='7d' and resampleSize =='1Min':
                popupmsg('Too much data, I am not updated yet to handle it')
        elif dataPace == 'tick':
                popupmsg('you r a fucking idiot')
        else:
                resampleSize = size
                datCounter = 9000
                candleWidth = width

def changeExchange(toWhat,pn):
	global exchange, DatCounter, programName
	exchange = toWhat
	programName = pn
	DatCounter = 9000
	
def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("!")
	label = ttk.Label(popup, text=msg, font=FUNNY_FONT)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
	B1.pack()
	popup.mainloop()
	
def animate(i):	# render in time intervals, not as updates happen
        global refreshRate, DatCounter

        if chartLoad:
                if paneCount == 1:
                        if dataPace == 'tick':
                                try:
                                        if exchange == "BTC-e":
                                                a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                                                a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                                                                                        
                                                dataLink = 'https://api.bitfinex.com/v1/trades/BTCUSD?limit=100' #?limit_trades=10'
                                                data = urllib.request.urlopen(dataLink)
                                                data = data.readline().decode("utf-8")
                                                data = json.loads(data)
                                                data = pd.DataFrame(data)

                                                data['datestamp'] = np.array(data['timestamp']).astype('datetime64[s]')
                                                allDates = data['datestamp'].tolist()

                                                buys = data[(data.loc[:,'type']=="buy")]  #updated to use .loc
        ##                                        buys.loc[:,'datestamp'] = pd.to_datetime(buys['timestamp'], unit='s')
                                                buyDates = (buys["datestamp"]).tolist()

                                                sells = data[(data.loc[:,'type']=="sell")] #updated to use .loc
        ##                                        sells.loc[:,"datestamp"]  = pd.to_datetime(sells['timestamp'], unit='s')
                                                sellDates = (sells["datestamp"]).tolist()

                                                volume = data['amount']

                                                a.clear()

        ##                                        a.plot_date(buys['datestamp'], buys["price"], "g",label="buys")
        ##                                        a.plot_date(sells['datestamp'], sells["price"], "r", label="sells")
                                                a.plot_date(buyDates, buys["price"], lightColor, label="buys")
                                                a.plot_date(sellDates, sells["price"], darkColor, label="sells")

                                                a2.fill_between(allDates, 0, volume, facecolor= 'g')
                                                a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                                                a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                                                plt.setp(a.get_xticklabels(), visible=False)
                                                
                                                a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                                                title = f"\nBitFinex BTCUSD Prices\nLast Price: {str(data['price'][0])}"
                                                a.set_title(title)
                                                priceData =data['price'].apply(float).tolist()

                                        if exchange == 'Bitstamp':
                                                a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                                                a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                                                                                        
                                                dataLink = 'https://www.bitstamp.net/api/transactions/' #?limit_trades=10'
                                                data = urllib.request.urlopen(dataLink)
                                                data = data.readline().decode("utf-8")
                                                data = json.loads(data)
                                                data = pd.DataFrame(data)

                                                data['datestamp'] = np.array(data['date'].apply(int)).astype('datetime64[s]')
                                                
                                                allDates = data['datestamp'].tolist()

##                                                buys = data[(data.loc[:,'type']=="buy")]  #updated to use .loc
##                                                buyDates = (buys["datestamp"]).tolist()
##
##                                                sells = data[(data.loc[:,'type']=="sell")] #updated to use .loc
##                                                sellDates = (sells["datestamp"]).tolist()

                                                volume = data['amount'].apply(float).tolist()

                                                a.clear()

                                                a.plot_date(allDates, data["price"], lightColor, label="buys")
##                                                a.plot_date(sellDates, sells["price"], darkColor, label="sells")
                                                a2.fill_between(allDates, 0, volume, facecolor= 'g')
                                                a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                                                a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                                                plt.setp(a.get_xticklabels(), visible=False)

                                                a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                                                title = f"\nBitstamp BTCUSD Prices\nLast Price: {str(data['price'][0])}"
                                                a.set_title(title)
                                                priceData =data['price'].apply(float).tolist()

                                        if exchange == 'Bitfinex':
                                                a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                                                a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                                                                                        
                                                dataLink = 'https://api.bitfinex.com/v1/trades/btcusd?limit=2000' #?limit_trades=10'
                                                data = urllib.request.urlopen(dataLink)
                                                data = data.readline().decode("utf-8")
                                                data = json.loads(data)
                                                data = pd.DataFrame(data)

                                                data['datestamp'] = np.array(data['timestamp']).astype('datetime64[s]')
                                                allDates = data['datestamp'].tolist()

                                                buys = data[(data.loc[:,'type']=="buy")]  #updated to use .loc
        ##                                        buys.loc[:,'datestamp'] = pd.to_datetime(buys['timestamp'], unit='s')
                                                buyDates = (buys["datestamp"]).tolist()

                                                sells = data[(data.loc[:,'type']=="sell")] #updated to use .loc
        ##                                        sells.loc[:,"datestamp"]  = pd.to_datetime(sells['timestamp'], unit='s')
                                                sellDates = (sells["datestamp"]).tolist()

                                                volume = data['amount'].apply(float).tolist()

                                                a.clear()

                                                a.plot_date(allDates, data["price"], lightColor, label="buys")
##                                                a.plot_date(sellDates, sells["price"], darkColor, label="sells")
                                                a2.fill_between(allDates, 0, volume, facecolor= 'g')
                                                a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                                                a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
                                                plt.setp(a.get_xticklabels(), visible=False)

                                                a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                                                title = f"\nBitFinex BTCUSD Prices\nLast Price: {str(data['price'][0])}"
                                                a.set_title(title)

                                                priceData =data['price'].apply(float).tolist()

                                        if exchange == "Huobi":
                                                pass
##                                                a = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
##                                                dataLink = 'http://seaofbtc.com/api/basic/price?key=1&tf=1d&exchange='+programName
##                                                data = urllib.request.urlopen(dataLink).read().decode()
##
##                                                data = json.loads(data)
                                                
                                except Exception as e:
                                        print('Failed because of:', e)
                                        
                        else:
                                if DatCounter > 12:
                                        try:
                                                if exchange =='Huobi':
                                                        if topIndicator != 'none':
                                                                a = plt.subplot2grid((6,4), (1,0), rowspan=5, colspan=4)
                                                                a2 = plt.subplot2grid((6,4),(0,0), sharex=a, rowspan=1, colspan=4)
                                                        else:
                                                                a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)

                                                else:
                                                        if topIndicator !='none' and bottomIndicator !='none':
                                                                # Main Graph
                                                                a = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)
                                                                # Volume
                                                                a2 = plt.subplot2grid((6,4),(4,0), sharex=a, rowspan=1, colspan=4)
                                                                # Bottom Indicator
                                                                a3 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                                                                # Top Indicator
                                                                a0 = plt.subplot2grid((6,4),(0,0), sharex=a, rowspan=1, colspan=4)

                                                        elif topIndicator != 'none':
                                                                # Main Graph
                                                                a = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)
                                                                # Volume
                                                                a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                                                                # Bottom Indicator
##                                                                a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                                                                # Top Indicator
                                                                a0 = plt.subplot2grid((6,4),(0,0), sharex=a, rowspan=1, colspan=4)

                                                        elif bottomIndicator != 'none':
                                                                # Main Graph
                                                                a = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4)
                                                                # Volume
                                                                a2 = plt.subplot2grid((6,4),(4,0), sharex=a, rowspan=1, colspan=4)
                                                                # Bottom Indicator
##                                                                a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                                                                # Top Indicator
                                                                a3 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)
                                                        else:
                                                                # Main Graph
                                                                a = plt.subplot2grid((6,4), (1,0), rowspan=5, colspan=4)
                                                                # Volume
                                                                a2 = plt.subplot2grid((6,4),(5,0), sharex=a, rowspan=1, colspan=4)

                                                data = urllib.request.urlopen('http://seaofbtc.com/api/basic/price?key=1&tf='+dataPace+'&exchange='+programName)
                                                data = data.decode()
                                                data = json.loads(data)
                                                dateStamp = np.srray(data[0]).astype('datetime64[s]')
                                                dateStamp = dateStamp.tolist()

                                                df = pd.DataFrame({'Datetime':dateStamp})
                                                df['Price'] = data[1]
                                                df['Volume'] = data[2]
                                                df['Symbol'] = 'BTCUSD'
                                                df['MPLDate'] = df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                                                df = df.set_index('Datetime')

                                                OHLC = df['Price'].resample(resampleSize, how='ohlc')
                                                OHLC = OHLC.dropna()

                                                volumeData = df['Volume'].resample(resampleSize, how={'volume':'sum'})

                                                OHLC['dateCopy'] = OHLC.index
                                                OHLC['MPLDates'] = OHLC['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                                                del OHLC['dateCopy']

                                                volumeData['dateCopy'] = volumeData.index
                                                volumeData['MPLDates'] = volumeData['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                                                del volumeData['dateCopy']

                                                priceData =OHLC['close'].apply(float).tolist()
                                                
                                                                              
                                        except Exception as e:
                                                print('failed in the non-tick animate:' +str(e))
	
def ShutProgram():
	app.destroy()

class SeaofBTCapp(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
##		tk.Tk.iconbitmap(self, default="icon-mongol-24.ico")
		tk.Tk.wm_title(self,"GhenghisKhan!!!")
		
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		menubar = tk.Menu(container)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save Settings", command = lambda: popupmsg("Not supported yet!"))
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=quit)
		menubar.add_cascade(label="File", menu=filemenu)
		
		exchangeChoice = tk.Menu(menubar, tearoff=1)
		exchangeChoice.add_command(label="BTC-e", 
			command=lambda: changeExchange("BTC-e", "btc-e"))
		exchangeChoice.add_command(label="Bitfinex", 
			command=lambda: changeExchange("Bitfinex", "bitfinex"))
		exchangeChoice.add_command(label="Bitstamp", 
			command=lambda: changeExchange("Bitstamp", "bitstamp"))
		exchangeChoice.add_command(label="Huobi", 
			command=lambda: changeExchange("Huobi", "huobi"))
		menubar.add_cascade(label="Exchange", menu=exchangeChoice)
		
		dataTF = tk.Menu(menubar, tearoff=1)
		dataTF.add_command(label = "Tick", command=lambda: changeTimeframe('tick'))
		dataTF.add_command(label = "1 day", command=lambda: changeTimeframe('1d'))
		dataTF.add_command(label = "3 days", command=lambda: changeTimeframe('3d'))
		dataTF.add_command(label = "1 week", command=lambda: changeTimeframe('7d'))
		menubar.add_cascade(label="Data Time Frame", menu=dataTF)
		
		OHLCI = tk.Menu(menubar, tearoff=1)
		OHLCI.add_command(label="Tick", command=lambda: changeSampleSize('tick', 0.0001))
		OHLCI.add_command(label="1 minute", command=lambda: changeSampleSize('1Min', 0.0005))
		OHLCI.add_command(label="5 minute", command=lambda: changeSampleSize('5Min', 0.003))
		OHLCI.add_command(label="15 minute", command=lambda: changeSampleSize('15Min', 0.008))
		OHLCI.add_command(label="30 minute", command=lambda: changeSampleSize('30Min', 0.016))
		OHLCI.add_command(label="1 Hour", command=lambda: changeSampleSize('1H', 0.032))
		OHLCI.add_command(label="3 Hour", command=lambda: changeTimeframe('3H', 0.096))
		menubar.add_cascade(label="OHLC Interval", menu=OHLCI)

		topIndi = tk.Menu(menubar, tearoff=1)
		topIndi.add_command(label="None",  command=lambda: addTopindicator("none"))
		topIndi.add_command(label="RSI",  command=lambda: addTopindicator("rsi"))
		topIndi.add_command(label="MACD",  command=lambda: addTopindicator("macd"))
		menubar.add_cascade(label='Top Indicator', menu=topIndi)

		mainIndi = tk.Menu(menubar, tearoff=1)
		mainIndi.add_command(label="None",  command=lambda: addMainindicator("none"))
		mainIndi.add_command(label="SMA",  command=lambda: addMainindicator("sma"))
		mainIndi.add_command(label="EMA",  command=lambda: addMainindicator("ema"))
		menubar.add_cascade(label='Main Indicator', menu=mainIndi)

		bottomIndi = tk.Menu(menubar, tearoff=1)
		bottomIndi.add_command(label="None",  command=lambda: addBottomindicator("none"))
		bottomIndi.add_command(label="RSI",  command=lambda: addBottomindicator("rsi"))
		bottomIndi.add_command(label="MACD",  command=lambda: addBottomindicator("macd"))
		menubar.add_cascade(label='Bottom Indicator', menu=topIndi)

		tradeButton = tk.Menu(menubar, tearoff=1)
		tradeButton.add_command(label='Manual Trading',
                                        command=lambda: popupmsg('this is not live yet'))
		tradeButton.add_command(label='Auto Trading',
                                        command=lambda: popupmsg('this is not live yet'))
		tradeButton.add_separator()
		tradeButton.add_command(label='Quick Buy',
                                        command=lambda: popupmsg('this is not live yet'))
		tradeButton.add_command(label='Quick Sell',
                                        command=lambda: popupmsg('this is not live yet'))
		tradeButton.add_separator()
		tradeButton.add_command(label='Setup Quick Buy/Sell',
                                        command=lambda:popupmsg('this is not live yet'))

		menubar.add_cascade(label='Trading', menu=tradeButton)

		startStop = tk.Menu(menubar, tearoff=1)
		startStop.add_command(label='resume',
                                      command=lambda: loadChart('start'))
		startStop.add_command(label='pause',
                                      command=lambda: loadChart('stop'))
		menubar.add_cascade(label='Resume/Pause client', menu=startStop)

		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label='Tutorial', command=tutorial)

		menubar.add_cascade(label='Help', menu=helpmenu)
		
		tk.Tk.config(self, menu=menubar)
		
		self.frames = {}
		
		for F in (StartPage, BTCe_Page):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		
		self.show_frame(StartPage)
		tk.Tk.iconbitmap(self, default="icon-mongol-24.ico")
		
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

def qf(param):
	print(param)
	
class StartPage(tk.Frame):
	
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="""ALPHA Bitcoin trading application
use at your own risk. There is no promise of warranty""", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Agree", 
							command=lambda: controller.show_frame(BTCe_Page))
		button1.pack()
				
		button2 = ttk.Button(self, text="Disagree", command=quit)
		# button2 = ttk.Button(self, text="Disagree", command=quit)	# alternative method to shutdown app
		button2.pack()
		
		
class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font=FUNNY_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		
class BTCe_Page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page!", font=FUNNY_FONT)
		label.pack(pady=10, padx=10)
		
		button1 = ttk.Button(self, text="Back to Home", 
							command=lambda: controller.show_frame(StartPage))
		button1.pack()
		
		canvas = FigureCanvasTkAgg(f,self)
		# canvas.show()	# deprecated
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		
		# toolbar = NavigationToolbar2TkAgg(canvas, self)	# deprecated
		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		
		
		
	
app = SeaofBTCapp()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=2500)#, blit=True)
app.mainloop()
