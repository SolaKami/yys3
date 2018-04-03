from robot import tansuorobot
import win32gui
import time

try:
    hwnd = win32gui.FindWindow(0, "阴阳师-网易游戏")
    win32gui.SetForegroundWindow(hwnd)
except:
    pass

time.sleep(3)

robot1 = tansuorobot.TanSuoRobot(100, 24)

# robot1.start()
robot1.tansuo()
