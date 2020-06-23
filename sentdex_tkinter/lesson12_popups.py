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

#    data = data["btc_usd"]
#    data = pd.DataFrame(data)
#    buys = data[(data['type']=="bid")]
#    buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
#    buyDates = (buys["datestamp"]).tolist()
#    sells = data[(data['type']=="ask")]
#    sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
#    sellDates = (sells["datestamp"]).tolist()
    data = pd.DataFrame(data)
#    buys = data
    data["datestamp"] = np.array(data["date"]).astype("datetime64[s]")
    buyDates=(data["datestamp"]).tolist()
    print(data.tail())
    a.clear()
    a.plot_date(buyDates, data["price"], "k", label="Price")
#    a.plot_date(sellDates, sells["price"]) 
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

        tk.Tk.config(self, menu=menubar)
        
        self.frames={}
        # for loop to populate dict with all the different pages, each page is its own class
        for F in (StartPage, PageOne, BTCe_Page):
            #frame = F(container, self)
            self.frames[F] = F(container, self)#frame
            #frame.grid(row=0, column=0, sticky="nsew")
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
app.geometry("800x600") # size the app
ani = animation.FuncAnimation(f, animate, interval=10000)
app.mainloop()
