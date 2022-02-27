#Actually I wanna try whether it can be used for anime girl or not
#If it is not working I'll use normal instead
import cv2

eyeCascade = cv2.CascadeClassifier("C:\\Users\\MBComputer\\anaconda3\\envs\\myenv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")

path = "D:\\GIT\\VISION_Turns_Red-1\\Eye detection\\Marin-chan.mp4"

def draw_box(img,classifier,scaleFactor,minNeighbors,color,text):
    #Convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #detect face position
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    
    for (x,y,w,h) in features:
        #Found eye border at x ,then the end must be x+width of face detected in features
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        #put text "It's Marin!"
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
    return img

def detectEye(img,eyeCascade):
    img = draw_box(img,eyeCascade,1.1,30,(255,0,0),"Eye")
    return img

cap = cv2.VideoCapture(path)
while(True):
    ret,frame = cap.read()
    frame = detectEye(frame,eyeCascade)
    cv2.imshow('Eye detection',frame)
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break

cap.release()
cv2.destroyAllWindows

#This one is able to detect eye however, it also detect something eles that is not related also.