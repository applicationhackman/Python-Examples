import webbrowser
import wx
from wx._core import EVT_MOTION


class AppFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Webbrowser Embeded",size=(500,500))
        openLink    =   wx.Button(self, -1, "Open", size=(100,100), pos=(0,0))
        openLink.Bind(wx.EVT_BUTTON, self.actOpenMove)


    def actOpenMove(self,ev):
        print("Act Open Move",ev)
        wx.B



if __name__ == '__main__':
    app =   wx.App()
    frame   =   AppFrame()
    frame.Show(True)
    app.MainLoop()