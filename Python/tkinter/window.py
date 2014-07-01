__author__ = 'chandra-1263'

import tkinter as tk
from tkinter import tix

class winApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.pack()

    def test(self):
        self.chooseCombo    =   tix.ComboBox(self, text='Do foo')
        self.chooseCombo.pack(side='left')




root = tk.Tk()
app = winApplication(master=root)
app.mainloop()



