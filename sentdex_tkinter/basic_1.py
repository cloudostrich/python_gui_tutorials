import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master = master
        
root = tk.Tk()
app = Window(root)
root.mainloop()
