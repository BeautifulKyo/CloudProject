# CloudProject
cloud computing repository

import tkinter.font
from tkinter import *
import boto3
from pprint import pprint
import image_helpers
import threading
from time import sleep
import os
import glob

client = boto3.client('rekognition')
#print(os.getcwd+'\images')
#os.chdir(r"C:\Users\seung\PycharmProjects\untitled2\images")


def raise_frame(frame):
    frame.tkraise()
def output(ff, frame):
    num=entry.get()
    n = str(num)
    image = n + '.png'
    imgbytes = image_helpers.get_image_from_file(image)
    rekesp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    how_many = len(rekesp['FaceDetails'])
    ff.tkraise()

    text="사람 수는 총 "+str(how_many)+"명입니다."
    l=Label(ff, text=text)
    l.place(x=150,y=100)
    l.img=PhotoImage(file=image)
    l.config(font=(44))
    l.config(image=l.img, compound='bottom')
    l.pack()


    Button(ff, text='RESTART', command=lambda: raise_frame(f1)).place(x=100,y=410)
    Button(ff, text='Quit',command=lambda: root.destroy()).place(x=170,y=410)
if __name__ == '__main__':

    root = Tk()
    entry=StringVar()
    #font=tkinter.font.Font(size=30)
    root.title("BOOK CRAPSHOOT GAME")
    root.geometry("640x500+100+100")
    f1 = Frame(root)
    f2 = Frame(root)
    f3 = Frame(root)
    f4 = Frame(root)

    for frame in (f1, f2, f3, f4):
        frame.grid(row=0, column=0, sticky='news')


    label1=Label(f1)
    label1.place(x=150, y=100)
    label1.img = PhotoImage(file='p.png')
    label1.config(image=label1.img, compound='bottom')
    label1.pack()

    butt=Button(f1, text='START', command=lambda: raise_frame(f2))
    butt.place(x=200,y=130)
    butt.pack()

    label2=Label(f2)
    label2.place(x=150, y=100)
    label2.img = PhotoImage(file='page.png')
    label2.config(image=label2.img, compound='bottom')
    label2.pack()

    e1=Entry(f2, textvariable=entry)

    e1.place(x=80,y=80)

    b=Button(f2, text='OK', command=lambda: output(f4, f3)).place(x=230,y=75)

    raise_frame(f1)
    root.mainloop()
