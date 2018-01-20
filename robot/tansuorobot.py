from engine import imageengine
from engine import mouseengine
from engine import registerengine
from base import baseenum
from base import log


class TanSuoRobot:

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
        log.log("start")
        if self.masterMode == baseenum.RobotMode.mastermode:
            self.masterstart()
        elif self.masterMode == baseenum.RobotMode.slavemode:
            self.salvestart()
        elif self.masterMode == baseenum.RobotMode.selfmode:
            self.selfstart()
        else:
            self.stop()
        return

    def salvestart(self):
        log.log("slave start")
        while(self._currentCount < self.countLimit):
            if self.isatendbattlewindow():
                self.clickendbattle()
            elif self.isatshowspoilswindow():
                self.clicklowerright()
            elif self.isatteaminvitewindow():
                self.clickyes()
            elif self.isatbaoxiangwindow():
                self.clickbaoxiang()
            # elif self.isatlosewindow():
            #     self.clicklose()
            # elif self.isatnoenergywindow():
            #     self.stop()
            # elif self.isatendbattlewindow():
            #     self.clickendbattle()
            elif self.isatwinwindow():
                self.clickwin()
            elif self.iszhunbei():
                self.clickzhunbei()
            # elif self.isatxuanshanginvitewindow():
            #     self.clickno()
            else:
                self.cannotrecognisesolog()
        return

    def masterstart(self):
        return

    def selfstart(self):
        return



# image recognition

    def isatwinwindow(self):
       return self.imageengine.find_picture("win")

    def isatlosewindow(self):
        return self.imageengine.find_picture("lose")

    def isatendbattlewindow(self):
        return self.imageengine.find_picture("endbattle")

    def isatbaoxiangwindow(self):
        return self.imageengine.find_picture("baoxiang")

    def isatshowspoilswindow(self):
        return self.imageengine.find_picture("showspoils")

    def isatteaminvitewindow(self):
        return self.imageengine.find_picture("yes")

    def isatnoenergywindow(self):
        return self.imageengine.find_picture("noenergy")

    def isatxuanshanginvitewindow(self):
        return self.imageengine.find_picture("xuanshanginvite")

    def isman(self):
        pass

    def iszhunbei(self):
        return self.imageengine.find_picture("zhunbei")

# action

# click action

    def clickwin(self):
        return self.mouseengine.clickdefault()

    def clicklose(self):
        return self.mouseengine.clickdefault()

    def clickendbattle(self):
        return self.mouseengine.clickdefault()

    def clickbaoxiang(self):
        return self.mouseengine.clickdefault()

    def clicklowerright(self):
        return self.mouseengine.clickadddefault(0,-152)

    def clickyes(self):
        # self.imageengine.find_picture("yes")
        return self.mouseengine.clickdefault()

    def clickno(self):
        return self.mouseengine.clickdefault()

    def cannotrecognisesolog(self):
        log.log("cannot recognise")
        return

    def clickzhunbei(self):
        return self.mouseengine.clickdefault()

# other action

    def stop(self):
        self._currentCount = self.countLimit
        log.log("stop")
        return
