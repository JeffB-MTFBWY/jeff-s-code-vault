from tkinter import *
import random
color =["red", "blue", "pink", "orange", "brown", "green", "light green", "yellow", "purple"]

w = Tk()
w.geometry("313x399+603+158")
w.title("Yukinaba City")
w["bg"] = random.choice(color)
#frame1 = Frame(w, bg="yellow", height=156, width=150, bd=20, relief="groove").pack()
image = PhotoImage(file="girl.png")
girllabel = Label(w, image=image,bd=2, relief="solid").pack()
label = Label(w, text="Ami (Godai)").pack()
fo = open("Dialog.txt", "r")
npctalk = fo.readlines()
comment = Text(w, height=10, width=30, bd=9, relief="sunken", bg=random.choice(color), wrap="word")
comment.pack()
comment.insert(END,random.choice(npctalk[0:11]))
testbutton = Button(w, text="ok", command=lambda:[print(END,random.choice(npctalk[0:11])),fo.close()].pack(side=BOTTOM)


w.mainloop()