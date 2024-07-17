from tkinter import *
from tkinter import ttk
 
import cv2

class TestFaceRecognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title('Test Face Recognition!')
        self.root.iconbitmap('gui/icon.ico')
        self.root.option_add("+Font", "consolas 25")

        #----Face recognition----#
        def face_recognition():
            video = cv2.VideoCapture(0)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            face_recognizer = cv2.face.LBPHFaceRecognizer_create()
            face_recognizer.read("TrainingData.yml")
            name_list = ["", "Tanawat Silsa-ard","Tanwat Suebsom"]

            while True:
                ret,frame = video.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    serial, conf = face_recognizer.predict(gray[y:y+h, x:x+w])
                    if(conf > 50):
                        cv2.putText(frame, name_list[serial]+str(conf), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
                    else:
                        cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
        
                cv2.imshow("Face Recognition Test",frame)

                key_exit = cv2.waitKey(1)
                if key_exit == ord('q'):
                    break

            video.release()
            cv2.destroyAllWindows()
            #print("====== Face Recognition Samples Complete ======")


        #----button----#
        button_1 = Button(root, text="Face Recognition",command=face_recognition,width=20,height=10,bg = "lightgreen")
        button_1.place(x=0,y=0)


        

if __name__ == '__main__':
    root = Tk()
    obj=TestFaceRecognition(root)
    root.mainloop()
