from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from time import sleep
from threading import Thread

window = Tk()
window.title("Tkinter OpenCV")

video = cv2.VideoCapture(0)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) // 2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2

canvas = Canvas(window, width = canvas_w, height= canvas_h , bg= "red")
canvas.pack()

bw = 0

def handleBW():
    global bw
    bw = 1 - bw

button = Button(window,text = "Black & White", command=handleBW)
button.pack()

photo = None
count = 0

def send_to_server():
    global button
    sleep(10)
    button.configure(text="ThangNC")
    return

def update_frame():
    global canvas, photo, bw, count
    # Doc tu camera
    ret, frame = video.read()
    # Ressize
    frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    # Chuyen he mau
    if bw==0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Convert hanh image TK
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    # Show
    canvas.create_image(0,0, image = photo, anchor=tkinter.NW)

    count = count +1
    if count%10==0:
        #send_to_server()
        thread = Thread(target=send_to_server)
        thread.start()

    window.after(15, update_frame)

update_frame()

window.mainloop()