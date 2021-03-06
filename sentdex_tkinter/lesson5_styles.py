import tkinter as tk
from tkinter import ttk # for styling buttons

LARGE_FONT= ("Times New Roman", 96, "bold")    #("Courier", 96) ("Verdana", 12)

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

        self.frames={}
        # for loop to populate dict with all the different pages, each page is its own class
        for F in (StartPage, PageOne, PageTwo):
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

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # parent is SeaofBTCapp class
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Visit Page 1", 
                command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two", 
                command=lambda:controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", 
                command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two", 
                command=lambda:controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", 
                command=lambda:controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page One", 
                command=lambda:controller.show_frame(PageOne))
        button2.pack()

app = SeaofBTCapp()
app.mainloop()
