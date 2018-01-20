from engine import imageengine
from engine import mouseengine
from engine import registerengine
from base import log
import time


class TupoRobot:

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

        addx = -20
        addy = 20
        while (self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture("jingong"):
                self.mouseengine.clickdefault()
                self._currentCount += 1
                time.sleep(3)
            elif self.imageengine.find_picture("tupo"):
                self.mouseengine.clickadddefault(addx, addy)
                time.sleep(3)
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("endbattle"):
                self.mouseengine.clickdefault()
