from tkinter import *
import random
import pygame
import os
import DMToolkit
#from PIL import Image, ImageTk

TotalEntries = 0



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





def drag_start(event):

    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):

    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y) 



pygame.init()
monster = "NOPE"

diceroll = pygame.mixer.Sound(resource_path(("d_roll.wav"))) 



GuardTalk = pygame.mixer.Sound(resource_path(("Haltt.wav")))
main = Tk()













def Page(x):

    
    main = Toplevel()

    def ButtonEvent(x):
        RoomButton = Button(main, command=lambda:RoomButton.place_forget())
        RoomButton.place(x=80, y=350)

        if x == 1:
            RoomButton.configure(text="LOOT!\nLoot x"+str(random.randint(1,4)))
        if x == 2:
            RoomButton.configure(text="BATTLE!\nSkeletons x"+str(random.randint(0,5))+"\nZombies x"+str(random.randint(0,5)))
        if x == 3:
            RoomButton.configure(text="BATTLE AND LOOT!\nSkeletons x"+str(random.randint(0,3))+"\nZombies x"+str(random.randint(0,3))+"\n\nLoot x"+str(random.randint(1,6)))
        if x == 4:
            RoomButton.configure(text="Nothing...")
        if x == 5:
            Type = ["Dart ("+str(random.randint(1,8))+" DMG)"] + ["Exploding Brick ("+str(random.randint(1,12))+" DMG)"] + ["Spear ("+str(random.randint(1,16))+" DMG)"] + ["Gas (Sleep)"] + ["Gas (Poison "+str(random.randint(1,4))+" hrs)"] + ["Gas (Poison "+str(random.randint(1,8))+" DMG)"]
            #+ ["Gas (Sleep)"]
            RoomButton.configure(text="TRAP!\nType:"+random.choice(Type)+"\nDetection:{}\nEvasion:{}".format(str(random.randint(10,16)), str(random.randint(10,18))))
        if x == 6:
            x == random.randint(1,6)




    ControlFrame = LabelFrame(main)
    UPBUTTON = Button(ControlFrame, text="↑")
    UPBUTTON.grid(column=1, row=0, sticky='news') 
    
    LEFTBUTTON = Button(ControlFrame, text="←")
    LEFTBUTTON.grid(column=0, row=1, sticky='news')

    RIGHTBUTTON =  Button(ControlFrame, text="→") 
    RIGHTBUTTON.grid(column=2, row=1, sticky='news')  

    DOWNBUTTON =  Button(ControlFrame, text="↓")
    DOWNBUTTON.grid(column=1, row=2, sticky='news')

    EVENTBUTTON = Button(ControlFrame, text="EVENT", command=lambda:[ButtonEvent(random.randint(1,6))])
    EVENTBUTTON.grid(column=0, columnspan=3, row=3, sticky='news')





    ControlFrame2 = LabelFrame(main)
    FLOOR2BUTTON  = Button(ControlFrame2, text="2F")
    FLOOR2BUTTON.pack(fill=X)
    FLOOR1BUTTON = Button(ControlFrame2, text="1F")
    FLOOR1BUTTON.pack()

    

    

    


     


    
    #main.attributes('-fullscreen', True)
    
    
    
    
    if x == 0:
        main.geometry("1032x719")
        r1 =interfacewindow(main, "TestMap", "Templemap", "Few Paths Forbidden", "5")
        


    if x == 1:
        r1 =interfacewindow(main, "Forest [Start]", "Forest0", "Few Paths Forbidden", "5")
        
    if x == 2:
        r1 =interfacewindow(main, "TestMap", "Village1_1", "Few Paths Forbidden", "5")

    if x == 3:
        r1 =interfacewindow(main, "TestMap", "ForestBattlemap", "Few Paths Forbidden", "5")
        

    if x ==4:
        r1 =interfacewindow(main, "Forest [1]", "Forest1", "Few Paths Forbidden", "5")
        
    if x == 5:
        r1 =interfacewindow(main, "Forest [2]", "Forest2", "Few Paths Forbidden", "5")
        

    if x == "GLUp":
        r1 =interfacewindow(main, "Goblin's Lace [Upstairs]", "GLupstairs", "tea-time", "5")
        ControlFrame2.place(x=80, y=200)
        FLOOR2BUTTON.config(command=lambda:"")
        FLOOR1BUTTON.config(command=lambda:Page("GLDown"))
        
        
    
    if x == "GLDown":
        r1 =interfacewindow(main, "Goblin's Lace [Downstairs]", "GLdownstairs", "tea-time", "5")
        ControlFrame2.place(x=80, y=200)
        FLOOR2BUTTON.config(command=lambda:Page("GLUp"))
        FLOOR1BUTTON.config(command=lambda:"")
        
    if x == "MH":
        r1 =interfacewindow(main, "Meadhaven", "Meadhaven", "harbor", "5")
        pygame.mixer.music.load(resource_path(("harbor.mp3"))), pygame.mixer.music.play(-1)
    
    if x == "Plains1":
        

        r1 =interfacewindow(main, "Plains [1]", "Battle1", "FeB", "10")
        playermarker2(main)

    if x == "Redboar1":
        r1 =interfacewindow(main, "Redboar Forest 1", "Redboar1", "FeB", "10")

    if x == "Redboar2":
        r1 =interfacewindow(main, "Redboar Forest 2", "Redboar2", "FeB", "10")

    if x == "Gate0":
        r1 =interfacewindow(main, "Derrinsgard [Southern Gate]", "Gate0", "FeB", "10")

    if x == "Manor0":
        r1 =interfacewindow(main, "Avernissi Manor", "ManorBattle", "FeB", "10")
        
        
    

        
        

    if x == "ManorB1A":
        r1 =interfacewindow(main, "Manor Basement 1A", "ManorB1_A", "FeB", "5")


    if x == "ManorInt1-1":
        r1 =interfacewindow(main, "Avernissi Manor [Entrance]", "ManorInt1_1", "FeB", "10")
        

    if x == "ManorInt1-2":
        r1 =interfacewindow(main, "Avernissi Manor [Dining Hall]", "ManorInt1_2", "FeB", "5")
        

    if x == "ManorInt1-3":
        r1 =interfacewindow(main, "Avernissi Manor [Stairs]", "ManorInt1_3", "FeB", "5")
        

    if x == "ManorInt2-1":
        r1 =interfacewindow(main, "Avernissi Manor [Hallway Floor 2]", "ManorInt2_1", "FeB", "5")
        

    if x == "Maze1_J":
        r1 =interfacewindow(main, "Manor Maze", "Maze1_J", "FeB", "5")


    #MAZE
    #-------MAZE A--------------
    if x == "Maze1-A1":

        r1 =interfacewindow(main, "Manor Maze [A-1]", "Maze1-R", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-B1")])
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-A2")])
        LEFTBUTTON.configure(state=DISABLED)


        #Placement Issues
        #Room Setup [Pending]

        

    if x == "Maze1-A2": #Maze Start

        r1 =interfacewindow(main, "Manor Maze [A-2]", "Maze1-X", "FeB", "5")


        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-A1")])
        RIGHTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-B2")])
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-A3")])
        LEFTBUTTON.configure(state=DISABLED)        

        
        #Room Setup [Pending]
        #Maze Exit/Start

        

    if x == "Maze1-A3":
        
        r1 =interfacewindow(main, "Manor Maze [A-3]", "Maze1-U", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-A2")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(state=DISABLED)

        #def StatueSet():

        StatueButton = Button(main, command=lambda:StatueFrame.place(x=900, y=200))
        StatueButton.place(x=610, y=530)


        def StatueAnswers(x, y):
            global TotalEntries, Bridd, Bladd, Dowrr
            
            if y == "Bride":
                if x == "Andrade Ostegarre" or x== "Chasity Wellwyrth":
                    Bridd = FAEntry.get()
                    FAEntry.config(state=DISABLED)
                    TotalEntries = TotalEntries+1
                    print(TotalEntries, Bridd)
                else:
                    FAEntry.delete(0, END)

            if y == "Blade":
                if x == "Aramil Liadon" or x=="Ralba Brenshu":
                    Bladd = SAEntry.get()
                    SAEntry.config(state=DISABLED)
                    TotalEntries = TotalEntries+1
                    print(TotalEntries, Bladd)
                else:
                    SAEntry.delete(0, END)

            if y == "Dowry":
                if x == "Wedna Argolyngxia" or x== "Horus Audlevance":
                    Dowrr = TAEntry.get() 
                    TAEntry.config(state=DISABLED)
                    TotalEntries = TotalEntries+1
                    print(TotalEntries, Dowrr)
                else:
                    TAEntry.delete(0, END)

            if TotalEntries >=3:
                StatueFrame.place_forget()
                S_ResultsLbl.configure(text="So Shall Be Written\nSo Shall Be Decreed\nBy The Light To Guide The World,\nBlind It In Splendor,\nBring Purification By The Flame:\n\n"+Bridd+" Commands\n"+Bladd+" Obeys\n"+Dowrr+" Set For Sacrifice")
                StatueResults.place(x=300, y=275)
                
                
                
            
                    

            
                    



        StatueFrame = LabelFrame(main)

        StatueLabel = Label(StatueFrame, text="Statue")
        StatueLabel.pack()

        FirstAnswerFrame = LabelFrame(StatueFrame)
        FALabel = Button(FirstAnswerFrame, text="~ELVISH~", command=lambda:[FALabel.configure(text="'The Bride'")])
        FALabel.pack()
        FAEntry = Entry(FirstAnswerFrame)
        FAEntry.pack()
        FAEntry.bind("<Return>", (lambda event:StatueAnswers(str(FAEntry.get()), "Bride")))
        FirstAnswerFrame.pack()

        SecondAnswerFrame = LabelFrame(StatueFrame)
        SALabel = Button(SecondAnswerFrame, text="~COMMON~", command=lambda:[SALabel.configure(text="'The Blade'")])
        SALabel.pack()
        SAEntry = Entry(SecondAnswerFrame)
        SAEntry.pack()
        SAEntry.bind("<Return>", (lambda event:StatueAnswers(str(SAEntry.get()), "Blade")))
        SecondAnswerFrame.pack()

        ThirdAnswerFrame = LabelFrame(StatueFrame)
        TALabel = Button(ThirdAnswerFrame, text="~DRACONIC~", command=lambda:[TALabel.configure(text="'The Dowry'")])
        TALabel.pack()
        TAEntry = Entry(ThirdAnswerFrame)
        TAEntry.pack()
        TAEntry.bind("<Return>", (lambda event:StatueAnswers(str(TAEntry.get()), "Dowry")))
        ThirdAnswerFrame.pack()

        CancelButton = Button(StatueFrame, text="Cancel", command=lambda:StatueFrame.place_forget())
        CancelButton.pack(fill=X)



        

        StatueResults = LabelFrame(main)
        S_ResultsLbl = Label(StatueResults)
        S_ResultsLbl.pack()
        OKButton = Button(StatueResults, text=">", command=lambda:[StatueResults.place_forget(), HiddenFloorButton.place(x=150, y=300)])
        OKButton.pack(side=RIGHT)


        HiddenFloorButton = Button(main, command=lambda:[main.destroy(), Page("Maze1-A4")])



        #SPECIAL?!?!

    if x == "Maze1-A4":
        r1 =interfacewindow(main, "Manor Maze [A-4]", "MazeA4", "FeB", "5")

        #Good to go! 
        #Exit Button to next scene?

    #-----------------------------
    #-----MAZE B------------------
    if x == "Maze1-B1":
        r1 =interfacewindow(main, "Manor Maze [B-1]", "Maze1_-", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-C1")])
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-A1")])


    if x == "Maze1-B2":
        r1 =interfacewindow(main, "Manor Maze [B-2]", "Maze1-T", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-C2")])
        DOWNBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-B3")])
        LEFTBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-A2")])




    if x == "Maze1-B3":
        r1 =interfacewindow(main, "Manor Maze [B-3]", "Maze1-U", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(),Page("Maze1-B2")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(state=DISABLED)


    

    if x == "Maze1-B4":
        r1 =interfacewindow(main, "Manor Maze [B-4]", "Maze1_-END2", "FeB", "5") 

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-C4")])
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(state=DISABLED)

        def OpenChest():
            CHESTButton.place_forget()
            CHESTButton.configure(image="", text="A stone slab (2/3)\nIt appears to be\nELVISH script\n\n[Item Code:'HAIMM']") 
            CHESTButton.configure(command=lambda:CHESTButton.place_forget())
            CHESTButton.place(x=200, y=100)



        main.Chst = PhotoImage(file=resource_path("chst.png"))
        CHESTButton = Button(main, image=main.Chst, command=lambda:[OpenChest()])        
        CHESTButton.place(x=250, y=225)
 
    #--------------------------
    # -------MAZE C-----------
    if x == "Maze1-C1":
        r1 =interfacewindow(main, "Manor Maze [C-1]", "Maze1_-", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D1")])
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-B1")])

    
    if x == "Maze1-C2":
        r1 =interfacewindow(main, "Manor Maze [C-2]", "Maze1_-2", "FeB", "5")

        
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-B2")])
        ControlFrame.place(x=80, y=200)


        def OpenChest():
            CHESTButton.place_forget()
            CHESTButton.configure(image="", text="A stone slab (1/3)\nIt appears to be\nDRACONIC script\n\n[Item Code:'KWQPB']")
            CHESTButton.place(x=200, y=100)



        main.Chst = PhotoImage(file=resource_path("chst.png"))
        CHESTButton = Button(main, image=main.Chst, command=lambda:[OpenChest()])        
        CHESTButton.place(x=900, y=225)

    if x == "Maze1-C3":
        r1 =interfacewindow(main, "Manor Maze [C-3]", "Maze1-R", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D3")])
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-C4")])
        LEFTBUTTON.configure(state=DISABLED)




    if x == "Maze1-C4":
        r1 =interfacewindow(main, "Manor Maze [C-4]", "Maze1_J", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-C3")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(state=DISABLED)
        LEFTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-B4")])


    #------------------------------------
    #------MAZE D--------------

    if x == "Maze1-D1":
        r1 =interfacewindow(main, "Manor Maze [D-1]", "Maze1-L", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(state=DISABLED)
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D2")])
        LEFTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-C1")])



    if x == "Maze1-D2":
        r1 =interfacewindow(main, "Manor Maze [D-2]", "Maze1_I", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D1")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D3")])
        LEFTBUTTON.configure(state=DISABLED)




    if x == "Maze1-D3":
        r1 =interfacewindow(main, "Manor Maze [D-3]", "Maze1-H", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D2")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D4")])
        LEFTBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-C3")]) 




    if x == "Maze1-D4":
        
        r1 =interfacewindow(main, "Manor Maze [D-4]", "Maze1-U", "FeB", "5")

        ControlFrame.place(x=80, y=200)
        UPBUTTON.configure(command=lambda:[main.destroy(), Page("Maze1-D3")])
        RIGHTBUTTON.configure(state=DISABLED)
        DOWNBUTTON.configure(state=DISABLED) 
        LEFTBUTTON.configure(state=DISABLED) 

        def OpenChest():
            CHESTButton.place_forget()
            CHESTButton.configure(image="", text="A stone slab (3/3)\nIt appears to be\nCOMMON script\n\n[Item Code:'UIFJI']") 
            CHESTButton.configure(command=lambda:CHESTButton.place_forget())
            CHESTButton.place(x=200, y=100)



        main.Chst = PhotoImage(file=resource_path("chst.png"))
        CHESTButton = Button(main, image=main.Chst, command=lambda:[OpenChest()])        
        CHESTButton.place(x=590, y=330)

        


     



Startbutton = Button(main, text="Button", command=lambda:Page(0))
Startbutton.pack()

            
  

class playermarker2:
    def __init__(self, main):

        
        self.root = main

                
        def reset():
            CLabel.config(text="Command")
            Button1.pack(fill=X)
            Button2.pack(fill=X)
            Button3.pack(fill=X)
            Button1.config(text="Attack", command=lambda:Interaction(monster, "ATK"))
            Button2.config(text="Talk", command=lambda:Interaction(monster, "TLK"))
            Button3.config(text="Stats", command=lambda:Interaction(monster, "STS"))
            CommandLF.place_forget()


        def critfail():
            ATK_E.delete(0, END)
            ATK_E.insert(0, "1")
            ATK_E.config(bg='black', fg='white')
            DMG_E.delete(0, END)
            DMG_E.insert(0, "X")

        def critsuccess():
            ATK_E.config(bg='red', fg='white')
            DMG_E.delete(0, END)
            
        


        def Battle(mon, wpn):
            Button1.pack_forget()
            Button2.pack_forget()
            Button3.pack_forget()
            
            CLabel.config(text=wpn)

            AttackFrame.pack()
                        
            ATKLabel.pack(side=LEFT)
            
            ATK_E.pack()

            DamageFrame.pack()

            
            DMGLabel.pack(side=LEFT)

            DMG_E.pack()

           
            M_Button.pack(fill=X) 

            R_Button.pack(fill=X)

            V_Button.pack(fill=X)

            if mon == "Orc":
                V_Button.pack_forget()
                M_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Orc", "Javelin\n(melee)")])
                R_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Orc", "Javelin\n(throw)")])

            if mon == "Hobgoblin":
                R_Button.pack_forget()
                M_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Hobgoblin", "Longsword\n(melee)")])
                V_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Hobgoblin", "Longsword\n(2-hand)")])

            if mon == "Bugbear":
                V_Button.pack_forget()
                M_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Bugbear", "Javelin\n(melee)")])
                R_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Bugbear", "Javelin\n(throw)")])

            if mon == "Guard":
                M_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Guard", "Spear\n(melee)")])
                R_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Guard", "Spear\n(throw)")])
                V_Button.configure(command=lambda:[ResultsFrame.pack_forget(), Battle("Guard", "Spear\n(2-hand)")])

            

            else:
                pass

            if wpn == "Javelin" or wpn == "Spear" or wpn =="Longsword":
                ExtraFrame.pack(side=RIGHT)
            else:
                ExtraFrame.pack_forget()



            
            OKButton.pack(side=BOTTOM)

            ResultsFrame.pack()

            if mon == "Companion":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Bite":
                    A = random.randint(7,26) 
                    ATK_E.insert(0, A)
                    E = random.randint(5,10)  
                    DMG_E.insert(0, E)
                    if A == 7:
                        critfail()
                    elif A == 26:
                        critsuccess()
                        DMG_E.insert(0, random.randint(6,16)) 
                    else:
                        ATK_E.config(bg='white', fg='black')


            if mon == "Zombie":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Slam":
                    A = random.randint(4,23) 
                    ATK_E.insert(0, A)
                    E = random.randint(2,7)  
                    DMG_E.insert(0, E)
                    if A == 4:
                        critfail()
                    elif A == 23:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,13)) 
                    else:
                        ATK_E.config(bg='white', fg='black')



            if mon == "Bandit":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Scimitar":
                    A = random.randint(4,23) 
                    ATK_E.insert(0, A)
                    E = random.randint(2,7)  
                    DMG_E.insert(0, E)
                    if A == 4:
                        critfail()
                    elif A == 23:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,13)) 
                    else:
                        ATK_E.config(bg='white', fg='black')

                if wpn == "L.Crossbow":
                    A = random.randint(4,23) 
                    ATK_E.insert(0, A)
                    E = random.randint(2,9)  
                    DMG_E.insert(0, E)
                    if A == 4:
                        critfail()
                    elif A == 23:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,17)) 
                    else:
                        ATK_E.config(bg='white', fg='black')



            if mon == "Cultist":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Scimitar":
                    A = random.randint(5,24) 
                    ATK_E.insert(0, A)
                    E = random.randint(3,8)  
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,14)) 
                    else:
                        ATK_E.config(bg='white', fg='black')


            if mon == "Goblin":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Scimitar" or wpn == "Shortbow":
                    A = random.randint(5,24) 
                    ATK_E.insert(0, A)
                    E = random.randint(3,8)  
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,14)) 
                    else:
                        ATK_E.config(bg='white', fg='black')

                        
            if mon == "Bugbear":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Morningstar": 
                    A = random.randint(5,24)  
                    ATK_E.insert(0, A)
                    E = random.randint(4,18) 
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,26))  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    

                if wpn == "Javelin\n(melee)":#melee
                    A = random.randint(5,24)  
                    ATK_E.insert(0, A)
                    E = random.randint(4,14)  
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,20))  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Javelin stuff")

                if wpn == "Javelin\n(throw)":#range
                    A = random.randint(5,24)  
                    ATK_E.insert(0, A)
                    E = random.randint(3,8) 
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,14)) #2d6+2  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Javelin2 stuff")


            if mon == "Skeleton":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Shortsword" or wpn == "Shortbow":
                    A = random.randint(5,24) 
                    ATK_E.insert(0, A)
                    E = random.randint(3,8)  
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,14)) 
                    else:
                        ATK_E.config(bg='white', fg='black')

            if mon == "Berserker":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Greataxe":
                    A = random.randint(6,25) 
                    ATK_E.insert(0, A)
                    E = random.randint(4,15) #1d12+3  
                    DMG_E.insert(0, E)
                    if A == 6:
                        critfail()
                    elif A == 25:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,27)) #2d12+3
                    else:
                        ATK_E.config(bg='white', fg='black')



            if mon == "Scout":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Shortsword": 
                    A = random.randint(5,24) 
                    ATK_E.insert(0, A)
                    E = random.randint(3,8) 
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,14)) 
                    else:
                        ATK_E.config(bg='white', fg='black')

                if wpn == "Longbow": 
                    A = random.randint(5,24) 
                    ATK_E.insert(0, A)
                    E = random.randint(3,10) 
                    DMG_E.insert(0, E)
                    if A == 5:
                        critfail()
                    elif A == 24:
                        critsuccess()
                        DMG_E.insert(0, random.randint(4,18)) 
                    else:
                        ATK_E.config(bg='white', fg='black')



            if mon == "Hobgoblin":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)

                if wpn == "Longsword\n(melee)" or wpn == "Longbow": 
                    A = random.randint(4,23)  
                    ATK_E.insert(0, A)
                    E = random.randint(2,9) 
                    DMG_E.insert(0, E)
                    if A == 4:
                        critfail()
                    elif A == 23:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,17))  
                    else:
                        ATK_E.config(bg='white', fg='black')

                if wpn == "Longsword\n(2-hand)": 
                    A = random.randint(4,23)  
                    ATK_E.insert(0, A)
                    E = random.randint(2,11) 
                    DMG_E.insert(0, E)
                    if A == 4:
                        critfail()
                    elif A == 23:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,21))  
                    else:
                        ATK_E.config(bg='white', fg='black')



            if mon == "Orc":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                if wpn == "Greataxe": 
                    A = random.randint(6,25)  
                    ATK_E.insert(0, A)
                    E = random.randint(4,15) 
                    DMG_E.insert(0, E)
                    if A == 6:
                        critfail()
                    elif A == 25:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,27))  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    

                if wpn == "Javelin\n(melee)":#melee
                    A = random.randint(6,25)  
                    ATK_E.insert(0, A)
                    E = random.randint(4,9)  
                    DMG_E.insert(0, E)
                    if A == 6:
                        critfail()
                    elif A == 25:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,15))  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Javelin stuff")

                if wpn == "Javelin\n(throw)":#range
                    A = random.randint(6,25)  
                    ATK_E.insert(0, A)
                    E = random.randint(4,9) 
                    DMG_E.insert(0, E)
                    if A == 6:
                        critfail()
                    elif A == 25:
                        critsuccess()
                        DMG_E.insert(0, random.randint(5,15)) #1d6+3  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Javelin2 stuff")


            if mon == "Guard":
                ATK_E.delete(0, END)
                DMG_E.delete(0, END)
                    

                if wpn == "Spear\n(melee)":
                    A = random.randint(1,20)  
                    ATK_E.insert(0, A+3)
                    E = random.randint(2,7)  #1d6+1
                    DMG_E.insert(0, E)
                    if A == 1:
                        critfail()
                    elif A == 20:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,13)) #2d6+1 
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Spear stuff")

                if wpn == "Spear\n(throw)":#range
                    A = random.randint(1,20)  
                    ATK_E.insert(0, A+3)
                    E = random.randint(2,7) 
                    DMG_E.insert(0, E)
                    if A == 1:
                        critfail()
                    elif A == 20:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,13)) #2d6+1  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Spear2 stuff")


                if wpn == "Spear\n(2-hand)":#versatile
                    A = random.randint(1,20)  
                    ATK_E.insert(0, A+3)
                    E = random.randint(2,9) #1d8+1 
                    DMG_E.insert(0, E)
                    if A == 1:
                        critfail()
                    elif A == 20:
                        critsuccess()
                        DMG_E.insert(0, random.randint(3,17)) #2d8+1  
                    else:
                        ATK_E.config(bg='white', fg='black')
                    print("Spear3 stuff")



                




        def Interaction(monster, y):
            if monster == "Berserker":
                if y == "ATK":
                    Button1.config(text="Greataxe", command=lambda:[Battle("Berserker", "Greataxe")])
                    Button2.pack_forget()
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Berserker ROAR!!")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Berserker    CR:2")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:67   AC: 13  Spd: 30ft\nSTR:16(+3)  DEX:12(+1)  CON:17(+3)\nINT:9(+0)  WIS:11(+0)   CHA:9(+0)\nSenses: Pass Per. 10\nLanguages: One (usually Common)\n\nRECKLESS:\nWhile active, has Adv. on melee atk rolls.\nOpponents also have Adv. on melee\n atk rolls against Berserker. ")

            if monster == "Ozel":
                def OzyAction(x):
                    OzyTalkWindow.delete(1.0, END)
                    OzyEntry.delete(0, END)

                    if x == "Greetz":

                        hellow = ["Waddaya want?"] + ["If you tip me really well, I promise I won't spit in your food!"] + ["I'm not on the menu...But my foot is! As a suppository!"] +\
                                ["Can you even afford the food here?"] + ["Hurry up, will ya? I don't have all day!"] + ["Buzz off!"] + ["No, YOU write it down!!!"] + ["I put the 'Goblin' in 'The Goblin's Lace'...\nBut I won't tell you where...."] +\
                                    ["*Burp* Excuse me!"] + ["No refunds! Sorry! Hehehe."] + ["No weapons allowed in the bar. Or I cut ya! Understand?"] + ["Call me 'shortstack' again and see what happens!!!"]
                            
                        greeting = random.choice(hellow)

                        OzyTalkWindow.insert(END, greeting)

                    if x == "FLIRT":
                        OzyTalkWindow.insert(END, "[If Pass, 'FLIRTPASS' if Fail, 'FLIRTFAIL']")

                    if x == "FLIRTPASS":
                        Flirtpass = ["*Blush* SHUT UP, you loser! ♥"] + ["NOT WHILE I'M WORKING, DUMBASS! ☺"]
                        Flirtsuccess = random.choice(Flirtpass)

                        OzyTalkWindow.insert(END, Flirtsuccess)

                    if x == "FLIRTFAIL":
                        thing = ["hag's nipple."] + ["mongrelfolk's third nostril."] + ["grell's tentacle."] + ["hellhound's taint."] + ["dried squilliam."] + ["bullywug's armpit."]
                        Flirtnope = ["PICK A HELL. Go there IMMEDIATELY."] + ["You can kiss the door. Or the floor. Your choice, pal!"] + ["Go lick a "+random.choice(thing)]

                        Flirtbad = random.choice(Flirtnope)

                        OzyTalkWindow.insert(END, Flirtbad)





                if y == "TLK":
                    CommandLF.place_forget()
                    TLabel.config(image=self.Ozy2Tlk)
                    TLabel.config(command=lambda:OzyAction("Greetz"))
                    PMarker.configure(bg='teal')
                    HPMaxSpinbox.pack_forget()
                    OzyTalkWindow = Text(PMarker, width=20, height=5, font='helvetica 8 bold', wrap='word')
                    OzyTalkWindow.pack()
                    
                    
                    OzyEntry = Entry(PMarker)
                    OzyEntry.pack()
                    OzyEntry.bind("<Return>", (lambda event:OzyAction(OzyEntry.get())))
                    print("Ozytalking") 

                if y == "STS":
                    CLabel.config(text="Ohzelmea (Goblin)")
                    Button1.pack()
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="A goblin girl rescued by the wizard Roscoe Flores.\nShe is currently employed at the Goblin's Lace.\nDespite her surly demeanor, she is surprisingly popular.")

                    




            if monster == "Bandit":
               
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Scimitar", command=lambda:[Battle("Bandit", "Scimitar")])
                    Button2.config(text="L.Crossbow", command=lambda:[Battle("Bandit", "L.Crossbow")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Stealyboi Grumbles")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Bandit    CR:1/8")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:11   AC: 12(leather)  Spd: 30ft\nSTR:11(+0)  DEX:12(+1)  CON:12(+1)\nINT:10(+0)  WIS:10(+0)  CHA:10(+0)\nSenses: Pass Per. 10\nLanguages: Usually Common")
            

            if monster == "Cultist":
                if y == "ATK":
                    Button1.config(text="Scimitar", command=lambda:[Battle("Cultist", "Scimitar")])
                    Button2.pack_forget()
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    
                    print("Cultist Mumblings")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Cultist    CR:1/8")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:9   AC: 12  Spd: 30ft\nSTR:11(+0)  DEX:12(+1)  CON:10(+0)\nINT:10(+0)  WIS:10(+0)   CHA:10(+0)\nSkills: Religion +2  Deception +2\nSenses: Pass Per. 10\nLanguages: One (usually Common)\n\nDARK DEVOTION:\nHas Advantage on Saves against\nbeing [Charmed] or [Frightened]")
                    

            if monster == "Companion":
                if y == "ATK":
                    CLabel.config(text="Command")
                    Button1.config(text="Bite", command=lambda:[Battle("Companion", "Bite")])
                    Button2.pack_forget()
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("WOOF!")
                    CommandLF.place_forget(), reset()
                    


                if y == "STS":
                    CLabel.config(text="Blink Dog    CR:1/4")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:22   AC: 16  Spd: 40ft\nSTR:12(+1)  DEX:17(+3)  CON:12(+1)\nINT:10(+0)  WIS:13(+1)  CHA:11(+0)\nSkills: Stealth +8  Perception+6\nSenses: Pass Per. 10\nLanguages: Understands Sylvan; Mute.\n\nKEEN HEARING/SMELL:\nHas Advantage on hearing/smell-based\nWisdom(Perception) checks.\n\nTELEPORT (Recharge 5-6):\nIncluding equipment worn/carried, teleports\n40ft to a visible unoccupied space\nCan Bite before or after teleporting.")
            

            if monster == "Zombie":
                if y == "ATK":
                    CLabel.config(text="Command")
                    Button1.config(text="Slam", command=lambda:[Battle("Zombie", "Slam")])
                    Button2.pack_forget()
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("BRAIIIIIINSSSS")
                    CommandLF.place_forget(), reset()
                    


                if y == "STS":
                    CLabel.config(text="Zombie    CR:1/4")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:22   AC: 8  Spd: 20ft\nSTR:13(+1)  DEX:6(-2)  CON:16(+3)\nINT:3(-3)  WIS:6(-2)  CHA:5(-2)\nImmunities:Poisoned(condition)\nSenses: DkVis 60ft, Pass Per. 8\nLanguages: Mute.\n\nUNDEAD FORTITUDE:\nAt 0 dmg, CON Save (DMG+5*)\nPass:Drops to 1 HP instead\nFail:Death\n*Auto-fail if Radiant or Critical Dmg")
                    


            if monster == "Skeleton":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Shortsword", command=lambda:[Battle("Skeleton", "Shortsword")])
                    Button2.config(text="Shortbow", command=lambda:[Battle("Skeleton", "Shortbow")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Skelebones rattle")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Skeleton    CR:1/4")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:13   AC: 13  Spd: 30ft\nSTR:10(+0)  DEX:14(+2)  CON:15(+2)\nINT:6(-2)  WIS:8(-1)   CHA:5(-2)\nVulnerabilities: Bludgeoning (damage)\nImmunities: Poisoned (condition)\nSenses: DkVis 60ft, Pass Per. 9\nLanguages:Mute\n\nSHORTBOW:\nRange: 80/320 ft")
                    

            if monster == "Scout":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Shortsword", command=lambda:[Battle("Scout", "Shortsword")])
                    Button2.config(text="Longbow", command=lambda:[Battle("Scout", "Longbow")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Scout talking")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Scout    CR:1/2")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:16   AC: 13  Spd: 30ft\nSTR:11(+0)  DEX:14(+2)  CON:12(+1)\nINT:11(+0)  WIS:13(+1)   CHA:11(+0)\nSkills: Stealth +6  Nature +4\nPerception +5  Survival +5\nSenses: Pass Per. 15\nLanguages:One (usually Common)\n\nKEEN SENSES:\nAdvantage on sight or hearing-based\nWisdom(Perception) checks.\nMULTIATTACK:\nMakes 2 melee or 2 ranged attacks\nLONGBOW:\nRange: 150/600 ft")
                    


            if monster == "Goblin":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Scimitar", command=lambda:[Battle("Goblin", "Scimitar")])
                    Button2.config(text="Shortbow", command=lambda:[Battle("Goblin", "Shortbow")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("GOBBO NOISES")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Goblin    CR:1/4")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:7   AC: 15  Spd: 30ft\nSTR:8(-1)  DEX:14(+2)  CON:10(+0)\nINT:10(+0)  WIS:8(-1)  CHA:8(-1)\nSkills: Stealth +6\nSenses: DkVis 60ft, Pass Per. 9\nLanguages: Common, Goblin\n\nNIMBLE ESCAPE:\nCan use Bonus Actions\n[DISENGAGE] or [HIDE]\nat the end of its turn.")
                    


            if monster == "Hobgoblin":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Longsword", command=lambda:[Battle("Hobgoblin", "Longsword")])
                    Button2.config(text="Longbow", command=lambda:[Battle("Hobgoblin", "Longbow")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("HOBBGOBBO NOISES")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Hobgoblin    CR:1/2")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:11   AC: 18(c.mail+shld)  Spd: 30ft\nSTR:13(+1)  DEX:12(+1)  CON:12(+1)\nINT:10(+0)  WIS:10(+0)  CHA:9(-1)\nSenses: DkVis 60ft, Pass Per. 10\nLanguages: Common, Goblin\n\nMARTIAL ADVANTAGE:\n+2d6 DMG if target creature\nis w/in 5' of an active ally\n(1x per turn)")
            


            if monster == "Orc":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Greataxe", command=lambda:[Battle("Orc", "Greataxe")])
                    Button2.config(text="Javelin", command=lambda:[Battle("Orc", "Javelin")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Orc Grunts")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Orc    CR:1/2")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:15   AC: 13  Spd: 30ft\nSTR:16(+3)  DEX:12(+1)  CON:16(+3)\nINT:7(-1)  WIS:11(+0)  CHA:10(+0)\nSkills: Intimidation +2\nSenses: DkVis 60ft, Pass Per. 10\nLanguages: Common, Orc\n\nAGGRESSIVE:\nCan use Bonus Action [DASH]\ntowards enemies it can see.")
                    


            if monster == "Guard":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Spear", command=lambda:[Battle("Guard", "Spear")])
                    Button2.pack_forget()
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Guardly mumblings")
                    pygame.mixer.find_channel().play(GuardTalk)
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Guard    CR:1/8")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:11   AC: 16  Spd: 30ft\nSTR:13(+1)  DEX:12(+1)  CON:12(+1)\nINT:10(+0)  WIS:11(+0)  CHA:10(+0)\nSkills: Perception +2\nSenses:Pass Per. 12\nLanguages: One (usually Common)\n\nSPEAR:\n*Melee--5ft  *Range--20/60ft")
                    



            if monster == "Bugbear":
                if y == "ATK":
                    CLabel.config(text="Attack!")
                    Button1.config(text="Morningstar", command=lambda:[Battle("Bugbear", "Morningstar")])
                    Button2.config(text="Javelin", command=lambda:[Battle("Bugbear", "Javelin")])
                    Button3.config(text="[Cancel]", command=lambda:[CommandLF.place_forget(), reset()])

                if y == "TLK":
                    print("Bugbear NOISES")
                    CommandLF.place_forget(), reset()


                if y == "STS":
                    CLabel.config(text="Bugbear      CR:1")
                    Button2.pack_forget()
                    Button3.pack_forget()
                    Button1.config(command=lambda:[CommandLF.place_forget(), reset()])
                    Button1.config(text="HP:27   AC: 16  Spd: 30ft\nSTR:15(+2)  DEX:14(+2)  CON:13(+1)\nINT:8(-1)  WIS:11(+0)  CHA:9(+0)\nSkills: Stealth +6  Survival +2\nSenses: DkVis 60ft, Pass Per. 10\nLanguages: Common, Goblin\n\nSURPRISE ATTACK:\n Dmg+2d6 on [Surprised] enemies\nit attacks in the first round of combat.")
                    
                    



        

            




        def HPAdjust(x):
            HPMaxSpinbox.configure(to=x)
            if x <= 0:
                PMarker.place_forget()


        def itemboxspot(x, y, thing):
            ItemLF.place_forget()
            ItemLF.place(x=x, y=y)
            I_Button3.pack_forget()
            I_Button4.pack_forget()
            I_Button5.pack_forget()
            I_Button6.pack_forget()
            I_Button7.pack_forget()
            I_Button8.pack_forget() 
            I_Parser.pack_forget()

            def recruit(x):
                ItemLF.place_forget()
                
                if x == 1: #Guard
                    TLabel.config(image=self.Guard)
                    HPMaxSpinbox.config(from_=0, to=11, width=2)
                    HPMaxSpinbox.insert(0, 11)
                    HPMaxSpinbox.pack()
                    TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Guard")])
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "gard")

                if x == 2: #cultist
                    TLabel.config(image=self.cult)
                    HPMaxSpinbox.config(from_=0, to=9, width=1)
                    HPMaxSpinbox.insert(0, 9)
                    HPMaxSpinbox.pack()
                    TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Cultist")])
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "kult")

                if x == 3: #orc                        
                    TLabel.config(image=self.orc)
                    HPMaxSpinbox.config(from_=0, to=15, width=2)
                    HPMaxSpinbox.insert(0, 15)
                    HPMaxSpinbox.pack()
                    TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Orc")])
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "ork")

                if x == "Temple":#healing temple
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Tmp")

                if x == "Item":#general loot
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Itm")

                if x == "Flora1":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Flo1")

                if x == "AricinEvent":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Arc")

                if x == "BahimboEvent":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Himbo")
                    

                if x == "CaramilEvent":
                    pass

                if x == "HarlowEvent":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Harl")
                    

                if x == "KopfgeldEvent":
                    pass

                if x == "OlgaEvent":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Olgz")
                    

                if x == "RoscoeEvent":
                    confirmmessagespot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Ross")
                    

                if x == "NonEvent":
                    pass




            if thing == "F1":
                ILabel.config(text="Forage")
                I_Button1.config(text="Pass")
                I_Button2.config(text="Fail")
                I_Button2.config(command=lambda:[ItemLF.place_forget(), TLabel.pack_forget()])
                I_Button1.config(command=lambda:[recruit("Flora1")])
                print("ITEM STUFF")


            if thing == "Itm?":
                I_Button1.config(text="Open")
                I_Button1.config(command=lambda:[recruit("Item")])
                print("ITEM STUFF")

            if thing == "Unk*":

                
                I_Button1.pack_forget()
                I_Button2.pack_forget()
                I_Button3.pack_forget()
                ILabel.pack_forget()

                ILabel.config(text="???")
                ILabel.grid(column=0, row=0, columnspan=2, sticky='news')

                I_Button1.config(text="Aricin", command=lambda:recruit("AricinEvent"))
                I_Button1.grid(column=0, row=1, sticky='news')
                #I_Button1.config(command...) 


                I_Button2.config(text="Bahimbo", command=lambda:recruit("BahimboEvent"))
                I_Button2.grid(column=0, row=2, sticky='news')
                #I_Button2.config(command...) 

                I_Button3.config(text="Caramil")
                I_Button3.grid(column=0, row=3, sticky='news')
                #I_Button3.config(command...)


                I_Button4.config(text="Harlow", command=lambda:recruit("HarlowEvent"))
                I_Button4.grid(column=0, row=4, sticky='news')
                #I_Button4.config(command...)


                I_Button5.config(text="Kopfgeld")
                I_Button5.grid(column=1, row=1, sticky='news')
                #I_Button5.config(command...)


                I_Button6.config(text="Olga", command=lambda:recruit("OlgaEvent"))
                I_Button6.grid(column=1, row=2, sticky='news')
                


                I_Button7.config(text="Roscoe", command=lambda:recruit("RoscoeEvent"))
                I_Button7.grid(column=1, row=3, sticky='news')
                


                I_Button8.config(text="----", command=lambda:ItemLF.place_forget())
                I_Button8.grid(column=1, row=4, sticky='news')
                #I_Button8.config(command...)

                I_Parser.grid(column=0, row=5, columnspan=2, sticky='news')

                #I_Parser.bind("<Return>", (lambda event:(I_Parser.get(x)))))

                

                




            if thing == "Temple":
                I_Button1.config(text="Heal")
                I_Button1.config(command=lambda:[recruit("Temple")])
                

            if thing == "Unk?":
                I_Button1.config(text="Talk")
                I_Button1.config(command=lambda:[recruit(random.randint(1,3))])
                

            

        def confirmmessagespot(x, y, got):
            AcquiredButton.place(x=x, y=y)
            AcquiredButton.config(command=lambda:AcquiredButton.place_forget())

            



            if got == "ork":
                AcquiredButton.config(text="ORC joined the fight!")

            if got == "kult": 
                AcquiredButton.config(text="CULTIST joined the fight!")
                 
            if got == "gard":
                AcquiredButton.config(text="GUARD joined the fight!") or AcquiredButton.config(text="GUARD ATTACKS!!")
                

            if got == "Itm":
                ITEMZ = [str(random.randint(1,30))+" Gold"]*3 + ["Potion of Healing"] + [str(random.randint(3,12))+random.choice([" arrows", " darts", " light crossbow bolts"])]*2 + [random.choice(["Dagger", "Shortsword", "Greatsword", "Longsword", "Greataxe", "Spear", "Handaxe"])+" "+random.choice(["\n(Spell Surge)"]+[""]*7)]
                AcquiredButton.config(text="Acquired:\n"+random.choice(ITEMZ))
                PMarker.place_forget()

            if got == "Flo1":
                Plants = [str(random.randint(1,4))+" Thelvenfaas\n(herb)"] + [str(random.randint(1,4))+" Gemmelrut\n(root)"] + [str(random.randint(1,4))+" Glassberries\n(berry)"] + [str(random.randint(1,4))+" Kushrooms\n(fungi)"] + [str(random.randint(1,4))+" Fairy's Nettle\n(herb)"] + [str(random.randint(1,4))+" Magemoss\n(plant)"] 
                AcquiredButton.config(text="Acquired:\n"+random.choice(Plants))
                PMarker.place_forget()


            if got == "Arc":
                def ArcOutcome(x):
                    EventChoice1.pack(fill=X)
                    EventChoice2.pack(fill=X)
                    EventChoice3.pack(fill=X)
                    EventChoice4.pack_forget()

                    if x == "A-B-A":
                        EventDialog.configure(text="He raises an eyebrow and nods approvingly, noticeably moved by your warrior's courtesy.\nVial in hand, he salutes then downs his\npotion before taking a stance readied for battle.\n'Let's see if the great Aricin Somnus truly is our better!'\n[ROLL INITIATIVE!]")
                        EventChoice1.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "A-B-B":
                        EventDialog.configure(text="'Rude!' Targus mutters under his breath.\nHe tosses his potion aside, preparing for your rush\n[Initiative order: 1-Aricin; 2-Targus]")
                        EventChoice1.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "A-B-C":
                        EventDialog.configure(text="'We're not WORDSMEN, we're SWORDSMEN..well...\nYou know what I mean!'\nTargus quickly downs his potion and charges at you.\n[Initiative order: 1-Targus  2-Aricin]\nPotion Effect: Heroism\nTargus has *+10 Temp HP *+1d4 to Attack rolls")
                        EventChoice1.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "A-B":
                        EventDialog.configure(text="You throw the potion aside.\nThe vial smashes against the ground,\nits contents inertly drenching the ground.\nThe aged copy looks at you with an expression\nof vague disappointment, but quickly recovers.\n'I'm still drinking mine,' he petulantly insists.") 
                        EventChoice1.configure(text="A: Let him drink his potion.", command=lambda:[ArcOutcome("A-B-A")])
                        EventChoice2.configure(text="B: Stop him from drinking his potion.", command=lambda:[ArcOutcome("A-B-B")])
                        EventChoice3.configure(text="C: Talk to him.", command=lambda:[ArcOutcome("A-B-C")])

                    if x == "A-A":
                        EventDialog.configure(text="'Bottoms up.' He salutes with an identical\npotion in hand, drinking it in unison with you.\nIn short time, you feel a surge of renewed vigor.\n\nPOTION OF HEROISM\n*+10 Temp HP\n*+1d4 to attack rolls & saves\n[Duration: 1hr ]\n\n[ROLL INITIATIVE]")
                        EventChoice1.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "A":
                        EventDialog.configure(text="'Yup. You're one of us all right.'\nHe leaps from the tree bough he once stood upon\nlanding a few feet in front of you. He extends\nhis hand forward and the hilt of a greatsword\nfills his clutch, the large weapon parallel\nto the ground as though it were weightless.\n'Are you wounded?' Before you can answer\nhe throws a familiar dark green potion your way.\n")
                        EventChoice1.configure(text="A: Drink the potion.", command=lambda:[ArcOutcome("A-A")])
                        EventChoice2.configure(text="B: Discard the potion.", command=lambda:[ArcOutcome("A-B")])
                        EventChoice3.configure(text="C: Pocket the potion.", command=lambda:[ArcOutcome("A-C")])

                    if x == "FULLHP":
                        EventDialog.configure(text="You are wounded.' Before you can answer\nTargus throws a familiar dark green potion your way.")
                        EventChoice1.configure(text="A: Drink the potion.", command=lambda:[ArcOutcome("A-A")])
                        EventChoice2.configure(text="B: Discard the potion.", command=lambda:[ArcOutcome("A-B")])
                        EventChoice3.configure(text="C: Pocket the potion.", command=lambda:[ArcOutcome("A-C")])



                    if x == "B-3A-A":
                        EventDialog.configure(text="Is Aricin at Full HP?")
                        EventChoice1.configure(text="A: YES.", command=lambda:[ArcOutcome("FULLHP")])
                        EventChoice2.configure(text="B: NO.", command=lambda:[ArcOutcome("A-B")])
                        EventChoice3.pack_forget()



                    if x == "B-3A":
                        EventDialog.configure(text="'Not sure yet,' he says with a roguish wink.\n'But I can say this...', He extends his hand outward.\nAfter a burst of light, his outstretched hand is\nfilled with a large greatsword held weightlessly parallel to the ground.\n'The Datuura Society isn't in the business of exuming the Nemmerlean race\nfor want of legendary orators'")
                        EventChoice1.configure(text="A: 'Agreed.' [FIGHT]", command=lambda:[ArcOutcome("B-3A-A")])
                        EventChoice2.configure(text="B: 'WAIT!' [TALK]", command=lambda:[ArcOutcome("B-3A-B")])
                        EventChoice3.configure(text="C: 'I don't have time for this.'\n[LEAVE]", command=lambda:[ArcOutcome("B-3A-C")])

                    if x == "B-A-A":
                        EventDialog.configure(text="To the best of your knowledge, you tell Targus\na comfortable measure of the truth.\n'Hmm...So the Convergence is upon us.\nYou'll see others like me now, if you haven't already.\nSome will be compelled to kill you,\nothers will wish to test you.\nSome may even be compelled to follow you. Even my knowledge of the details is limited.'")
                        EventChoice1.configure(text="A: So which one are you?", command=lambda:[ArcOutcome("B-3A")])
                        EventChoice2.configure(text="B: What is 'the Convergence'?", command=lambda:[ArcOutcome("A-B")])
                        EventChoice3.configure(text="C: Pocket the potion.", command=lambda:[ArcOutcome("A-C")])


                    if x == "ARC_END":
                        EventLabelFrame.place_forget()
                        



                    if x == "NotReadyEND":
                        EventDialog.configure(text="Targus turns and walks away...")
                        EventChoice1.configure(text="END", command=lambda:[ArcOutcome("ARC_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()



                    if x == "NotReady2":
                        EventDialog.configure(text="'Look for me at Vasan-Ruke', Targus says.\nBy a touch of strange magic, he has already created\na parting distance from you.\n'If my time allows, I shall properly test your strength there!'")

                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("NotReadyEND")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "NotReady":
                        EventDialog.configure(text="Targus nods, his mood and expression pensive.\n'You aren't ready yet. Strong, but not ready.'")
                        
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("NotReady2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "LIE_FAIL2":
                        EventDialog.configure(text="'Just answer me this one thing. Do so honestly\nand I'll leave you be...\nAre you truly the one worthy to lead Them?")
                        EventChoice1.configure(text="Yes [Persuasion]", command=lambda:[ArcOutcome("B-3A")])
                        EventChoice2.configure(text="No", command=lambda:[ArcOutcome("NotReady")])
                        EventChoice3.configure(text="Who is...'Them'?", command=lambda:[ArcOutcome("NotReady")])


                    if x == "LIE_FAIL":
                        EventDialog.configure(text="Targus sees through your attempted lie.\nInstead of anger, he seems...amused.\n'Yeah, you're right,' he admits.\nI wouldn't trust me either if I were in your shoes...'")

                        EventChoice1.configure(text="A: So which one are you?", command=lambda:[ArcOutcome("LIE_FAIL2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "LIE":
                        EventDialog.configure(text="You consider withholding the truth from Targus.\nHow does it fare?\nDECEPTION 12")

                        EventChoice1.configure(text="PASS", command=lambda:[ArcOutcome("LIE_PASS")])
                        EventChoice2.configure(text="FAIL", command=lambda:[ArcOutcome("LIE_FAIL")])#
                        EventChoice3.configure(text="Tell him the truth", command=lambda:[ArcOutcome("B-A-A")])

                    if x == "LIE_PASS2":
                        EventDialog.configure(text="'But I'm curious to see if you've got\na chance at getting to the\ntruth beneath it all....'")#

                    if x == "LIE_PASS":
                        EventDialog.configure(text="'Hmm...'\nTargus is silent for a while, but soon he speaks:\n'I suppose there's a lot we still don't know.'")

                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("LIE_PASS2")])#
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "B-A":
                        EventDialog.configure(text="'You drank your vial and survived.\nPretty sure you're the one the Society's been waiting for.\nSo...tell me.\nWhat happened after you drank the Nemmerlean elixir?'")
                        
                        EventChoice1.configure(text="A: Tell him the truth", command=lambda:[ArcOutcome("B-A-A")])
                        EventChoice2.configure(text="B: Lie [CHA (Deception)] ", command=lambda:[ArcOutcome("LIE")])
                        EventChoice3.configure(text="C: Answer with a question.", command=lambda:[ArcOutcome("B-A-C")])


                    if x == "FULLCLONE9":
                        EventDialog.configure(text="'I once called it 'STARSHOT'. My gift to you.\nIt's a Spell Surge Weapon. A Nemmerlean one as well.'\nHe extends the lance to you.\n'About that dance...'")
                        EventChoice1.configure(text="I thought you'd never ask...[FIGHT]", command=lambda:[ArcOutcome("B-3A-A")])
                        EventChoice2.configure(text="Not interested [DECLINE]", command=lambda:[ArcOutcome("NotReady")])
                        EventChoice3.pack_forget()
                        
                        

                    if x == "FULLCLONE8":
                        EventDialog.configure(text="'Thanks for listening', Targus concludes, with disarming humility.\n'You know...I want you to have this', he adds.\nHe concentrates, extending his arm to his side\nA moment later, in a flash of light, a shimmering lance fills his hand.")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE9")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "FULLCLONE7":
                        EventDialog.configure(text="'As for the vials...\nThe Nemmerlean Water of the Universe...\nThe Ancient Nemmerleans believed that by approximately now,\nthe dawning of the Dragon Emmissary Milennium,\nthat the Nemmerlean race will emerge from its slumber.\nNo one knows what that means.\nJust that the Water of the Universe has a lot to do with it...\nAnd that's all I know.'")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE8")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "FULLCLONE6":
                        EventDialog.configure(text="'I'm almost done,'\nTargus insists.\n\n[The conversation has become a SHORT REST\nYou may expend Hit Dice to recover]")
                        EventChoice4.pack()
                        EventChoice1.configure(text="Continue. No rush.", command=lambda:[ArcOutcome("FULLCLONE7")])#
                        EventChoice2.configure(text="Wrap it up, already!", command=lambda:[ArcOutcome("CLONEQUICK")])
                        EventChoice3.configure(text="Let's just FIGHT already.", command=lambda:[ArcOutcome("FULLCLONE3")])#fight.
                        EventChoice4.configure(text="You know what? I'm done!", command=lambda:[ArcOutcome("C")])
                        



                    if x == "FULLCLONE5":
                        #Valykarja -- Jedi, SOLDIER, SeeD...esteemed super-powered warrior class. Said to be the wielders of the original Spell Surge weapons..
                        EventDialog.configure(text="'The Nemmerlean bloodline is thin, but not extinct', Targus says.\n'Even within you, it might be as little as a single drop's worth\nfloating in your veins. But it was strong enough for the\nSociety and their advanced Necromancy to extrapolate all they needed from you,\nand thus...US', he says, gesturing toward himself.")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE6")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "FULLCLONE4":
                        EventDialog.configure(text="Targus nods approvingly before continuing:\n'If the Datuura Society can restore magic NATIVE to humans,\nthat would be a tremendous step in them\ncurrying favor with MULTIPLE parties of interest:\nThe Cult of Ulm, Tolmician Partisans...even the king of Rodolis would think twice about\npassing up the prospect of reviving their legendary Valykarja...'")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE5")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "CLONEQUICK":
                        EventDialog.configure(text="'Hmm...How do I put this succinctly?\n*You are a specimen of the ancient Nemmerlean race\na breed of humans naturally gifted with magic.\n*The Datuura Society created duplicates\nof you to expand their political reach.\n*The vials are meant to awaken something\nwithin us in coincidence with the Dragonborn Millenium.\n\nI take it you're ready to fight now?'") 
                        EventChoice1.configure(text="I thought you'd never ask...[FIGHT]", command=lambda:[ArcOutcome("B-3A-A")])
                        EventChoice2.configure(text="Not interested [DECLINE]", command=lambda:[ArcOutcome("NotReady")])
                        EventChoice3.pack_forget()


                    if x == "FULLCLONE3":
                        EventDialog.configure(text="Targus asks:\n'Bored yet?'")
                        EventChoice4.pack()
                        EventChoice1.configure(text="Nope. Go on.", command=lambda:[ArcOutcome("FULLCLONE4")])#
                        EventChoice2.configure(text="Changed my mind.\nGimme the quick version", command=lambda:[ArcOutcome("CLONEQUICK")])#
                        EventChoice3.configure(text="Let's just FIGHT already.", command=lambda:[ArcOutcome("B-3A-A")])
                        EventChoice4.configure(text="You know what? I'm done!", command=lambda:[ArcOutcome("C")])
                        

                    if x == "FULLCLONE2":
                        EventDialog.configure(text="Targus begins:\n'The Datuura Society has reason to believe that you are a Nemmerlean.\n'What's that?!', you ask? A tribe of humans from a LONG time ago\nwho innately had the gift of magic: No blessings or curses from entities,\nnot a drop of dragon or elf blood in their veins,\nnot even a school to teach them...\njust regular humans in the wild; gifted with magic.'")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE3")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "FULLCLONE":
                        EventDialog.configure(text="Targus is pleased.\n'Did I just make a new drinking buddy?!\nOh...clones. Right!'")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("FULLCLONE2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "CLONES3":
                        EventDialog.configure(text="'Before I answer your question,\nI must ask; do we, as men cut from the same\nliteral and proverbial cloth share such a trait?'")
                        EventChoice1.configure(text="Yes [Give me the FULL answer]", command=lambda:[ArcOutcome("FULLCLONE")])
                        EventChoice2.configure(text="No [Give me the SHORT answer].", command=lambda:[ArcOutcome("CLONEQUICK")])
                        EventChoice3.configure(text="Quit stalling! [FIGHT] ", command=lambda:[ArcOutcome("LIE")])#Go to fight
                        EventChoice4.configure(text="I regret everything [DISMISS].", command=lambda:[ArcOutcome("C")])


                    if x == "CLONES2":
                        EventDialog.configure(text="'I, myself, am a thorough man, Mister Somnus:\nThorough in battle, thorough in bed,\nand thorough in boring explanations...'")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("CLONES3")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "CLONES":
                        EventDialog.configure(text="Targus chuckles.\n'I thought you'd ask a harder question!'")
                        
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("CLONES2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "TARGUSBARGAIN":
                        EventDialog.configure(text="'I can tell you what I know\nabout the Datuura Society,\nand their plans for...us...\nBut! It'll cost you: A dance.'")
                        EventChoice1.configure(text="[Ask why you are the template\nfor the clones]", command=lambda:[ArcOutcome("CLONES")])
                        EventChoice2.configure(text="[Ask about the Datuura Society] ", command=lambda:[ArcOutcome("LIE")])
                        EventChoice3.configure(text="[Ask about the dreams/visions]")
                        EventChoice4.configure(text="['I don't have time for this!']")
                        EventChoice4.pack()




                    if x == "B-C":
                        EventDialog.configure(text="Targus smiles.\n'Nothing is free. Not even for Aricin Somnus.'\nBefore you can respond, he raises a finger.")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("TARGUSBARGAIN")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "B":
                        EventDialog.configure(text="'So you know the game,' he says.\n'That makes you a little smarter than the others.'\nHe eyes you for a moment, sizing you up.\n'My name is Targus. And you...are Aricin Somnus'")
                        EventChoice1.configure(text="A: What else do you know about me?", command=lambda:[ArcOutcome("B-A")])
                        EventChoice2.configure(text="B: You don't know anything about me!\n[ATTACK!]", command=lambda:[ArcOutcome("B-B")])
                        EventChoice3.configure(text="C: Targus...I need answers!", command=lambda:[ArcOutcome("B-C")])

                    if x == "C":
                        EventDialog.configure(text="'My time is too brief for petulant children.\nPerhaps you are not yet ready...'\nWith the snap of his fingers, the man vanishes... ")
                        EventChoice1.configure(text=">", command=lambda:[ArcOutcome("ARC_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == 0:

                        pygame.mixer.music.load(resource_path(("TargTheme.mp3"))), pygame.mixer.music.play(-1)
                        EventLabel.config(image=self.TargTlk)

                        EventDialog.configure(text="'I knew it. I knew I'd find you before my time\nwould come to an end'") 
                        
                        EventChoice1.configure(text="A: I'll end 'your time' all right!\n[FIGHT] ", command=lambda:[ArcOutcome("A")])
                        EventChoice2.configure(text="B: Another clone, I take it?", command=lambda:[ArcOutcome("B")])
                        EventChoice3.configure(text="C: ...Whatever.", command=lambda:[ArcOutcome("C")])




                EventLabelFrame.place(x=x, y=y)
                
                EventDialog.configure(text="You hear a voice from above, in essence, yours,\n though haggard and shaped with an accent all its own.") 
                EventChoice1.configure(text=">", command=lambda:[ArcOutcome(0)])
                EventChoice2.pack_forget()
                EventChoice3.pack_forget()
                EventChoice4 = Button(EventLabelFrame)


            if got == "Himbo":

                def HimboOutcome(x):
                 
                    EventChoice1.pack(fill=X)
                    EventChoice2.pack(fill=X)
                    EventChoice3.pack(fill=X)
                    EventChoice4.pack_forget()

                    if x == "AMHuman":
                        EventDialog.configure(text="Little Mister Please and Thank You emits something of a laugh.\nIt is unpleasant.\nLike the aural assault of nails screeching against a chalkboard\nand the supernaturally tactile sense of\nsuch friction pressing against your very soul.")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("Look1-3")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "Look1-4":
                        EventDialog.configure(text="'Good', the creature says, seemingly directly to your mind.\n'Bahimbo IS human,' he says with a mocking jeer.")

                        EventChoice1.configure(text="Agree. Bahimbo IS human", command=lambda:[HimboOutcome("AMHuman")])
                        EventChoice2.configure(text="Ask what he wants.", command=lambda:[HimboOutcome("WDYW")])
                        EventChoice3.configure(text="Attack him! [FIGHT]", command=lambda:[HimboOutcome("BAHFIGHT")])

                    if x == "Look1-3":
                        EventDialog.configure(text="You recognize this form as a potentially eldritch being:\n\n'Little Mister Please-And-Thankyou'")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("Look1-3")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "Look1-2":
                        EventDialog.configure(text="A tiny, mono-eyed creature looks up at you.\nIts iris, the size of a peach stone,\nappears to almost vibrate within the sea of a violent dark\nred sclera that seems to shape the tiny creature's head.\nIts tube-like shadow-dark body glistens\nlike wormflesh where touched by the light.") 
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("Look1-3")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "Look1":
                        EventDialog.configure(text="You turn around.\nAnd adjust your line of sight downward.")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("Look1-2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()
                        
                    
                    if x == "Look2-2":
                        EventDialog.configure(text="'Well GOOOOOOOD GRIEF!',\nthe dwarven man says with a chuckle.\n'Ya sure made that harder'n pullin'\na sore orc tusk, now didn't ya!?'")
                        
                        #turns out to be Nathaniel Twinney! Calm, soothing music!

                    if x == "Run":
                        EventDialog.configure(text="You consider fleeing, but your\nbody refuses to obey you...")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("DNLook2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()



                    if x == "DNLook2":
                        talk = ["BUT THOU MUST"]*2 + ["PLEEEEEEASSSSEEEEE"]*2 + ["DO AS I COMMAND"]*2 + ["...please...and...thank you..."]
                        LMPT = random.choice(talk)

                        EventDialog.configure(text=LMPT+", BeRhInIkE!!!")

                        if LMPT == talk[6]:
                            EventChoice1.configure(text="[Face him]", command=lambda:[HimboOutcome("Look2")])
                            EventChoice2.configure(text="[Face him]", command=lambda:[HimboOutcome("Look2")])
                            EventChoice3.configure(text="[Face him]", command=lambda:[HimboOutcome("Look2")])

                        else:
                            EventChoice1.configure(text="[Face him]", command=lambda:[HimboOutcome("Look2")])
                            EventChoice2.configure(text="[Refuse]", command=lambda:[HimboOutcome("DNLook2")])
                            EventChoice3.configure(text="[Run]", command=lambda:[HimboOutcome("Run")])



                    if x == "Look2":
                        EventDialog.configure(text="You turn your body to align yourself\nwith the direction of the sound's\napparent origin...")

                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("Look2-2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "DNLook1-2":
                        EventDialog.configure(text="BeRhInIkE!!!")

                        EventChoice1.configure(text="[Face the voice]", command=lambda:[HimboOutcome("Look2")])
                        EventChoice2.configure(text="[Do NOT Face the voice]", command=lambda:[HimboOutcome("DNLook2")])
                        EventChoice3.pack_forget()

                    if x == "DNLook1-1":
                        EventDialog.configure(text="'It's all right', he insists.\n'You can turn and face me...'")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("DNLook1-2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "DNLook1":
                        EventDialog.configure(text="'Never thought I'd run into you here!'\nA recently familiar voice says from behind you.\nIt sounds like the dwarven gentleman\nyou befriended at the bar known as Seamus's.")
                        EventChoice1.configure(text=">", command=lambda:[HimboOutcome("DNLook1-1")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                EventLabelFrame.place(x=x, y=y)
                
                EventDialog.configure(text="You are alone. But soon the tranquility\nof the moment is disrupted as you\nsense from behind you are being watched...") 
                EventChoice1.configure(text="[Look Behind You]", command=lambda:[HimboOutcome("Look1")])
                EventChoice2.configure(text="[Do NOT Look Behind You]", command=lambda:[HimboOutcome("DNLook1")])
                EventChoice3.pack_forget()
                EventChoice4 = Button(EventLabelFrame)
                

            if got == "Harl":
                def HarlOutcome(x):
                    EventChoice4.pack_forget()
                    EventChoice1.pack(fill=X)
                    EventChoice2.pack(fill=X)
                    EventChoice3.pack(fill=X)
                    #EventLabel.pack_forget()

                    if x == "Item1Accept":
                        EventDialog.configure(text="'An excellent choice!' Simon beams.\n'I hope those potions serve you well!'\nSimon packs away the remaining items.\n'We'd best be off then. Be safe, Harlow. May the Light of Ulm protect you!'")
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("A-B2_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "Item2Accept":
                        EventDialog.configure(text="'Knowledge is power, afterall,' Simon says.\n'Those notes [Item Code:MMSPE] should help with the trickier crevices of the manse.'\nSimon packs away the remaining items.\n'We'd best be off then. Be safe, Harlow. May the Light of Ulm protect you!'")
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("A-B2_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "Item3Accept":
                        EventDialog.configure(text="'So you went with the scroll afterall...' Simon nods with approval.\n'If you ever find yourself in Oerstrum, ask for Euzo.\nTell him I sent you. He might make another one of those for you if he likes you!'\nSimon packs away the remaining items.\n'We'd best be off then. Be safe, Harlow. May the Light of Ulm protect you!'")
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("A-B2_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "ItemALLPASS2":
                        EventLabel.config(image=self.SiTlk)
                        EventDialog.configure(text="....")
                        EventChoice1.configure(text=">", command=lambda:[EventChoice1.configure(command=lambda:[PMarker.place_forget(), EventLabelFrame.place_forget()]), EventDialog.configure(text="Absolutely flabbergasted, Simon simply walks away.\nYou can hear general mutterings in his wake,\nmostly variations of 'How?' and 'That's impossible...right?!?'\nuntil he is no longer within your sight.")])

                    if x == "ItemALLPASS":
                        EventLabel.config(image="", text="Acquired:")
                        EventDialog.configure(text="*Reconaissance Log [Item Code: MMSPE]\n*Spell Surge Scroll\n*Potion of Fire Breathing\n*Potion of Gaseous Form*\nPotion of Greater Healing\n*Healing Potion x3")
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("ItemALLPASS2")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    

                    if x == "ItemALL":
                        EventDialog.configure(text="Are you sure you want to do that?\nHe's staring RIGHT at you...\n[Dexterity(Sleight of Hand) DC:15]\n[DISADVANTAGE]")
                        EventChoice1.configure(text="I'm TOO lucky! [Pass]", command=lambda:[HarlOutcome("ItemALLPASS")])
                        EventChoice2.configure(text="It was at this moment\nHarlow knew... [Fail]", command=lambda:HarlOutcome("ItemALLFAIL"))
                        EventChoice3.configure(text="Just kidding!", command=lambda:HarlOutcome("A-B2-B-B2"))

                    if x == "Item3":
                        EventDialog.configure(text="Magic Scroll:\n Temporarily turns a non-magical weapon\ninto a Spell Surge weapon.\nLasts for only 24-hours though.")
                        EventChoice1.configure(text="Hmm...Alright!", command=lambda:[HarlOutcome("Item3Accept")])
                        EventChoice2.configure(text="Nah. What's next?", command=lambda:HarlOutcome("A-B2-B-B2"))
                        EventChoice3.configure(text="", command=lambda:"")

                    if x == "Item2":
                        EventDialog.configure(text="Reconnaissance Log:\n Contains information and tips\nfor navigating the Avernissi Villa.")
                        EventChoice1.configure(text="I'll take it!", command=lambda:[HarlOutcome("Item2Accept")])
                        EventChoice2.configure(text="What else ya got?", command=lambda:HarlOutcome("A-B2-B-B2"))
                        EventChoice3.configure(text="", command=lambda:"")



                    if x == "Item1":
                        EventDialog.configure(text="Potion Set:\n*Potion of Fire Breathing\n*Potion of Gaseous Form*\nPotion of Greater Healing\n*Healing Potion x3\n\nIs this your selection?")
                        EventChoice1.configure(text="Sure", command=lambda:[HarlOutcome("Item1Accept")])
                        EventChoice2.configure(text="No", command=lambda:HarlOutcome("A-B2-B-B2"))
                        EventChoice3.configure(text="", command=lambda:"")

                    if x == "A-B2-B-B2":
                        EventDialog.configure(text="'Pick one!'")
                        EventChoice1.configure(text="Potion Set (6)", command=lambda:[HarlOutcome("Item1")])
                        EventChoice2.configure(text="Reconnaissance Log", command=lambda:HarlOutcome("Item2"))
                        EventChoice3.configure(text="Magic Scroll", command=lambda:HarlOutcome("Item3"))
                        EventChoice4.configure(text="Take them all!", command=lambda:[HarlOutcome("ItemALL")])

                        EventChoice4.pack()


                    if x == "A-B2-B-B":
                        EventDialog.configure(text="'Excellent! 'Divide and conquer' it is then!'\nSimon begins to rummage through\nthe pockets of his garb.'We don't have much time,\nbut I don't want to\nleave you empty-handed!'\nHe lays out a set of three different items, placing them on the ground before you.")
                        EventChoice3.configure(text=">", command=lambda:[HarlOutcome("A-B2-B-B2")])
                        EventChoice1.configure(text="", command=lambda:"")
                        EventChoice2.configure(text="", command=lambda:"")

                    if x == "A-B2-B-A2":
                        EventDialog.configure(text="'Oh, and you're welcome by the way,' Simon adds,\ncasually pointing out two\nunconscious guards along his path.\n'If I were a thieving man, I'd take\nprofitable advantage of such careless slumber...\nBut since I'M not...'\nSimon whistles to himself as he distances away from your sight.\n[Loot x2]")
                        EventChoice3.configure(text=">", command=lambda:[PMarker.place_forget(), EventLabelFrame.place_forget()])

                    if x == "A-B2-B-A":
                        EventDialog.configure(text="Simon laughs, shaking his head in amusement as\nhe resumes his departure.\n'I should have known better.\nI'll go my way and you go yours. Perhaps we'll meet\nagain in the middle as usual?'")
                        EventChoice3.configure(text=">", command=lambda:[HarlOutcome("A-B2-B-A2")])
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        

                    if x == "A-B2-B":
                        EventDialog.configure(text="Simon stops in his tracks before turning to face you\n'Actually...You're right; it IS better to blindside our\nfoe as two separate blades striking both\nhigh and low simultaneously rather than\na single blow all at once! Brilliant!'")

                        EventChoice1.configure(text="A: 'Uh...WHAT?!?!'", command=lambda:[HarlOutcome("A-B2-B-A")])
                        EventChoice2.configure(text="B: 'Y-yeah! Exactly!'", command=lambda:[HarlOutcome("A-B2-B-B")])
                        EventChoice3.configure(text="C: 'I was just trying to tell you\nyour shoes are untied. Dork.'", command=lambda:[HarlOutcome("A-B-C_END")])

                    if x == "A-B-C_END":
                        EventDialog.configure(text="'Yeah, yeah...', Simon intones, waving dismissimively.\nEven his pace concedes defeat as\nhe puts more effort into making\ndistance until he can no longer be seen.\n'Oh, and you might want to watch out for those\nguards behind you! I softened them up for you,\nbut it appears their break time is over!'\n[ROLL INITIATIVE! Guards x2, 50%HP each]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[PMarker.place_forget(), EventLabelFrame.place_forget()])
                        playermarker2(main)
                        playermarker2(main)

                    if x == "A-B2_END":
                        EventDialog.configure(text="'You know where to find me if need be,'\nSimon utters as he soon recedes from view.")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[PMarker.place_forget(), EventLabelFrame.place_forget()])
                        

                    if x == "A-B2":
                        EventDialog.configure(text="Simon dismisses himself with a\nformal benedictive gesture.\nHe turns and begins to make a\ndisplay of walking away, albeit slowly...")
                        
                        EventChoice1.configure(text="A: Let him", command=lambda:[HarlOutcome("A-B2_END")])
                        EventChoice2.configure(text="B: 'Wait!'", command=lambda:[HarlOutcome("A-B2-B")])
                        EventChoice3.configure(text="C: Throw insults\nbehind his back.", command=lambda:[HarlOutcome("A-B-C_END")])

                    if x == "A-B":
                        EventDialog.configure(text="'Right...well...'\nSimon sheepishly returns his hand to his side\n'If you've any intentions toward investigating\nthe Avernissi Villa up ahead, there's a strong liklihood\nwe may have a chance to revisit this matter should\nit be written for our Lights to meet again.")
                        
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("A-B2")])
                        EventChoice2.configure(text="", command=lambda:[""])
                        EventChoice3.configure(text="", command=lambda:[""])

                    if x == "A-A_END":
                        EventDialog.configure(text="[Simon has joined the Party!]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])


                    if x == "A-A":
                        EventDialog.configure(text="Simon beams with excitement.\n'Excellent! I'm certain whatever lies ahead\nwill be of little match for the two of us working in tandem.\nJust say the word and your injuries are as good as healed,\nand your fatigue will be as forgotten\nas the Dwarven Halls of Gwandatholir!'")
                        EventChoice1.configure(text=">", command=lambda:[HarlOutcome("A-A_END")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "FIGHTSIMON":
                        pass

                    if x == "ULMCHAT":
                        pass

                    if x == "SIMONCHAT":
                        EventDialog.configure(text="'Oh, uh...I'm not THAT kind of cleric,' Simon insists.\n")

                        EventChoice1.configure(text="")
                        EventChoice2.configure(text="")
                        EventChoice3.configure(text="")


                    if x == "RUDE":
                        EventDialog.configure(text="'Well now that we've got that out of the way...'")

                        EventChoice1.configure(text="[Ask him what he's doing here]", command=lambda:[HarlOutcome("RUDE")])
                        EventChoice2.configure(text="[Ask him about Ulm]\n(Religion Check)", command=lambda:[HarlOutcome("ULMCHAT")])
                        EventChoice3.configure(text="You're welcome.", command=lambda:[HarlOutcome("RUDE")])



                    if x == "INSULTSIMON":
                        EventDialog.configure(text="'I happen to be quite alright with it, thank you very much!'")

                        EventChoice1.configure(text="I'm kidding. Calm down, nerd.", command=lambda:[HarlOutcome("RUDE")])
                        EventChoice2.configure(text="Yeah yeah, whatever.", command=lambda:[HarlOutcome("RUDE")])
                        EventChoice3.configure(text="You're welcome.", command=lambda:[HarlOutcome("RUDE")])

                

                    if x == "B":
                    
                        EventLabel.config(image=self.SiTlk)
                        TLabel.config(image=self.Simn)

                        EventDialog.configure(text="'Ah, of course! We haven't properly met yet!\nMy name is Simon. Simon Antonius.\nI am a cleric of the TRUE form of Ulm, and--'") 


                        EventChoice1.configure(text="You're one of those Ulm bastards?!?\n[ATTACK]", command=lambda:[HarlOutcome("FIGHTSIMON")])
                        EventChoice2.configure(text="You're one of those Ulm bastards?!?\nAnswer me!", command=lambda:[HarlOutcome("ULMCHAT")])
                        EventChoice3.configure(text="Picked an odd place to proselytize, buddy.", command=lambda:[HarlOutcome("SIMONCHAT")])

                        EventChoice4.pack(fill=X)
                        EventChoice4.configure(text="'Simon', huh? Sounds like a nerd name to me.", command=lambda:[HarlOutcome("INSULTSIMON")])




                    if x == "A":
                        SimonReasons = ["perhaps we can put our differences aside for something greater?"] + ["perhaps it would be a good idea for us to finally work together?"] +["perhaps I can prove to you once again that we are in fact a good team?"]
                        
                        EventLabel.config(image=self.SiTlk)
                        TLabel.config(image=self.Simn)
                        EventDialog.configure(text="'I-I assure you, Harlow, our encounters haven't been deliberate!\nBelieve it or not, I'm just as perplexed by the odds\nof us running into one another so frequently as you are!\nBut since we're here....\n"+random.choice(SimonReasons)+"\nSimon extends his hand in a gesture of comraderie.\nHe patiently awaits your response.")
                        
                        EventChoice1.configure(text="A: Shake his hand.", command=lambda:[HarlOutcome("A-A")])
                        EventChoice2.configure(text="B: Decline his offer", command=lambda:[HarlOutcome("A-B")])
                        EventChoice3.configure(text="C: [Indifferent Stare]", command=lambda:[HarlOutcome("A-C")])

                        





                EventLabelFrame.place(x=x, y=y)

                pygame.mixer.music.load(resource_path(("SimonTheme.mp3"))), pygame.mixer.music.play(-1)
                
                EventDialog.configure(text="As you go deeper into the orchard grove, your path is crossed\nby a kind-faced youth in religious garb. He smiles\nwarmly before speaking to you, saying\n'Once again, it seems the will of Ulm has united us,\nmy good sir...or shall I say, 'lady'?")
                EventChoice1.configure(text="A: For the last time,Simon, LEAVE ME ALONE!!.", command=lambda:[HarlOutcome("A")])
                EventChoice2.configure(text="B: Who...are you?\n(I've never seen you before in my life!)", command=lambda:[HarlOutcome("B")])
                EventChoice3.configure(text="C: So it seems, old friend...", command=lambda:[HarlOutcome("C")])
                EventChoice4 = Button(EventLabelFrame)


            if got == "Olgz":
                def OlgOutcome(x):
                    EventChoice1.pack(fill=X)
                    EventChoice2.pack(fill=X)
                    EventChoice3.pack(fill=X)
                    EventChoice4.pack_forget()

                    if x == "A":
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                        EventDialog.config(text="You draw your weapon and rush the would-be assailant\nwho is despite being seemingly prepared,\nis decidedly NOT ready for your onslaught.\n\nCOMBAT\nFirst Initiative: Olga\nTheodore Status: LVL3 Exhaustion\n*HP: 50% *Move: 50% *DisAdv Checks, Saves, and Attacks")
                        EventChoice1.config(text=">", command=lambda:EventLabelFrame.place_forget())



                    if x == "LEAVE":
                        EventLabel.config(image="")
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()
                        EventDialog.config(text="You've decided you've wasted enough time here.\nYour comrades are likely still in need of you.\nYou briefly consider coming back to check\non the boy after the situation at hand is dealt with...\nEND")
                        EventChoice1.config(text=">", command=lambda:EventLabelFrame.place_forget())

                    if x == "TUCKHIMIN":
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()
                        EventDialog.config(text="You spend a careful moment looking for a secure spot\nto conceal the boy while he rests. Unless luck is\ndecidedly against him, he is set to sleep soundly and safely.\nYou even take an extra moment to provide him a small amount of food and water.\nAs you set off to leave, you can't help but notice\nthe cherubic manner in which the child sleeps.")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("LEAVE"))


                    if x == "MEDLOW":
                        EventDialog.config(text="The boy is fine.\nHe passed out from exhaustion.")
                        EventChoice1.config(text="[You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        EventChoice2.config(text="[Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="[Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        
                        



                    if x == "MEDMID":
                        EventDialog.config(text="The boy is exhausted.\nHe is also running a low fever.")
                        EventChoice1.config(text="[You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        EventChoice2.config(text="[Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="[Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        


                    if x == "MEDHIGH":
                        EventDialog.config(text="The boy is deeply exhausted.\nHe also seems to be running a low-grade fever.\nHe will require at least a few\ndays of uninterrupted rest.")
                        EventChoice1.config(text="[You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        EventChoice2.config(text="[Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="[Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        



                    if x == "Trip-B":
                        EventDialog.config(text="You examine the unconscious boy\n[WIS (Medicine)]")
                        EventChoice1.config(text="1-10", command=lambda:OlgOutcome("MEDLOW"))
                        EventChoice2.config(text="11-16", command=lambda:OlgOutcome("MEDMID"))
                        EventChoice3.config(text="17+", command=lambda:OlgOutcome("MEDHIGH"))



                    if x == "Trip-A":
                        EventDialog.config(text="You call out to him,\nbut to no avail...")
                        EventChoice1.config(text="A: [Examine if he's ok]\n[Wis(Medicine)]", command=lambda:OlgOutcome("Trip-B"))#
                        EventChoice2.config(text="B: [Leave him]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="C: [STEAL!]\n[DEX(Sleight of Hand) Check]", command=lambda:OlgOutcome("STEAL"))



                    if x == "Trip":
                        EventChoice4.pack()
                        EventDialog.config(text="The drow boy is facedown and doesn't seem to be moving.\nWhat do you do?")

                        EventChoice1.config(text="A: [Call out to him]", command=lambda:OlgOutcome("Trip-A"))
                        EventChoice2.config(text="B: [Examine if he's ok]\n[Wis(Medicine)]", command=lambda:OlgOutcome("Trip-B"))#
                        EventChoice3.config(text="C: [Leave him]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice4.config(text="D: [STEAL!]\n[DEX(Sleight of Hand) Check]", command=lambda:OlgOutcome("STEAL"))


                    if x == "B-A-B-B":
                        EventDialog.config(text="'I do, dammit!' he angrily insists.\nThe boy then repeats his intricate dagger flourishes,\nleading into a well-choreographed set of movements and strikes at a set\nof imaginary opponents. His footing gradually worsens\nas he struggles to fight exertion and exhaustion. The dance ends\nabruptly when he trips and faceplants into the ground.")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("Trip"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "B-A-B-C-C":
                        EventDialog.config(text="You decide that this is perhaps not your problem to solve...\nYou are reminded of the others who are counting\non you at this very moment.\nAs you leave the orchard, and the drow boy,\nyou briefly wonder how many other stories of tragedy lie ahead,\nand if it is even possible for you to prevent any more of them.")
                        EventChoice1.config(text=">", command=lambda:EventLabelFrame.place_forget())
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "BOY":
                        EventLabel.config(image="")
                        EventDialog.config(text="The Boy is extremely exhausted, suffering from LEVEL 3 EXHAUSTION\nFor more info, use Parser Code: 'ALKJA'")
                        EventChoice1.config(text=">", command=lambda:EventLabelFrame.place_forget())
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "SLAP-A-A3-NO-YES":
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                        EventDialog.config(text="...'I'll...save you, Liehn...This time...I'll do it...',\nthe boy vows aloud to the whispers of dreams.\nHis hot tears wet the back of your neck\nas you carry him with you outside of the orchard")
                        EventChoice1.config(text="[About the boy]", command=lambda:OlgOutcome("BOY"))




                    if x == "SLAP-A-A3-NO":
                        #EventChoice3.pack(fill=X)
                        EventDialog.config(text="You begin to explain the myriad reasons\n it is unsound to add a child to your ranks.\nYour words fall on deaf ears as the boy remains bowed to the ground.\nIt is then that you realize he finally succumbed to much-needed\nrest several moments ago.")

                        EventChoice1.config(text="'Fine, you changed my mind, kid...'[Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        EventChoice2.config(text="[Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="[Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        


                    if x == "SLAP-A-A3":  #Theodore begs you, throwing himself prostrate.  You have choices...they all end with the realization that he's finally out cold...
                        EventDialog.config(text="Help the boy get his revenge?\n[Enlist him as a Companion to the party]")
                        #EventChoice2.pack(fill=X)
                        EventChoice1.config(text="[Yes]", command=lambda:OlgOutcome("SLAP-A-A3-YES"))#
                        EventChoice2.config(text="[No]", command=lambda:OlgOutcome("SLAP-A-A3-NO"))



                    if x == "SLAP-A-A2":
                        EventDialog.config(text="'But what if YOU joined me?!'\nHis tired eyes brim with a pleading\nhope that briefly transcends his exhaustion\n'Will you help me get revenge...against Avernissi?\nI'm...I'm begging you!'")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("SLAP-A-A3"))

                    if x == "SLAP-A-A":
                        EventChoice2.pack_forget()
                        EventDialog.config(text="'I did...what I had to do...to survive...'\nhe repeats low and to himself....")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("SLAP-A-A2"))

                        




                    if x == "SLAP-A":
                        EventChoice3.pack_forget()
                        EventDialog.config(text="'I DID WHAT I HAD TO DO TO SURVIVE!'\nhe angrily retorts")

                        EventChoice1.config(text="A: 'Congratulations, kid! You found my point!'", command=lambda:OlgOutcome("Slap-A-A"))
                        EventChoice2.config(text="B: 'Yes...like a coward.'", command=lambda:OlgOutcome("Slap-A-B"))#

                    if x == "SLAP-B":
                        EventDialog.config(text="You explain to him how foolhardy and\nunrealistic his expectations of the situation must have been.\nAfter a while, he seems to calm and realize\nhe only would have gotten himself killed as well\nhad he done things much differently.")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("SLAP-A-A"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "SLEEPY":
                        EventDialog.config(text="He is practically asleep where he stands.\nHis words silence and are quickly\nreplaced with the rhythm of gentle snoring.")
                        EventChoice1.config(text="A: [You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        EventChoice2.config(text="B: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice3.config(text="C: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        

                    if x == "SLAP-C-NAP":
                        EventDialog.config(text="'I'll sleep when I'm damn near ready,\nyou knife-eared...stuck up...\n*yawwn*\n...day-skinned....'")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("SLEEPY"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    
                    if x == "TURNAROUND":
                        EventDialog.config(text="'HEY! Look at me when I'm talking,\nto you, you knife-eared\n...stuck up...\n*yawwn*\n...day-skinned....'")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("SLEEPY"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()




                    if x == "SLAP-C-IGNORE":
                        EventDialog.config(text="'Hey! Where do you think you're going!?!'\nAs you make distance, the yells at your\nback continue then abruptly stop...")
                        EventChoice1.config(text="[Keep walking...]", commmand=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="[Turn around...]", commmand=lambda:OlgOutcome())#
                        EventChoice3.pack_forget()

                    if x == "SLAP-C":
                        EventDialog.config(text="'Oh yeah?! The first one's free,\nyou muscle-brained Day-skin! Nobody disrespects me TWICE and gets away with it!'")

                        EventChoice1.config(text="'I'll pay for it this time...\nBut you better have change!\n[FIGHT]", commmand=lambda:OlgOutcome("A"))
                        EventChoice2.config(text="'So cranky...somebody needs a nap!'", commmand=lambda:OlgOutcome("SLAP-C-NAP"))#
                        EventChoice3.config(text="[Ignore him/Walk away]", commmand=lambda:OlgOutcome("SLAP-C-IGNORE"))

         

                    if x == "SLAP":
                        EventDialog.config(text="SLAP!\n'WHAT WAS THAT FOR, YOU BITCH!?!'\nThe boy clutches his cheek, rage quickly\nredefining his tears.")

                        EventChoice1.config(text="A: 'For running away!'", command=lambda:OlgOutcome("SLAP-A"))
                        EventChoice2.config(text="B: 'For being ridiculously hard on yourself!'", command=lambda:OlgOutcome("SLAP-B"))
                        EventChoice3.config(text="C: 'Because I wanted to. Care for another?'", command=lambda:OlgOutcome("SLAP-C"))



                    if x == "B-A-B-C-B2-C":
                        EventDialog.config(text="Berate him for...")

                        EventChoice1.config(text="A: Running away!", command=lambda:OlgOutcome("SLAP-A"))
                        EventChoice2.config(text="B: Being needlessly hard on himself!", command=lambda:OlgOutcome("SLAP-B"))
                        EventChoice3.config(text="C: Slap some sense into him!\n[THEN choose A or B]", command=lambda:OlgOutcome("SLAP"))

                    if x == "DEXFAIL":
                        followup = ["'Put me down and go away!'"] + ["'At least consider somewhere more private...'"] + ["'Wait until I'm a LITTLE older first...'"] + ["'I gotta girlfriend my own age...'"]
                        EventDialog.config(text="'You nasty day-skin creep...', the boy moans.\n"+random.choice(followup))
                        
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.pack_forget()

                    if x == "DEXMID":
                        STEAL = ['A CITY MAP (Oerstrum)'] + ["Thieves Tools"] + ["A tiny golden pendant\n[ITEM CODE:'SPRIP']"] + [str(random.randint(2,10))+" GP"]
                        EventDialog.config(text="The boy mumbles incoherently,\nbut otherwise your attempt goes smoothly.\nFrom his pockets, you acquire\n\n"+random.choice(STEAL))

                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.pack_forget()

                    if x == "DEXHIGH":
                        STEAL = ['A CITY MAP (Oerstrum)'] + ["Thieves Tools"] + [str(random.randint(2,10))+" GP"]
                        EventDialog.config(text="The boy barely notices your touch.\nAlong with "+random.choice(STEAL)+",\na small gold necklace spills from the boy's pockets\nand lands on the ground.\nA tiny golden pendant\n[ITEM CODE:'SPRIP']")
                        
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.pack_forget()




                    if x == "STEAL":
                        EventDialog.config(text="Check the kid for valuables...\n[DEX (Sleight of Hand) Check]")

                        EventChoice1.config(text="1-10", command=lambda:OlgOutcome("DEXFAIL"))
                        EventChoice2.config(text="11-16", command=lambda:OlgOutcome("DEXMID"))
                        EventChoice3.config(text="17+", command=lambda:OlgOutcome("DEXHIGH"))



                    if x == "VENT":
                        EventDialog.config(text="You simply moderate your embrace\nas the boy seems compelled to continue...\n'Those robed bastards...their damn chanting...\nit all happened so fast...'\nIn one last burst of exertion, he hugs you tight,\nas though gleaning your much-needed strength for himself.\nHe then seems to go limp in your hold.")
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.config(text="C: [Check him for valuables]\n[DEX(Sleight of Hand)]", command=lambda:OlgOutcome("STEAL"))
                        
                        

                    if x == "B-A-B-C-B2":
                        #EventChoice2.pack(fill=X)
                        #EventChoice3.pack(fill=X)
                        

                        EventDialog.config(text="'I was useless! I did nothing!\nLiehn needed me to save her...\nand I-I just ran away!'")

                        EventChoice1.config(text="A: [Let him vent]", command=lambda:OlgOutcome("VENT"))#
                        EventChoice2.config(text="B: [Console him]")#
                        EventChoice3.config(text="C: [Berate him]", command=lambda:OlgOutcome("B-A-B-C-B2-C"))


                    if x == "B-A-B-C-B":
                        
                        EventDialog.config(text="You envelop the boy in a firm, but gentle embrace.\nDespite his efforts to remain composed,\nhis sobs erupt further as he melts into your grasp.")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("B-A-B-C-B2"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()


                    if x == "B-A-B-C":

                        pygame.mixer.music.fadeout(1200)
                        pygame.mixer.music.load(resource_path(("Sad1.mp3"))), pygame.mixer.music.play(-1)

                        EventDialog.config(text="'I...couldn't save her...'. The boy falls to his knees.\nHis weapons roll loose from his grip.\nSoon, tears well from his eyes and\ntrench down his dirt-smudged face.")

                        EventChoice1.config(text="A: [Observe him]", command=lambda:OlgOutcome("B-A-B-C-A"))#
                        EventChoice2.config(text="B: [Comfort him]", command=lambda:OlgOutcome("B-A-B-C-B"))
                        EventChoice3.config(text="C: [Walk away...]", command=lambda:OlgOutcome("B-A-B-C-C"))



                    if x == "B-A-B":
                        EventDialog.config(text="'I-I know how to fight, dammit!' the boy insists.\nAn irritated exhaustion drips through his cracked voice.") 

                        EventChoice1.config(text="A: If you insist...[FIGHT]", command=lambda:OlgOutcome("A"))
                        EventChoice2.config(text="B: If you insist...[Playful/teasing]", command=lambda:OlgOutcome("B-A-B-B"))
                        EventChoice3.config(text="C: And knowing when you don't\nhave to is just as important\n[Calm him down]", command=lambda:OlgOutcome("B-A-B-C"))



                    if x == "Mercy":
                        EventDialog.config(text="You warn him again that his attack\nwill not go as he believes it will.\nAlas, by his stubborn charge, it seems\nyour words have fallen on obstinate ears...")
                        EventChoice1.config(text=">", command=lambda:[OlgOutcome("DODGE") or OlgOutcome("HIT")])
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()
                        

                    if x == "B-A":
                        EventDialog.config(text="You know his stance seems too\nunorthodox for practical use.\nYou barely know where to begin\nin correcting him if you wanted to.")

                        EventChoice1.config(text="A: Oh well. Amateur's gonna learn the hard way![FIGHT]", command=lambda:OlgOutcome("A"))
                        EventChoice2.config(text="B: Give him some basic combat advice", command=lambda:OlgOutcome("B-A-B")) 
                        EventChoice3.config(text="C: Have pity on the child.", command=lambda:OlgOutcome("Mercy"))


                    if x == "B-B":
                        EventDialog.config(text="Experience and training inform your assessment:\nHis defensive stance will do very little\ngood against your size advantage.\nLikewise, his stance and footing all but telegraph\nhis forthcoming opening lunge.\nYou feel smarter for seeing this coming,\nbut also recognize this particular amateur is\njust THAT painfully obvious...")
                        EventChoice1.config(text="[Offer to point these errors out to him]", command=lambda:OlgOutcome("B-A-B"))
                        EventChoice2.config(text="[Fight him anyway.]", command=lambda:OlgOutcome("A"))
                        EventChoice3.config(text="[Try to talk him out of it...]", command=lambda:OlgOutcome("B-B-C"))


                    if x == "DODGE":
                        EventChoice4.pack()
                        EventDialog.config(text="You casually side-step the drow boy's attack.\nHe falls to the ground and begins to grumble.\nSuccumbing to exhaustion, he loses consciousness.")
                        
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.config(text="C: [Check him for valuables]\n[DEX(Sleight of Hand)]", command=lambda:OlgOutcome("STEAL"))
                        EventChoice4.config(text="D: [You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        

                    if x == "HIT":
                        EventChoice4.pack()

                        EventDialog.config(text="Though his daggers suggest otherwise,\nhe settles with going for a punch.\nIt is well-aimed, but ineffective.\nHis fist glances off your abdomen, skewing his balance.\nHe collides uselessly into your torso,\nalready unconscious on arrival.")
                        
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.config(text="C: [Check him for valuables]\n[DEX(Sleight of Hand)]", command=lambda:OlgOutcome("STEAL"))
                        EventChoice4.config(text="[You can't leave him like this...Take him with you]", command=lambda:OlgOutcome("SLAP-A-A3-NO-YES"))
                        
                        


                    if x == "CHA_FAIL":
                        EventLabel.config(image=self.TheoTalk)

                        EventDialog.config(text="'ENOUGH TALK! YOU'RE GOING DOWN!'\nThe boy charges at you recklessly...\nDo you...")
                        EventChoice1.config(text="[Dodge]", command=lambda:OlgOutcome("DODGE"))
                        EventChoice2.config(text="[Take the hit]", command=lambda:OlgOutcome("HIT"))
                        EventChoice3.pack_forget()


                    if x == "TALK_PASS":
                        EventLabel.config(image=self.TheoTalk)

                        EventDialog.config(text="The boy's posture relaxes,\nfinally recognizing that you\nmean him no harm...")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("B-A-B-C"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()

                    if x == "SCARE_PASS":
                        EventLabel.config(image=self.TheoTalk)

                        EventDialog.config(text="The young drow loses his grip\non his daggers. He mutters a swear\nas he leans to pick them up.\nIn the process, his balance fails.\nHe hits the ground like a felled tree.\nHe's unconscious, breathing; fast asleep.")
                        EventChoice1.config(text="A: [Let him rest. Leave him where he lays...]", command=lambda:OlgOutcome("LEAVE"))
                        EventChoice2.config(text="B: [Leave him. But make sure he's safe and comfortable first.]", command=lambda:OlgOutcome("TUCKHIMIN"))
                        EventChoice3.config(text="C: [Check him for valuables]\n[DEX(Sleight of Hand)]", command=lambda:OlgOutcome("STEAL"))
                        

                        

                    if x == "B-B-C":
                        EventLabel.config(image="")
                        EventDialog.config(text="Convince the boy to stand down.\n[CHA 12 (Persuasion or Intimidation)]")
                        EventChoice1.config(text="[PASS (Intimidation)]", command=lambda:OlgOutcome("SCARE_PASS"))
                        EventChoice2.config(text="[PASS (Persuasion)]", command=lambda:OlgOutcome("TALK_PASS"))
                        EventChoice3.config(text="[FAIL]", command=lambda:OlgOutcome("CHA_FAIL"))


                    if x == "B-C2":
                        EventDialog.config(text="Even more apparent to you now,\nis the fact that the boy is running on fumes.\nHis eyes betray a weariness of far too many\nnights of poor, if any rest. He looks to collapse\nat any moment.")
                        EventChoice1.config(text="[Offer to point these errors out to him]", command=lambda:OlgOutcome("B-B-A"))  
                        EventChoice2.config(text="[Fight him anyway.]", command=lambda:OlgOutcome("B-B-B"))
                        EventChoice3.config(text="[Try to talk him out of it...]", command=lambda:OlgOutcome("B-B-C"))


                    if x == "B-C":
                        EventDialog.config(text="All signs point to inexperience.\nFrom his over-earnest grip on his daggers,\nto the exaggerated depth and width of his stance.\nThis boy is no threat to any combatant with actual training.")
                        EventChoice1.config(text=">", command=lambda:OlgOutcome("B-C2"))
                        EventChoice2.pack_forget()
                        EventChoice3.pack_forget()
                    if x == "B":
                        EventDialog.config(text="You take a moment to assess\nthe youth standing before you...\nWisdom(Perception) Check result:")

                        EventChoice1.config(text="1-10", command=lambda:OlgOutcome("B-A"))
                        EventChoice2.config(text="11-16", command=lambda:OlgOutcome("B-B"))
                        EventChoice3.config(text="17+", command=lambda:OlgOutcome("B-C"))


                    if x == 0:
                        EventLabel.config(image=self.TheoTalk)
                        #EventChoice2.pack(fill=X)
                        #EventChoice3.pack(fill=X)

                        EventDialog.config(text="A drow boy clad in tattered black leather,\nhis stance low and ready to attack!\nHe draws a pair of daggers and\nflourishes them with an impressive display of dexterity.")
                        
                        EventChoice1.config(text="A:Don't expect me to go easy on you\njust because you're a child...[FIGHT]", command=lambda:OlgOutcome("A"))
                        
                        EventChoice2.config(text="B:Critique his stance\n[Wisdom/Perception Check]", command=lambda:OlgOutcome("B"))
                        
                        EventChoice3.config(text="C: Escalate/De-escalate the situation\n[Charisma Check]", command=lambda:OlgOutcome("B-B-C"))
                        
                    


                EventLabelFrame.place(x=x, y=y)

                EventDialog.configure(text="Just as you sense you are being watched,\na figure separates from the shroud of foliage...")
                EventChoice1.configure(text=">", command=lambda:OlgOutcome(0))
                EventChoice2.pack_forget()
                EventChoice3.pack_forget()

                
                
                
                EventChoice4 = Button(EventLabelFrame)
                

            if got == "Ross":
                def RossOutcome(x):
                    EventChoice1.pack(fill=X)
                    EventChoice2.pack(fill=X)
                    EventChoice3.pack(fill=X)
                    EventChoice4.pack_forget()
                    
                    if x == "GoblinDies":
                        EventDialog.configure(text="his spear plants firmly into the goblin's side.\nShe lets out one last painful cry as the last of her life drains.")
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        TLabel.config(image=self.Guard)
                        PMarker.configure(bg='blue')
                        HPMaxSpinbox.config(from_=0, to=11, width=2)
                        HPMaxSpinbox.insert(0, 11)
                        HPMaxSpinbox.pack()
                        TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Guard")])
                    
                        

                    if x == "A_END":
                        EventDialog.configure(text="As you distance yourself from the motionless form, a guard lunges toward her...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("GoblinDies")])

                    if x == "B-A-A_END":
                        EventDialog.configure(text="You decide that the goblin woman has caused enough distraction.\nSticking your nose deeper into her business is likely to reward you with\nonly more trouble than its worth.\nBesides, your allies are likely in greater need of your attention at the moment...") 
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[PMarker.place_forget(), EventLabelFrame.place_forget()])

                    if x == "B-A-B-A_END":
                        PMarker.place_forget()
                        EventDialog.configure(text="You get the feeling that\nyou've made a nemesis today...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "B-A-B-B_END":
                        PMarker.place_forget()
                        EventDialog.configure(text="You get an odd feeling that\nthis one's going to be the death of you someday...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "B-A-B-C_END":
                        PMarker.place_forget()
                        EventDialog.configure(text="You get the odd feeling that\nyou're likely going to marry this girl someday...") 
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        

                    if x == "B-A-B":
                        EventDialog.configure(text="You call out to her, but to no avail.\nShe hobbles on her injured leg until she is able to disappear into the woods once again.\nWhen you think she has completely vanished, you hear a sourceless voice:\n'You will address me by my name; that's Ohzelmea Breexug, you loutish buffoon!'...\n[Insight Check]") 
                        EventChoice1.configure(text="1-10", command=lambda:[RossOutcome("B-A-B-A_END")])
                        EventChoice2.configure(text="11-16", command=lambda:[RossOutcome("B-A-B-B_END")])
                        EventChoice3.configure(text="17+", command=lambda:[RossOutcome("B-A-B-C_END")])





                    if x == "B-A-C-A_END":
                        EventDialog.configure(text="Your wounds are too fresh to not compromise your efforts\nand soon the goblin girl is lost to the forest.")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[random.choice([RossOutcome("B-A-A_END") or RossOutcome("B-A-B-B_END") or RossOutcome("B-A-B-A_END")]) ])

                    if x == "B-A-C":
                        EventDialog.configure(text="How well do you fare in chasing her?\n[Dexterity OR Strength(Athletics)]")
                        EventChoice1.configure(text="1-10", command=lambda:[RossOutcome("B-A-C-A_END")])
                        EventChoice2.configure(text="11-16", command=lambda:[RossOutcome("B-A-C-B_END")])
                        EventChoice3.configure(text="17+", command=lambda:[RossOutcome("B-A-C-C_END")])
                        
                        
                        
                    if x == "B-B-A":
                        EventDialog.configure(text="You notice her hand twiches in agitated readiness,\na waking burst of exertion poised to reach\nfor a dagger hidden within the folds of her ragged clothes.\nJust as you process what you've seen, a pair of hostile goblins,\nweapons drawn, reveal themselves for the attack!\nThe woman slips back into unconsciousness, leaving her defense,\nas well as your own, completely to your care.\n[ROLL INITIATIVE]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        playermarker2(main)
                        playermarker2(main)


                    if x =="B-B-B-A":
                        EventLabel.config(image="")
                        EventDialog.configure(text="COMBAT\n\nInitiative:\n1st:Roscoe(ranged attack)\n2nd:Enemy Goblin(arrow)\n3rd:Ohzelmea\n\nENCOUNTER CODES:\n'GGDED'--Ohzelmea dies\n'GGTHX'--Ohzelmea survives")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "PROTECT":
                        EventLabel.config(image="")
                        EventDialog.configure(text="ROLL INITIATIVE\n*Roscoe  *Enemy Goblin  *Ohzelmea\n\nWhile protecting the girl, any damage\ninflicted upon her will be deducted\nfrom your Hit points.\n\nENCOUTNER CODES:\n'GGDED'--Ohzelmea dies\n'GGTHX'--Ohzelmea survives")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "B-B-B-B":
                        EventLabel.config(image="")
                        EventDialog.configure(text="Instinctively, you dive atop the girl.\nShielding her with your body,\nyou take ("+str(random.randint(3,8))+") damage as the arrow\nsinks into the back of your shoulder." )
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:RossOutcome("PROTECT"))

                    if x == "DODGE_BATTLE":
                        EventDialog.configure(text="ROLL INITIATIVE\n*Roscoe  *Enemy Goblin  *Ohzelmea\n\nWhile protecting the girl, any damage\ninflicted upon her will be deducted\nfrom your Hit points.\n\nENCOUTNER CODES:\n'GGDED'--Ohzelmea dies\n'GGTHX'--Ohzelmea survives")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "DODGE_SOLO_BATTLE":
                        EventDialog.configure(text="ROLL INITIATIVE\n*Roscoe  *Enemy Goblin  *Ohzelmea\n\nENCOUTNER CODES:\n'GGDED'--Ohzelmea dies\n'GGTHX'--Ohzelmea survives")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "DODGE_SOLO":
                        arrowshot = ["misses Roscoe!"]*2 +["hits Roscoe!\nYou take ("+str(random.randint(3,8))+") damage!"] + ["misses Ohzelmea!"] +["hits Ohzelmea!\nShe takes ("+str(random.randint(3,8))+") damage!"]*2
                        EventDialog.configure(text="The arrow "+random.choice(arrowshot))
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("DODGE_SOLO_BATTLE")])



                    if x == "B-B-B-D":
                        EventLabel.config(image="")
                        EventDialog.configure(text="Instinctively, you evade the line of fire...\nLeaving the girl to fend for herself...\nThe goblin above lets its arrow fly...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("DODGE_SOLO")])



                    if x == "DODGE":
                        arrowaction = ["hits "+random.choice(["Roscoe" or "Ohzelmea"])+"!\nIt inflicts ("+str(random.randint(3,8))+") damage"] + ["zips by "+random.choice(["Roscoe" or "Ohzelmea"])+"\nplanting resolute in the ground\nwhere they once were."]
                        EventDialog.configure(text="The arrow "+random.choice(arrowaction))
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:RossOutcome("DODGE_BATTLE"))


                    if x == "B-B-B-C":
                        EventLabel.config(image="")
                        EventDialog.configure(text="You attempt to move yourself and the girl out of harm's way.\nIn doing so, you make a generally easier target\nfor your assailant to hit")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:RossOutcome("DODGE"))



                    if x == "B-B-B":
                        EventChoice4.pack()

                        EventDialog.configure(text="You hear unusual rustling in the trees above...\nYour suspicions are confirmed by a betraying glint\nof a nocked arrowhead's flash within the green.")
                        EventChoice1.configure(text="A: Strike first! [Ranged]", command=lambda:[RossOutcome("B-B-B-A")])
                        EventChoice2.configure(text="B: Protect the girl\n[Take damage inflicted on her as your own]", command=lambda:[RossOutcome("B-B-B-B")])
                        EventChoice3.configure(text="C: Dodge AND protect the girl\n[Enemy attacks with advantage]", command=lambda:[RossOutcome("B-B-B-C")])
                        EventChoice4.configure(text="D: Fend for yourself. Dodge", command=lambda:[RossOutcome("B-B-B-D")])




                    if x == "B-C3":
                        EventDialog.configure(text="You take a moment to admire your handiwork, perhaps even utter a witty one-liner.\nAs you finish savoring the moment and return your attention\nto the goblin woman, she has already made considerable distance from you.")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("B-A-B")])

                    if x == "B-C2":
                        EventDialog.configure(text="The gobliness lunges at you, falling for a feigned lapse in your guard.\nHer dagger finds a differnt mark as you intercept its path and seize it from her hand.\nIn the same smooth motion, you fling it with deadly accuracy to the goblin\nawaiting its chance to ambush.\nYou hear the mortal, gruesome snap of bone as the lifeless would-be assailant lands hard onto the unforgiving ground.")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("B-C3")])

                    if x == "B-C":
                        EventDialog.configure(text="In rare form, your senses encompass the entirety of your immediate surroundings.\nThe goblin female is weakened, but seems to be\nmustering up strength to mount a sneak attack.\nUnbeknownst to her, a hostile goblin hidden in the\n trees above nocks and arrow into his shortbow and takes aim for her heart...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("B-C2")])
                        
                    if x == "B-B":
                        EventDialog.configure(text="Your senses are alert, but unevenly divided.\nYou focus on...")
                        EventChoice1.configure(text="A: The goblin. Something's not right here...", command=lambda:[RossOutcome("B-B-A")])
                        EventChoice2.configure(text="B: Your surroundings. Something's not right here...", command=lambda:[RossOutcome("B-B-B")])
                        EventChoice3.pack_forget()



                    if x == "B-A":
                        EventDialog.configure(text="You're almost certain there is no immediate danger among the trees...\nHowever, a slight rustling in the nearby bushes catches your attention.\nIt is at that moment, you feel a sharp pain at your torso!\nThe goblin woman, now fully alert, draws her blade from your side\nand sprints for the forest....\nuntil her injuries remind her of her limited mobility...")
                        EventChoice1.configure(text="A: Let her go. You probably scared her.", command=lambda:[RossOutcome("B-A-A_END")])
                        EventChoice2.configure(text="B: Call out to her.", command=lambda:[RossOutcome("B-A-B")])
                        EventChoice3.configure(text="C: Chase her down!", command=lambda:[RossOutcome("B-A-C")])


                    if x == "B":
                        EventDialog.configure(text="You wisely decide to assess the situation before taking any rash action.\n[Make a Perception(Wisdom) check]")
                        EventChoice1.configure(text="A: 1-10.", command=lambda:[RossOutcome("B-A")]) 
                        EventChoice2.configure(text="B: 11-15", command=lambda:[RossOutcome("B-B")])
                        EventChoice3.configure(text="C: 16+", command=lambda:[RossOutcome("B-C")])


                    if x == "NAME":
                        EventDialog.configure(text="'My name is Ohzelmea clon Pyolgrik, daughter of--'\nHer introduction is clipped short as a guard emerges from the nearby foliage, ready to attack!\n[ROLL INITIATIVE!]\n[Ohzelmea HP: 100%, Movement 100%]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        playermarker2(main)


                    if x == "FLIRTYES":
                        EventDialog.configure(text="She chuckles until her laughter\nends with a round of snorting.\nShe thanks you for your help and begins\nto properly introduce herself...")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("NAME")])



                    if x == "FLIRT":
                        EventDialog.configure(text="Ease her mind with an attempt at flirtation\n[CHA (Persuasion)--16]")
                        EventChoice1.configure(text="PASS", command=lambda:[RossOutcome("FLIRTYES")]) 
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text="FAIL", command=lambda:[RossOutcome("FLIRTNO")])#




                    if x == "WHAHAPPEN":
                        EventDialog.configure(text="'My leg got caught in a deer trap', she reluctantly admits.\nDoesn't seem like she'll tell you\nmuch more than that...")
                        EventChoice1.configure(text="Who are you?", command=lambda:[RossOutcome("NAME")]) 
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text="Flirt with her\n[CHA (Persuasion)]", command=lambda:[RossOutcome("FLIRT")])



                    if x == "C-C_END2":
                        EventDialog.configure(text="'Th-thank you...' she almost shyly mutters\nwhile she tests the limits of your restoration.\nShe nods in approval, pleased with the results.")
                        EventChoice1.configure(text="Who are you?", command=lambda:[RossOutcome("NAME")]) 
                        EventChoice2.configure(text="What happened here?", command=lambda:[RossOutcome("WHAHAPPEN")])
                        EventChoice3.configure(text="Flirt with her\n[CHA (Persuasion)]", command=lambda:[RossOutcome("FLIRT")])

                        
                    if x == "C-C_END":
                        EventDialog.configure(text="You expertly tend to the gobliness's wounds.\nShe is fully conscious by the time your work is done.") 
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])

                    if x == "C-B_END":
                        EventDialog.configure(text="Bickering and banter continues for an indefinite amount of time...\nLong enough to attract the attention of a pair of guards!\n[ROLL INITIATIVE!]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        playermarker2(main)
                        playermarker2(main)

                    if x == "C-B":
                        EventDialog.configure(text="Though it takes longer than you'd like, you manage to dress the goblin woman's wounds.\nShe regained consciousnes somewhere amidst your efforts and began berating you through the process.\n[Ohzelmea HP:100%, Movement:50%]")
                        EventChoice1.pack_forget() #Full HP, HALF Movement
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("C-B_END")])

                    
                    if x == "C-A_END":
                        EventDialog.configure(text="An orc appears from the other end of the projectile's trajectory,\nsmugly chewing on the last bites of an apple plucked from the orchard.\nHe smiles in anticipation of perhaps another appetite meeting its fill...\n[ROLL INITIATIVE!]")
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[EventLabelFrame.place_forget()])
                        playermarker2(main)

                    if x == "C-A2":
                        EventDialog.configure(text="Her eyes go wide as though realizing her mistake.\nBefore you could reply, she wraps herself around your head,\nusing her full body weight to bring you to the ground as\na javelin zips past your former position,\nembedding itself into the trunk of a nearby tree.") 
                        EventChoice1.pack_forget()
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("C-A_END")])

                    if x == "C-A":
                        EventLabel.config(image=self.Ozytlk)
                        EventDialog.configure(text="'My heart's over HERE, dumbass!'\nshe angrily intones.\n She shifts your hand from her breast to\na more clinical position on her chest.\n[Ohzelmea HP:50% Movement:50%]")
                        EventChoice1.pack_forget() #Full HP, HALF Movement
                        EventChoice2.pack_forget()
                        EventChoice3.configure(text=">", command=lambda:[RossOutcome("C-A2")])

                    if x == "C":
                        EventDialog.configure(text="You quickly begin the process of administering first aid...\n[Wisdom(Medicine) Check]")
                        EventChoice1.configure(text="A: 1-10.", command=lambda:[RossOutcome("C-A")]) 
                        EventChoice2.configure(text="B: 11-15", command=lambda:[RossOutcome("C-B")])
                        EventChoice3.configure(text="C: 16+", command=lambda:[RossOutcome("C-C_END")])

                        
                            

                EventLabelFrame.place(x=x, y=y)
                EventDialog.configure(text="You see a gobliness, unconscious, covered in mud, and clutching her ankle.\nA fresh trail of blood leads deeper into the grove.")
                EventChoice1.configure(text="A: Ignore her. This is obviously a trap.", command=lambda:[RossOutcome("A_END")])
                EventChoice2.configure(text="B: Check the surrounding area for any danger", command=lambda:[RossOutcome("B")])
                EventChoice3.configure(text="C: Prioritize her care. She seems to be fading fast.", command=lambda:[RossOutcome("C")])
                EventChoice4 = Button(EventLabelFrame)
                
            if got == "Tmp":
                AcquiredButton.config(text="Temple Healing!\nTemple loses/Creature gains\n"+str(random.randint(1,4))+"+CON HP!")
                    

        def wordboxspot(x,y, monster):
            CommandLF.place_forget()
            CommandLF.place(x=x, y=y)
            #Button1.config(text="Attack")
            #Button2.config(text="Talk")
            #Button3.config(text="Stats")


            
            if monster == "Goblin":
                print("GOBBOBOY!")
                Button1.config(command=lambda:[Interaction("Goblin", "ATK")])
                Button2.config(command=lambda:[Interaction("Goblin", "TLK")])
                Button3.config(command=lambda:[Interaction("Goblin", "STS")])

            elif monster == "Berserker":
                print("CraeCrae boy!")
                Button1.config(command=lambda:[Interaction("Berserker", "ATK")])
                Button2.config(command=lambda:[Interaction("Berserker", "TLK")])
                Button3.config(command=lambda:[Interaction("Berserker", "STS")])

                     
            elif monster == "Cultist":
                print("Cult-o boy!")
                Button1.config(command=lambda:[Interaction("Cultist", "ATK")])
                Button2.config(command=lambda:[Interaction("Cultist", "TLK")])
                Button3.config(command=lambda:[Interaction("Cultist", "STS")])

            elif monster == "Scout":
                print("Cult-o boy!")
                Button1.config(command=lambda:[Interaction("Scout", "ATK")])
                Button2.config(command=lambda:[Interaction("Scout", "TLK")])
                Button3.config(command=lambda:[Interaction("Scout", "STS")])

            elif monster == "Zombie":
                print("Zombo-o boy!")
                Button1.config(command=lambda:[Interaction("Zombie", "ATK")])
                Button2.config(command=lambda:[Interaction("Zombie", "TLK")])
                Button3.config(command=lambda:[Interaction("Zombie", "STS")])

            elif monster == "Companion":
                print("Pupper-gal!")
                Button1.config(command=lambda:[Interaction("Companion", "ATK")])
                Button2.config(command=lambda:[Interaction("Companion", "TLK")])
                Button3.config(command=lambda:[Interaction("Companion", "STS")])

            elif monster == "Guard":
                print("Guardy boy!")
                Button1.config(command=lambda:[Interaction("Guard", "ATK")])
                Button2.config(command=lambda:[Interaction("Guard", "TLK")])
                Button3.config(command=lambda:[Interaction("Guard", "STS")])

            
        
                

            elif monster == "Bugbear":
                print("Buggie boy!")
                Button1.config(command=lambda:[Interaction("Bugbear", "ATK")])
                Button2.config(command=lambda:[Interaction("Bugbear", "TLK")])
                Button3.config(command=lambda:[Interaction("Bugbear", "STS")]) 

            elif monster == "Bandit":
                print("BanditoBoy!")
                Button1.config(command=lambda:[Interaction("Bandit", "ATK")])
                Button2.config(command=lambda:[Interaction("Bandit", "TLK")])
                Button3.config(command=lambda:[Interaction("Bandit", "STS")]) 

            elif monster == "Hobgoblin":
                print("HoboGobbo!")
                Button1.config(command=lambda:[Interaction("Hobgoblin", "ATK")])
                Button2.config(command=lambda:[Interaction("Hobgoblin", "TLK")])
                Button3.config(command=lambda:[Interaction("Hobgoblin", "STS")]) 

            elif monster == "Skeleton":
                print("BoneDaddy!")
                Button1.config(command=lambda:[Interaction("Skeleton", "ATK")])
                Button2.config(command=lambda:[Interaction("Skeleton", "TLK")])
                Button3.config(command=lambda:[Interaction("Skeleton", "STS")]) 

            elif monster == "Orc":
                print("MeanGreen!")
                Button1.config(command=lambda:[Interaction("Orc", "ATK")])
                Button2.config(command=lambda:[Interaction("Orc", "TLK")])
                Button3.config(command=lambda:[Interaction("Orc", "STS")]) 

            elif monster == "Ozel":
                CLabel.config(text="Ohzelmea")
                Button1.pack_forget()
                Button2.config(command=lambda:[Interaction("Ozel", "TLK")])
                Button3.config(command=lambda:[Interaction("Ozel", "STS")])
                


            

            else:          
                print(monster)


        def EntryToggle(x):
            if x == 0:
                Entry1.pack()
                
                #wordboxspot(PMarker.winfo_x() + 64, PMarker.winfo_y() - 32)
                #print(PMarker.winfo_x() + 32, PMarker.winfo_y())

            elif x == 1:
                Entry1.pack_forget()
                TLabel.config(command=lambda:EntryToggle(0))

            
        

            

       

        def EFunctions(x):
            global monster
            Entry1.delete(0, END)
            
            try:
                PMarker.configure(bg=x)
                #PMarker['bg'] == x
                print(PMarker['bg'])
                
            except:
                pass
                                

            if x == "":
                PMarker.place_forget()

            if x == "0":
                PMarker.place_forget()


            if x == "Goblin":
                TLabel.config(image=self.gobby)
                PMarker.configure(bg='red')
                HPMaxSpinbox.config(from_=0, to=7)
                HPMaxSpinbox.insert(0, 7)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Goblin")])

            if x == "Berserker":
                TLabel.config(image=self.brskr)
                HPMaxSpinbox.config(from_=0, to=67, width=2)
                HPMaxSpinbox.insert(0, 67)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Berserker")])

            if x == "Bugbear":
                TLabel.config(image=self.bugbr)
                PMarker.configure(bg='purple')
                HPMaxSpinbox.config(from_=0, to=27, width=2)
                HPMaxSpinbox.insert(0, 27)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Bugbear")])

            if x == "Hobgoblin":
                TLabel.config(image=self.hgobbo)
                PMarker.configure(bg='green')
                HPMaxSpinbox.config(from_=0, to=11, width=2)
                HPMaxSpinbox.insert(0, 11)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Hobgoblin")])

            if x == "Bandit":
                TLabel.config(image=self.bndt)
                PMarker.configure(bg='brown')
                HPMaxSpinbox.config(from_=0, to=11, width=2)
                HPMaxSpinbox.insert(0, 11)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Bandit")])

            if x == "Cultist":
                TLabel.config(image=self.cult)
                PMarker.configure(bg='crimson')
                HPMaxSpinbox.config(from_=0, to=9, width=1)
                HPMaxSpinbox.insert(0, 9)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Cultist")])

            if x == "Guard":
                TLabel.config(image=self.Guard)
                PMarker.configure(bg='blue')
                HPMaxSpinbox.config(from_=0, to=11, width=2)
                HPMaxSpinbox.insert(0, 11)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Guard")])

            if x == "Skeleton":
                TLabel.config(image=self.Skel)
                HPMaxSpinbox.config(from_=0, to=13, width=2)
                HPMaxSpinbox.insert(0, 13)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Skeleton")])

            if x == "Orc":
                TLabel.config(image=self.orc)
                PMarker.configure(bg='dark green')
                HPMaxSpinbox.config(from_=0, to=15, width=2)
                HPMaxSpinbox.insert(0, 15)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Orc")])

            
                

            if x == "Scout":
                TLabel.config(image=self.Scout)
                PMarker.configure(bg='light green')
                HPMaxSpinbox.config(from_=0, to=16, width=2)
                HPMaxSpinbox.insert(0, 16)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Scout")])

            if x == "Zombie":
                TLabel.config(image=self.zmbi)
                HPMaxSpinbox.config(from_=0, to=22, width=2)
                HPMaxSpinbox.insert(0, 22)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Zombie")])

                
            

                
            #PARTY MEMBERS
            if x == "Aricin":
                TLabel.config(image=self.Aric)
                PMarker.configure(bg='gold')
                HPMaxSpinbox.config(from_=0, to=48, width=2)
                HPMaxSpinbox.insert(0, 48)

            
                
                
                
                
            if x == "Axel":
                TLabel.config(image=self.Axl)
                PMarker.configure(bg='orange')
                HPMaxSpinbox.config(from_=0, to=64, width=2)
                HPMaxSpinbox.insert(0, 64)

            if x == "Noir":
                TLabel.config(image=self.Noi)
                PMarker.configure(bg='purple')
                HPMaxSpinbox.config(from_=0, to=44, width=2)
                HPMaxSpinbox.insert(0, 44)

        

            if x == "Bahimbo":
                TLabel.config(image=self.Bmbo)
                PMarker.configure(bg='orange')
                HPMaxSpinbox.config(from_=0, to=44, width=2)
                HPMaxSpinbox.insert(0, 44)
                

            if x == "Caramil":
                TLabel.config(image=self.Cmil)
                PMarker.configure(bg='purple')
                HPMaxSpinbox.config(from_=0, to=42, width=2)
                HPMaxSpinbox.insert(0, 42)

            if x == "Harlow":
                TLabel.config(image=self.Hrlo)
                PMarker.configure(bg='white')
                HPMaxSpinbox.config(from_=0, to=49, width=2)
                HPMaxSpinbox.insert(0, 49)

            
            if x == "Ophelia":
                TLabel.config(image=self.Ophe)
                PMarker.configure(bg='#dcd8c0')
                HPMaxSpinbox.config(from_=0, to=59, width=2)
                HPMaxSpinbox.insert(0, 59)

            #NPCS

            if x == "V?":
                TLabel.config(image=random.choice([self.VM1, self.VW1, self.VB1, self.VG1]))
                PMarker.configure(bg='teal')
                HPMaxSpinbox.config(from_=0, to=4, width=2)
                HPMaxSpinbox.insert(0, 4)

            if x == "VM1":
                TLabel.config(image=self.VM1)
                PMarker.configure(bg='teal')
                HPMaxSpinbox.config(from_=0, to=4, width=2)
                HPMaxSpinbox.insert(0, 4)

            if x == "VW1":
                TLabel.config(image=self.VW1)
                PMarker.configure(bg='teal')
                HPMaxSpinbox.config(from_=0, to=4, width=2)
                HPMaxSpinbox.insert(0, 4)

            if x == "VB1":
                TLabel.config(image=self.VB1)
                PMarker.configure(bg='teal')
                HPMaxSpinbox.config(from_=0, to=4, width=2)
                HPMaxSpinbox.insert(0, 4)

            if x == "VG1":
                TLabel.config(image=self.VG1)
                PMarker.configure(bg='teal')
                HPMaxSpinbox.config(from_=0, to=4, width=2)
                HPMaxSpinbox.insert(0, 4)

            if x == "Persephone":
                TLabel.config(image=self.Prse)
                PMarker.configure(bg='crimson')

            if x == "Ozy1":
                TLabel.config(image=self.Ozy1)
                PMarker.configure(bg='brown')

            if x == "Ozy2":
                TLabel.config(image=self.Ozy2)
                PMarker.configure(bg='teal')
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Ozel")])
                

            if x == "Theo":
                TLabel.config(image=self.TheoIcon)
                PMarker.configure(bg='gray')


            if x == "Amelie":
                TLabel.config(image=self.Amle)
                PMarker.configure(bg='navy blue')

            if x == "Toothless":
                TLabel.config(image=self.TtD)
                PMarker.configure(bg='hot pink')
                HPMaxSpinbox.config(from_=0, to=22, width=2)
                HPMaxSpinbox.insert(0, 22)
                TLabel.config(command=lambda:[wordboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Companion")])


            if x == "Chasity":
                TLabel.config(image=self.Chas)
                PMarker.configure(bg='black')


            if x == "Unk?":
                TLabel.config(image=self.Mystery)
                HPMaxSpinbox.pack_forget()
                PMarker.configure(bg='teal')
                TLabel.config(command=lambda:[itemboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Unk?")])

            if x == "Unk*":
                TLabel.config(image=self.Mystery)
                HPMaxSpinbox.pack_forget()
                PMarker.configure(bg='red')
                TLabel.config(command=lambda:[itemboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Unk*")])


            if x == "Itm?":
                TLabel.config(image=self.Chst)
                HPMaxSpinbox.pack_forget()
                PMarker.configure(bg='teal')
                TLabel.config(command=lambda:[itemboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Itm?")])


            if x == "Flora1":
                TLabel.config(image=self.Leaf)
                S = random.randint(10,16)
                HPMaxSpinbox.config(from_=0, to=S, width=2)
                HPMaxSpinbox.insert(0, S)
                PMarker.configure(bg='teal')
                TLabel.config(command=lambda:[itemboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "F1")])

            if x == "Fire1":
                TLabel.config(image=self.Fire)
                F = random.randint(1,6)
                HPMaxSpinbox.config(from_=0, to=F, width=2)
                HPMaxSpinbox.insert(0, F)
                PMarker.configure(bg='red')
                
            if x == "Temple":
                TLabel.config(image=self.tmpl)
                P = random.randrange(20,50,5)
                HPMaxSpinbox.config(from_=0, to=P, width=2)
                HPMaxSpinbox.insert(0, P)
                PMarker.configure(bg='teal')
                TLabel.config(command=lambda:[itemboxspot(PMarker.winfo_x() + 35, PMarker.winfo_y() + 32, "Temple")])


            #OBJECTS
            if x == "Tavern1": #1d12 per tav level
                PMarker.configure(bg='brown')
                TLabel.config(image=self.Tavvy, bd=0)
                Q = random.randint(0,12) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)

            if x == "Weapon1": 
                PMarker.configure(bg='brown')
                TLabel.config(image=self.WpnShp, bd=0)
                Q = random.randint(0,12) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)

            if x == "Armor1": 
                PMarker.configure(bg='brown')
                TLabel.config(image=self.ArmShp, bd=0)
                Q = random.randint(0,12) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)


            if x == "Magic1":
                PMarker.configure(bg='brown')
                TLabel.config(image=self.MagShp, bd=0)
                Q = random.randint(0,12) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)

            if x == "Smithy1":
                PMarker.configure(bg='brown')
                TLabel.config(image=self.BSmith, bd=0)
                Q = random.randint(0,12) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)

            if x == "Door":
                PMarker.configure(bg='brown') 
                TLabel.config(image=self.door, bd=0)
                Q = random.randint(10,16) #1d12
                HPMaxSpinbox.config(from_=0, to=Q, width=2)
                HPMaxSpinbox.insert(0, Q)

            


                

            Entry1.pack_forget()

            
            
        #--------------MARKER BODY-------------------------------------------
        

        PMarker = Frame(main, pady=5, bd=1)

        

        PMarker['bg'] == 'gray'

        TLabel = Button(PMarker)
        TLabel.pack()
        TLabel.bind("<Button-3>", (lambda event:EntryToggle(0)))

        Entry1 = Entry(PMarker, width=6)
        Entry1.bind("<Return>", (lambda event:EFunctions(str(Entry1.get()))))

        HPMaxSpinbox = Spinbox(PMarker, width=2, from_=0)
        HPMaxSpinbox.insert(0, "??")
        
        

        HPMaxSpinbox.bind("<Return>", (lambda event:HPAdjust(int(HPMaxSpinbox.get()))))
        HPMaxSpinbox.pack()
   

        PMarker.place(x=10, y=10) 
        


        

        PMarker.bind("<Button-1>", drag_start)
        PMarker.bind("<B1-Motion>", drag_motion)
        
        

        #IMAGES
        #PARTY
        self.Aric = PhotoImage(file=(resource_path('Arcn.png')))   
        self.Cmil = PhotoImage(file=(resource_path('Cmil.png')))  
        self.Rsco = PhotoImage(file=(resource_path('Rsco.png')))  
        self.Kopf = PhotoImage(file=(resource_path('Kopf.png')))
        self.Olga = PhotoImage(file=(resource_path('Olga.png')))
        self.Bmbo = PhotoImage(file=(resource_path('Bmbo.png')))
        self.Hrlo = PhotoImage(file=(resource_path("Hrlo.png")))
        self.Ophe = PhotoImage(file=(resource_path("Ophe.png")))

        

        #NPCS
        self.Ozytlk = PhotoImage(file=(resource_path("OzeeTalk.png")))
        self.Ozy1 = PhotoImage(file=(resource_path("Ozy1.png")))
        self.Ozy2 = PhotoImage(file=(resource_path("Ozy2.png")))
        self.Prse = PhotoImage(file=(resource_path("Prse.png")))
        self.Amle = PhotoImage(file=(resource_path("Amle.png")))
        self.Chas = PhotoImage(file=(resource_path("Chas.png")))
        self.Mystery = PhotoImage(file=(resource_path("Unk.png")))
        self.Guard = PhotoImage(file=(resource_path("Guard.png")))


        self.VM1 = PhotoImage(file=(resource_path("VM1.png")))
        self.VW1 = PhotoImage(file=(resource_path("VW1.png")))
        self.VB1 = PhotoImage(file=(resource_path("VB1.png")))
        self.VG1 = PhotoImage(file=(resource_path("VG1.png")))

        self.TtD = PhotoImage(file=(resource_path("TtD.png")))

        self.Simn = PhotoImage(file=(resource_path("Simonicon.png")))
        self.SiTlk = PhotoImage(file=(resource_path("Simontalk.png")))


        self.TargTlk = PhotoImage(file=(resource_path("TargusTlk.png")))
        self.Ozy2Tlk = PhotoImage(file=(resource_path("Ozytalk.png")))


        self.TheoIcon= PhotoImage(file=(resource_path("TheodoreIcon.png")))
        self.TheoTalk= PhotoImage(file=(resource_path("TheodoreTalk.png")))
        #ENEMIES
        self.Skel = PhotoImage(file=(resource_path("Skel.png")))
        self.cult = PhotoImage(file=(resource_path('Cult.png')))
        self.gobby = PhotoImage(file=(resource_path('Gobo.png')))
        self.bugbr = PhotoImage(file=(resource_path('Bubr.png')))
        self.zmbi  = PhotoImage(file=(resource_path("zmbi.png")))
        self.orc = PhotoImage(file=(resource_path("Orc.png")))
        self.Scout = PhotoImage(file=(resource_path("Sct.png")))
        self.brskr = PhotoImage(file=(resource_path("Brskr.png")))
        self.hgobbo = PhotoImage(file=(resource_path("hobgob.png")))
        self.bndt = PhotoImage(file=(resource_path("bndt.png")))

        #OBJECTS
        self.Tavvy = PhotoImage(file=(resource_path("TavSign.png")))
        self.WpnShp = PhotoImage(file=(resource_path("WpnShp.png")))
        self.BSmith = PhotoImage(file=(resource_path("BSmith.png")))
        self.MagShp = PhotoImage(file=(resource_path("MagShp.png")))
        self.ArmShp = PhotoImage(file=(resource_path("ArmShp.png")))
        self.Chst = PhotoImage(file=(resource_path("chst.png")))
        self.tmpl = PhotoImage(file=(resource_path("tmpl.png")))
        self.door = PhotoImage(file=(resource_path("Door.png")))
        self.Leaf = PhotoImage(file=(resource_path("leaf.png")))
        self.Fire = PhotoImage(file=(resource_path("Fire.png")))
 
#---------------------ITEM MENU----------------------------------------------
        ItemLF = LabelFrame(main)

        ILabel = Label(ItemLF, text="Item")
        ILabel.pack(fill=X)

        I_Button1 = Button(ItemLF, text="Open")
        I_Button1.pack(fill=X)
        I_Button2 = Button(ItemLF, text="Cancel", command=lambda:ItemLF.place_forget())
        I_Button2.pack(fill=X)
        I_Button3 = Button(ItemLF)
        I_Button4 = Button(ItemLF)

        I_Button5 = Button(ItemLF)
        I_Button6 = Button(ItemLF)
        I_Button7 = Button(ItemLF)
        I_Button8 = Button(ItemLF)

        I_Parser = Entry(ItemLF)

        

#---------------------COMMAND MENU--------------------------------------------
        CommandLF = LabelFrame(main)
        
        CLabel = Label(CommandLF, text="Command")
        CLabel.pack()

        Button1 = Button(CommandLF, text="Attack")
        Button1.pack(fill=X, side=TOP)

        Button2 = Button(CommandLF, text="Talk")
        Button2.pack(fill=X)

        Button3 = Button(CommandLF, text="Stats")
        Button3.pack(fill=X, side=BOTTOM)

        


        
#---------------------------------------------------------------------------------
        #CommandLF = LabelFrame(main)
        ResultsFrame = Frame(CommandLF)
        OKButton = Button(ResultsFrame, text="OK", command=lambda:[ResultsFrame.pack_forget(), CommandLF.pack_forget(), reset()])

        

        AttackFrame = Frame(ResultsFrame)
        ATKLabel = Label(AttackFrame, text="ATK")
        ATK_E = Entry(AttackFrame, width=2)

        DamageFrame = Frame(ResultsFrame)
        DMGLabel = Label(DamageFrame, text="DMG")
        DMG_E = Entry(DamageFrame, width=2)

        ExtraFrame = Frame(ResultsFrame)
        M_Button = Button(ExtraFrame, text="Melee")
        R_Button = Button(ExtraFrame, text="Range")
        V_Button = Button(ExtraFrame, text="2-Hand")


#-------------------------------------------------------------------------
#-----------ITEM/PERSON ACQUIRED INFO
        AcquiredButton = Button(main)

        EventLabelFrame = LabelFrame(main)
        EventLabel = Label(EventLabelFrame)
        EventLabel.pack()

        EventDialog = Label(EventLabelFrame)
        EventDialog.pack()

        EventChoice1 = Button(EventLabelFrame)
        EventChoice1.pack(fill=X)

        EventChoice2 = Button(EventLabelFrame)
        EventChoice2.pack(fill=X)

        EventChoice3 = Button(EventLabelFrame)
        EventChoice3.pack(fill=X)

        EventLabelFrame.bind("<Button-1>", drag_start)
        EventLabelFrame.bind("<B1-Motion>", drag_motion)

class InitiativeTrack:
      def __init__(self, InitiativeInterface):
          
           
            def Namechange(x):
                if x == "Bandit":
                    NameEntry.config(bg='brown'), NameEntry.config(fg='white')
                if x == "Cultist":
                    NameEntry.config(bg='crimson'), NameEntry.config(fg='white')
                if x == "Guard":
                    NameEntry.config(bg='blue'), NameEntry.config(fg='white')
                if x == "Orc":
                    NameEntry.config(bg='dark green'), NameEntry.config(fg='white')
                if x == "Bugbear":
                    NameEntry.config(bg='purple'), NameEntry.config(fg='white')
                if x == "Hobgoblin":
                    NameEntry.config(bg='green'), NameEntry.config(fg='white')
                if x == "Goblin":
                    NameEntry.config(bg='red'), NameEntry.config(fg='white')
                if x == "Scout":
                    NameEntry.config(bg='light green'), NameEntry.config(fg='white')
                else:
                    NameEntry.config(bg=NameEntry.get()), NameEntry.config(fg='white')
                    
                


            self.InitiativeInterface = InitiativeInterface


            MasterFrame = Frame(InitiativeInterface)
            MasterFrame.pack(pady=5, side=BOTTOM)

            MasterFrame.bind("<Button-1>", drag_start)
            MasterFrame.bind("<B1-Motion>", drag_motion)




            EntryFrame = Frame(MasterFrame)
            EntryFrame.pack(side=TOP)
            
            InitEntry = Entry(EntryFrame, width=2)
            InitEntry.pack(side=LEFT)
            NameEntry = Entry(EntryFrame, width=15)
            NameEntry.pack(side=LEFT)
            NameEntry.bind("<Return>", (lambda event:[Namechange(NameEntry.get())]))



            #NameEntry.bind("<Return>", (lambda event:[NameEntry.config(bg=NameEntry.get()), NameEntry.config(fg='white')]))

            


            Cancel = Button(EntryFrame, text="X", command=lambda:[MasterFrame.pack_forget() or MasterFrame.place_forget()])
            Cancel.pack(side=LEFT)


            HPAC = Frame(MasterFrame)
            
            ACENTRY = Label(HPAC, text="AC")
            ACENTRY.pack(side=LEFT)
            ACSCORE = Entry(HPAC, width=2)
            ACSCORE.pack(side=LEFT)

            HPAC.pack(side=LEFT)




class interfacewindow:
    def __init__(self, root, title, mapz, jamz, F):
          
         
          main = root
          main['bg'] = 'black'
          
          root.title(title)

          BIGPICTURE = Frame(root, bg='black')
          BIGPICTURE.pack()


          PICFrame = Frame(BIGPICTURE, bd=0)
          PICFrame.pack(side=LEFT)

          Frame1 = Frame(BIGPICTURE, bd=0)
          Frame1.pack()

          root.picmap = PhotoImage(file=(resource_path(mapz+".png")))
          Maplabel = Label(PICFrame, image=root.picmap, bd=0)
          Maplabel.pack(side=LEFT)

          self.Foggy = Label(main, height=40, width=70, bg='black')


          self.Foggy.bind("<Button-1>", drag_start)
          self.Foggy.bind("<B1-Motion>", drag_motion)


          def fightsong(x):
              TurnButton.place(x=600, y=200)
              if x == 1:
                  TurnButton.configure(text='Player Turn', bg='dark blue')
                  TurnButton.configure(command=lambda:[TurnButton.place_forget(),pygame.mixer.music.fadeout(3600), pygame.mixer.music.load(resource_path(("Battle-Conflict.mp3"))), pygame.mixer.music.set_volume(0.2), pygame.mixer.music.play(-1)])
                    
              if x == 2:
                  TurnButton.configure(text='Enemy Turn', bg='dark red')
                  TurnButton.configure(command=lambda:[TurnButton.place_forget(),pygame.mixer.music.fadeout(3600), pygame.mixer.music.load(resource_path(("battle-dark.mp3"))), pygame.mixer.music.play(-1)])


          
          BottomInterface = Frame(root, width=50, bg="blue", bd=3, relief=RAISED) 

          DummyFrame = Frame(BottomInterface, height=90, bg='blue')
          DummyFrame.pack(side=RIGHT)


          ParserBar = Entry(BottomInterface)  
          
          ParserBar.bind("<Return>", (lambda event:CommandLine(str(ParserBar.get()))))
          MapsizeLabel = Label(BottomInterface, text="1sq = "+F+" ft")

          TurnLabelFrame = LabelFrame(BottomInterface, bd=0)
          PlayerTurnButton = Button(TurnLabelFrame, text="Player Turn", bg='dark blue', fg='white', command=lambda:fightsong(1))
          PlayerTurnButton.pack(side=LEFT)
          EnemyTurnButton = Button(TurnLabelFrame, text="Enemy Turn", bg='dark red', fg='white', command=lambda:fightsong(2))
          EnemyTurnButton.pack()

          TurnButton = Button(main, fg='white', font='helvetica 12 bold')
          
         

          InitiativeInterface = Frame(Frame1, bg='blue', bd=3, relief=RAISED)

          InitiativeInterface.pack(fill=Y)

          def InsCards():
              INSC = [
                  'Nemesis\nTarget NPC becomes your permanent foe. Draw a card each time they appear and cause trouble', 
                  'Scholar\nAdvantage on History or Insight', 
                  'Hard to Resist\nGain +2 to Spell DC', 
                  'Feint\nAfter a missed attack, try again with Advantage', 
                  'Zig-Zag\nDisengage as a free action',
                  'Arcane Surge\nAll your spell slots act as one level higher for this encounter',
                  'Taunt\nTarget foe attacks you relentlessly',
                  'Perfect Form\nAdvantage on Athletics or Acrobatics',
                  'True Woodsman\nAdvantage on Animal Handling or Survival',
                  'True Survivor\nAdvantage on Saving Throw',
                  'Vigorous\nGain +1 to max HP on level up',
                  'Recovery\nRecover up to 3 hit dice',
                  'Not For Thee...\nNegates 1 failed Death Save (self)',
                  'I Know Someone\nImmediately find someone who will assist as much as possible.',
                  'Familiar Place [1]\nYou know the surroundings as though you have a map of it.',
                  'Familiar Place [2]\nYou have a helpful, but questionable contact here.',
                  'Familiar Place [3]\nYou know 1 secret concerning this place.',
                  'Vital Shot\nOn hit, give enemy disadvantage for 1d4 rounds.',
                  'Always Alert\nRoll with Advantage on a Perception or Investigation Check',
                  'Accurate\nGain +2 on Attack Roll',
                  "Well Studied\nGain Advantage on an Arcana or Religion roll",
                  "Slick\nGain Advantage on either a Sleight of Hand or Stealth roll"
                  'Love Interest\nYou become the target NPCs love interest. Draw a card each time they appear and cause trouble',
                  "Beginner's Luck\nAdd Proficiency Bonus to one skill check in which you are not proficient (single use)",
                  'Survivor\nGain +2 on a Save Throw',
                  "Team Leader\nOn a group check only one person needs to succeed",
                  "Supporter [1]\nGrant +2 to an ally's Ability or Attack roll",
                  "Supporter [2]\nAdd your skill bonus to an ally who uses\na skill in which you are at least 'proficient'",
                  "Favor of the Warrior [1]\nGain Advantage for 2 Attacks",
                  "Favor of the Warrior [2]\nTarget ally draws 2 Cards",
                  "Favor of the Warrior [3]\nAdvantage on Athletics",
                  "Favor of Lady Luck [1]\nReroll a Nat 1",
                  "Favor of Lady Luck [2]\nTake 12 instead of rolling",
                  "Favor of Lady Luck [3]\nOne-shot 'Calm Emotions' spell",
                  "You Go First\nYour turn is before initiative formally begins\nCan also be used to place yourself\nat the top of initiative\nbetween rounds of combat",
                  "Instinctive Dodge\nA physical attack automatically fails to hit you.\nRoll with Advantage if the Attack requires a Dex Save.\n(Negates only one part of a multi-attack)",
                  "Advantage\nRoll with Advantage on a Skill, Ability, or Attack Roll",
                  "Silver Tongue\nAdvantage on Deception or Persuasion",
                  'Meanwhile...\nThe DM must play out a scene happening elsewhere\nbetween important campaign characters\n(cannot be used during combat).'

                        ]


              InsButton.place(x=200, y=100)
              InsButton.configure(text=random.choice(INSC))



          InsButton = Button(main, bg='orange', fg='white', font='helvetica 12 bold', command=lambda:InsButton.place_forget())
          







        
          
            
          def DMStuff(x):
              DMInfoFrame.place_forget()
              InfoButton.config(bg="SystemButtonFace", fg='black', font="TkDefaultFont")
              InfoButton.place(x=200, y=100)

              if x == "Conditions":
                  def Cond_Page(x):
                      InfoButton.place_forget()
                      InfoButton.place(x=200, y=100)
                      InfoButton.configure(command=lambda:InfoButton.place_forget())
                      if x == 1:
                          InfoButton.configure(text="Conditions [2/3]:\n\nPARALYZED:\n*Afflicted is Incapacitated;incapable of movement,\nspeech, action, or reaction.\n*Auto-fails Str and Dex saves\n*Attacks against afflicted have Advantage\n*If the attacker is w/in 5', attacks that hit\nthe afflicted are considered Critical.\n\nPETRIFIED:\n*Afflicted, along with nonmagical items worn\n or carried become solid (usually stone)\nWeight increases by a factor of 10. Ceases aging.\n*Incapacitated, unaware of surroundings\n*Attack rolls against afflicted have advantage\n*Autofails Str/Dex saves\n*Resistance to all damage\n*Immune to poisons and diseases.\nAny currently active poisons/diseases are suspended, not neutralized.\n\nPOISONED:\n*Disadvantage on Attack rolls and Ability Checks.\n\nPRONE:\nMovement is restricted to Stand(half movement to end Prone), or Crawl\n*Attack with Disadvantage\n*Enemies attackers w/in 5' attack with Advantage\nOtherwise, attack with Disadvantage.")
                          InfoButton.configure(command=lambda:[Cond_Page(2)])
                      if x == 2:
                          InfoButton.configure(text="Conditions [3/3]:\n\nRESTRAINED:\n*Speed becomes 0; no bonus speed benefits\n*Attacks have Disadvantage; Attacked with Advantage\n*Dex Saves at Disadvantage.\n\nSTUNNED:\nIncapacitated; faltering speech.\n*Autofail Str/Dex Saves\n*Attacked with Advantage.\n\nUNCONSCIOUS:\n*Incapacitated; no speech, no movement, unaware\n*Drops held possessions; falls Prone.\nAutofails Str/Dex saves\n*Attacked with Advantage.\nAttackers w/in 5' that hit land Crits.\n\nEXHAUSTION:\n(Effects are cumulative!)\nLevel 1: Disadvantage on Ability checks\nLevel 2: Speed halved\n3: Disadvantage on Attacks and Saves\n4: Max HP halved\n5:Speed = 0\n6: Death\n\n[Food, drink, and Long Rest reduce a reversible Exhaustion Level by 1] ")




                  InfoButton.configure(text="Conditions [1/3]:\n\nBLIND:\nAuto-fails sight-based ability checks\nAttacks against afflicted have Advantage.\nAfflicted attacks with Disadvantage.\n\nCHARMED:\n*Afflicted cannot target the charmer\nwith harmful abilities, attacks, or spells.\n*Charmer has advantage on any social\nability interaction with the afflicted\n\nDEAFENED:\nAuto-fail any hearing-based ability checks\n\nFRIGHTENED:\nAfflicted has Disadvantage on Ability Checks\nand Attack rolls while source of fear is in line of sight\n*Afflicted cannot willingly move closer to its source of fear.\n\nGRAPPLED:\nSpeed is 0; no bonus speed benefits.\n\nINVISIBLE:\nCannot be seen without magic or Special sense.\nCan be detected by noise or tracks\n*Attacks toward target are at disadvantage.\nAttacks from target are at advantage.")
                  InfoButton.configure(command=lambda:[Cond_Page(1)])

              if x == "Cover":
                  def C_Page(x):
                      if x == 1:
                          InfoButton.configure(text="")

                  InfoButton.configure(text="Cover:\n\nHalf (1/2):\n +2 AC and Dex Saves. Obstacle protects\nat least half of the target's body\nExample: Creatures, narrow tree trunk, low wall\n\nThree-Quarters (3/4):\n+5 AC and Dex Saves\nExamples: Thick tree trunk, arrow slit, portcullis\n\nTotal Cover:\nConcealed completely. Usually vulnerable\nonly to homing-or AoE spells.")

              if x == "CombatActs":
                  def R_Page(x):
                      InfoButton.place_forget()
                      InfoButton.place(x=200, y=100)
                      InfoButton.configure(command=lambda:InfoButton.place_forget())
                      if x == "S":
                          InfoButton.configure(text="")
                      if x == "L":
                          InfoButton.configure(text="")

                  InfoButton.configure(text="Combat Actions:\n\nDASH:\nMake two Movement actions instead of Move+Attack.\nSpeed effectively doubled.\n\nDISENGAGE:\nMovement doesn't provoke Opportunity Attacks for the rest of the turn.\n\nDODGE:\nVisible attackers attack with disadvantage and you Dex Save with Advantage.\n\nHELP:\n*Give Advantage to an ally's ability check (before start of your next turn)\n*Give Advantage to an ally's attack (before start of your next turn; target must be w/in 5' of you)\n\nHIDE:\nMake a Dex(Stealth) check in an attempt to Hide\n\nREADY:\nUse your turn to withhold a specific Reaction to a determined trigger\n(ie, If the goblin approaches teammate X, I will use Magic Missile!)\n\nSEARCH:\nUse your action to make a Wisdom(Perception) check\nor an Intelligence(Investigation) check to find something.\n\nUSE AN OBJECT:\nUse items or interact with objects in the battlefield\nExamples: Open doors, pull levers, Drink a Potion")

              if x == "Rest":
                  

                  InfoButton.configure(text="Rest:\n\nSHORT REST:\nAt least 1 hour of downtime; light activity.\nOne or more Hit Die can be spent. HD+CON = HP restored\n*Monks can regain ki, and Warlocks regain Spell Slots from Short Rests\n*Some Class Abilities replenish with Short Rests\n\nLONG REST:\n8 hours; no more than 2 of which on watch.\n*An hour+ of strenuous activity (ie, adventuring activity) negates rest.\n*Regain all expended Spell Slots and Class Abilities\n*Regain up to Half of max Hit Die.\n*1 Long Rest per 24-hour period.\n*Must have at least 1 HP prior to rest to gain benefit.")
                


          def CommandLine(x):
              ParserBar.delete(0, END)
              
              if x == "Temple":
                  pygame.mixer.music.stop()
                  Page(0)
              if x == "Village":
                  Page(2)
              if x == "Forest0":
                  Page(1)
              if x == "Forest1":
                  Page(4)
              if x == "Forest2":
                  Page(5)
              if x == "GL2":
                  Page("GLUp")
              if x == "GL1":
                  Page("GLDown")
              if x == "MH":
                  Page("MH")
              if x == "Plains1":
                  Page("Plains1")
              if x == "Gate0":
                  Page("Gate0")
              if x == "Manor0":
                  Page("Manor0")

              if x == "Redboar1":
                  Page("Redboar1")

              if x == "Redboar2":
                  Page("Redboar2")

              if x == "ManorInt1-1":
                  Page("ManorInt1-1")


              if x == "ManorInt1-2":
                  Page("ManorInt1-2")

              if x == "ManorInt1-3":
                  Page("ManorInt1-3")

              if x == "ManorInt2-1":
                  Page("ManorInt2-1")

              if x == "Maze1_J":
                  Page("Maze1_J")

              if x == "ManorB1A":
                  Page("ManorB1A")


              #MAZE

              if x == "Maze1-A1":
                  Page("Maze1-A1")

              if x == "Maze1-A2":
                  Page("Maze1-A2")

              if x == "Maze1-A3":
                  Page("Maze1-A3")

              if x == "Maze1-A4":
                  Page("Maze1-A4")

              if x == "Maze1-B2":
                  Page("Maze1-B2")

                  

              

                  


              if x == "Party":
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)
                  playermarker2(PICFrame)

                  

                  

              if x == "ADD":
                  InitiativeTrack(InitiativeInterface)

              if x == "ADD2":
                  InitiativeTrack(InitiativeInterface)
                  InitiativeTrack(InitiativeInterface)

              if x == "ADD4":
                  InitiativeTrack(InitiativeInterface)
                  InitiativeTrack(InitiativeInterface)
                  InitiativeTrack(InitiativeInterface)
                  InitiativeTrack(InitiativeInterface)

              
              if x == "Fog":
                  self.Foggy.place(x=0, y=0)

              if x == "STARSHOT":
                  InfoButton.place(x=600, y=200)
                  InfoButton.config(bg="SystemButtonFace", fg='black', font="TkDefaultFont")
                  InfoButton.config(text="STARSHOT (Lance):\nAttribute Intelligence:10\nSpell:Magic Missile [1d4+1 Force dmg; each (3 darts)]\nCharge:Spell Surge Modifier; Recharge 1/day\nSpell Surge 20:Spell Powerup\nSpell Surge 1:Inert, until full recharge\n\nCarved from a rare dark-blue mineral.\nA small cloud of white sparks\noccasionally orbit the tip.")
          
                  

              if x == "VICTORY":
                  pygame.mixer.music.fadeout(1200), pygame.mixer.music.load(resource_path(("jingle1.mp3"))), pygame.mixer.music.play()
                  InfoButton.place(x=600, y=200)
                  InfoButton.configure(text="VICTORY!", bg='dark blue', fg='white', font='Helvetica 16 bold italic')

              if x == "TARGUS":
                  pygame.mixer.music.fadeout(1200), pygame.mixer.music.load(resource_path(("TargTheme.mp3"))), pygame.mixer.music.play(-1)
                  
              if x == "SIMON":
                  pygame.mixer.music.fadeout(1200), pygame.mixer.music.load(resource_path(("SimonTheme.mp3"))), pygame.mixer.music.play(-1)
            #HINTS AND PROMPTS
              if x == "DMNotes":
                  DMInfoFrame.place(x=200, y=200)

              if x == "SIZE":
                  print(main.geometry())

              if x == "Help":
                  InfoButton.place(x=200, y=100)
                  InfoButton.config(text="Instructions:\n1) Right-click to produce a token.\n2) Right-click on token button\nto enter Marker Commands\n\nParser Commands:\n*COMMANDS--Lists Parser/Token Commands\n\n*MAPS--Lists available maps\n\n*COMBAT--FE Style Combat rules")
              if x == "COMMANDS":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Interface Commands:\nADD2 = Adds 2 initiative slots\nParty = Adds 8 markers\n\nMarker Commands:\n*Cultist *Bugbear *Scout\n*Goblin  *Guard  *Orc\n*Unk? *Flora1 *Itm?\n*Skeleton  *Zombie  *Berserker\n*Hobgoblin *Fire  *V?  \n*Bandit *Temple *Door")

              if x == "COMBAT":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="'Fire Emblem' Style Combat:\nOn Turn\n1)Aggressor turn proceeds as normal [Movement, Action, Bonus Action]\n2)Attacked opponent(s) counter if in range; NO movement\n3) Aggressor finishing touch [usually a single/simple attack]")
              
              if x == "MAPS":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Maps:\nForest0 = Forest Start\nForest1 = Forest Maze\nForest2 = Forest Exit\nGL2 = Goblin's Lace Upstairs\nGL1 = Goblin's Lace Downstairs\nMH = Meadhaven\nGate0 = Derrinsgard Southern Gate\nManor0 = Avernissi Manor (field)\nManorInt1-1 = Manor (Entrance)\nManorInt1-2 = Manor (Hallway)\nManorInt1-3 = Manor (Stairway)\nManorInt2-1 = Manor (2nd Fl. Hall)\nTemple = Temple?\nVillage = Slums\nMaze1-A2 = Maze Start\nPlains1 = Plains[1]")

              if x == "Glassberries":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Glassberries:\nSometimes called 'Waterberries';\nnamed for their clear appearance\n[~1 SP ea]")

              if x == "Thelvenfaas":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Thelvenfaas:\nA vibrant green herb\nA staple ingredient for both\nbeginner and advanced herbalists\n[1 GP ea]")

        
              if x == "Gemmelrut":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Gemmelrut:\nThis wrinkley brown root has a pungent cinnamon-like scent\nA popular additive for tea, baking, and smoking.\nGood for concoctions that specialize in focus and-or relaxation\n[1.25 GP ea]")

              if x == "Kushroom":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Kushroom:\nThese green, white-spotted mushrooms were\nonce rumored to be the secret to ever-lasting life.\nSlowly gaining legality in most kingdoms.\n[value varies]")

              if x == "Fairy's Nettle":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Fairy's Nettle:\nA light green herb whose leaves resemble fairy's wings.\nIts stinging leaves dissolve when boiled. Tea made from the needles is said to be sweet and medicinally potent\n[25 CP ea]")

              if x == "Magemoss":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="Magemoss:\nAlso known as 'Rainbow Moss'.\nComes in various colors, such as purple, blue, and red.\nStudies have yet to confirm if the coloration holds any particular significance.\n[1 SP ea]")

          
              if x == "ManorTrap1":
                  InfoButton.place(x=200, y=200)

              if x == "ManorTrap2":
                  InfoButton.place(x=200, y=200)

              if x == "MMSPE":
                  InfoButton.place(x=200, y=200)
                  Avnotes = ["Janu 6 998  (Entry 1)\nI've infiltrated the Avernissi household as a member of the villa staff.\nThe current majordomo, a Pre-War Battle Golem? It calls itself Ophelia.\n 'She' seems to have taken a suspicious interest in me.\nAt this point, I am uncertain if she is a more than she appears...\na counter-operative to my investigation?\nTwo weeks in and already a chance my efforts may be thwarted...\n        -C.W."] +\
                            ["Marsu 17 998\nThe manor seems unusually busy for no marked reason.\nIncreased activity throughout the night-time hours,\nhowever, no signs of departure from household grounds.\nIt is getting harder for me to move freely in the premises.\nOphelia is always watching.\n   -C.W."] + ["Marsu 28\nCelestials...Dragons...Banners...Thrones...\nAll in pairs. That is a clue.\nThe connection is still a mystery to me...\n    -C.W."] +\
                            ["Febris 21 998\nSignore Avernissi has been throwing a number of lavish parties\nwith a suspicious number of political friends and enemies alike.\nIf I didn't know any better, I believe Ophelia has informed\nhim of her suspicions of me. I must move more carefully."] + ["Abriel 8 998\nA strange young woman visited the villa today.\nI initially thought she may have been\nan ally sent by you. However, she didn't\nseem fluent in any of the agreed upon signs...\n  -C.W."] +\
                            ["Abriel 23 998\nThe Basement! Another Summoning is being prepared there!\n As instructed, I will begin egress procedures and secure records...\n  - C.W."] + ["Marsu 1 998\n↑ → → → ↓ ↓ ← ↓ ←\n ↑ → → → ↓ ↓ ↓\n→ →\n   -C.W."] + ["Febris 9 998\n'May the petition of your prayers be\nsent to the gods below\nto be heard by those on high...'\nA strange inscription I read on the back of\none of the paintings...I think it bears significance.\nDoes it mean anything to you?\n    -C.W."]
                  
                  InfoButton.config(text=random.choice(Avnotes))
                  #Janu Febris Marsu Abriel Makku Jun Jull Aogus Sepda Octuul Nova Decca

              if x == "KWQPB":
                  InfoLabel.place(x=200, y=200)
                  InfoButton.config(text="A list of names [Tablet 1/3]:\n*Horus Audelvance   *Grevor Thisbane\n*Wedna Argolyngxia   *Esda Sarson\n*Eglon Durskhemmer  *Kelvet Harger")
                  InfoLFLBL.config(text="A tablet written in Draconic\nfound in the Avernissi Villa catacombs.\nCan your party read Draconic?")
                
              if x == "HAIMM":
                  InfoLabel.place(x=200, y=200)
                  InfoButton.config(text="A list of names [Tablet 2/3]:\n*Irina Grenram   *Daephnis Laoba\n*Margolia Avernissi   *Andrade Ostegarre\n*Chasity Wellwyrth   *Sanfa Morin")
                  InfoLFLBL.config(text="A tablet written in Elvish\nfound in the Avernissi Villa catacombs.\nCan your party read Elvish?")

              if x == "UIFJI":
                  InfoLabel.place(x=200, y=200)
                  Decline.configure(command=lambda:[InfoLabel.place_forget(), InfoButton.place(x=200, y=200), InfoButton.configure(text="You dumb, illiterate fucks...-_-'")])
                  InfoButton.config(text="A list of names [Tablet 3/3]:\n*Sethren Kole   *Aramil Liadon\n*Myrzarius Toirsteeg   *Ralba Brenshu\n*Rendol Halstion   *Arvold Durer")
                  InfoLFLBL.config(text="A tablet written in Common\nfound in the Avernissi Villa catacombs.\nCan your party read Common?")

              if x == "ALKJA":
                  InfoButton.place(x=200, y=200)
                  InfoButton.config(text="The Boy is extremely exhausted, suffering from LEVEL 3 EXHAUSTION\nHe will not recover until he has had 3 days'worth of\nfood, drink, and rest. Until then, he is a liability to be protected.\nWhile carrying The Boy, movement is reduced by 50%,\nand at least one hand is considered occupied, (negating use of 2-handed weapons)\nIn combat, Actions can be used to pick up, or lower The Boy\nIf The Boy is left unattended by any party members for more than the span\nof two adjacent maps, he is presumed captured and lost.")


          
          InfoButton = Button(main, bg="SystemButtonFace", fg='black', font="TkDefaultFont", command=lambda:InfoButton.place_forget())
          
          InfoLabel = LabelFrame(main)
          InfoLFLBL = Label(InfoLabel)
          InfoLFLBL.pack()
          Confirm = Button(InfoLabel, text="Y", command=lambda:[InfoLabel.place_forget(), InfoButton.place(x=200, y=200)])
          Confirm.pack(side=LEFT)
          Decline = Button(InfoLabel, text="N", command=lambda:InfoLabel.place_forget())
          Decline.pack(side=RIGHT)
          



          

          Maplabel.bind("<Button-3>",(lambda event:playermarker2(PICFrame)))



          DMInfoFrame = LabelFrame(main)
          DMInfoLabel = Label(DMInfoFrame, text="DM Notes")
          DMInfoLabel.pack()

          ConditionsButton = Button(DMInfoFrame, text="Conditions", command=lambda:[DMStuff("Conditions")])
          ConditionsButton.pack(fill=X)

          CombatActionsButton = Button(DMInfoFrame, text="Combat Actions", command=lambda:[DMStuff("CombatActs")])
          CombatActionsButton.pack(fill=X)

          CoverButton = Button(DMInfoFrame, text="Cover Rules", command=lambda:[DMStuff("Cover")])
          CoverButton.pack(fill=X)

          RestingButton = Button(DMInfoFrame, text="Rest", command=lambda:[DMStuff("Rest")])
          RestingButton.pack(fill=X)


          

         
          
#-----------------------------------------------------------------------------------------------------------

         
                  
        #DICEBOX FRAME-----------------------------------------------------------
        
          main.dicepic = PhotoImage(file=(resource_path(("D20.png"))))
          dx = "20"
          dc = "100"



          def dicechoice(dc):
            DiceEntry.configure(state=NORMAL)
            DiceEntry.delete(0, END)

            if dc == "100":
                main.dicepic.configure(file=(resource_path(("D100.png"))))
                CenterButton.configure(command=lambda:[dice("100")])
                RightButton.configure(command=lambda:dicechoice("4"))

            if dc == "4":
                main.dicepic.configure(file=(resource_path(("D4.png"))))
                CenterButton.configure(command=lambda:[dice("4")])
                RightButton.configure(command=lambda:dicechoice("6"))

            if dc == "6":
                main.dicepic.configure(file=(resource_path(("D6.png"))))
                CenterButton.configure(command=lambda:[dice("6")])
                RightButton.configure(command=lambda:[dicechoice("8")])

            if dc == "8":
                main.dicepic.configure(file=(resource_path(("D8.png"))))
                CenterButton.configure(command=lambda:[dice("8")])
                RightButton.configure(command=lambda:dicechoice("10"))

            if dc == "10":
                main.dicepic.configure(file=(resource_path(("D10.png"))))
                CenterButton.configure(command=lambda:dice("10"))
                RightButton.configure(command=lambda:dicechoice("12"))
                
            if dc == "12":
                main.dicepic.configure(file=(resource_path(("D12.png"))))
                CenterButton.configure(command=lambda:dice("12"))
                RightButton.configure(command=lambda:dicechoice("20"))

            if dc == "20":
                main.dicepic.configure(file=(resource_path(("D20.png"))))
                CenterButton.configure(command=lambda:dice("20"))
                RightButton.configure(command=lambda:dicechoice("100"))


            DiceEntry.configure(state=DISABLED)

            
                

          def dice(dx):
            pygame.mixer.find_channel().play(diceroll)
            DiceEntry.configure(state=NORMAL)
            DiceEntry.delete(0, END)
            
            if dx == "4":
                DiceEntry.insert(END, random.randint(1,4))

            if dx == "6":
                DiceEntry.insert(END, random.randint(1,6))

            if dx == "8":
                DiceEntry.insert(END, random.randint(1,8))

            if dx == "10":
                DiceEntry.insert(END, random.randint(1,10))

            if dx == "12":
                DiceEntry.insert(END, random.randint(1,12))
                
            if dx == "20":
                DiceEntry.insert(END, random.randint(1,20))
                
            if dx == "100":
                DiceEntry.insert(END, random.randint(1,100))
                

            DiceEntry.configure(state=DISABLED)

     


        
          ProtoFrame1 = Frame(BottomInterface, bg='blue')
          ProtoFrame1.pack(side=LEFT)

          ProtoFrame2 = Frame(BottomInterface, height=20, width=30, bg='blue')
          ProtoFrame2.pack(side=RIGHT)

          


          

          DiceFrame = Frame(ProtoFrame1)

          DiceLabelFrame = LabelFrame(DiceFrame)


          CenterButton = Button(DiceLabelFrame, image=main.dicepic, command=lambda:dice(dx))
          CenterButton.grid(column=1, row=0)

          DiceEntry = Entry(CenterButton, width=3)
          DiceEntry.place(x=15, y=35)   

          RightButton = Button(DiceLabelFrame, text=">", command=lambda:dicechoice(dc))
          RightButton.grid(column=2, row=0, sticky='news')
          DiceLabelFrame.pack()


           
          DiceFrame.pack(side=RIGHT)

          BottomInterface.pack(side=BOTTOM, fill=BOTH) 



          #----------------------------------------
          #MUSIC CONTROLS
          

          MusicFrame = Frame(ProtoFrame1)

          MusicLF = LabelFrame(MusicFrame)
          MusicLF.pack()
          MapMusic = Button(MusicLF, text="Music", command=lambda:[pygame.mixer.music.load(resource_path((jamz+".mp3"))), pygame.mixer.music.play(-1)])
          MapMusic.pack(fill=X)
          OFFBtn = Button(MusicLF, text="OFF", command=lambda:[pygame.mixer.music.stop()])
          OFFBtn.pack(fill=X)

          
          MusicFrame.pack(side=LEFT)


          #------------------------------------
          #HELP/INSTRUCTIONS

          HelpButton = Button(ProtoFrame1, width=3, text="?", font="Helvetica 22 bold", command=lambda:CommandLine("Help"))
          HelpButton.pack(side=RIGHT, padx=10)

          ParserBar.pack()
          MapsizeLabel.pack()
          TurnLabelFrame.pack()


          DMScreen = Button(ProtoFrame2, text="DM\nNOTES", height=2, font="Helvetica 12 bold", command=lambda:CommandLine("DMNotes"))
          DMScreen.pack(side=LEFT)

          DMTules = Button(ProtoFrame2, text="DM\nTOOLS", height=2, font="Helvetica 12 bold", command=lambda:[DMToolkit.DMTOOLS()])
          DMTules.pack(side=LEFT, padx=10)

          INSP = Button(ProtoFrame2, text="INSPIRATION\nCARDS", height=2, font="Helvetica 12 bold", command=lambda:InsCards())#[DnDTools.Insp()])
          INSP.pack(side=LEFT)
          
          



#----------------------------------------------------------------------------
      #INITIATIVE

          ADDButton = Button(InitiativeInterface, text="ADD", padx=50, command=lambda:InitiativeTrack(InitiativeInterface))
          ADDButton.pack(fill=X)

          
              


   
mainloop()