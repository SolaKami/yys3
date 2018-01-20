from engine import imageengine
from engine import mouseengine
from engine import registerengine
from base import log
import time


class YaoqifengyingRobot:

    def __init__(self, countlimit):

        # for control battle count
        self.countLimit = countlimit
        # current battle count
        self._currentCount = 0

        # engine initial
        self.registerengine = registerengine.RegisterEngine()
        self.imageengine = imageengine.ImageEngine(self.registerengine)
        self.mouseengine = mouseengine.MouseEngine(self.registerengine)

        return

    def start(self):

        addx = 750
        addy = 36
        while(self._currentCount < self.countLimit):
            ret = 0
            if False:
                pass
            elif self.haifangzhu():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.guishihei():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.erkounv():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.xiaosongwan():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.gunv():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.tiaotiaogege():
                ret = self.mouseengine.clickadddefault(addx, addy)
            elif self.rihefang():
                ret = self.mouseengine.clickadddefault(addx, addy)
            if ret:
                self._currentCount += 1
                time.sleep(0.5)


    def startspecial(self,limit,name):
        self.countLimit = limit
        addx = 750
        addy = 36
        while (self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture(name):
                self.mouseengine.clickadddefault(addx, addy)
                self._currentCount += 1
            elif self.imageengine.find_picture("homezudui"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("yaoqifengying"):
                time.sleep(0.5)
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("endbattle"):
                self.mouseengine.clickdefault()

    def startshiju(self):
        while (self._currentCount < self.countLimit):
            ret = 0
            if self.shiju():
                ret = self.mouseengine.clickadddefault(600, 36)
            elif self.fennudeshiju():
                ret = self.mouseengine.clickadddefault(600, 36)
            if ret:
                self._currentCount += 1
                time.sleep(0.5)


# image recognition
    def haifangzhu(self):
       return self.imageengine.find_picture("haifangzhu")

    def erkounv(self):
        return self.imageengine.find_picture("erkounv")

    def guishihei(self):
        return self.imageengine.find_picture("guishihei")

    def xiaosongwan(self):
        return self.imageengine.find_picture("xiaosongwan")

    def shiju(self):
        return self.imageengine.find_picture("shiju")

    def fennudeshiju(self):
        return self.imageengine.find_picture("fennudeshiju")

    def gunv(self):
        return self.imageengine.find_picture("gunv")

    def tiaotiaogege(self):
        return self.imageengine.find_picture("tiaotiaogege")

    def rihefang(self):
        return self.imageengine.find_picture("rihefang")

    def iszhunbei(self):
        return self.imageengine.find_picture("zhunbei")

    def isatwinwindow(self):
       return self.imageengine.find_picture("win")

    def isatlosewindow(self):
        return self.imageengine.find_picture("lose")

    def isatendbattlewindow(self):
        return self.imageengine.find_picture("endbattle")

    def isatnoenergywindow(self):
        return self.imageengine.find_picture("noenergy")
