from robot import tansuorobot
import win32gui
import time

hwnd = win32gui.FindWindow(0,"阴阳师-网易游戏")
win32gui.SetForegroundWindow(hwnd)

time.sleep(3)

robot1 = tansuorobot.TanSuoRobot(100, 16)

# robot1.start()
robot1.tansuo()
