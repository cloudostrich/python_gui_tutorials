import tkinter as tk
import PIL  # Image, ImageTk
from PIL import Image, ImageTk

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
        
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        filee = tk.Menu(menu)
        filee.add_command(label="Save")
        filee.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=filee)
        
        edite = tk.Menu(menu)
        edite.add_command(label="Show Image", command=self.showImg)
        edite.add_command(label="Show Text", command=self.showTxt)
        menu.add_cascade(label="Edit", menu=edite)
                
    def client_exit(self):
        exit()  # built-in python function
        
    def showImg(self):
        load = Image.open('./pics/mona.jpg')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=30)
        
    def showTxt(self):
        text = tk.Label(self, text="Hey there good looking!")
        text.pack()
    
root = tk.Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
