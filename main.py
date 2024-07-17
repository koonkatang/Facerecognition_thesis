from tkinter import *
from tkinter import ttk
from face_train import FaceTraining
from face_data_collect import DataSetCollect
from test_face_recognition import TestFaceRecognition
class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title('Face Recognition!')
        self.root.iconbitmap('gui/icon.ico')
        self.root.option_add("+Font", "consolas 25")

        Label(root, text= "FACE RECOGNITION SYSTEM", bg = "black", fg = "white", width = "300", height = "2", font = "consolas 25 bold").pack()
        #----data collect button----#
        Button(root, text="data collect",width=20,height=10,command=self.face_data_collect,bg = "pink").pack()
        #----train button----#
        Button(root, text="train",command=self.face_train,width=20,height=10,bg = "light blue").pack()
        #TEST Face regcognmition button#
        Button(root, text="Face Regcognition",command=self.test_face_recognition,width=20,height=10,bg = "lightgreen").pack()
        


    # Funtion 
    def test_face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = TestFaceRecognition(self.new_window)

    def face_data_collect(self):
        self.new_window = Toplevel(self.root)
        self.app = DataSetCollect(self.new_window)

    def face_train(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceTraining(self.new_window)

#root = __init__()
if __name__ == '__main__':
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

