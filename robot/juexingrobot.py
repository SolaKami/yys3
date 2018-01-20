from engine import imageengine
from engine import mouseengine
from engine import registerengine
from base import baseenum
from base import log
import time


class JuexingRobot:

    def __init__(self,  mastermode, countlimit):
        # master or slave or self mode
        # 1-master
        # 2-slave
        # 3-self
        self.masterMode = mastermode
        # for control battle count
        self.countLimit = countlimit
        # current battle count
        self._currentCount = 0

        # engine initial
        self.registerengine = registerengine.RegisterEngine()
        self.imageengine = imageengine.ImageEngine( self.registerengine)
        self.mouseengine = mouseengine.MouseEngine(self.registerengine)

        return

    def start(self):
        log.log("juexing start")
        while(self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture("tiaozhan"):
                self.mouseengine.clickdefault()
                self._currentCount += 1
                time.sleep(1)
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("endbattle"):
                self.mouseengine.clickdefault()
        log.log("juexing start")
        return



