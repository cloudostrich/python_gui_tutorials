import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import urllib
import json
import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
FUNNY_FONT = ("Comic Sans MS", 12)
style.use("ggplot")
# style.use("dark_background")

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
		
def animate(i):	# render in time intervals, not as updates happen
	dataLink = 'https://api.bitfinex.com/v1/trades/BTCUSD' #?limit_trades=10'
	data = urllib.request.urlopen(dataLink)
	data = data.read().decode("utf-8")
	data = json.loads(data)
	# print(len(data), type(data))
	# print(data[0])
	# databu = data[0]
	databu = pd.DataFrame(data)
	# print(databu)
	
	buys = databu[(databu['type']=="buy")].copy()
	buys["datestamp"]  = np.array(buys["timestamp"]).astype("datetime64[s]")
	buyDates = (buys["datestamp"]).tolist()
	
	sells = databu[(databu['type']=="sell")].copy()
	sells["datestamp"]  = np.array(sells["timestamp"]).astype("datetime64[s]")
	sellDates = (sells["datestamp"]).tolist()
	
	a.clear()
	a.plot_date(buyDates, buys["price"])
	a.plot_date(sellDates, sells["price"])

	
def ShutProgram():
	app.destroy()

class SeaofBTCapp(tk.Tk):
	
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.iconbitmap(self, default="icon-mongol-24.ico")
		tk.Tk.wm_title(self,"GhenghisKhan!!!")
		
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames = {}
		
		for F in (StartPage, BTCe_Page):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		
		self.show_frame(StartPage)
		
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
ani = animation.FuncAnimation(f, animate, interval=1000)#, blit=True)
app.mainloop()
