import cv2
import numpy as np
import os
import pyttsx3
import time
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/trainer.yml')
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['Sarah', 'Spencer', 'Dan', 'Charlie', 'Daniel', 'Elizabeth', 'Mothership'] 
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.3,
        minNeighbors = 5
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        face = gray[y:y+h,x:x+w]
        id, confidence = recognizer.predict(face)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            engine.say('Hello')
            engine.say(id)
            if (id == 'Spencer'):
                engine.say('Why do you not have a job?')
                time.sleep(1)
                engine.runAndWait()
                break
            elif (id == 'Sarah'):
                engine.say('Hello Beautiful')
                time.sleep(1)
                engine.runAndWait()
                break
            elif (id == 'Mothership'):
                engine.say('You are old')
                time.sleep(1)
                engine.runAndWait()
                break
            elif (id == 'Dan'):
                engine.say('I believe you have cancer!')
                time.sleep(1)
                engine.runAndWait()
            break
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    engine.runAndWait()
    engine.stop()
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()