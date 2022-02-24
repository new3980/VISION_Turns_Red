import cv2
from cv2 import IMREAD_COLOR
from cv2 import IMREAD_GRAYSCALE
from cv2 import IMREAD_UNCHANGED

#Pls comment each section while using

#To avoid cpp182: error: cv::cvtColor. So I used path instead
path = "D:\\GIT\\VISION_Turns_Red-1\\checking\\ghostinshell.jpg"
#change from rgb to grayscale
img = cv2.imread(path,0)
#3 choices: IMREAD_COLOR 1 / IMREAD_GRAYSCALE 0 / IMREAD_UNCHANGED -1
#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#name of tab
cv2.imshow('Name of this tab',img)
cv2.waitKey(0)
cv2.destroyAllWindows

#create new image
outputpath = "D:\\GIT\\VISION_Turns_Red-1\\checking\\ghostinshellgray.jpg"
cv2.imwrite(outputpath,img)