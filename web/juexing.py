from robot import juexingrobot
from base import baseenum


robot1 = juexingrobot.JuexingRobot(baseenum.RobotMode.slavemode, 10)

robot1.start()
