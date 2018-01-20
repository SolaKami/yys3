from robot import tansuorobot
from base import baseenum


robot1 = tansuorobot.TanSuoRobot(baseenum.RobotMode.slavemode, 100)

robot1.start()
