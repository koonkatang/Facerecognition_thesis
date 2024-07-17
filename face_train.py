
import cv2
import numpy as np
from PIL import Image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

class FaceTraining:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title('Face Training')
        self.root.iconbitmap('gui/icon.ico')
        self.root.option_add("+Font", "consolas 25")

        title_lbl=Label(root, text="Data Training", bg = "black", fg = "white", width = "300", height = "2", font = "consolas 25 bold")
        title_lbl.place(x=0,y=0,width=1280,height=50)

        #-----Data Training-----#:
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        path = 'datasets'
        def getImagesData(path): 
            image_paths = [os.path.join(path,f) for f in os.listdir(path)] 
            faces = []
            ids = []
            for image_path in image_paths:
                face_image = Image.open(image_path).convert('L')
                face_np = np.array(face_image, 'uint8')
                id = os.path.split(image_path)[1].split('.')[1]
                id = int(id)
                faces.append(face_np)
                ids.append(id)
                cv2.imshow("training", face_np)
                cv2.waitKey(1)
            return ids, faces

        IDs, face_data = getImagesData(path)
        face_recognizer.train(face_data, np.array(IDs))
        face_recognizer.write("TrainingData.yml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training Status", "Training Complete!")
        #print("====== Training Complete ======")

if __name__ == '__main__':
    root = Tk()
    obj=FaceTraining(root)
    root.mainloop()
