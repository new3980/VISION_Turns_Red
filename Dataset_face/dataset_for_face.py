#Create dataset for face remember (I will try in anime version also)
#Need to send input for training by extracting only subject faces and delete remaining area
#Still can't figure how to extract 2 faces or more
import cv2

path = "D:\\GIT\\VISION_Turns_Red-1\\REF_path\\YADA.mp4"

faceCascade = cv2.CascadeClassifier("C:\\Users\\MBComputer\\anaconda3\\envs\\myenv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
anime = cv2.CascadeClassifier("C:\\Users\\MBComputer\\anaconda3\\envs\\myenv\\Lib\\site-packages\\cv2\\data\\lbpcascade_animeface.xml")

#function for create dataset
#id = differences between faces
#When face is deteceted from video > crop > create file for keeping data (img_id)
def grouping(img,id,img_id):
    #str(id) = order that find face 
    #str(img_id) = order that seen this same face
    cv2.imwrite("D:\\GIT\\VISION_Turns_Red-1\\Dataset_face\\data\\pics_"+str(id)+"_"+str(img_id)+".jpg",img) 

def draw_box(img,classifier,scaleFactor,minNeighbors,color,text):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords = []
    for (x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
        cv2.putText(img,text,(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
        coords = [x,y,w,h]
    return img,coords

def detect(img,faceCascade,img_id):
    img,coords = draw_box(img,faceCascade,1.1,20,(255,0,0),"Face")  #img full , crop = cropped
    #to check that every part of face is detected x,y,w,h
    if len(coords) == 4: #ครบ 4 มั้ย
        id = 1                        #y;y+h
        crop = img[coords[1]:coords[1]+coords[3],coords[0]:coords[0]+coords[2]]
        grouping(crop,id,img_id)

    return img

img_id = 0  #initial value

cap = cv2.VideoCapture(path)
while(True):
    ret,frame = cap.read()
    frame = detect(frame,faceCascade,img_id)
    cv2.imshow('Who is there',frame)
    img_id = img_id + 1
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()