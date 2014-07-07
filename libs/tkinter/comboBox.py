__author__ = 'chandrasekar.g'

import tkinter as tk

import  tkinter.tix as tx

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.pack()

    def CreateComboBox(self):
            self.comboElement   =   tx.ComboBox(self, option="Good")
            self.comboElement.pack(self='left')
            self.comboElement.grid()


app = Application(master=None)
app.master.minsize(500,400)
app.mainloop()