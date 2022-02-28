#Use previous extracted face picture for training
import os
from isort import file
import numpy as np
import cv2
from PIL import Image
from scipy.misc import face #for grayscale converting

#dir : files location
#data_dir = "D:\\GIT\\VISION_Turns_Red-1\\Dataset_face\\faces"
def train_classifier(data_dir):
    
    path = [os.path.join (data_dir,file) for file in os.listdir(data_dir)] #get path

    faces = []
    ids = []
    for image in path:
        #to grayscale
        img = Image.open(image).convert("L") 
        imageNP = np.array(img, 'uint8') #put in array, unsigned int 8 bit
        #Actually the "." can be changed depend on the symbol we choose, in this case I named my files pics_1_xx.jpg
        #So split must be split("_")
        #It means I choose id 1 (this case I only have Yada's face)
        id = int(os.path.split(image)[1].split("_")[1])
        #print("" + str(id))   #check if the output is out desired path or not
        faces.append(imageNP) #add trained one to array
        ids.append(id)
    
    ids = np.array(ids)

    #For face remember 
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("D:\\GIT\\VISION_Turns_Red-1\\Data_train\\YadaClass.xml")

#this is path that defined in def tran_classifier(data_dir)
pos = "D:\\GIT\\VISION_Turns_Red-1\\Dataset_face\\data"
train_classifier(pos)
