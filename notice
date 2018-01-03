import win32con
import win32gui
import win32ts
import time


WM_WTSSESSION_CHANGE        = 0x2B1

def myststa(code):
    sata = []
    timeArray = time.localtime()
    nowtime=time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
    if code==7:
        sata="锁定 "+nowtime

    elif code==8:
        sata = "解锁 " + nowtime

    with open('foo.txt', 'a') as f:
        f.write(sata)
        f.write("\n")
        f.close()
class WTSMonitor():
    className = "WTSMonitor"
    wndName = "WTS Event Monitor"

    def __init__(self):
        wc = win32gui.WNDCLASS()
        wc.hInstance = hInst = win32gui.GetModuleHandle(None)
        wc.lpszClassName = self.className
        wc.lpfnWndProc = self.WndProc
        self.classAtom = win32gui.RegisterClass(wc)

        style = 0
        self.hWnd = win32gui.CreateWindow(self.classAtom, self.wndName,
            style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            0, 0, hInst, None)
        win32gui.UpdateWindow(self.hWnd)
        win32ts.WTSRegisterSessionNotification(self.hWnd, win32ts.NOTIFY_FOR_ALL_SESSIONS)

    def start(self):
        win32gui.PumpMessages()

    def stop(self):
        win32gui.PostQuitMessage(0)

    def WndProc(self, hWnd, message, wParam, lParam):
        if message == WM_WTSSESSION_CHANGE:
            self.OnSession(wParam, lParam)

    def OnSession(self, event, sessionID):
        print(event)
        myststa(event)

if __name__ == '__main__':
    m = WTSMonitor()
    x=m.start()
