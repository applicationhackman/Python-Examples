__author__ = 'chandrasekar.g'

import tkinter as tk

class app(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.pack()
        self.createText()

    def createText(self):

        self.textItem   =   tk.Text(self)

        # setting element background color
        self.textItem['background'] =   '#878787'  # gray family

        # setting font color
        self.textItem['foreground'] =   'white'

        # setting font styles
        self.textItem['font']       =   "Arial 20 bold"

        # setting font space
        self.textItem['tabs']       =   8

        # on select element border color  / highlight of element color
        self.textItem["highlightcolor"] =   "green"


        # selected background color
        self.textItem['selectbackground']   =   '#f7bc3d'   # orange family

        # selected text color
        self.textItem['selectforeground']   =   '#0d8ea5'   # blue family

        # cursor
        self.textItem['cursor']             =   'hand2'

        # border width / margin
        self.textItem['borderwidth']        =   28

        # select border width
        self.textItem['selectborderwidth']  =   10


        # height relative to parent / master
        self.textItem['width']  =   25


        # width relative to parent / master
        self.textItem['height']  =   10

        # spacing 1
        self.textItem['spacing1']   =   10


        # spacing 1
        self.textItem['takefocus']   =   10


        self.textItem.grid()
        self.textItem.pack(side='left')



mainapp  = app(master=None)
mainapp.master.title("Simple text ")
mainapp.master.minsize(500,500)
mainapp.mainloop()
