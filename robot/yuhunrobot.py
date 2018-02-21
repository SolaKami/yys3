from engine import imageengine
from engine import mouseengine
from engine import registerengine
from base import baseenum
from base import log
import time


class YuhunRobot:

    def __init__(self, countlimit):
        # engine initial
        self.registerengine = registerengine.RegisterEngine()
        self.imageengine = imageengine.ImageEngine(self.registerengine)
        self.mouseengine = mouseengine.MouseEngine(self.registerengine)

        # master or slave or self mode
        # 1-master
        # 2-slave
        # 3-self
        self.masterMode = self.registerengine.mastermode
        # for control battle count
        self.countLimit = countlimit
        # current battle count
        self._currentCount = 0
        return


    def yuhunsiji(self):
        log.log("yuhun start")
        while (self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickadddefault(0,-60)
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("dianjijixu"):
                self.mouseengine.clickdefault()
            if self.masterMode == baseenum.RobotMode.mastermode:
                if self.imageengine.find_picture("queding"):
                    self.mouseengine.clickdefault()
                elif self.imageengine.find_picture("zidongkaishi") and self.imageengine.find_picture("kaishizhandou"):
                    self.mouseengine.clickdefault()
                    self._currentCount += 1
                    time.sleep(3)
                elif self.imageengine.find_picture("morenyaoqing"):
                    self.mouseengine.clickdefault()
            if self.masterMode == baseenum.RobotMode.slavemode:
                if self.imageengine.find_picture("allyes"):
                    self.mouseengine.clickdefault()
                elif self.imageengine.find_picture("yes"):
                    self.mouseengine.clickdefault()
                elif self.imageengine.find_picture("zidongkaishi"):
                    self.mouseengine.clickdefault()
            if self.masterMode == baseenum.RobotMode.selfmode:
                if self.imageengine.find_picture("tiaozhan"):
                    self.mouseengine.clickdefault()
                    self._currentCount += 1
                    time.sleep(3)
        log.log("yuhun start")




    def yeyuanhuo(self):
        while (self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickadddefault(0, -60)
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("dianjijixu"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("tiaozhan"):
                time.sleep(5)
                self.mouseengine.clickdefault()




