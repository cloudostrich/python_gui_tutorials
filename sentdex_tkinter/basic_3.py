import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=tk.BOTH, expand=1)
        quitButton = tk.Button(self, text="Quit", command=self.client_exit) # command binds button to function
        quitButton.place(x=0, y=0)
        
    def client_exit(self):
        exit()  # built-in python function
        
root = tk.Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
