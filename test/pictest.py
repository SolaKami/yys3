import os
import cv2
from matplotlib import pyplot as plt
from PIL import ImageGrab
import numpy as np

backgroundshot = ImageGrab.grab()
backgroundshot.size = (1280, 800)
backgroundshot.save("/Users/sunxiaowei/Desktop/1.png")
backgroundimage = np.array(backgroundshot.convert('L'))
project_dir = os.path.dirname(os.getcwd())+"/Resource/mac"

print(project_dir)
# img = cv2.imread(project_dir+"/1.png", 0)
img = backgroundimage


img2 = img.copy()
template = cv2.imread(project_dir+"/teaminvite.png", 0)

w, h = template.shape[::-1]

# 6 中匹配效果对比算法
methods = ['cv2.TM_CCOEFF_NORMED']
#methods = [ 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()

    method = eval(meth)

    res = cv2.matchTemplate(img, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        print(1-min_val)
    else:
        top_left = max_loc
        print(max_val)
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    print
    meth
    plt.subplot(221), plt.imshow(img2, cmap="gray")
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(template, cmap="gray")
    plt.title('template Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(res, cmap="gray")
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img, cmap="gray")
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()