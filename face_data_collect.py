from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2

class DataSetCollect:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title('Data Set Collect!')
        self.root.iconbitmap('gui/icon.ico')
        self.root.option_add("+Font", "consolas 25")

        # title_lbl=Label(root, text="Data Set Collect", bg = "black", fg = "white", width = "300", height = "2", font = "consolas 25 bold")
        # title_lbl.place(x=0,y=0,width=1280,height=50)

        #-----Text Box-----#:
        label_1=Label(root, text="Enter Your ID: ", fg="black", font = "Arial 35 bold")
        label_1.grid(row=0,column=0,padx=5,pady=10)

        textbox = Entry(root, width=10, font = "Arial 35 bold")
        textbox.grid(row=0, column=1,)

        def submit_id():
            text_id = textbox.get()
            emptylabel.config(text="Your Id is: " + text_id)
        
        #-----Data set collecting-----#:
        text_id = IntVar()
        
        def face_cropped():
            #text_id = input("Enter Your ID: ")
            video = cv2.VideoCapture(0)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            count = 0

            while True:
                ret,frame = video.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.05, 5)
                for (x, y, w, h) in faces:
                    count += 1
                    cv2.imwrite("datasets/User."+str(text_id)+"."+str(count)+".jpg", gray[y:y+h, x:x+w])
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        
                cv2.imshow("Face Recognition Test",frame)

                if count > 100:
                    break

                key_exit = cv2.waitKey(1)
                if key_exit == ord('q'):
                    break

            video.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Data Set Collected!")

        #-----Button-----#:
        button1 = Button(root, text="Submit", width=10, height=1, font = "Arial 16 bold", command=submit_id)
        button1.grid(row=1, column=1,sticky=W)

        button2 = Button(root, text="Collect face Data", width=20, height=1, font = "Arial 16 bold", command=face_cropped)
        button2.grid(row=2, column=1,sticky=W)

        emptylabel = Label(root, fg="Red", font = "Arial 25 bold")
        emptylabel.grid(row=3, column=1,sticky=W)

if __name__ == '__main__':
    root = Tk()
    obj=DataSetCollect(root)
    root.mainloop()

