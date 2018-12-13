
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
os.chdir(r"C:\Users\seung\PycharmProjects\untitled2\images")


def raise_frame(frame):
    frame.tkraise()
def output(ff3, ff4):
    num=entry.get() #엔트리값 받아오기
    image = num + '.png'
    imgbytes = image_helpers.get_image_from_file(image)
    rekesp = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])
    how_many = len(rekesp['FaceDetails'])

    ff3.tkraise()   #프레임f3로 이동

    label1 = Label(ff3)  # 라벨 생성
    label1.place(x=150, y=100)  # 위치
    label1.img = PhotoImage(file='result.png')  # 이미지
    label1.config(image=label1.img, compound='bottom')  # 이미지추가
    label1.pack()  # 배치

    #사람 수
    te=Label(ff3,text=how_many)
    te.place(x=170,y=90)    #위치
    te.config(font=(44))    #글자크기 수정

    #+버튼
    bu1=Button(ff3,  command=lambda: raise_frame(ff4))  #프레임4로 이동
    bu1.place(x=130,y=170)
    logo = PhotoImage(file='+.png') #이미지
    bu1.img = logo.subsample(5, 5)
    bu1.config(image=bu1.img, compound=LEFT, bd=0)

    #quit버튼
    bu2=Button(ff3, command=lambda: root.destroy()) #클릭시 종료
    bu2.place(x=170,y=170)
    logo1 = PhotoImage(file='quit.png') #이미지
    bu2.img = logo1.subsample(5, 5)
    bu2.config(image=bu2.img, compound=LEFT, bd=0)


    #4번째 프레임
    l=Label(ff4)    #사진출력
    l.place(x=150,y=100)    #위치
    l.img=PhotoImage(file=image)
    l.config(image=l.img, compound='bottom')
    l.pack()


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

    #시작버튼
    butt=Button(f1, command=lambda: raise_frame(f2))
    butt.place(x=400,y=230) #위치
    logo = PhotoImage(file='start.png') #이미지
    butt.img = logo.subsample(5, 5)
    butt.config(image=butt.img, compound=LEFT,bd=0) #이미지 추가



    ##f2 프레임
    label2=Label(f2)    #두번째 프레임에 라벨 생성
    label2.place(x=150, y=100)  #위치
    label2.img = PhotoImage(file='page.png')    #이미지
    label2.config(image=label2.img, compound='bottom')  #이미지 추가
    label2.pack()   #위젯배치

    # 텍스트박스
    e1=Entry(f2, textvariable=entry)
    e1.place(x=80,y=80) #위치

    #ok버튼
    b=Button(f2, text="OK",command=lambda: output(f3,f4))
    b.place(x=230,y=75)  # 위치

    raise_frame(f1)
    root.mainloop()
