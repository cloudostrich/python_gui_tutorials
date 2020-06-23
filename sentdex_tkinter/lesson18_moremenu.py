import tkinter as tk
from tkinter import ttk # for styling buttons

# matplotlib imports and backend configuration
import matplotlib
matplotlib.use("TkAgg") # use backend TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk #NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
import urllib.request   # urllib has no attribute request, so must import urllin.request
import json

LARGE_FONT= ("helvetica", 33, "bold")    #("Courier", 96) ("Verdana", 12)
NORMAL_FONT= ("helvetica", 23, "bold")
SMALL_FONT= ("helvetica", 13, "bold")
style.use("ggplot")

f = Figure() # size from tkinter frame, not mpl-Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

# exchange, timeframes, sample sizes
exchange = "BTC-e"
DatCounter = 9000
programName = "btc-e"
resampleSize="15Min"
DataPace = "1d"
candleWidth = 0.008

# Indicator stuff
topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"
EMAs = []
SMAs = []

chartLoad = True

def loadChart(run):
    global chartLoad
    if run == "start":
        chartLoad = True
    elif run == "stop":
        chartLoad = False

def tutorial():
    pass

def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    if what != "none":
        if middleIndicator == "none":
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:",middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            if what == "ema":
                midIQ = tk.Tk()
                #midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:",middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
                
        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your SMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:",middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()



                
            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want your EMA to be.")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0,10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle indicator set to:",middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

    else:
        middleIndicator = "none"
            

