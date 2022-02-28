#Before face detection, it begins with drawing into order to identify parts
#see drawing opencv document: https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html
import cv2

path = "D:\\GIT\\VISION_Turns_Red-1\\Drawing function\\pinku.png"
img = cv2.imread(path,1)
#The most simple is coordinate system in which is needed parameter to draw

#choose only 1 function to be specific (then want all then no need)

#1 Line (img,startpoint,finalpoint,color(BGR),thickness)
#img = cv2.line(img,(0,0),(255,255),(255,0,0),2)

#2 Arrow line (same with line)
#img = cv2.arrowedLine(img,(0,0),(500,500),(255,0,0),10)

#for 2D shapes if thickness = -1 means filled with that certain color

#3 Rectangle (img,upperleft edge,lowerright edge,color,thickness)
#img = cv2.rectangle(img,(80,80),(444,444),(255,0,0),3)

#4 Circle (img,center,radius,color,thickness) กูจัดให้ 2 ที่ลือๆ
img = cv2.circle(img,(415,313),(100),(255,0,0),3)
img = cv2.circle(img,(217,252),(69),(255,0,0),3)

#5 Text (img,'text',bottomleft corner,fontFace,fontScale,color,thickness,lineType)
img = cv2.putText(img,"I like this pic so much bro",(17,528),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

cv2.imshow('Pink profile',img)

cv2.waitKey(0)
cv2.destroyAllWindows

#create new image (result is written one by one)
outputpath = "D:\\GIT\\VISION_Turns_Red-1\\Drawing function\\texting on fav pic.jpg"
cv2.imwrite(outputpath,img)

#Next is face detection
#Nopparuj J.