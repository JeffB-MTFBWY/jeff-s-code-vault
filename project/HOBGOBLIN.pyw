from tkinter import *
import random
colors = ['blue', 'red', 'yellow', 'purple', 'green', 'pink', 'orange', 'grey', 'light blue']

def roll(x):
    Attack1_Entry.delete(0, END)
    Attack1_Entry2.delete(0, END)
    Attack2_Entry.delete(0, END)
    Attack2_Entry2.delete(0, END)
    STREntry.delete(0, END)
    DEXEntry.delete(0, END)
    CONEntry.delete(0, END)
    INTEntry.delete(0, END)
    WISEntry.delete(0, END)
    CHAEntry.delete(0, END)

    if x == 'longsword':
        Attack1_Entry.insert(END, random.randint(4,23))
        Attack1_Entry2.insert(END, random.randint(2,9))

    if x == 'longbow':
        Attack2_Entry.insert(END, random.randint(4,23))
        Attack2_Entry2.insert(END, random.randint(2,9))
    
    if x == 'orc_str':
        STREntry.insert(END, random.randint(2, 21))

    if x == 'orc_dex':
        DEXEntry.insert(END, random.randint(2,21))

    if x == 'orc_con':
        CONEntry.insert(END, random.randint(2,21))

    if x == 'orc_int':
        INTEntry.insert(END, random.randint(1,19))

    if x == 'orc_wis':
        WISEntry.insert(END, random.randint(1,20))

    if x == 'orc_cha':
        CHAEntry.insert(END, random.randint(1,20))
        

main = Tk()
main.title("Hobgoblin")
image = PhotoImage(file='Hobgoblin.png')
OrcLabel =  Label(main, image=image,bd=2, relief="solid")
OrcLabel.grid()

miscEntry = Entry(main)
miscEntry.place(x=140, y=20)

InitEntry = Entry(main, width=2)
InitEntry.place(x=270, y=20)

InitEntry.insert(0, random.randint(2,21))


#ATTACK 1
Frame1 = Frame(main, bg=random.choice(colors))
Frame1.grid(row=3, column=0)

Attack1_Button = Button(Frame1, text='Longsword ', command=lambda:roll('longsword'))
Attack1_Button.grid(row=1, column=0)

Attack1_AtkLabel = Label(Frame1, text="ATK")
Attack1_AtkLabel.grid(row=1, column=1)

Attack1_Entry = Entry(Frame1, width=2)
Attack1_Entry.grid(row=1, column=2)

Attack1_DmgLabel = Label(Frame1, text="DMG")
Attack1_DmgLabel.grid(row=1, column=3)

Attack1_Entry2 = Entry(Frame1, width=2)
Attack1_Entry2.grid(row=1, column=4)

#ATTACK 2
Attack2_Button = Button(Frame1, text='  Longbow  ', command=lambda:roll('longbow'))
Attack2_Button.grid(row=4, column=0)

Attack2_AtkLabel = Label(Frame1, text="ATK")
Attack2_AtkLabel.grid(row=4, column=1)

Attack2_Entry = Entry(Frame1, width=2)
Attack2_Entry.grid(row=4, column=2)

Attack2_DmgLabel = Label(Frame1, text="DMG")
Attack2_DmgLabel.grid(row=4, column=3)

Attack2_Entry2 = Entry(Frame1, width=2)
Attack2_Entry2.grid(row=4, column=4)

#STAT ROLLS
#STR
STRButton = Button(Frame1, text="STR", command=lambda:roll('orc_str'))
STRButton.grid(row=5, column=0)

STREntry = Entry(Frame1, width=2)
STREntry.grid(row=5, column=0, sticky=E)

#DEX
DEXButton = Button(Frame1, text="DEX", command=lambda:roll('orc_dex'))
DEXButton.grid(row=5, column=1)

DEXEntry = Entry(Frame1, width=2)
DEXEntry.grid(row=5, column=2)

#CON
CONButton = Button(Frame1, text="CON", command=lambda:roll('orc_con'))
CONButton.grid(row=5, column=3)

CONEntry = Entry(Frame1, width=2)
CONEntry.grid(row=5, column=4)

#INT
INTButton = Button(Frame1, text="INT", command=lambda:roll('orc_int'))
INTButton.grid(row=5, column=5)

INTEntry = Entry(Frame1, width=2)
INTEntry.grid(row=5, column=6)

#WIS
WISButton = Button(Frame1, text="WIS", command=lambda:roll('orc_wis'))
WISButton.grid(row=5, column=7)

WISEntry = Entry(Frame1, width=2)
WISEntry.grid(row=5, column=8)

#CHA
CHAButton = Button(Frame1, text="CHA", command=lambda:roll('orc_cha'))
CHAButton.grid(row=5, column=9)

CHAEntry = Entry(Frame1, width=2)
CHAEntry.grid(row=5, column=10)

mainloop()