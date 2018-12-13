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

    text="사람 수는 총 "+how_many+"명입니다."
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
    root.title("BOOK CRAPSHOOT GAME")   #title
    root.geometry("640x500+100+100") #gui크기
    f1 = Frame(root)    #프레임
    f2 = Frame(root)
    f3 = Frame(root)
    f4 = Frame(root)

    for frame in (f1, f2, f3, f4):
        frame.grid(row=0, column=0, sticky='news')

    ###f1프레임
    label1=Label(f1)    #라벨 생성
    label1.place(x=150, y=100)  #위치
    label1.img = PhotoImage(file='p.png')   #이미지
    label1.config(image=label1.img, compound='bottom')  #이미지추가
    label1.pack()   #배치

    butt=Button(f1, command=lambda: raise_frame(f2))#버튼
    butt.place(x=400,y=230) #위치
    logo = PhotoImage(file='start.png')
    butt.img = logo.subsample(5, 5)
    butt.config(image=butt.img, compound=LEFT,bd=0)

    #butt.pack() #배치

    ##f2 프레임
    label2=Label(f2)    #두번째 프레임에 라벨 생성
    label2.place(x=150, y=100)  #위치
    label2.img = PhotoImage(file='page.png')    #이미지
    label2.config(image=label2.img, compound='bottom')  #이미지 추가
    label2.pack()   #위젯배치

    e1=Entry(f2, textvariable=entry)    #텍스트박스

    e1.place(x=80,y=80) #위치

    b=Button(f2, text="OK",command=lambda: output(f4, f3))
    b.place(x=230,y=75)  # 위치
    raise_frame(f1)
    root.mainloop()
