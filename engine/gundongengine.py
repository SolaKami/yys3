import win32api
import win32con
from pymouse import PyMouse

def slide_up(x,y,h):
    m = PyMouse()
    m.move(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -h)
    return