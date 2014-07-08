__author__ = 'chandrasekar.g'

import tkinter as tk
import webbrowser as web

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master=None)
        self.pack()
        self.definingButton()

    def openURL(self):
            web.open("http://google.com")

    def definingButton(self):

        #   creating button

        self.showButton         =   tk.Button(self)

        self.cursorButton       =   tk.Button(self, text="Mouse over for cursor")

        self.fontFaceButton    =   tk.Button(self, text="Font face : Times New Roman")

        self.fontSizeButton    =   tk.Button(self, text="Font size : 18")

        self.fontBoldButton    =   tk.Button(self, text="Font style : Bold")

        self.fontItalicButton  =   tk.Button(self, text="Font Style : Italic")

        self.fontStrikeButton  =    tk.Button(self, text="Font Strike : Strike")

        self.justifyTextCenterBtn =    tk.Button(self, text="justify center")

        self.justifyTextLeftBtn =    tk.Button(self, text="justify left")

        self.justifyTextRightBtn =    tk.Button(self, text="justify right")

        self.BotderReliefGrroveBtn        =    tk.Button(self, text="Border Style")

        self.geometryButton               =    tk.Button(self, text='geometry Button')

        self.openInBrowser                =     tk.Button(self, text="Open in browser")

        self.openInBrowser['command']     =     self.openURL



    #
    #   Standard options / properties
    #


        #   setting cursor option 'hand2'

        self.cursorButton['cursor']     =   'hand2'

        #   setting font properties

        self.fontFaceButton['font']       =    'Arial'

        self.fontSizeButton['font']       =     'Arial 18'

        self.fontBoldButton['font']       =     'Arial 14 bold'

        self.fontItalicButton['font']     =     'Arial 14 italic'

        self.fontStrikeButton['font']     =     'Arial 14'

        self.justifyTextCenterBtn['justify']    =   'center'
        self.justifyTextCenterBtn['width']      =   15

        self.justifyTextLeftBtn['justify']      =   'left'
        self.justifyTextLeftBtn['width']        =   15


        self.justifyTextRightBtn['justify']      =   'right'
        self.justifyTextRightBtn['width']        =   15

        self.BotderReliefGrroveBtn['relief']           =  'groove'

        self.ColorButton                        =   "#RRRGGGBBB"



    #
    #   Widget specific options / options
    #

        #   setting text

        self.showButton['text']         =   'I am Button'

        #   setting height

        self.showButton['height']       =   5

        #   setting width

        self.showButton['width']        =   15



        self.cursorButton.pack(side='top')
        self.fontFaceButton.pack(side='top')
        self.fontSizeButton.pack(side='top')
        self.fontBoldButton.pack(side='top')
        self.fontItalicButton.pack(side='top')
        self.fontStrikeButton.pack(side='top')


        self.BotderReliefGrroveBtn.pack(side='top')
        self.showButton.pack(side='bottom')

        self.justifyTextLeftBtn.pack(side='left')
        self.justifyTextCenterBtn.pack(side='left')
        self.justifyTextRightBtn.pack(side='left')


        self.openInBrowser.pack(side='bottom')










app =   Application(master=None)
app.master.title("Simple Button Application")
app.master.minsize(500,500)
app.mainloop()
