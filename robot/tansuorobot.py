from engine import imageengine
from engine import mouseengine
from engine import registerengine
from engine import gundongengine
from base import baseenum
from base import log
import time
import random


class TanSuoRobot:

    def __init__(self, countlimit, zhangjie):
        # engine initial
        self.registerengine = registerengine.RegisterEngine()
        self.imageengine = imageengine.ImageEngine( self.registerengine)
        self.mouseengine = mouseengine.MouseEngine(self.registerengine)
        self.zhangjie = zhangjie

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


    def tansuo(self):
        log.log("tansuo start")
        while (self._currentCount < self.countLimit):
            if False:
                pass
            elif self.imageengine.find_picture("win"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("zhunbei"):
                self.mouseengine.clickadddefault(0,-100)
            elif self.imageengine.find_picture("showspoils"):
                self.mouseengine.clickadddefault(0, 500)
            elif self.imageengine.find_picture("endbattle"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("baoxiang"):
                self.mouseengine.clickdefault()
            elif self.imageengine.find_picture("ditubaoxiang"):
                self.mouseengine.clickdefault()
            else:
                if self.masterMode == baseenum.RobotMode.selfmode:
                    if self.imageengine.find_picture("tansuo"):
                        self.mouseengine.clickdefault()
                if self.masterMode == baseenum.RobotMode.mastermode:
                    if self.imageengine.find_picture("yaoqingzudui"):
                        self.mouseengine.clickdefault()
                if self.masterMode == baseenum.RobotMode.slavemode:
                    if self.imageengine.find_picture("yes"):
                        self.mouseengine.clickdefault()
                ##
                if baseenum.RobotMode.slavemode != self.masterMode:
                    if self.imageengine.find_picture("zhangjie"):
                        if self.imageengine.find_picture("zhangjie%s"%(self.zhangjie)):
                            # 每打3把，暂停30秒
                            if self._currentCount > 1 and self._currentCount%3 == 0:
                                time.sleep(random.randint(19,59)/10)
                            else:
                                time.sleep(random.randint(9,49)/10)
                            self.mouseengine.clickdefault()
                            self._currentCount += 1
                        else:
                            # 在章节页面，但是没有找到指定章节时，滚动一下
                            gundongengine.slide_up(self.registerengine.lastlastx,self.registerengine.lastlasty,-300)
                    elif self.imageengine.find_picture("boss"):
                        self.mouseengine.clickdefault()
                        time.sleep(random.randint(1,3))
                    elif self.imageengine.find_picture("xiaoguai"):
                        self.mouseengine.clickdefault()
                        time.sleep(random.randint(1, 3))
                    # 没有找到敌人时，但是又在副本里面时走一步
                    elif self.imageengine.find_picture("suodingchuzhan"):
                        self.mouseengine.clickadddefault(0, -80)
                        time.sleep(random.randint(5,20)/10)
        log.log("tansuo end")

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
