from tkinter import *
import random
color =["red", "blue", "pink", "orange", "brown", "green", "light green", "yellow", "purple"]

w = Tk()
w.geometry("313x399+603+158")
w.title("Yukinaba City")
w["bg"] = random.choice(color)
image = PhotoImage(file="girl.png")
girllabel = Label(w, image=image,bd=2, relief="solid").pack()
label = Label(w, text="Ami (Godai)").pack()
fo = open("Dialog.txt", "r")
npctalk = fo.readlines()
fo.close()
comment = Text(w, height=10, width=30, bd=9, relief="sunken", bg=random.choice(color), wrap="word")
comment.pack()
comment.insert(END,random.choice(npctalk[0:11]))

testbutton = Button(w, text="ok", command=lambda:w.destroy()).pack(side=BOTTOM)


w.mainloop()


#Figure out how to clear that text screen so new quotes can cycle not pile up!