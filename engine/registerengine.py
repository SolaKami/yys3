from base import baseenum
import configparser

class RegisterEngine:

    lastx = 0
    lasty = 0
    lastlastx = 0
    lastlasty = 0

    # ratex = 1.50
    # ratey = 1.50
    # ospath = 'mac_win10_deskapp'

    # ratex = 0
    # ratey = 0
    # ospath = ''

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("c://yys.conf")
        mode = config['yys']['mode']
        if mode == "master":
            self.mastermode = baseenum.RobotMode.mastermode
        elif mode == "slave":
            self.mastermode = baseenum.RobotMode.slavemode
        elif mode == "self":
            self.mastermode = baseenum.RobotMode.selfmode

        self.ospath = config['yys']['ospath']
        self.ratex = float(config['yys']['ratex'])
        self.ratey = float(config['yys']['ratey'])

        print("mode:",self.mastermode)
        print("path:",self.ospath)
        print("ratex:",self.ratex)
        print("ratey:",self.ratey)



    #     pc_win10_deskapp = 'pc_win10_deskapp'
    #     pc_win10_mumu = 'pc_win10_mumu'
    #     mac_win10_deskapp = 'mac_win10_deskapp'
    #     mac_win10_mumu = 'mac_win10_mumu'
    #     mac_macos_mumu = 'mac_macos_mumu'


