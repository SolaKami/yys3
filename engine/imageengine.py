import os
import cv2
from PIL import ImageGrab
import numpy as np
from base import log
from base import baseenum

class ImageEngine:

    def __init__(self, registerengine):
        self.registerengine = registerengine
        self.ospath = registerengine.ospath
        self.method = 'cv2.TM_CCOEFF_NORMED'


    def getimagebypath(self, imagename):
        rootpath = os.path.dirname(os.getcwd()) + "/Resource/" + "%s" % self.ospath + "/"
        imagepath = rootpath + imagename + ".png"

        # Log.log(imagepath)

        image = cv2.imread(imagepath,0)
        return image

    def find_picture(self, imagename):

        try:
            # get image by image name
            image = self.getimagebypath(imagename)

            # get screen shot
            # backgroundshot = ImageGrab.grab((0, 0, self.endx, self.endy))
            backgroundshot = ImageGrab.grab()
            # backgroundshot.save("C:\\Users\\baijuyi\\Documents\\GitHub\\yys2\\Resource\\1.png")

            # convert screen shot to image
            backgroundimage = np.array(backgroundshot.convert('L'))

            res = cv2.matchTemplate(backgroundimage, image, eval(self.method))

            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            # similar rate
            value = max_val

            if value > 0.9:
                # get picture position
                top_left = max_loc

                # get center point
                w, h = image.shape[::-1]
                x = int(top_left[0])
                y = int(top_left[1])

                #compute click point
                x = int(top_left[0] + w / 2)
                y = int(top_left[1] + h / 2)


                # resize location if macos
                x = int(x / self.registerengine.ratex)
                y = int(y / self.registerengine.ratey)

            else:
                x = 0
                y = 0
            log.log("image name is '%s' and similar value is '%s' and x,y is '%s,%s'" % (imagename, value, x, y))
            self.registerengine.lastx = x
            self.registerengine.lasty = y
            return x
        except:
            return 0











    #
    # def match(self,img2,template2):
    #     template = template2.copy()
    #     w, h = template.shape[::-1]
    #     x = 0
    #     y = 0
    #     value = 0
    #
    #
    #     # 6 中匹配效果对比算法
    #     methods = ['cv2.TM_CCOEFF_NORMED']
    #
    #     # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    #
    #     for meth in methods:
    #         img = img2.copy()
    #
    #         method = eval(meth)
    #
    #         res = cv2.matchTemplate(img, template, method)
    #
    #
    #
    #         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #
    #         if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #             top_left = min_loc
    #             value = min_val
    #         else:
    #             top_left = max_loc
    #             value = max_val
    #
    #
    #         x = int(top_left[0] + w / 2)
    #         y = int(top_left[1] + h / 2)
    #
    #     if value > 0.9:
    #         return x, y
    #     else:
    #         return 0, 0