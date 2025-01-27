from cgitb import text
from distutils.command.config import LANG_EXT
from tkinter.tix import Tk
from turtle import title
from typing import Counter
import googletrans
from tkinter import *
import speech_recognition as sr
import translate as tr
A = sr.Recognizer()


def Translator():
    lbl_top = Label(myroot,text="Please Talk ...")
    lbl_top.config(font=("Arial",22,"bold"),bg="lime",width=24)
    lbl_top.grid(row=0)
 
    bt1 = Button(myroot, text="Start To talk",command=get_speech)
    bt1.config(font=("Arial",18),bg="yellow",width=10,fg="red")
    bt1.grid(row=1,pady=20)

def get_speech():
    try:
        with sr.Microphone(device_index=0) as sourcr:
           reslut = A.listen(sourcr)
           mytext = A.recognize_google(reslut)
           
           print(mytext)
           

    except:
        print("Device could'n recognize your voice")
        

def show_my_text(mytext,origin_text):
    global myCounter
    label_show_text = f"label_name{myCounter}"
    label_show_text_orgin = Label(myroot,text=origin_text)
    label_show_text = Label(myroot,text=mytext)
    label_show_text_orgin.config(font=("arial",20,"bold"),fg="red",width=20)
    label_show_text.config(font=("yekan",20,"bold"),fg="lime",width=20)
    label_show_text_orgin.grid(row=myCounter+1)
    label_show_text.grid(row=myCounter)
    myCounter+=1


get_speech()
