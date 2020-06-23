import tkinter
window = tkinter.Tk()
window.title("Gaia")
window.geometry("600x480")
img = tkinter.PhotoImage(file='./pics/mongol.gif')
window.tk.call('wm', 'iconphoto', window._w, img)
window.mainloop()
