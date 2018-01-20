from pymouse import PyMouse
from base import log

class MouseEngine:

    # initial function
    def __init__(self,registerengine):
        self.registerengine = registerengine

    # default click, click the location find
    def clickdefault(self):
        x = self.registerengine.lastx
        y = self.registerengine.lasty
        log.log("click and location x,y '%s, %s' " % (x, y))
        return self.leftclick(x,y)

    # base click by x y
    def leftclick(self,x,y):
        m = PyMouse()
        m.move(x, y)
        m.click(x, y, 1)
        return 1

    def clickadddefault(self, addx, addy):
        x = int(self.registerengine.lastx + addx/self.registerengine.ratex)
        y = int(self.registerengine.lasty + addy/self.registerengine.ratey)
        log.log("click and location x,y '%s, %s' " % (x, y))
        return self.leftclick(x, y)

    # slide
    def slide_down(self, x, y, h):
        m = PyMouse()
        m.move(x, y)
        m.press(x, y, 1)
        m.move(x, y + h)
        m.release(x, y + h, 1)
        return

    # move
    def move(self, x, y):
        m = PyMouse()
        m.move(x, y)
        return

    def movedefault(self):
        x = self.registerengine.lastx
        y = self.registerengine.lasty
        m = PyMouse()
        m.move(x, y)
        return

    # def move_from_to(x1, y1, x2, y2):
    #     y = int((y2 - y1) / 20)
    #     x = int((x2 - x1) / 20)
    #     m = PyMouse()
    #     m.move(x1, y1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #     num = 1
    #     while num <= 18:
    #         num += 1
    #         x2 = x1 + x * num
    #         y2 = y1 + y * num
    #         time.sleep(0.05)
    #         m.move(x2, y2)
    #         print("moveto  %d  %d" % (x2, y2))
    #     time.sleep(0.5)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    #     return
