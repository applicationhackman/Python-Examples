__author__ = 'chandrasekar.g'

import tkinter as tk
from tkinter import tix

class winApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.pack()
        self.log()

    def log(self):
        print(" Application loading ")




root = tk.Tk()
app = winApplication(master=root)
app.master.title("Sample window application")
app.master.minsize(500,500)
app.mainloop()



