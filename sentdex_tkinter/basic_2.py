import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=tk.BOTH, expand=1)
        quitButton = tk.Button(self, text="Quit")
        quitButton.place(x=0, y=0)
        
root = tk.Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