def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    elif what == "none":
        topIndicator = what
        DatCounter = 9000

    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text = "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)

            topIndicator = group
            DatCounter = 9000
            print("Set top indicator to",group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()


    elif what == "macd":
        topIndicator = "macd"
        DatCounter = 9000

        
def addBottomIndicator(what):
    global bottomIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    elif what == "none":
        bottomIndicator = what
        DatCounter = 9000

    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text = "Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0,14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)

            bottomIndicator = group
            DatCounter = 9000
            print("Set bottom indicator to",group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()


    elif what == "macd":
        bottomIndicator = "macd"
        DatCounter = 9000  


def changeTF(tf):
    global DataPace, DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OLHC interval")
    else: 
        DataPace = tf
        DatCounter = 9000
        print("DataPace: ", DataPace, ": resampleSize: ", resampleSize)

def changeSampleSize(size,width):
    global resampleSize, DatCounter, candleWidth
    if DataPace == "7d" and size == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OLHC interval")
    elif DataPace == "tick" and size != "tick":
        popupmsg("You're currently viewing tick data, not OHLC.")
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width
        print("DataPace: ", DataPace, ": resampleSize: ", resampleSize)


def changeExchange(toWhat, pn):
    global exchange, DatCounter, programName
    exchange = toWhat
    programName = pn
    DatCounter = 9000

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=SMALL_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

def animate(i):
    dataLink = 'https://api.btcmarkets.net/market/BTC/AUD/trades?limit=100' #'https://btc-e.com/api/3/trades/btc_usd?limit=2000' btc is no more
    data = urllib.request.urlopen(dataLink)
    data = data.read().decode("utf-8")  # no readall
    data = json.loads(data)
    data = pd.DataFrame(data)
    data["datestamp"] = np.array(data["date"]).astype("datetime64[s]")
    buyDates=(data["datestamp"]).tolist()
    print(data.tail())
    a.clear()
    a.plot_date(buyDates, data["price"], "k", label="Price")
    a.legend(bbox_to_anchor=(0,1.02,1,.102), loc=3, ncol=2, borderaxespad=0)
    title = "btcmarkets AUD trades\nLast Price: "+str(data["price"].iloc[-1])
    a.set_title(title)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default="@./pics/mongol.xpm")
        img = tk.PhotoImage(file='./pics/mongol.gif')
        self.tk.call('wm', 'iconphoto', self._w, img)
        tk.Tk.wm_title(self, "Sea of Bullshit")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda:popupmsg("Not Supported Yet!!!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="btcmarkets",command=lambda:changeExchange("btcmarkets","btcmkt"))
        exchangeChoice.add_command(label="Bitfinex",command=lambda:changeExchange("Bitfinex","bitfinex"))
        exchangeChoice.add_command(label="BitStamp",command=lambda:changeExchange("Bitstamp","bitstamp"))
        exchangeChoice.add_command(label="Huobi",command=lambda:changeExchange("Huobi","huobi"))
        menubar.add_cascade(label="Exchange", menu=exchangeChoice)
        
        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick", command=lambda: changeTF('tick'))
        dataTF.add_command(label="1 Day", command=lambda: changeTF('1d'))
        dataTF.add_command(label="3 Day", command=lambda: changeTF('3d'))
        dataTF.add_command(label="1 Week", command=lambda: changeTF('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=dataTF)
        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label="Tick", command=lambda:changeTF('tick'))
        OHLCI.add_command(label="1 minute", command=lambda: changeSampleSize('1Min', 0.0005))
        OHLCI.add_command(label="5 minute", command=lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label="15 minute", command=lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label="30 minute", command=lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label="1 Hour", command=lambda: changeSampleSize('1H', 0.032))
        OHLCI.add_command(label="3 Hour", command=lambda: changeSampleSize('3H', 0.096))
        menubar.add_cascade(label="OHLC Interval", menu=OHLCI)

        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None",command=lambda: addTopIndicator('none'))
        topIndi.add_separator()
        topIndi.add_command ( label="RSI", command=lambda: addTopIndicator('rsi'))
        topIndi.add_command ( label="MACD",command=lambda: addTopIndicator('macd'))
        menubar.add_cascade(label = "Top Indicator", menu = topIndi)

        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command ( label="None",command=lambda: addMiddleIndicator('none'))
        mainI.add_separator()
        mainI.add_command ( label="SMA",command=lambda: addMiddleIndicator('sma'))
        mainI.add_command ( label="EMA",command=lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label = "Main Graph Indicator", menu = mainI)

        bottomI = tk.Menu(menubar, tearoff=1)
        bottomI.add_command ( label="None",command=lambda: addBottomIndicator('none'))
        bottomI.add_separator()
        bottomI.add_command ( label="RSI",command=lambda: addBottomIndicator('rsi'))
        bottomI.add_command ( label="MACD",command=lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label = "Bottom Indicator", menu = bottomI)

        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label = "Manual Trading",command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label = "Automated Trading",command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label = "Quick Buy",command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label = "Quick Sell",command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label = "Set-up Quick Buy/Sell",command=lambda: popupmsg("This is not live yet"))
        menubar.add_cascade(label="Trading", menu=tradeButton)

        startStop = tk.Menu(menubar, tearoff = 1)
        startStop.add_command( label="Resume",command = lambda: loadChart('start'))
        startStop.add_command( label="Pause",command = lambda: loadChart('stop'))
        menubar.add_cascade(label = "Resume/Pause client", menu = startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        tk.Tk.config(self, menu=menubar)
        self.frames={}
        # for loop to populate dict with all the different pages, each page is its own class
        for F in (StartPage, PageOne, BTCe_Page):
            self.frames[F] = F(container, self)#frame
            self.frames[F].grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # raises page to the front

def qf(param):
    print(param)

def ShutProgram():
    app.destroy()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # parent is SeaofBTCapp class
        label = tk.Label(self, text="""Alpha Bitcoin trading application.\nUse at your own risk.\nThere is no promise of warranty.""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Agree", 
                command=lambda:controller.show_frame(BTCe_Page))
        button1.pack()
        button2 = ttk.Button(self, text="Disagree", 
                command=quit)
        button2.pack()
       

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", 
                command=lambda:controller.show_frame(StartPage))
        button1.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", 
                command=lambda:controller.show_frame(StartPage))
        button1.pack()

        # plt.show()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()   # not canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)



app = SeaofBTCapp()
app.geometry("1280x720") # size the app
ani = animation.FuncAnimation(f, animate, interval=10000)
app.mainloop()
