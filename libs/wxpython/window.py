 #!/bin/env python

import wx

class App(wx.Frame):

   def __init__(self):
      wx.Frame.__init__(self, None, -1, "Application", size=(800, 800), pos=(0,20))



if __name__ ==  '__main__':
    app = wx.App()
    frame   =   App()
    frame.Show(True)
    app.MainLoop()