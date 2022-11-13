import random
from tkinter import*


def DMTOOLS():

    main = Tk()
    main.title("DM Toolkit")
    main.geometry("600x420")


    Infotext = Text(main, height=8, width=70, font="helvetica 8 bold", wrap='word')
    Infotext.pack()

    Frame0 = Frame(main)
    Frame0.pack()

    Frame1 = Frame(main)
    Frame1.pack()

    Frame2 = Frame(main)
    Frame2.pack()

    def spellsurge(x):
        Infotext.delete(1.0, END)

        if x == 0:
            Attribute = ["Intelligence"] + ["Wisdom"] + ["Charisma"]
            SSThresh = [str(random.randint(10,16))]
            element = ["Fire"] + ["Cold"] + ["Electricity"] + ["Poison"] + ["Acid"] + ["Thunder"] + ["Random"] + ["Choice"]
            Spell = ["Magic Missile [1d4+1 Force dmg; each (3 darts)]"] + ["Healing Word [1d4+Spell Surge Mod]"] + ["Sanctuary (Wis DC=SST)"] + ["Ray of Sickness [2d8 poison dmg; CON Save=SST]"] + ["False Life [1d4+4 temp HP]"] + ["Chromatic Orb ("+random.choice(element)+")  [3d8 dmg]"]
            Charges = [str(random.randint(1,4))+" charges; NO RECHARGE"] + [str(random.randint(1,4))+" charges; RECHARGE 1/day"] + ["Spell Surge Modifier; Recharge 1/day"] + ["Spell Surge Modifier; No Recharge"]
            High = ["No Charge Loss"] + ["Free Action"] + ["Spell Powerup"] + ["No Bonus"]
            Low = ["Wild Magic"] + ["Weapon Break"] + ["No Penalty"] + ["Inert, until full recharge"]


            Infotext.insert(END, "Attribute {}:{}\nSpell:{}\nCharge:{}\nSpell Surge 20:{}\nSpell Surge 1:{}".format(random.choice(Attribute), random.choice(SSThresh), random.choice(Spell), random.choice(Charges), random.choice(High), random.choice(Low)))

        if x == 1:
            rolls = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            rolls2 = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            rolls3 = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            rolls4 = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            rolls5 = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            rolls6 = [str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))]
            race =  ["Dragonborn STR+2; CHA+1       SPD: 30ft"] +["Dwarf CON+2     Hill Dwarf WIS+1       SPD: 25ft"] +["Elf DEX+2     High Elf INT+1       SPD: 30ft"] + ["Gnome INT+2     Rock Gnome CON+1       SPD: 25ft"] + ["Half-Elf CHA+2; 2 Abilities +1 EACH       SPD: 30ft"] + ["Half-Orc STR+2; CON+1       SPD: 30ft"] + ["Halfling DEX+2     Lightfoot CHA+1       SPD: 25ft"] + ["Human +1 ALL       SPD: 30ft"] + ["Tiefling INT+1; CHA+2       SPD: 30ft"]
            commonz = ["Fisher"]*2 + ["Forester"] + ["Laborer"]*4 + ["Messenger"]*4 + ["Sailor"] + ["Serf"]*4 + ["Servant"]*2 + ["Shepherd"] + ["Trapper"]
            crime = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler"]
            entertain = ["Actor", "Dancer", "Fire-eater", "Jester", "Juggler", "Instrumentalist", "Poet", "Singer", "Storyteller", "Tumbler"]
            cspick = ["Religion*", "Nature*", "Religion*"]
            fapick = ["Investigation*(The Harpers)", "Religion*(Order of the Gauntlet)", "Nature*(The Emerald Enclave)", "History*(The Lord's Alliance)", "Deception*(Zhentarim)"]
            hpick = ["Arcana*, Investigation*"] + ["Arcana*, Religion*"] + ["Arcana*, Survival*"] + ["Investigation*, Religion*"] + ["Investigation*, Survival*"] + ["Religion*, Survival*"] 
            ubpick = ["Deception*, Insight*"] + ["Deception*, Persuasion*"] + ["Deception*, Stealth*"] + ["Insight*, Persuasion*"] + ["Insight*, Stealth*"] + ["Persuasion*, Stealth*"]
            bground = ["ACOLYTE [Insight, Religion]"] + ["CHARLATAN [Deception, Sleight of Hand]"] + ["CITY WATCH [Athletics, Insight]"] + ["CLAN CRAFTER [History, Insight]"] + ["CLOISTERED SCHOLAR [History, "+random.choice(cspick)+"]"] + ["COURTIER [Insight, Persuasion]"] + ["CRIMINAL("+random.choice(crime)+") [Deception, Stealth]"] + ["ENTERTAINER("+random.choice(entertain)+") [Acrobatics, Performance]"] +\
                ["FACTION AGENT [Insight, "+random.choice(fapick)+"]"] + ["FAR TRAVELER [Insight, Perception]"] + ["FOLK HERO [Animal Handling, Survival]"] + ["GUILD ARTISAN [Insight, Persuasion]"] + ["HAUNTED ONE ["+random.choice(hpick)+"]"] + ["HERMIT [Medicine, Religion]"] + ["NOBLE [History, Persuasion]"] + ["OUTLANDER [Athletics, Survival]"] + ["SAGE [Arcana, History]"] + ["SAILOR [Athletics, Perception]"] +\
                ["SOLDIER [Athletics, Intimidation]"] + ["URBAN BOUNTY HUNTER ["+random.choice(ubpick)+"]"] + ["URCHIN [Sleight of Hand, Stealth]"] 
            

            barbs = ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]

            bahd = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]

            clerk = ["History"] + ["Insight"] + ["Medicine"] + ["Persuasion"] + ["Religion"] 


            drude = ["Arcana"] + ["Animal Handling"] +["Insight"] +["Medicine"] +["Nature"] +["Perception"] +["Religion"] + ["Survival"] 


            fght = ["Acrobatics"] +["Animal Handling"] + ["Athletics"] + ["History"] + ["Insight"] + ["Intimidation"] + ["Perception"] + ["Survival"] 


            mnk = ["Acrobatics"] + ["Athletics"] + ["History"] + ["Insight"] + ["Religion"] + ["Stealth"] 
            
                
            pald = ["Athletics"] +["Insight"] + ["Intimidation"] + ["Medicine"] + ["Persuasion"] + ["Religion"] 
            
            
            rngr = ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survial"]


            rogg = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
            
            

            sorc = ["Arcana"] + ["Deception"] + ["Insight"] + ["Intimidation"] + ["Persuasion"] + ["Religion"]
                

            warl = ["Arcana"] + ["Deception"] + ["History"] + ["Intimidation"] + ["Investigation"] + ["Nature"] + ["Religion"] 

            wiz = ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"] 



            klass = ["BARBARIAN "+str(random.sample(barbs,2))+"; Save Throws: STR, CON\nHP: 12+CON   HitDie:1d12"] + ["BARD "+str(random.sample(bahd,3))+"; Save Throws: DEX, CHA\nHP: 8+CON   HitDie:1d8"] + ["CLERIC "+str(random.sample(clerk,2))+"; Save Throws: WIS, CHA\nHP: 8+CON   HitDie:1d8"] + ["DRUID "+str(random.sample(drude,2))+"; Save Throws: INT, WIS\nHP: 8+CON   HitDie:1d8"] + ["FIGHTER "+str(random.sample(fght,2))+"; Save Throws: STR, CON\nHP: 10+CON   HitDie:1d10"] +\
                    ["MONK "+str(random.sample(mnk,2))+"; Save Throws: STR, DEX\nHP: 8+CON   HitDie:1d8"] +["PALADIN "+str(random.sample(pald,2))+"; Save Throws: WIS, CHA\nHP: 10+CON   HitDie:1d10"]+["RANGER "+str(random.sample(rngr,3))+"; Save Throws: STR, DEX\nHP: 10+CON   HitDie:1d10"] +["ROGUE "+str(random.sample(rogg,4))+"; Save Throws: DEX, INT\nHP: 8+CON   HitDie:1d8"] + ["SORCEROR "+str(random.sample(sorc,2))+"; Save Throws: CON, CHA\nHP: 6+CON   HitDie:1d6"] + ["WARLOCK "+str(random.sample(warl,2))+"; Save Throws: WIS, CHA\nHP: 8+CON   HitDie:1d8"] + ["WIZARD "+str(random.sample(wiz,2))+"; Save Throws: INT, WIS\nHP: 6+CON   HitDie:1d6"] 
            

            Infotext.insert(END, "Roll 1: {}".format(random.choice(rolls))+" "*7+"Roll 2: {}".format(random.choice(rolls2))+" "*7+"Roll 3: {}".format(random.choice(rolls3))+"\nRoll 4: {}".format(random.choice(rolls4))+" "*7+"Roll 5: {}".format(random.choice(rolls5))+" "*7+"Roll 6: {}\nRace: {}".format(random.choice(rolls6), random.choice(race))+"\nBackground: {}".format(random.choice(bground)))
            Infotext.insert(END, "\nClass: {}".format(random.choice(klass)))

        if x == 2:
            Infotext.insert(END, "Spell Surge Tutorial\nTake an action to Spell Surge! Roll d20+mod vs the weapon's Spell Surge Threshold (SST).\n\n*PASS--Weapon is charged. Spell is usable on next turn if Concentration is held.\n(DC = CON 10 or 1/2 dmg; whichever is greater) \n*FAIL--Failed action. No charge consumed.")



    def objects(x):
        Infotext.delete(1.0, END)

        if x == 0: #trinkets
            pass
            trinket = [
                        "A coin from a foreign country",
                        "A tiny bottle of sand",
                        "A pristine chisel",
                        "A padlock. It won’t stay shut.",
                        "An odd compass",
                        "An ornate marble (#"+str(random.randint(1,127))+" of 127)",
                    ]
            adj = ["goofy", "voluptuous", "sexy", "cartoonish", "angry", "energetic", "lithe"]
            race = [' human ', ' elvin ', ' dwarven ', ' gnome ', ' orc ', ' goblin ', ' tiefling ', ' tabaxi ', ' dragonborn ']
            gender = ['man', 'woman']
            trait = [
                    "It's from a legendary lost civilization",
                    "The object has touch-based Mending . The effect ends when contact ends.",
                    "The potent spark of a green flame is trapped inside of it.",
                    "A small illusion of a "+str(random.choice(adj))+str(random.choice(race))+str(random.choice(gender))+" dances on top of it.",
                    "It's magnetically drawn to whatever color is on its holder's mind.",
                    "It's lucky! (Grants one-time use of the Halfling feature 'Luck', then becomes mundane).",
                    ]

            Infotext.insert(END, "TRINKET\n"+random.choice(trinket)+"\n\n(IF MAGICAL)\n"+random.choice(trait))










        if x == 1: #books
            
            titles = [
                "ALL the Ways to Skin a Cat (Vol XVIII)\n(Tabitha Flaye)", 
                "How to Win Fiends and Influence People\n(Devlan D. Skyes)",
                "'What’s In Your Bag of Holding?': How to Be Prepared for ANYTHING'\n(Itol Ismeine)",
                "108 Principles of Elvin Magic\n(I-Liu Xun)",
                "'Goblin Knight Grifflegroff' and Other Songs, Ballads, and Tales\n(Aenslinn Merrin; Foreword by Lukodias Merrin)",
                "Dwarven Remedies for Elvin Maladies\n(Anonymous)",
                "Doppelganger:How to Fake It Til You Make It\n(Dariel Yoo)",
                "Choke-hold!: A Bar-Bearian's Guide to Wrestling Bears....In BARS!\n(Pol Arbier)" ,
                "Speak Loudly and Carry A Big Axe\n(Warren Dyawunse)",
                "The Garden Debunked: Dark Secrets of the Cult of Singularity\n(Bramberly Rosethorn)",
                "'Run This Town Like You Own It!' and Other Halfling Sayings\n(Anonymous)",
                "The Mischievous Merchants of Fenricci' And Other Tales by Laurel N. Connell\n(Transcribed by Ignatius Evermore)",
                "Into the Feywild: The Mysterious Disappearance of the Happy Jackal Expeditionary Group\n(Elizabeth Nimdok)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 2: Combat Habit\n(Joshua Jorgansen)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 1: Specter Ichor\n(Joshua Jorgansen)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 3: Comet Centurions\n(Joshua Jorgansen)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 4: Shattered Quartz\n(Joshua Jorgansen)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 5: Aurem Breeze\n(Joshua Jorgansen)",
                "The Peculiar Happenings of One Twice-Named Joe, Part 6: Boulder Sea\n(Joshua Jorgansen)",
                "Blacksmithing Made Easy\n(Eglon Durskhemmer)",
                "Where the Silver Road Leads\n(Doraelious Terver; foreword by Noelle Elkbright)",
                "Transmutation of the Elvish Soul: A Beginner's Guide to Lunar Alchemy\n(Noelle Elkbright)",
                "The Silver Path: 12 Principles of Lunar Alchemy to Live By\n(Noelle Elkbright)",
                "Terminatur and The Circle of the Green Hand\n(Transcribed by Dorian Lemiuex)",
                "Terminatur and The Fanciful Jewelers\n(Transcribed by Dorian Lemiuex)",
                "The War of Rebirth, The First 10 Years\n(Adrulus Hakes)",
                "The Good Tiefling\n(Samael Pryde)",
                "Glamm-MORE, An Autobiography of Lusteice Glamm\n(edited by Samael Pryde)",
                "The War of Rebirth: A Rodolisian Perspective\n(Ardulus Hakes)",
                "Homesteads & Humans Player's Handbook (3.5 Edition)\n(Draco Flygax)",
                "Across the Winds of Time: Part I of the 'Betrothal' Cycle\n(Elizabeth Nimdok)",
                "A Love Worth Waiting For: Part II of the 'Betrothal' Cycle\n(Elizabeth Nimdok)",
                "A Kiss To the Past: Part III of the 'Betrothal' Cycle\n(Elizabeth Nimdok)",
                "A Kiss To the Past 2: A Rose for the Future; A 'Betrothal Cycle' Side-Story\n(Elizabeth Nimdok)",
                "'I Got DANCE In My Pants!' The Slightly Embellished Autobiography of Pol Adbul The Bard"
            ]

            Infotext.insert(END, random.choice(titles))



        if x == 2: #wildmagic
            changes = ["increases", "decreases"]
            card = [
                'Roll on this table at the start of each of your turns for the next minute (10 combat rounds). Ignore this result on subsequent rerolls.', 
                'For the next minute, you can see any invisible creature if you have line of sight on it.', 
                'A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you, then disappears one minute later.', 
                'You cast Fireball as a 3rd-level spell centered on yourself.', 
                'You cast Magic Missile as a 5th-level spell.',
                'Your height '+random.choice(changes)+' by '+str(random.randint(1,10))+' inches.',
                'You cast Confusion centered on yourself.',
                'For the next minute, you regain 5 hitpoints at the start of each of your turns',
                'You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode from off your face.',
                'You cast Grease centered on yourself.',
                'Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw.',
                'Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.',
                'An eye appears on your forehead for the next minute. During that time, you have advantage on sight-reliant Wisdom(Perception) checks.',
                'For the next minute, all your spells with a casting time of 1 action have a casting time of 1 bonus action.',
                'You teleport up to 60 feet to an unoccupied space of choice that you can see.',
                'You are transported to the Astral Plane until the end of your next turn. You then return to the space you previously occupied or the nearest unoccupied space if that space is occupied.',
                'Maximize the damage of the next damaging spell you cast within the next minute.',
                'Your age '+random.choice(changes)+' by '+str(random.randint(1,10))+' year(s).',
                str(random.randint(1,6))+' flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened by you. They vanish after 1 minute.',
                'You regain '+str(random.randint(2,20))+'HP.',
                'You turn into a potted plant until the start of your next turn. In plant form, you are incapacitated and have vulnerability to all damage. At 0HP, your pot breaks and your form reverts.',
                'For the next minute, you can teleport up to 20ft as a bonus action on each of your turns.',
                'You cast Levitate on yourself.',
                'A DM-controlled unicorn appears in a space within 5ft of you, then disappears 1 minute later.',
                "You can't speak for the next minute. Whenever you try, pink bubbles float from your mouth.",
                'A spectral shield hovers before you for the next minute.\n(+2 AC and immunity to Magic Missile)',
                'For the next '+str(random.randint(5,30))+' days, you are immune to intoxication via alcohol.',
                'Your hair falls out. It grows back within 24 hours.',
                "For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flame.",
                'You regain your lowest-level expended spell slot.',
                'For the next minute you must shout when you speak.',
                'You cast Fog Cloud centered on yourself.',
                'Up to three creatures you choose within 30ft of you take '+str(random.randint(4,40))+' lightning dmg.',
                'You are frightened by the nearest creature until the end of your turn.',
                'Each creature within 30ft of you is invisible for the next minute. The invisibility ends on a creature when it attacks or casts a spell.',
                'You are resistant to all damage for the next minute.',
                'A random creature within 60ft of you becomes poisoned for '+str(random.randint(1,4))+' hours.',
                'You glow with bright light in a 30ft radius for the next minute. Any creature that ends its turn within 5ft of you is blinded until the end of its next turn.',
                "You cast Polymorph on yourself. If you fail the saving throw, you become a sheep for the spell's duration.",
                'Illusory butterflies and flower petals flutter in the air within 10ft of you for the next minute.',
                'You can take one additional action immediately.',
                'Each creature within 30ft of you takes '+str(random.randint(1,10))+' necrotic dmg. You regain HP equal to the sum of necrotic dmg dealt.',
                'You cast Mirror Image.',
                'You cast Fly on a random creature within 60ft of you.',
                "You become invisible for the next minute. During that time, other creatures can't hear you.\nThe invisibility ends if you attack or cast a spell.",
                "If you die within the next minute, you immediately ressurect as though by the Reincarnate spell.",
                "Your size increases by one category for the next minute.",
                "You and all creatures within 30ft of you gain vulnerability to piercing dmg for the next minute.",
                "You are surrounded by faint ethereal music for the next minute.",
                "You regain all expended sorcery points."


            ]


            Infotext.insert(END, random.choice(card))

    def fortune(x):
        Infotext.delete(1.0, END)

        if x == 0:
        
            Fortune = [
                "cover...purpose...spendid...rainy...marble",
                "profuse...water...question...sag...bread",
                "swot...seed...common...run...insult",
                "friend...pollute...crime...offer...offer",
                "lively...cloistered...roof...disgusted...oranges",
                "sally...fish...erratic...tie...branch",
                "battle...moo...unbecoming...bereave...chivalrous",
                "you...pain...real...begins...connection",
                
            ]

            Infotext.insert(END, random.choice(Fortune))

        if x == 1:
            Magic8Ball = [
                "As I see it, yes",
                "Ask again later",
                "Better not tell you now...",
                "Cannot predict now",
                "Concentrate, and ask again",
                "Don't count on it",
                "It is certain",
                "It is decidedly so",
                "Most likely",
                "My reply is 'no'",
                "My sources say 'no'",
                "Outlook not so good",
                "Outlook good",
                "Reply hazy, try again",
                "Signs point to yes",
                "Very doubtful",
                "Without a doubt",
                "Yes",
                "Yes-definitely",
                "You may rely on it"
            ]

            Infotext.insert(END, random.choice(Magic8Ball))

        if x == 2:
            Fortunehints =[
                "The eyes of the gods are all around you...\n(Cult of Ulm spies)",
                "Mind your diet...\n(Henry Cooper/FARM)",
                "New faces bear ancient wounds...\n(Persephone)",
                "Culture speaks from the past to the present...\n[Bahimbo]",
                "A half-burned bridge doubles apprehension for all who depend upon it...\n[Margaret/Ulga]",
                "Loyalties spread wide is fealty thinly given...[Caramil]",
                "Ask for a reward and a meager one will be given. Ask for no reward and...",
                "Your true self is the key.",
                "A friend of a friend may lend a friendly hand",
                "Aid from a place loathed may bring results favored.",
                "Think three times before your next plan",
                "Dig deep. Strength from within is very powerful today!",
                "It takes many to build a fortress; and many more to keep it.",
                "Remember your prayers and your oaths",
                "Decide wisely before breaking promises. Decide wisely before cementing them as well",
                "What you seek may not be what you need...",
                "Magic brings problems; magic brings solutions.",
                "If you are lost, retrace your steps.",
                "A new friend may bring new perspective",
                "Beware of children..."

            ]

            Infotext.insert(END, random.choice(Fortunehints))

    def dungeon(x):
        Infotext.delete(1.0, END)

        if x == 'boss':
            superboss = ["ogre zombie"] + ["Nightmare"] + ["bearded devil"] + ["black pudding"] + ["minotaur skeleton"] + ["hellhound"]
            finalboss = ["a group of "+str(random.randint(3,5))+" cultists attempting to summon a "+random.choice(superboss)+" .\nThe ritual will complete if not stopped in "+str(random.randint(2,8))+" rounds."] + ["a manticore"] + ["a mad wizard"]
            minions = ["cultists x"+str(random.randint(2,4))] + ["goblins x"+str(random.randint(2,4))] + ["kobolds x"+str(random.randint(2,4))] + ["zombies x"+str(random.randint(2,4))] + ["skeletons x"+str(random.randint(2,4))] + ["bandits x"+str(random.randint(2,4))] + ["none"]
            gimmick = ["None"] + ["The room is riddled with traps. After movement, each creature must pass a Dex Check of 10+1d6.\nFailure inflicts 1d6 trap dmg (any type) and ends the creature's turn."] + ["An object granting its holder a beneficial effect is in the center of the room."] + ["Damaging the minions heals the Boss."]
            

            Infotext.insert(END, "Boss: {}\nMinions: {}\n\nGimmick: {}".format(random.choice(finalboss), random.choice(minions), random.choice(gimmick)))

        if x == 'stairs':
            stairtype = ["spirals"]*2 + ["opens to a shaft "]*2 + ["opens to a shaft with an elevator "]
            direction = ["up"]*5 + ["down"]*13
            lvls = [" one level"]*9 + [" two levels"]*3 + [" three levels"]*2
            where = [" passage 20ft long [PASSAGE]"]*6 + [' chamber [CHAMBER]']*5 + [" dead end"]*2
            

            Infotext.insert(END, "This stairway "+random.choice(stairtype)+" "+random.choice(direction)+random.choice(lvls)+" to a"+random.choice(where))
                


        if x == 1:
            Lobby = [
                "Square 20x20ft; passage on each wall",
                "Square 20x20ft; door on 2 walls, passage on third",
                "Square 40x40ft; doors on 3 walls",
                "Rectangle 80x20ft; a row of pillars down the middle; two passages leading from each long wall; doors on each short wall",
                "Rectangle 20x40ft; passage on each wall",
                "Circle; 40ft diameter; one passage at each cardinal direction",
                "Circle; 40ft diameter; one passage at each cardinal direction; well in the middle of the room (may lead to a lower level)",
                "Square 20x20ft; door on two walls; passage on third wall; secret door on 4th wall",
                "Passage 10ft wide; T-intersection",
                "Passage 10ft wide; 4-way intersection"
                ]

            Infotext.insert(END, random.choice(Lobby))
        
        if x == 2:
            feature = ["with a double row of pillars", "with a row of pillars down the middle", "20ft high, gallery 10ft above floor, allows access to level above", "20ft high"]
            Pwidth = ["A 5ft wide passage"]*2 + ["A 10ft wide passage"]*5 + ["A 20ft wide passage"]*2 + ["A 30ft wide passage"]*2 + ["A 40ft wide passage; "+random.choice(feature)]
            yesno = ["Yes"]*1 + ["No"]*9
            direction = ["left", "right"]
            Passage = ["Continue straight 30ft; no doors or side passages"]*2 + ["Continue straight 30ft; door to the "+random.choice(direction)+", then continue for another 10 ft"] + ["Continue straight 20ft; passage ends at a door"] + ["Continue straight 20ft; side passage to the "+random.choice(direction)+" then an additional 10ft ahead"]*4 \
                + ["Continue straight 20ft, comes to a dead end\nSecret Door: "+random.choice(yesno)] + ["Continue straight 20ft then the passage turns "+random.choice(direction)+", and continues 10ft"]*4 + ["Chamber (click Chamber button)"]*5 + ["Stairs (click Stairs button)"]

            Infotext.insert(END, random.choice(Pwidth)+"\n"+random.choice(Passage))

        if x == 3:
            doortype = ["A wooden door"]*10 + ["A wooden door (barred/locked)"]*2 + ["A stone door"] + ["A stone door (barred/locked)"] + ["An iron door"] + ["An iron door(barred/locked)"] + ["A secret door"] + ["A secret door (barred/locked)"] + ["A portcullis"] + ["A portcullis (locked in place)"]
            beyonddoor = ["passage extending 10ft, then T intersection extending 10ft to the left and right"]*2 + ["passage 20ft straight ahead"]*6 +["chamber  (click Chamber)"]*10 + ["set of stairs (click Stairs)"] + ["false door (trapped!)"]

            Infotext.insert(END, random.choice(doortype)+" leads to a\n"+random.choice(beyonddoor))

        if x == 4:
            normalchamber = ["0"]*5 + ["1"]*6 +["2"]*4 + ["3"]*3 +["4"]*2
            largechamber =  ["0"]*3 + ["1"]*5 +["2"]*5 + ["3"]*4 +["4"]*1 + ["5"]*1 +["6"]*1
            chambertype = ["Chamber: Square, 20x20ft\nExits: "+random.choice(normalchamber)]*2 + ["Chamber: Square, 30x30ft\nExits: "+random.choice(normalchamber)]*2 + ["Chamber: Square, 40x40ft\nExits: "+random.choice(normalchamber)]*2 + ["Chamber: Rectangle, 20x30ft\nExits: "+random.choice(normalchamber)]*2 + ["Chamber: Rectangle, 30x40ft\nExits: "+random.choice(normalchamber)]*3 + ["Chamber: Rectangle, 40x50ft\nExits: "+random.choice(normalchamber)]*2 + ["Chamber: Rectangle, 50x80ft\nExits: "+random.choice(largechamber)] + ["Chamber: Circle, 30ft diameter\nExits: "+random.choice(largechamber)] + ["Chamber: Circle, 50ft diameter\nExits: "+random.choice(normalchamber)] + ["Chamber: Octagon 40x40ft\nExits: "+random.choice(largechamber)] + ["Chamber: Octagon 60x60ft\nExits: "+random.choice(largechamber)] + ["Chamber: Trapezoid, ~40x60ft\nExits: "+random.choice(largechamber)]

            Infotext.insert(END, random.choice(chambertype))

        if x == 5:
            Trap = ["Fire: "+str(random.randint(1,6))+" dmg"] + ["Fire: "+str(random.randint(2,12))+" dmg"] + ["Acid: "+str(random.randint(1,6))+" dmg"] + ["Acid: "+str(random.randint(2,12))+" dmg"] + ["Poison: "+str(random.randint(1,6))+" dmg"] + ["Poison: "+str(random.randint(2,12))+" dmg"] + ["Explosion: "+str(random.randint(1,6))+" dmg"] + ["Explosion: "+str(random.randint(2,12))+" dmg"] 
            Puzzleprize = ["Progress"] + ["Lore"] + ["Trap evaded"] + ["Magic Item"] + ["Item"] + ["Gold x"+str(random.randint(6,36))]
            Enemies = ["Guards x"+str(random.randint(1,4))] + ["Guards x"+str(random.randint(2,8))] + ["Cultist(s) x"+str(random.randint(1,4))] + ["Cultists x"+str(random.randint(2,8))] + ["Goblins(s) x"+str(random.randint(1,4))] + ["Goblins x"+str(random.randint(2,8))]
            Treasure1 = ["Gold x"+str(random.randint(1,6))] + ["Gold x"+str(random.randint(2,12))] + ["Item"] + ["Minor magic item"] + ["Contents damaged"]
            Treasure = ["Gold x"+str(random.randint(1,6))] + ["Gold x"+str(random.randint(2,12))] + ["Item"] + ["Chest (TRAPPED!) Investigation:"+str(random.randint(10,15))+"\n\n"+ random.choice(Trap)+"\n\n"+random.choice(Treasure1) ] + ["Minor magic item"] + ["Monster: Mimic!"]
            NPC1 = ["useful"] + ["useless"]
            NPC2 = ["injured"] + ['dead'] + ["unharmed"] + ['hostile']
        

            a = random.randint(1,6)

            if a == 1:     
                Infotext.insert(END, "Encounter: "+random.choice(Enemies))

            if a == 2:
                Infotext.insert(END, "You found:\n"+random.choice(Treasure))

            if a == 3:
                Infotext.insert(END, "You find a figure in the room:\n"+random.choice(NPC1)+" "+random.choice(NPC2))

            if a == 4:
                Infotext.insert(END, "TRAP!\nPerception(Perc):{}\nEvasion (Dex Save):{}".format(str(random.randint(10,15)), str(random.randint(10,15)))+"\n\nFailing Perception yields rolling Evasion w/disadvantage.\n\n"+random.choice(Trap))

            if a == 5: 
                Infotext.insert(END, "Puzzle Reward:\n"+random.choice(Puzzleprize))

            if a == 6:
                Infotext.insert(END, "The area seems empty...a little too empty...")


    def city(x):
        Infotext.delete(1.0, END)

        if x == 1:
            race = ["human", "elf", "half-elf", "half-orc", "goblin", "hobgoblin", "tiefling", "dragonborn ("+random.choice(["black", "blue", "brass", "bronze", "copper", "gold", "green", "red", "silver", "white"])+")", "dwarf", "gnome", "halfling", "human", "human", "drow"]
            nameparts1 =["Jer", "Sar", "Ter", "Jep",  "Li", "Kor", "Az", "Myr", "Ad", "Nal", "Nor",  "Ez", "Mil", "Har", "Ru", "Bar", "Jul", "Dro", "Ao", "Zor", "Ban", "Ben", "Cal", "Da", "Tre", "Jar", "Char", "Dol", "Mul", "Yu", "A", "Ste", "Holm", "Raol", "Gen", "Por", "Al", "Sha", "Shal", "Shae", "Hyu", "Ral", "Ki", "Quen", "Kai", "Dae", "San", "Quan", "Dolo", "Vas", "Sea", "Bor", "Sier", "Wil", "Ther", "Dun", "Hu", "Ei", "Uth", "Wed", "Eu", "Lei", "Esa", "If", "Ippo", "Mar", "Ren", "Her", "Ro", "Zo", "Lu", "Dar", "Pa", "Pe", "Go", "Wes", "Lao", "Ten", "Moi", "Bren"] #80
            nameparts2 =["ah", "ry", "en", "dis", "ovis", "ben", "ul", "io", "am", "ric", "ol", "rah", "da", "ba", "than", "ly", "ia", "vi", "jin", "don", "phen", "sey", "", "mion", 'fus', "vor", "les", "vis", "dren", "o", "ai", "ese", "yn", "vnor", "bor", "aba", "dur", "trid", "hanna", "ina", "pa", "fa", "bediah", "ediah", "dekai", "ph", "vand", "van", "phnis", "dra", "doro", "oleth", "ti", "mus", "ias", "re", "liam", "ey", "al", "na", "ni", "mmri", "alna", "ro", "ghla", "esh", "son", "bert", "an", "zo", "hn", "ke", "on", "tra", "ris", "ter", "zarus", "shu", "rah", "za" ] #80
            names = [random.choice(nameparts1)+random.choice(nameparts2)]
            
            surname = ["Essandoh", "Cerisa", "Idanys", "Nakil", "Werik", "Eula", "Airyn", "Gashabe", "Tierney", "Milosi", "Inavyce", "Sancha", "Selwyn", "Rosael", "Gashabe", "Taiya", "Dorfmida", "Yalyn", "Taureana", "Turhan", "Lakiva", "Inyanga", "Lis", "Luz", "Nilda", "Meeno", "Yeralis", "Hyuliya", "Jasiel", "Feika", "Otani", "Melita", "Mila", "Elchin", "Zerie", "Mirielle", "Yevgeniya", "Bandra", "Sullock", "Xiomara", "Nyoka", "Seweryn", "Damaris", "Plaxedes"] 

            Infotext.insert(END, random.choice(names)+" "+random.choice(surname)+"\n"+random.choice(race))

        if x == 2:
            condition = ['run-down [2]'] + ['remodeled [5]'] + ['fairly new-looking [6]'] + ['well-maintained [3]'] + ['in shambles [1]'] +['better than average [4]']
            location = [
                "A temple",
                "A shrine",
                "A Cathedral",
                "A soothsayer's home",
                "A bar",
                "A theater",
                "A tavern",
                "A park",
                "An arena",
                "A brothel",
                "A wise elder",
                "A townhall",
                "A tea/coffee shop",
                "A citywatch post",
                "A barracks\n(benign; the people generally appreciate the military presence)",
                "A barracks\n(maligned; the people generally disdain the military presence)",
                "A martial arts school (monk)",
                "A marketplace",
                "A school",
                "An ironworks",
                "A general store",
                "A magic store",
                "A common store",
                "A painter's guildhall",
                "A sculptor's guildhall",
                "An illusionists guildhall", 
                "A writer's guildhall",
                "A singer's guildhall",
                "An apothecary",
                "A leather tannery",
                "A flour mill",
                "A fishery",
                "A winery",
                "A brick factory",
                "A bakery"


            ]

            Infotext.insert(END, random.choice(location))
            Infotext.insert(END, "\n\nCondition (relative to the area):\n"+random.choice(condition))

        if x == 3:
            strongrumor = ["People are going missing, yet chickens are abundant..."] + ["A legendary party of heroes once thought dead is still alive! And they're somewhere in Derrinsgard!"] +["There's a man who can turn into a chicken. And he fights for justice from the shadows!"] +["A band of partisans is planning an anti-Rodolisian coup!"] + ["There's a subterranean city beneath Derrinsgard!"]
            weakrumor = ["A local tavern uses human breastmilk to make their cheese"] + ["There's a bar ran by a succubus that takes men's seed while they sleep!"] +["The 'Dick Rippers' aren't real. It was just the workings of a hungry bear!"] +["Random wizard gossip..."] +["Random commoner gossip..."]
            gods = ["Parthuul\n*Largest denomination, *water, creation, life, magic, mysteries\nfavors dragonborn", "Ulm\n*Unity, resolution, finality\nfavors humans", "Aedor\n3rd Largest *earth *Resolve, Perseverence, Heartiness\ndwarves", "Ismultaar\nFire *combat, passion, aggression, destructive half of creation; goblinoids, orcs, soldiers", "Heth\nWind, *Luck, serendipity, intuition; Elves"]
            childreason = ["It's a ruse to corner the heroes into an alley (attacked by 1d6 commoners)"] + ["Child lost their parents"] +["Child is hunger and doesn't have money for food"] + ["Child is scamming the party for money/food...may or may not genuinely need it!"]
            game = ["Shells", "Woodelf Ceelo"]
            reason = ["She caught him looking at another woman"] + ["He was out late drinking with the lads"] + ["He lost too much money gambling"] +["He didn't come home last night"] + ["He said something embarassing about her."] +["He confessed he was already married!"]
            songtype = ["jaunty", "dreary", "romantic", "upbeat", "motivating", "soothing"]
            race = ["human", "elf", "half-elf", "half-orc", "goblin", "hobgoblin", "tiefling", "dragonborn", "dwarf", "gnome", "halfling"]
            gender = ["male", "female"]
            adj = ["very attractive", "moderately attractive", "attractive", "plain", "unfortunate-looking", "hideous"]
            yell = ["the Dragonborn Millenium being nigh"] + ["Tolmik needing to get over the war"] + ["Rodolisian overlords"] + ["the injustice of Tolmician blood being spilt to fight Rodolisian wars"] + ["the forthcoming of Ulm the Unborn, God-being of Singularity"] + ["the Champion of Ulm is among us!"] + ["the prophecies of Madam Wyvern"]
            CE = [
                "You see guards chasing a child for petty theft",
                "A group of young artists are performing outside a tavern",
                "Children are watching as a young wizard entertains them with cantrips",
                "You hear someone on a street corner yelling about "+random.choice(yell),
                "A nearby bard ("+random.choice(adj)+" "+random.choice(race)+" "+random.choice(gender)+") sings and plays a "+random.choice(songtype)+" tune while making a point of having strong eye contact with you.",
                "A young magician is struggling to maintain control of a large stack of books and scrolls as he runs down the street",
                "A bickering couple walks by; Perception Check("+str(random.randint(10,16))+"):\n"+random.choice(reason),
                "An old woman is gambling on a street corner. Her game of choice:"+random.choice(game),
                "A booth is set up with children gathered around. They're watching a puppet show.",
                "A young child recognizes the adventurers and begs for their autographs. They are disappointed to find they are not the adventurers they originally thought.",
                "A child is crying\n"+random.choice(childreason),
                "Guards stop the party. Search them to see if they match the wanted poster in their hands",
                "A swarm of rats runs across the street",
                "A row of "+str(random.randint(3,7))+" lepers plead for alms",
                "Two muscular men wrestle in a square while onlookers place bets.",
                "A man pulls a cart filled with fresh fish. He offers you a bargain to buy the lot.",
                "A maddened horse plunges into a screaming crowd, hooves flailing",
                "A vendor offers delicious skewers of meat and vegetables",
                "A sad-looking maiden sells flowers for a pittance.",
                "A solitary soldier leans drunkently against a wall, his/her helmet slipping down over their eyes.",
                "A tall old woman attempts to sell you her slave, a "+random.choice(race)+" young man with one arm. ",
                "The players notice a new shop or location",
                "A turbaned man charms snakes from a basket with his flute",
                "A young couple dances shamelessly to music only they seem to be able to hear",
                "City guards are laughing and playing games with local children.",
                "A chicken lands nearby. It was thrown out of a window from above",
                "You overhear a religious debate about the god/goddess "+random.choice(gods),
                "A band of thugs make menacing eye contact with you. One of them bites his thumb (at you)...",
                "The party sees a stranger clad in white with a red mohawk. He hoods himself as though he sees you take notice of him...(Henry)",
                "A young woman in tattered armor sits despondently in the shadows of a nearby alley. (Klaura)",
                "You witness a "+random.choice(race)+" gang fight about to commence...",
                "You see an attractive "+random.choice(race)+" man sunbathing on a nearby roof. He winks once he sees he has your attention",
                "You see an attractive "+random.choice(race)+" woman sunbathing on a nearby roof. She winks once she sees she has your attention",
                "You overhear a rumor Perception("+str(random.randint(5,20))+")\nPASS: "+random.choice(strongrumor)+"\nFAIL: "+random.choice(weakrumor)


            ]
            Infotext.insert(END, random.choice(CE))


    #PERSON GENERATOR

    def peeps(x):
        Infotext.delete(1.0, END)

        if x == "P":
            Infotext.insert(END, "The Person Generator generates a physical description for generic NPCs. Users are encouraged to take the generated result at face value. Adjust outcomes to taste/preference/racial traits as applicable.")

        if x == "M":
            color = ["Blonde", "Red", "Brown", "Black", "White"]*3 + ["Unconventional"]
            length = ["Very short", "Short", "Medium", "Long-ish", "Long", "Very Long"]
            texture = ["Straight", "Wavy", "Curly"]

            ecolor = ["Hair Match", "Brown", "Blue", "Green", "Gray", "Hazel", "Unconventional"]
            express = ["Happy", "Sad", "Brooding", "Vacant", "Angry", "Stern", "Starry", "Distant", "[nondescript]"]

            height = ["Short"] + ["Middling"]*3 + ["Tall"]*2 
            bod = ["Endomorph (fat, muscle)"] + ["Mesomorph (solid, strong)"] + ["Ectomorph (long, lean)"]
            bild = ["Underweight"] + ["Lean"] + ["Average"]*3 + ["Athletic"]*2 + ["Full-figured"] + ["Overweight"]

            skin = ["sickly pale"] + ["fair"] + ["olive-brown"] + ["tanned"] + ["bronzed"] + ["dark"]

            adjz = ["sinister"] + ["welcoming"] + ["roguish"] + ["charming"] + ["mischievous"]
            markz = ["faint, subtle"]*3 + ["deep, overt"] 
            #lipz = ["full"] + ["pouty"] + ["thin"] 
            face = ["Smile ({})".format(random.choice(adjz))] + ["Facial mark/scar ({})".format(random.choice(markz))] + ["Eyes"]#+ ["Particularly {} lips".format(random.choice(lipz))]
                

            Infotext.insert(END, "HAIR-- {},  {},  {}\n".format(random.choice(color), random.choice(length), random.choice(texture)))
            Infotext.insert(END, "EYES-- {},  {}\n".format(random.choice(ecolor), random.choice(express)))
            Infotext.insert(END, "BODY-- Stature: {}  Structure: {}  Build: {}\n".format(random.choice(height), random.choice(bod), random.choice(bild)))
            
            Infotext.insert(END, "COMPLEXION-- {}\n".format(random.choice(skin)))
            Infotext.insert(END, "STRIKING FEATURE-- {}".format(random.choice(face)))
            


    def settlement(x):
        BigTown = random.randint(0,1)
        Infotext.delete(1.0, END)
        TownPrefix = ["New ", "Old ", "East ", "West ", "South ", "North ", "Little "] + [" "]*14
        nameparts1 =["Jer", "Sar", "Ter", "Jep",  "Li", "Kor", "Az", "Myr", "Ad", "Nal", "Nor",  "Ez", "Mil", "Har", "Ru", "Bar", "Jul", "Dro", "Ao", "Zor", "Ban", "Ben", "Cal", "Da", "Tre", "Jar", "Char", "Dol", "Mul", "Yu", "A", "Ste", "Holm", "Raol", "Gen", "Por", "Al", "Sha", "Shal", "Shae", "Hyu", "Ral", "Ki", "Quen", "Kai", "Dae", "San", "Quan", "Dolo", "Vas", "Sea", "Bor", "Sier", "Wil", "Ther", "Dun", "Hu", "Ei", "Uth", "Wed", "Eu", "Lei", "Esa", "If", "Ippo", "Mar", "Ren", "Her", "Ro", "Zo", "Lu", "Dar", "Pa", "Pe", "Go", "Wes", "Lao", "Ten", "Moi", "Bren"] #80
        nameparts2 =["ah", "ry", "en", "dis", "ovis", "ben", "ul", "io", "am", "ric", "ol", "rah", "da", "ba", "than", "ly", "ia", "vi", "jin", "don", "phen", "sey", "", "mion", 'fus', "vor", "les", "vis", "dren", "o", "ai", "ese", "yn", "vnor", "bor", "aba", "dur", "trid", "hanna", "ina", "pa", "fa", "bediah", "ediah", "dekai", "ph", "vand", "van", "phnis", "dra", "doro", "oleth", "ti", "mus", "ias", "re", "liam", "ey", "al", "na", "ni", "mmri", "alna", "ro", "ghla", "esh", "son", "bert", "an", "zo", "hn", "ke", "on", "tra", "ris", "ter", "zarus", "shu", "rah", "za" ] #80
        names = [random.choice(nameparts1)+random.choice(nameparts2)]
        TownSuffix = ["ton", "ville", "town", "ford", "fort", "land", "shire", "borough", "", ""]

        Full_Town = [random.choice(TownPrefix)+random.choice(nameparts1)+random.choice(nameparts2)+random.choice(TownSuffix)]
            
        Leadership = ["Governor/Mayor", "Council (elders)", "Council (laborers)", "Guildmaster", "Judge/Magistrate", "Sheriff/Constable"]*4 + ["Syndicate", "Anarchy", "Cabal", "Junta"] + ["Council (oligarchy)"]*2
        L_Style = ["Contested", "Fair", "Illegitimate", "Lout", "Puppet", "Draconian", "Tyrannical", "Weak"]
        racial_demographics = ["Human"] + ["Elf"] + ["Dwarf"] + ["Halfling"] + ["Half-elf"] +["Tiefling"] + ["Dragonborn"]

        if x == 0:
            
            Infotext.insert(END, "The Settlement generator creates a town based on size, population, number of points of interest, and other factors worth consideration.")

        if x == 1: #Thorp
            
            Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(20,80))+" (Thorp)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,3))+"\nPOINTS OF INTEREST: "+str(4)+"\nAUTHORITY: "+random.choice(Leadership))

        if x == 2:#Hamlet

            Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(81,400))+" (Hamlet)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,3))+"\nPOINTS OF INTEREST: "+str(random.randint(0,2)+4)+"\nAUTHORITY: "+random.choice(Leadership))
            
        if x == 3:#Village
            Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(401,900))+" (Village)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,4))+"\nPOINTS OF INTEREST: "+str(random.randint(2,4)+4)+"\nAUTHORITY: "+random.choice(Leadership))
            
            

        if x == 4:#TOWN
            
            if BigTown == 0:#SMALL
                Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(901,2000))+" (Small Town)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,5))+"\nPOINTS OF INTEREST: "+str(random.randint(4,6)+4)+"\nAUTHORITY: "+random.choice(Leadership))
            
            if BigTown == 1:#LARGE
                Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(2001,5000))+" (Large Town)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,5))+"\nPOINTS OF INTEREST: "+str(random.randint(5,6)+4)+"\nAUTHORITY: "+random.choice(Leadership))
            
            

        if x == 5:#City
            if BigTown == 0:#SMALL
                Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(5001,12000))+" (Small City)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,6))+"\nPOINTS OF INTEREST: "+str(random.randint(6,8)+4)+ " "*9+"DISTRICTS: "+str(random.randint(2,3))+"\nAUTHORITY: "+random.choice(Leadership))
            
            if BigTown == 1:#LARGE
                Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(12001,25000))+" (Large City)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,6))+"\nPOINTS OF INTEREST: "+str(random.randint(7,8)+4)+ " "*9+"DISTRICTS: "+str(random.randint(2,3))+"\nAUTHORITY: "+random.choice(Leadership))
            

        if x == 6:#METROPOLIS
            Infotext.insert(END, "TOWN NAME: "+random.choice(Full_Town)+"    POPULATION: "+str(random.randint(25001,60000))+" (Metropolis)\nDEMOGRAPHIC: "+str(random.sample(racial_demographics,7))+"\nPOINTS OF INTEREST: "+str(random.randint(8,12)+4)+ " "*9+"DISTRICTS: "+str(random.randint(4,6))+"\nAUTHORITY: "+random.choice(Leadership))
            
            

    def tavern(x):
        Infotext.delete(1.0, END)
        
        if x == 0:#Tavern Name
            
            #Bar Name
            adj = ['Absent-minded', 'Ale-soused', 'Bloated', 'Belly-Laughing', 'Curmudgeonly', 'Cankered', 'Drooping', 'Dancing', 'Elated', 'Effervescent', 'Fanciful', 'Foppish', 'Galloping', 'Golden', 'Half-Baked', 'Hapless', 'Indolent', "Idiot's", 'Jolly', 'Jarring', 'Knotty-Pated', "King's",'Lazy', 'Lumbering', 'Mammering', 'Masterful', 'Nagging', 'Naughty', 'Onion-Eyed', 'Ough-Hewn', 'Prancing', 'Plume-Plucked', 'Quacking', "Queen's", 'Ribauld', 'Reeky', 'Surly','Sallow', 'Trembling', 'Tickled', 'Urchin-Snouted', 'Unwitting', 'Voluptuous', 'Vain', 'Wilting', 'Wild', "Xanathar's", "eXecutioner's", 'Yellow', 'Yelping', 'Zealous', 'Zesty']

            noun = [' Applejohn', ' Ape', ' Barnacle', ' Bugbear', ' Coxcomb', ' Canary', ' Dog', ' Dragon', ' Elephant', ' Epiphany', ' Frog', ' Flagon', ' Goat', ' Goddess', ' Hippopotamus', ' Hedge-Pig', ' Idiot', ' Ingrate', ' Jack', ' Judge', ' Knot-Head', ' Knave', ' Lout',' Letcher', ' Marmoset', ' Man-o-War', ' Nut-Hook', ' Nightingale', ' Ox', ' Orphan', ' Pig', ' Pigeon-Egg', ' Quiver', ' Quail', ' Radish', ' Rattlesnake', ' Strumpet', ' Skainsmate', ' Troubadour', ' Trebuchet', ' Urchin', ' Unicorn', ' Vicar', ' Vassal', ' Wombat', ' Whey-Face', ' Xenolith', ' Xylocarps', ' Youngling', ' Yeoman', ' Zebra', ' Zebu'] 
            
            #Proprietor/Assistant traits
            age =["young ", "middle-aged ", "geriatric ", "good-looking ", "misshapen ", "vivacious"]
            race = ["Human", "Dwarven", "Half-Elvin", "Elvin", "Gnomish", "Halfling", "Tiefling", "Half-Orc", "Dragonborn"]
            gender = [" man"]*9 + [" woman"]*9 + [" being"]*2
            feature = [" limp", " scarred face", " cheerful smile", " world-weary look", " missing eye", " mischievous grin", " sophisticated air"]

            C = ["A popular orator"] + ["A celebrated troubador"] + ["A popular man/woman about town"]
            W = ["belligerent customer"] + ["in relation to Specialty"] + ["no discernible reason"] + ["peak business hours"] + ["special guest: "+random.choice(C)]
            Q = ["raucus recently quelled"] + ["dwindling patronage"] + ["Specialty/event recently ended"]
            Usual = ["Raucus (dive bar)"] + ["Relaxed (lounge)"] + ["Trendy (lounge)"] + ["Lively (cabaret)"] + ["Trendy (cabaret)"]
            Current = ["Same as usual."] + ["Quieter than usual ("+random.choice(Q)+")"] + ["Wilder than usual ("+random.choice(W)+")"]
            special = ["Bard-offs"] + ["Gambling"] + ["Fighting Ring"] + ["None"] + ["Adventurer Hangout"] + ["Miscreant Hangout"] + ["Wizard/Spellcaster's Hangout"] + ["Commoner's Hangout"] + ["Thinker's/Philosopher's Hangout"] + ["Traveler's Hangout"] +["Open Stage"]

            Nametype = [random.choice(adj)+random.choice(noun)] + [random.choice(noun)+" &"+random.choice(noun)] 
            Infotext.insert(END, "The "+random.choice(Nametype))
            Infotext.insert(END, "\n\nProprietor: A "+random.choice(age)+random.choice(race)+random.choice(gender)+" with a"+random.choice(feature))
            Infotext.insert(END, "\nServer: A "+random.choice(age)+random.choice(race)+random.choice(gender)+" with a"+random.choice(feature))
            Infotext.insert(END, "\n\nUsual Atmosphere: {}\nCurrent Atmosphere: {}\nSpecialty: {}".format(random.choice(Usual), random.choice(Current), random.choice(special)))

        if x == 1: #Food Name 

            Foodsyl1 = ["Om"] + ["Pi"] + ["Chiv"] + ["Yo"] + ["Fral"] + ["Bis"] + ["Do"] + ["Ra"] + ["Su"] + ["Pan"] + ["Mi"] + ["Tre"] + ["Lae"] + ["Gru"] + ["Dyoh"] + ["Ven"] +["Mar"] + ["Abo"] + ['Pil'] 
            Foodsyl2 = ["lette"] + ["ken"] + ["ya"] + ["bas"]  + ["gurt"] + ["ffu"] + ["zinn"] + ["fa"] + ["shaa"] + ["'oto"] +["khur"] + ["bbeis"] + ["niet"] + ["pollo"] + ["kochi"] + ["luto"] + ["cho"]

            group = [" meat-based "] + [" fruit-based "] + [" vegetable-based "] + [" legume-based "] + [" seafood-based "]
            foodtype = [" soup "] + [" salad "] + [" stew "] + [" bread "] + [" pie "] + [" delicacy "] + [" porridge "] + [" cheese "] + [" omlette "]
            prep = [" cold. "] + [" hot. "] + [" at room temperature. "]
            flav = [" salty "] + [" bitter "] + [" sour "] + [" sweet "] + [" umami "] + [" spicy "]
            feel = [" crunchy "] + [" creamy "] + [" chunky "] + [" gamey "] + [" chewy "] + [" greasy "] + [" fatty "] + [" smooth "] + [" tender "]
            after = [" bloated "] + [" sleepy "] + [" energetic "] + [" satisfied "] + [" dehydrated "] + [" inebriated "] + [" relaxed "] + [" frisky "]
            subtaste = [" strong "]  + [" subtle "]  + [" neutral "] + [" complementary "]
            #rating = ["1/10--This is not food. This is POISON! (1d6 poison dmg)"] +["2/10--Not even fit for animals!"]+ ["3/10--Not fit for [racial] consumption."] + ["4/10--Did a rat cook this?"]*3 +["5/10--An untested first attempt on the cook's part?"]*3 + ["6/10--Not bad! Won't likely try it again...but surprisingly adequate."]*4 +\
            #    ["7/10--Quite fine! A few flaws short of excellent!"]*4 + ["8/10--Might have to try this again!"] + ["9/10--Might just be a new favorite food!"] + ["10/10--Quite possibly the best thing you've ever eaten!"]
            
            Infotext.insert(END, random.choice(Foodsyl1)+random.choice(Foodsyl2)+"  ["+str(random.randint(1,6))+" GP]\n")
            Infotext.insert(END, "This dish is a"+random.choice(group)+random.choice(foodtype)+"served"+random.choice(prep))
            Infotext.insert(END, "\nIts dominant flavor is"+random.choice(flav)+"with a"+random.choice(subtaste)+"aftertaste skewed towards"+random.choice(flav)+". It has a rather"+random.choice(feel)+"texture. ")
            Infotext.insert(END, "Most people tend to feel"+random.choice(after)+"after eating this meal.\n")
            #Infotext.insert(END, "\nRating: "+random.choice(rating))
            
        if x == 2: #DRINK
            #DRINK NAME
            adj = ["A"] + ["The"] + ["Red"] + ["Black"] + ["Gold"] + ["Blue"] + ["Grand"] + ["Purple"]
            name = ["Champion's"] + ["King's"] + ["Dragon's"] + ["Queen's"] + ["Giant's"] + ["Cauldron's"] + ["Witch's"] + ["Mist"] + ["Hold's"] + ["Valley"] + ["Succubus's"]
            fluid = ["Revenge"] + ["Ichor"] + ["Brew"] + ["Water"] + ["Blood"] + ["Elixir"] + ["Nectar"] + ["Tea"] + ["Luck"] + ["Jinx"] + ["Wand"] + ["Merrythought"]  + ["Periapt"] + ["Cordial"] + ["Philter"] + ["Courage"] + ["Mount"] + ["Breath"] + ["Downpour"] + ["Harlot"]

            #DRINK FLAVORS
            texture = ["flat"] + ["fizzy"] + ["smooth"] + ["thin"] + ["syrupy"] + ["frothy"]
            itens = ["strong"] + ["subtle"] + ["neutral"] + ["crisp"]
            dom = ["sweet"] + ["sour"] + ["bitter"] + ["spicy"] + ["astringent"]
            flavur = ["herbal"] + ["barley"] + ["fruit"]
            drank = ["wine"] + ["grog"] + ["ale"] + ["mead"] +["cider"]
            colur = ["dark"] + ["reddish"] + ["yellowish"] + ["orange"] + ["green"] + ["clear"]
            temp = ["chilled."] + ["hot."] + ["at room temperature."]
            #Drink Flavor possibilities: 32400!!
            #Drink Names: 880*2

            Infotext.insert(END,random.choice(adj)+" "+random.choice(name)+" "+random.choice(fluid)+"  ["+str(random.randint(1,20))+" SP]\n")
            Infotext.insert(END,"This "+random.choice(dom)+" "+random.choice(flavur)+" "+random.choice(drank)+" has a "+random.choice(colur)+" hue and a "+random.choice(itens)+" flavor. It has a "+random.choice(texture)+" feel to it. It is usually served "+random.choice(temp))
            

    def travel(x):
        Infotext.delete(1.0, END)

        if x == "ins":

            Infotext.insert(END, "The typical travel day consists of 4 events. The DM can determine if these events are Encounters(combat), or Roleplay(non-combat) situations. Travel situaitons may start as one and become the other. Some may even lengthen, or shorten the time it takes to arrive at a destination. Roleplay events often encourage your players to interact with one another, swapping stories in character, or even making observations about one another! ")


        if x == 0:#Encounter
            readiness = [" have not noticed you yet...(Stealth to avoid/ambush possible)"] + [" are ready to attack! (Roll initiative!)"]*3 + [" see you, but do not engage. (Combat/Negotiate possible. Stealth at disadvantage)"]*2
            mons = ["orcs", "goblins", "hobgoblins", "bandits", "kobolds"]
            
            wild = ["pair of wolves"]
            time = ["No time to escape! (Surprised!)"] + ["Just enough time to prepare for battle! (roll initiative)."]*6 + ["Enough time left to avoid the conflict...or mount an ambush! (Stealth)."]*3
            
            enc = [
                "The party comes across a band of "+str(random.randint(2,6))+" "+random.choice(mons)+"!\nThey"+random.choice(readiness),
                "The party comes across a wild "+random.choice(wild)+"!\nThere is..."+random.choice(time)

            ]

            Infotext.insert(END, random.choice(enc))

        if x == 1:#RP

            d = ["Highest d-20"] + ["Lowest D-20"]
            
            cup = [random.choice(["golden", "silver", "copper", "pewter"])+" "+random.choice(["goblet", "chalice"])+" with "+random.choice(["no particular adornment", "gold filigree", "silver filigree", "a skull motif", "a dragon motif", "a mermaid motif", "an ominous eye motif", "a large prominent jewel"])]
            adj = ["dancing"] + ["smiling"] + ["laughing"] + ["dancing"] + ["frowning"] + ["crying"] + ["faceless"] + ["pewter"] + ["golden"] + ["wooden"]
            iitems = ["a ring ["+str(random.randrange(10, 20, 5))+"GP"] + ["a figurine of a "+random.choice(adj)+" "+random.choice(["pixie ", "unicorn ", "dryad ", "imp ", "merman ", "mermaid ", "dragon "])+str(random.randrange(5, 25, 5))+"GP"] + ["a "+random.choice(cup)+str(random.randrange(5, 25, 5))+"GP"]
            maaterials = ["food/rations x"+str(random.randint(1,6))]
            goolds = [str(random.randrange(0, 50, 5))+"GP, "+str(random.randrange(0, 20))+"SP, and "+str(random.randint(0,50))+"CP"]*3 + [""]
            paarty = ["a group of "+str(random.randint(3,12))+random.choice([" men", " women", " men and women", " men, women, and children"])+random.choice([" none", " a few", " some", " most", " all"])+" of whom appear to be injured."]  + ["a lone "+random.choice(["man", "woman"])+" who appears to be "+random.choice(["fine.", "mildly injured.", "severely injured.", "dead."])] + [" a family perhaps? A man, a woman, and "+random.choice(["two", "three"])+" children. Overall, they seem "+random.choice(["fine", "distraught", "in dire need", "in the worst way..."])]
            w_damage = ["beyond repair."] + ["salvagable with the right tools and effort (DC = 15; 1 hour per attempt)."]
            
            rp =["On their travels, the party encounters a broken wagon. It is "+random.choice(w_damage)+"\nThe wagon contains:\n"+random.choice(iitems)+"\n"+random.choice(maaterials)+"\n"+random.choice(goolds)+".\nIt is being attended to by "+random.choice(paarty)] + ["It looks like it's going to rain soon...The party has "+str(random.randint(1,4))+" hours to find/prepare shelter"] +["The party crosses paths with a traveling merchant who has "+str(random.randint(2,7))+" random items to sell."]+ ["The sky is especially breathtaking right now! Unless travelling with urgency, the party spends time admiring the view and cloud-watching (up to an hour)\n\nEach party member, describe a cloud!"] + ["Traveler(s) tell of a rumored cache of loot hidden within "+str(random.randint(1,4))+" days travel from here."]+ ["D20-highest notices something about D20-lowest"] +\
                ["ALL PLAYERS ROLL D-20s!\n"+random.choice(["D20-Highest", "D20-Lowest"])+" loses "+random.choice(["an unequipped weapon", str(random.randint(2,8))+" rations", "their pack (ie, Dungeoneer's Pack, Priest's Pack, etc)", "their tools/skills kit (ie, Healer's kit, Herbalism kit, Navigator's tools, etc)"])+"\nItem Recovery DC: Investigation OR Perception "+str(random.randint(10,18))+"\nPASS = Item Recovered without penalty\nFAIL = Item Recovered; Roll an Encounter Event OR The Item is lost.\nCRIT PASS = Item Recovered; Roll a Travel Event that happens simultaneously with this one.\nCRIT FAIL = Item is lost; roll a Travel Encounter"] + ["ALL PLAYERS ROLL D-20s!\n"+random.choice(["D20-Highest", "D20-Lowest"])+" entertains the group (with a story, song, joke, etc)!\n[ie, A setting/character appropriate retelling of a favorite movie, book, tvshow, etc]"] +\
                ["The road is awkwardly quiet...Will anyone break this unbearable silence?!?"]

            Infotext.insert(END, random.choice(rp))

        if x == 2:#RP OR Encounter
            random.choice([travel(0), travel(1)])
            

            
    def quest(x):
        Infotext.delete(1.0, END)

        if x == 0: #menu description
            Infotext.insert(END, "This menu can be used to generate simple quests.\nCopy/paste the results of each button onto a notepad to generate a basic 3-Act adventure outline.\nEdit these results to best fit your campaign or the story you wish your adventure to tell!")
            pass

        if x == 1: #act i events
            PAL = ["dungeon   "+str(random.randint(1,4))+" days travel; approx"] + ["forest   "+str(random.randint(1,4))+" days travel; approx"] + ["town/city   "+str(random.randint(1,4))+" days travel; approx"] + ["swamp   "+str(random.randint(1,4))+" days travel; approx"] + ["cave   "+str(random.randint(1,4))+" days travel; approx"] 
            AP = [random.choice(["Elderly", "Young", "Mysterious", "Dying", "VERY young"])+" "+random.choice(["beggar", "criminal", "mage", "aristocrat", "peasant", "merchant", "priest/ess"])]
            IoI = ["Treasure map"] + ["Mysterious scroll"] + ["Person ("+random.choice(["colleague", "male family member", "female family member"])+")"] + ["Magic Item ("+random.choice(["orb", "wand", "talisman", "arcane focus", "unassuming item"])+")"]
            KC = ["Bandits"] + ["Cultists"] + ["Orcs"]+ ["Goblinoids"] +["Monsters ("+random.choice(["Aberration", "Beast", "Construct", "Fiend", "Humanoid", "Undead", "Unspecified"])+")"] 
            Req = ["To come along with"] + ["Resolution within "+str(random.randint(1,6))+" day(s)"] + ["None"]
            Intent = ["Rescued/Retrieved"] + ["Escorted/Delivered"] + ["Destroyed/Assassinated"]
            Infotext.insert(END, "Adventure Patron: {}\nItem of Interest: {}\nIoI Intent: {}\nPrimary Adventure Locale: {}\nKnown Complication: {}\nThe Adventure Patron Requests: {}".format(random.choice(AP), random.choice(IoI), random.choice(Intent), random.choice(PAL), random.choice(KC), random.choice(Req)))
            

        if x == 2: #act ii events
            T1 = ["Encounters the expected complication"] + ["Encounters an unexpected complication."] + ["Briefly sees the item/person of interest, or receives an important bit of info regarding it..."] + ["Arrives at the primary adventure location with surprisingly little incident"] + ["Encounters the expected opposition. A reason to doubt their employer is given..."] + ["Gains new and important info about the the primary adventure location."]
            T2 = ["The party is trapped. Only way out is to progress onward."] + ["The party is trapped by overwhelming forces blocking the obvious exit."] + ["Someone from the party has unnerving ties to this location"] #3/6
            Twist = ["The quest objective is not what it seems. Introduce the REAL mission objective."] + ["The quest-giver's true intentions are revealed"] + ["A party member's "+random.choice(["nemesis", "romantic interest", "family member", "mentor", "friend"])+" is involved. Seemingly "+random.choice(["captured by the enemy", "helping the enemy", "on a mission of their own..."])] #3/6
            Boon = ["The party finds a new ally!"] + ["The party finds an important piece of campaign lore/info that will come in handy later"] + ["The party finds a helpful, unrelated Item/Person of Interest"] + ["None"] #4/6
            Peril = ["An unexpected 'mini-boss' encounter awaits the party"] + ["The antagonists have a Large/Huge/Gargantuan and/or area-collapsing creature at their disposal (ie: "+ random.choice(["a minotaur", "a cyclops", "a dragon/wyrmling"]) + " etc)"] + ["An additional enemy faction is involved"] #3/6
            A_adj = ["mad", "vengeful", "possessed", "scheming"]
            Antagonist = [" A "+random.choice(A_adj)+" "+random.choice(["Wizard", "Noble", "Knight", "Doppleganger", "Acolyte", "Vampire Spawn", "Commoner in possession of a cursed/powerful item", "Duergar"])]
            Infotext.insert(END, "En route to the Locale: {}\nAt the location: {}\nTwist:{}\nBoon:{}\nPeril:{}\nQuest Antagonist:{}".format(random.choice(T1), random.choice(T2), random.choice(Twist), random.choice(Boon), random.choice(Peril), random.choice(Antagonist)))

        if x == 3: #act iii events

            PT = ["The patron died a long time ago..."] + ["None"]*8 + ["The patron was genuinely unaware of any twists involved"]*4 + ["The patron witheld information for reasons that are mostly "+random.choice(["understandable", "unacceptable", "reasonable"])]*6 + ["was in league with the villain the entire time!"]
            Reward = ["Paid as agreed upon!"] + ["Paid in an object of equal/greater value"] + ["Unable to pay..."] + ["Paid, plus extra!"]
            Reveal = ["Patron freely explains everything with intent of correcting any misunderstandings"] + ["Patron is coy, answering only direct questions, and doing so evasively"] + ["Patron is uncomfortable when asked to reveal anything."]

            Infotext.insert(END, "Patron Twist: {}\nPayment: {}\nRevelation(s): {}".format(random.choice(PT), random.choice(Reward), random.choice(Reveal)))

    def trees(x):
        Infotext.delete(1.0, END)

        if x == 0:
            Infotext.insert(END, "The Forest Generator creates forest environments. Decide how many zones or areas you need, and allow the generator to do the rest!\nCanopy: Details available lighting in the zone\nTree Spacing: Describes tree density; useful for cover (or lack thereof)\nUnderbrush: Terrain difficulty\nFlora: Plants likely encountered (for foraging)\nFauna: Animals or creatures for hunting, or potential combat.\nArea Features: Notes any special zone details.\nNext Area: Explains routes to other areas.")
            pass
        if x == "forest":
            AREA = ["LARGE: ("+str(random.randrange(100,360, 10))+"x"+str(random.randrange(100,360, 10))+")"] + ["MEDIUM: ("+str(random.randrange(50,180, 10))+"x"+str(random.randrange(50,180, 10))+")"] + ["SMALL: ("+str(random.randrange(25,90, 5))+"x"+str(random.randrange(25,90, 5))+")"]
            CANOPY = ["DENSE; sky is blocked"] + ["THICK; sky is barely visible"] + ["SPARSE; sky is easily visible"]
            TREE_SPACING = ["DENSE: 2 trees per 15 sqft"] + ["THICK: 1 tree per 15 sqft"] + ["THIN: 1 tree per 20 sqft"] + ["SPARSE: ~1 tree per 25 sqft "]
            UNDERBRUSH = ["DENSE: covered roots and detritus mats the floor; difficult terrain (DC 10)--every movement"] + ["THICK: heavy underbrush makes terrain challenging in some spots; (DC 5)--every other movement"] + ["THIN: light underbrush, exposed roots. Difficult terrain DC 5--at DM's discretion"] + ["SPARSE: Mostly grass and easily avoidable roots. (Crit fails can be attributed to terrain)"]
            FLORA = ["Glassberries x"+str(random.randint(1,4))+" (Survival DC:"+str(random.randint(10,16))+")" , "Thelvenfaas x"+str(random.randint(1,4))+"(Survival DC:"+str(random.randint(10,16))+")", "Gemmelrut x"+str(random.randint(1,4))+"(Survival DC:"+str(random.randint(10,16))+")", "None", "??? Mushrooms x"+str(random.randint(1,4))+"(Survival DC:"+str(random.randint(10,16))+")"]
            FAUNA = ["None"]*5 + ["Elk x"+str(random.randint(1,6))]*3 + ["Kobolds x"+str(random.randint(1,6))]*2 + ["Goblins x"+str(random.randint(1,4))]*2 + ["Boar x"+str(random.randint(1,2))]*3 + ["GIANT BOAR!*"] + ["Badger"]*2 + ["Black Bear"]*2
            AREA_FEATURES = ["None"] + ["This area has water in the form of "+random.choice(["a stagnant lake", "a freshwater lake", "a stream", "a small brook"])]
            NEXT_AREA = ["A clear path leads from this area to the next"+random.choice([".", ". A hidden path (Survival DC "+str(random.randint(11,16))+") reveals "+random.choice([random.choice(FLORA), random.choice(FAUNA)])])] + ["The path is overgrown and uncertain here. Survival DC "+str(random.randint(10,16))+" reveals the path to new area"]

            Infotext.insert(END, "Area Size: {}\nCanopy: {}\nTree Spacing: {}\nUnderbrush: {}\nFlora: {}\nFauna: {}\nArea Features: {}\nTraversal: {}".format(random.choice(AREA), random.choice(CANOPY), random.choice(TREE_SPACING),random.choice(UNDERBRUSH), random.choice(FLORA),random.choice(FAUNA), random.choice(AREA_FEATURES), random.choice(NEXT_AREA)))

        if x == "animals":
            Infotext.insert(END, "Unless stated otherwise, assume fauna does not immediately notice the party. A party stealth check vs the creature's passive perception can affirm the party has gone unnoticed. Of course, careless actions can compromise cover as appropriate.")
            pass
        if x == "plants":
            Infotext.insert(END, "Use your imagination to describe the fauna listed and their properties. It is encouraged, but not necessary to add your own to the list. Consider giving these items a market value, or even funtional use in creating potions, medicines, and poisons!")        

    def shop(x):
        Infotext.delete(1.0, END) 

        if x == 0:#General Shop

            Set1 = ["1: Caltrops(20) [1 GP]"+" "*15+"7: Crowbar [2 GP]\n2: Tent (2-person) [2 GP]"+" "*9+"8: Jug/Pitcher [2 CP]\n3: Shovel [2 GP]"+" "*25+"9: Waterskin [2 SP]\n4: Torch [1 CP]"+" "*25+"10: Tinderbox [5 SP]\n5: 10-ft Pole [5 CP]"+" "*19+"11: Ration (1day) [5 SP]\n6: Mess kit [2 SP]"+" "*21+"12: oil (flask) [1 SP]\n     "]


            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(Set1))

        if x == 1:#Clothing Shop
            clothes = ["1: Perfume [5 GP]"+" "*18+"7: Clothes(common) [5 SP]\n2: Robe [1 GP]"+" "*25+"8: Clothes(travelers) [2 GP]\n3: Clothes(fine) [15 GP]"+" "*8+"9: Clothes(costume) [5 GP]\n4: Pouch [5 SP]"+" "*22+"10: Soap [2 CP]\n5: Waterskin [1 SP*]"+" "*14+"11: Ration (1day) [5 SP]\n6: Leather armor [10 GP]"+" "*5+"12: Cotton (sq.yd) [5 SP]\n     "]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(clothes))

        if x == 2:#Magic Shop 1
            magi = ["1: Arcane Focus(Crystal) [10 GP]"+" "*5+"7: Spellbook [50 GP]\n2: Arcane Focus(Orb) [20 GP]"+" "*11+"8: Ink Pen [2 CP]\n3: Arcane Focus(Rod) [10 GP]"+" "*11+"9: Hourglass [25 GP]\n4: Arcane Focus(Staff) [5 GP]"+" "*10+"10: Robe [2 GP*]\n5: Arcane Focus(Wand) [10 GP]"+" "*7+"11: Trinket [d100 GP]\n6: Alchemist's Fire (flask) [50 GP]"+" "*2+"12: Special Order"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(magi))    

        if x == 3:#Magic Shop 2 (SHRINE)
            magi = ["1: Holy Symbol(Amulet) [5 GP]"+" "*9+"7: Candle [1 CP]\n2: Holy Symbol(Reliquary) [5 GP]"+" "*5+"8: Vial [1 GP]\n3: Holy Symbol(Emblem) [5 GP]"+" "*7+"9: Hourglass [25 GP]\n4: Holy Water(flask) [25 GP]"+" "*14+"10: Robe [2 GP*]\n5: Potion of Healing [50 GP]"+" "*14+"11: Book [25 GP]\n6: Alms/Blessings [Any]"+" "*19+"12: Rations [2 SP*]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(magi))   # Ink (1oz. bottle) [10 GP]   Component Pouch [25 GP]     Book [25 GP]

        if x == 4:#Weapon Shop 1 (Simple)
            wpn1 = ["1: Club [1 SP]"+" "*33+"7: Dagger [2 GP]\n2: Hammer [2 GP]"+" "*25+"8: Handaxe [5 GP]\n3: Javelin [5 SP]"+" "*28+"9: Mace [5 GP]\n4: Morningstar [15 GP]"+" "*14+"10: Quarterstaff [2 SP]\n5: Spear [1 GP]"+" "*28+"11: Sickle [1 SP]\n6: Sling [1 SP]"+" "*30+"12: Greatclub [2 SP]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(wpn1))   #      Book [25 GP]

        if x == 5:#Weapon Shop 2 (Martial)
            wpn2 = ["1: Battleaxe [10 GP]"+" "*26+"7: Blowgun [10 GP]\n2: Crossbow (light) [75 GP]"+" "*12+"8: Glaive [20 GP]\n3: Crossbow (heavy) [50 GP]"+" "*9+"9: Flail [10 GP]\n4: Greataxe [30 GP]"+" "*25+"10: Halberd [20 GP]\n5: Greatsword [50 GP]"+" "*19+"11: Lance [10 GP]\n6: Longsword [15 GP]"+" "*20+"12: Maul [10 GP]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(wpn2))   #      Book [25 GP]      

        if x == 6:#Weapon Shop 3 (Misc)
            wpn3 = ["1: Longbow [50 GP]"+" "*18+"7: Rapier [25 GP]\n2: Pike [5 GP]"+" "*29+"8: Net [1 GP]\n3: Scimitar [25 GP]"+" "*20+"9: Shortsword [10 GP]\n4: Trident [5 GP]"+" "*22+"10: Warpick [5 GP]\n5: Warhammer [15 GP]"+" "*11+"11: Whip [2 GP]\n6: Arrows (20) [1 GP]"+" "*14+"12: Sling Bullets (20) [4 CP]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(wpn3))   #            

        if x == 7:#Armor (Misc)
            wpn3 = ["1: Breastplate [400 GP]"+" "*10+"7: Chainmail [75 GP]\n2: Chain shirt [50 GP]"+" "*13+"8: Full Plate [1500 GP]\n3: Half-plate [750 GP]"+" "*14+"9: Hide [10 GP]\n4: Leather [10 GP]"+" "*17+"10: Padded [5 GP]\n5: Ring Mail [30 GP]"+" "*15+"11: Scale Mail [50 GP]\n6: Splint Mail [200 GP]"+" "*11+"12: Studded Leather [45 GP]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(wpn3))   #           

        if x == 8:#Random (Misc)
            wpn3 = ["1: Ink (1oz. bottle) [10 GP]"+" "*9+"7: Antitoxin (vial) [50 GP]\n2: Component Pouch [25 GP]"+" "*3+"8: Book [25 GP]\n3: Grappling Hook [2 GP]"+" "*11+"9: Signet Ring [5 GP]\n4: Spyglass [1000 GP]"+" "*16+"10: Healer's Kit [5 GP]\n5: Steel mirror [5 GP]"+" "*17+"11: Shield [30 GP]\n6: Iron pot [2 GP]"+" "*25+"12: Silk rope (50') [10 GP]"]

            Infotext.insert(END, "This store sells "+str(random.randint(3,8))+" items\n") #d6+2 items 
            Infotext.insert(END, random.choice(wpn3))   #            


    def mon(x):
        
        if x == "TESTING":
            main = Toplevel()
            r1 =monsterset(main, "TESTING", "GOB")
            
        if x == "BANDIT":
            main = Toplevel()
            r1 =monsterset(main, "Bandit", "Medium Humanoid; any race;\nany non-lawful alignment", 10, 12, 11, 2, "30", "11(+0)", "12(+1)", "12(+1)", "10(+0)", "10(+0)", "10(+0)", "Senses: Pass.Perception 10\nLanguages:One. Usually Common", "", "SCIMITAR[⚔]: +3 to hit,\nreach 5ft one target. Hit:[1d6+1] slash dmg", "LIGHT CROSSBOW[➳]: +3 to hit,\nrange 80/320ft\n one target. Hit:[1d8+1] pierce dmg", 0,1,1,0,0,0) #Mon name, Mon description, ACLow, ACMax, HPMAX, HPdigits, Speed, STRSTAT, DEXSTAT, CONSTAT, INTSTAT, WISSTAT, CHARSTAT, SAVES/SKILLS/SENSES/LANGUAGES, FEATS, ATTACK1, ATTACK2
            
            
        if x == "WOLF":
            main = Toplevel()
            r1 =monsterset(main, "Wolf", "Medium beast; unaligned", 10, 13, 11, 2, "40", "12(+1)", "15(+2)", "12(+1)", "3(-3)", "12(+1)", "6(-2)", "Skills: Stealth +4  Perception +3\nSenses: Pass.Perception 13", "KEEN HEARING AND SMELL: The wolf has advantage\non Wis(Perception) checks reliant on hearing/smell\n\nPACK TACTICS: The wolf has adv. on an attack roll against a \ncreature if the wolf has an active ally w/in 5ft of it", "BITE[⚔]: +4 to hit,\nreach 5ft one target. Hit:[2d4 +2] pierce dmg\nIf the target is a creature, it must succeed\non a DC 11 STR save or be knocked prone.", "", 1,2,1,-3,1,-2)
            
        if x == "SKELETON":
            main = Toplevel()
            r1 =monsterset(main, "Skeleton", "Medium undead; lawful evil", 10, 13, 13, 2, "30", "10(+0)", "14(+2)", "15(+2)", "6(-2)", "8(-1)", "5(-2)", "Damage Vulnerabilities: Bludgeoning\nCondition Immunities: Poisoned\nSenses: Pass.Perception 9,  Darkvision 60ft\nLanguages:Understands languages spoken in life; mute", "", "SHORTSWORD[⚔]: +4 to hit,\nreach 5ft one target. Hit:[1d6+2] slash dmg", "SHORTBOW[➳]: +4 to hit,\nrange 80/320ft\n one target. Hit:[1d6+2] pierce dmg", 0, 2, 2, -2, -1, -2 ) #Mon name, Mon description, ACLow, ACMax, HPMAX, HPdigits, Speed, STRSTAT, DEXSTAT, CONSTAT, INTSTAT, WISSTAT, CHARSTAT, SAVES/SKILLS/SENSES/LANGUAGES, FEATS, ATTACK1, ATTACK2
            
            
            
        if x == "ORC":
            main = Toplevel()
            r1 =monsterset(main, "Orc", "Medium Humanoid orc, chaotic evil", 10,13,15,2,"30", "16(+3)", "12(+1)", "16(+3)", "7(-1)", "11(+0)", "10(+0)", "Skills: Intimidation +2\nSenses: Pass.Perception 10, Darkvision(60ft)","AGGRESSIVE: As a bonus action, the orc can move\nup to its speed toward a hostile creature that it can see", "GREATAXE[⚔] +5 to hit\nreach:5ft, one target, Hit:[1d12+3] slash dmg", "JAVELIN[⚔/➳] +5 to hit\nreach:5ft; range:30/120ft, one target\nHit:[1d6+3] pierce dmg", 3, 1, 3, -1, 0, 0 )   
        
        if x == "Goblin":
        
            main = Toplevel()
            main.title("Goblin")
            
            def roll(x):
                if x == 'atk1':
                    ATKEntry.delete(0, END), ATKEntry.insert(END, "M")
                    DmgEntry.delete(0, END), DmgEntry.insert(END, str(random.randint(3,8)))
                    
                if x == 'atk2':
                    ATKEntry.delete(0, END), ATKEntry.insert(END, "R")
                    DmgEntry.delete(0, END), DmgEntry.insert(END, str(random.randint(3,8)))
                    
                if x == "Str":
                    STREntry.delete(0, END), STREntry.insert(END, str(random.randint(1,19)))
                    
                if x == "Dex":
                    DEXEntry.delete(0, END), DEXEntry.insert(END, str(random.randint(3,22)))
                    
                if x == "Con":
                    CONEntry.delete(0, END), CONEntry.insert(END, str(random.randint(1,20)))
                    
                if x == "Int":
                    INTEntry.delete(0, END), INTEntry.insert(END, str(random.randint(1,20)))
                    
                if x == "Wis":
                    WISEntry.delete(0, END), WISEntry.insert(END, str(random.randint(1,19)))
                    
                if x == "Cha":
                    CHAEntry.delete(0, END), CHAEntry.insert(END, str(random.randint(1,19)))
                    

            Frame0 = Frame(main, bd=2, relief=SOLID)
            Frame0.pack(side=LEFT)

            InfoLF = LabelFrame(Frame0)
            InfoName = Label(InfoLF, text="Goblin", bd=2, relief=SOLID)
            InfoName.grid(column=0, row=0)

            MiscEntry = Entry(InfoLF)
            MiscEntry.grid(column=1, row=0)

            Initiative = Entry(InfoLF, width=2)
            Initiative.insert(0, random.randint(1,20))
            Initiative.grid(column=2, row=0)


            ChaDetails = Label(InfoLF, text="Small  humanoid(goblinoid)   neutral evil")
            ChaDetails.grid(column=0, row=2, columnspan=2)
            InfoLF.pack()

            padframe = Frame(Frame0, height=5)
            padframe.pack()

            #AC STUFF------------------------
            Frame1 = Frame(Frame0)
            Frame1.pack()

            ACLabel = Label(Frame1, text="AC", bd=3, relief=SUNKEN)
            ACLabel.grid(column=0, row=0)

            AC = Spinbox(Frame1, from_=10, to=15, width=2)
            AC.insert(0, 15)
            AC.grid(column=1, row=0)
            #Separator Label------
            Separator = Label(Frame1, text="")
            Separator.grid(column=2, row=0, padx=10)

            #HP STUFF--------------------------


            HPLabel = Label(Frame1, text="HP", bd=3, relief=SUNKEN)
            HPLabel.grid(column=3, row=0)#(column=0, row=1)

            HP = Spinbox(Frame1, from_=0, to=7, width=1)
            HP.insert(0, 7)
            HP.grid(column=4, row=0)#(column=1, row=1)

            #Separator Label------------------------
            Separator = Label(Frame1, text="")
            Separator.grid(column=5, row=0, padx=10)
            #Movement-------------------------------
            MoveLabel = Label(Frame1, text="Spd: 30ft")
            MoveLabel.grid(column=6, row=0)

            #STATS
            Statframe = Frame(Frame0, bd=1, relief=SOLID)
            Statframe.pack()

            #STR
            STRFrame = Frame(Statframe, bd=1, relief=SOLID)
            STRFrame.pack(side=LEFT)

            STRLabelframe = LabelFrame(STRFrame)
            STRBUTTON = Button(STRLabelframe, text="STR", command=lambda:roll("Str"))
            STRBUTTON.pack()
            STRLabel = Label(STRLabelframe, text="8 (-1)")
            STRLabel.pack()
            STREntry = Entry(STRLabelframe, width=2)
            STREntry.pack()
            STRLabelframe.pack()

            #DEX
            DEXFrame = Frame(Statframe, bd=1, relief=SOLID)
            DEXFrame.pack(side=LEFT)

            DEXLabelframe = LabelFrame(DEXFrame)
            DEXBUTTON = Button(DEXLabelframe, text="DEX", command=lambda:roll("Dex"))
            DEXBUTTON.pack() 
            DEXLabel = Label(DEXLabelframe, text="14 (+2)")
            DEXLabel.pack()
            DEXEntry = Entry(DEXLabelframe, width=2)
            DEXEntry.pack()
            DEXLabelframe.pack()

            #CON
            CONFrame = Frame(Statframe, bd=1, relief=SOLID)
            CONFrame.pack(side=LEFT)

            CONLabelframe = LabelFrame(CONFrame)
            CONBUTTON = Button(CONLabelframe, text="CON", command=lambda:roll("Con"))
            CONBUTTON.pack()
            CONLabel = Label(CONLabelframe, text="10(+0)")
            CONLabel.pack()
            CONEntry = Entry(CONLabelframe, width=2)
            CONEntry.pack()
            CONLabelframe.pack()

            #INT
            INTFrame = Frame(Statframe, bd=1, relief=SOLID)
            INTFrame.pack(side=LEFT)

            INTLabelframe = LabelFrame(INTFrame)
            INTBUTTON = Button(INTLabelframe, text="INT", command=lambda:roll("Int"))
            INTBUTTON.pack()
            INTLabel = Label(INTLabelframe, text="10(+0)")
            INTLabel.pack()
            INTEntry = Entry(INTLabelframe, width=2)
            INTEntry.pack()
            INTLabelframe.pack()


            #WIS
            WISFrame = Frame(Statframe, bd=1, relief=SOLID)
            WISFrame.pack(side=LEFT)

            WISLabelframe = LabelFrame(WISFrame)
            WISBUTTON = Button(WISLabelframe, text="WIS", command=lambda:roll("Wis"))
            WISBUTTON.pack()
            WISLabel = Label(WISLabelframe, text="8(-1)")
            WISLabel.pack()
            WISEntry = Entry(WISLabelframe, width=2)
            WISEntry.pack()
            WISLabelframe.pack()

            #CHA
            CHAFrame = Frame(Statframe, bd=1, relief=SOLID)
            CHAFrame.pack()

            CHALabelframe = LabelFrame(CHAFrame)
            CHABUTTON = Button(CHALabelframe, text="CHA", command=lambda:roll("Cha"))
            CHABUTTON.pack()
            CHALabel = Label(CHALabelframe, text="8(-1)")
            CHALabel.pack()
            CHAEntry = Entry(CHALabelframe, width=2)
            CHAEntry.pack()
            CHALabelframe.pack()


            #DETAILS
            SecondaryFrame= Frame(Frame0, bd=2, relief=SOLID)
            SecondaryFrame.pack()

            #Blahblah = Label(SecondaryFrame, text="Save Throws: STR+4  CON+2").pack()
            Blahblah2 = Label(SecondaryFrame, text="Skills: Stealth+4").pack()
            #Blahblah3 = Label(SecondaryFrame, text="Dmg Resistance(s): Fire").pack()
            Blahblah4 = Label(SecondaryFrame, text="Senses: Pass.Perception 9;  Darkvision 60ft").pack()
            Blahblah5 = Label(SecondaryFrame, text="Languages: Common, Goblin").pack()
            
            #FEATURES
            FeatureFrame = Frame(Frame0, bd=2, relief=SOLID)
            FeatLabel = Label(FeatureFrame, text="NIMBLE ESCAPE: The goblin can Disengage\nor Hide as a bonus action on each of its turns.")
            FeatLabel.pack()
            FeatureFrame.pack()

            #ACTIONS
            ACTSFrame = Frame(Frame0, bd=2, relief=SOLID)
            ACTSLabel=Label(ACTSFrame, text="ACTIONS")
            ACTSLabel.pack()
            ACTION1 = Button(ACTSFrame, text="SCIMITAR[⚔]: +4 to hit,\nreach 5ft one target. Hit:[1d6+2] slash dmg", command=lambda:roll("atk1"))
            ACTION1.pack()
            ACTION2 = Button(ACTSFrame, text="SHORTBOW[➳]: +4 to hit,\nrange 80/320ft\n one target. Hit:[1d6+2] pierce dmg", command=lambda:roll("atk2"))
            ACTION2.pack()
            
            ACTSFrame.pack()


            MasterActionFrame = Frame(Frame0)
            MasterActionFrame.pack()

            ActionFrame = Frame(MasterActionFrame)
            ActionFrame.pack(side=LEFT)

            

            
            

            #ATTACK/DAMAGE STUFF
            ATKDMGFrame = Frame(Frame0, bd=2, bg='dark red', relief=SOLID)

            ATKLabel = Label(ATKDMGFrame, bg='dark red', fg='gold',text="ATK")
            ATKLabel.grid(column=0, row=0)

            ATKEntry = Entry(ATKDMGFrame, width=2)
            ATKEntry.grid(column=1, row=0)


            DmgLabel = Label(ATKDMGFrame, bg='dark red', fg='gold',text="DMG")
            DmgLabel.grid(column=2, row=0)

            DmgEntry = Entry(ATKDMGFrame, width=2)
            DmgEntry.grid(column=3, row=0)

            Separator = Label(ATKDMGFrame, text="", bg='dark red')
            Separator.grid(column=4, row=0, padx=5)
            
            ATKDMGFrame.pack()

            





    ButtonLF1 = LabelFrame(Frame0)
    Button1 = Button(ButtonLF1, text="City Encounters", command=lambda:city(3))
    Button1.pack()
    Button2 = Button(ButtonLF1, text="NPCs", command=lambda:city(1))
    Button2.pack(fill=X)
    Button3 = Button(ButtonLF1, text="Locations", command=lambda:city(2))
    Button3.pack(fill=X)


    ButtonLF1.pack(side=LEFT)



    PersonLF = LabelFrame(Frame0)

    PersonButton = Button(PersonLF, bd=0, text="Person\nGenerator", command=lambda:peeps("P"))
    PersonButton.pack(fill=X)
    MaleButton = Button(PersonLF, text="Go!", command=lambda:peeps("M"))
    MaleButton.pack(fill=X)

    PersonLF.pack(side=LEFT)








    ButtonLF3 = LabelFrame(Frame0)
    Button1 = Button(ButtonLF3, text="Cryptic words", command=lambda:fortune(0))
    Button1.pack(fill=X)
    Button2 = Button(ButtonLF3, text="Yes/no", command=lambda:fortune(1))
    Button2.pack(fill=X)
    Button3 = Button(ButtonLF3, text="Hint", command=lambda:fortune(2))
    Button3.pack(fill=X)
    ButtonLF3.pack(side=LEFT)


    ButtonLF4 = LabelFrame(Frame0)
    Button1 = Button(ButtonLF4, text="SpellSurge Weapon", command=lambda:spellsurge(0))
    Button1.pack(fill=X)
    Button3 = Button(ButtonLF4, text="SpellSurge Tips", command=lambda:spellsurge(2))
    Button3.pack(fill=X)

    Button2 = Button(ButtonLF4, text="Roll Stats!", command=lambda:spellsurge(1))
    Button2.pack(fill=X)

    ButtonLF4.pack(side=LEFT)


    ButtonLF5 = LabelFrame(Frame0)
    Button1 = Button(ButtonLF5, text="Trinkets", command=lambda:objects(0))
    Button1.pack(fill=X)
    Button1 = Button(ButtonLF5, text="Books", command=lambda:objects(1))
    Button1.pack(fill=X)
    Button1 = Button(ButtonLF5, text="Wild Magic", command=lambda:objects(2))
    Button1.pack(fill=X)

    ButtonLF5.pack(side=LEFT)
    #------------------------------------------------

    #SHOPS------------------------------------------
    ButtonSet1 = LabelFrame(Frame1)
    SetLabel = Label(ButtonSet1, text="Shops")
    SetLabel.grid(column=0, row=0, sticky='nesw')

    Button1 = Button(ButtonSet1, text="Common Shop", command=lambda:shop(0))
    Button1.grid(column=0, row=1, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Clothing Shop", command=lambda:shop(1))
    Button1.grid(column=0, row=2, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Magic Shop", command=lambda:shop(2))
    Button1.grid(column=1, row=1, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Magic Shop2", command=lambda:shop(3))
    Button1.grid(column=1, row=2, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Weapon Shop", command=lambda:shop(4))
    Button1.grid(column=2, row=1, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Weapon Shop2", command=lambda:shop(5))
    Button1.grid(column=2, row=2, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Weapon Shop3", command=lambda:shop(6))
    Button1.grid(column=2, row=3, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Armor Shop", command=lambda:shop(7))
    Button1.grid(column=1, row=3, sticky='nesw')
    Button1 = Button(ButtonSet1, text="Misc Shop", command=lambda:shop(8))
    Button1.grid(column=0, row=3, sticky='nesw')


    ButtonSet1.pack(side=LEFT)


    #TAVERN--------------------------------
    ButtonSet2 = LabelFrame(Frame1)
    SetLabel = Label(ButtonSet2, text="Tavern")
    SetLabel.pack(fill=X)
    TButton = Button(ButtonSet2, text="Name", command=lambda:tavern(0))
    TButton.pack(fill=X)
    TButton = Button(ButtonSet2, text="Food", command=lambda:tavern(1))
    TButton.pack(fill=X)
    TButton = Button(ButtonSet2, text="Drink", command=lambda:tavern(2))
    TButton.pack(fill=X)


    ButtonSet2.pack(side=LEFT, padx=10)



    #DICE SET----------------
    DiceSet = LabelFrame(Frame1)
    DieLabel = Label(DiceSet, text="Dice")
    DieLabel.grid(column=0, columnspan=2, row=0, sticky='news')

    Buttond4 = Button(DiceSet, text="d4", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,4)))])
    Buttond4.grid(column=0, row=1, sticky='news')

    Buttond4 = Button(DiceSet, text="d6", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,6)))])
    Buttond4.grid(column=1, row=1, sticky='news')

    Buttond4 = Button(DiceSet, text="d8", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,8)))])
    Buttond4.grid(column=0, row=2, sticky='news')

    Buttond4 = Button(DiceSet, text="d10", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,10)))])
    Buttond4.grid(column=1, row=2, sticky='news')

    Buttond4 = Button(DiceSet, text="d12", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,12)))])
    Buttond4.grid(column=0, row=3, sticky='news')

    Buttond4 = Button(DiceSet, text="d20", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,20)))])
    Buttond4.grid(column=1, row=3, sticky='news')

    Buttond4 = Button(DiceSet, text="d100", command=lambda:[Infotext.delete(1.0, END), Infotext.insert(END, str(random.randint(1,100)))])
    Buttond4.grid(column=2, rowspan=3, row=1, sticky='news')




    DiceSet.pack(side=LEFT, padx=10)

    #TOWN---------------------
    TownGen = LabelFrame(Frame1)
    TownLabel = Button(TownGen, bd=0, text="Town Generator", command=lambda:[settlement(0)])
    TownLabel.grid(column=0, columnspan=2, row=0, sticky='news')

    ThorpButton = Button(TownGen, text="1) Thorp", command=lambda:[settlement(1)])
    ThorpButton.grid(column=0, row=1, sticky='news')

    HamletButton = Button(TownGen, text="2) Hamlet", command=lambda:[settlement(2)])
    HamletButton.grid(column=1, row=1, sticky='news')

    VillageButton = Button(TownGen, text="3) Village", command=lambda:[settlement(3)])
    VillageButton.grid(column=0, row=2, sticky='news')

    TownButton = Button(TownGen, text="4) Town", command=lambda:[settlement(4)])
    TownButton.grid(column=1, row=2, sticky='news')

    CityButton = Button(TownGen, text="5) City", command=lambda:[settlement(5)])
    CityButton.grid(column=0, row=3, sticky='news')

    MetroButton = Button(TownGen, text="6) Metropolis", command=lambda:[settlement(6)])
    MetroButton.grid(column=1, row=3, sticky='news')

    TownGen.pack(side=LEFT, padx=10)



    #TRAVEL------
    TravelSet = LabelFrame(Frame2)

    Label0 = Button(TravelSet, bd=0, text="Travel", command=lambda:travel("ins"))
    Label0.pack(fill=X)



    Button1 = Button(TravelSet, text="Encounter", command=lambda:travel(0))
    Button1.pack(fill=X)

    Button1 = Button(TravelSet, text="Roleplay", command=lambda:travel(1))
    Button1.pack(fill=X)

    Button1 = Button(TravelSet, text="Random", command=lambda:travel(2))
    Button1.pack(fill=X)

    TravelSet.pack(side=LEFT, padx=10)

    #--------------------------------------------
    #DUNGEON GENERATOR
    ButtonLF2 = LabelFrame(Frame2)
    DungeonLabel = Label(ButtonLF2, text="Dungeon Generator")
    DungeonLabel.grid(column=0, columnspan=3, row=0, sticky='news')

    Button1 = Button(ButtonLF2, text="Start", command=lambda:dungeon(1))
    Button1.grid(column=0, row=1, sticky='news')


    Button2 = Button(ButtonLF2, text="Passage", command=lambda:dungeon(2))
    Button2.grid(column=1, row=1, sticky='news')


    Button3 = Button(ButtonLF2, text="Door", command=lambda:dungeon(3))
    Button3.grid(column=2, row=1, sticky='news')

    ButtonB = Button(ButtonLF2, text="Boss", command=lambda:dungeon('boss'))
    ButtonB.grid(column=2, row=2, sticky='news')




    Button4 = Button(ButtonLF2, text="Chamber", command=lambda:dungeon(4))
    Button4.grid(column=0, row=2, sticky='news') 

    ButtonS = Button(ButtonLF2, text="Stairs", command=lambda:dungeon('stairs'))
    ButtonS.grid(column=1, row=2, sticky='news') 


    Button5 = Button(ButtonLF2, text="Room Contents", command=lambda:dungeon(5))
    Button5.grid(column=0, columnspan=3, row=3, sticky='news')


    ButtonLF2.pack(side=LEFT, padx=10)


    #----------------------------------------------------------
    #ADVENTURE GENERATOR
    AdvLblF = LabelFrame(Frame2)
    AdvButton = Button(AdvLblF, bd=0, text="Adventure Generator", command=lambda:quest(0))
    AdvButton.pack(fill=X)
    A1B = Button(AdvLblF, text="Act I", command=lambda:quest(1))
    A1B.pack(fill=X)
    A2B = Button(AdvLblF, text="Act II", command=lambda:quest(2))
    A2B.pack(fill=X)
    A3B = Button(AdvLblF, text="Act III", command=lambda:quest(3))
    A3B.pack(fill=X)

    AdvLblF.pack(side=LEFT, padx=10)



    ForestLF = LabelFrame(Frame2)
    ForestButton = Button(ForestLF, bd=0, text="Forest Generator", command=lambda:trees(0))
    ForestButton.pack(fill=X)
    ForestScene = Button(ForestLF, text="Forest", command=lambda:trees("forest"))
    ForestScene.pack(fill=X)
    FaunaButton = Button(ForestLF, text="Flora", command=lambda:trees("animals"))
    FaunaButton.pack(fill=X)
    FloraButton = Button(ForestLF, text="Fauna", command=lambda:trees("plants"))
    FloraButton.pack(fill=X)

    ForestLF.pack(side=LEFT, padx=10)


    MONLF = LabelFrame(Frame2)
    MonsterButton = Button(MONLF, bd=0, text="Monster Generator" )
    MonsterButton.pack(fill=X)
    MonButton1 = Button(MONLF, text="Goblin", command=lambda:mon("Goblin"))
    MonButton1.pack(fill=X)
    MonButton2 = Button(MONLF, text="TEST", command=lambda:mon("TESTING"))
    #MonButton2.pack(fill=X)
    MonButton3 = Button(MONLF, text="Bandit", command=lambda:mon("BANDIT"))
    MonButton3.pack(fill=X)
    MonButton4 = Button(MONLF, text="Orc", command=lambda:mon("ORC"))
    MonButton4.pack(fill=X)
    MonButton5 = Button(MONLF, text="Skeleton", command=lambda:mon("SKELETON"))
    MonButton5.pack(fill=X)
    MonButton6 = Button(MONLF, text="Wolf", command=lambda:mon("WOLF"))
    MonButton6.pack(fill=X)
    MONLF.pack(side=LEFT)


    class monsterset:
        def __init__(self, main, monname, mondescript, ACLOW, ACHIGH, HPMAX, HPDIGITS, MONSPD, STRSTAT, DEXSTAT, CONSTAT, INTSTAT, WISSTAT, CHASTAT, SSSL, FEATS, ATTACK1, ATTACK2, STRSCORE, DEXSCORE, CONSCORE, INTSCORE, WISSCORE, CHASCORE):
            
            self.main = main
            
            
            
            main.title(monname)
            
            def roll(x):
                D20 = random.randint(1,20)
                if x == "Str":
                    STREntry.delete(0, END), STREntry.insert(END, D20+STRSCORE)
                
                if x == "Dex":
                    DEXEntry.delete(0, END), DEXEntry.insert(END, D20+DEXSCORE)
                    
                if x == "Con":
                    CONEntry.delete(0, END), CONEntry.insert(END, D20+CONSCORE)
                    
                if x == "Int":
                    INTEntry.delete(0, END), INTEntry.insert(END, D20+INTSCORE)
                    
                if x == "Wis":
                    WISEntry.delete(0, END), WISEntry.insert(END, D20+WISSCORE)
                    
                if x == "Cha":
                    CHAEntry.delete(0, END), CHAEntry.insert(END, D20+CHASCORE)
                    
                
                    
                
            
            Frame0 = Frame(main, bd=2, relief=SOLID)
            Frame0.pack(side=LEFT)

            InfoLF = LabelFrame(Frame0)
            InfoName = Label(InfoLF, text=monname, bd=2, relief=SOLID)
            InfoName.grid(column=0, row=0)

            MiscEntry = Entry(InfoLF)
            MiscEntry.grid(column=1, row=0)

            Initiative = Entry(InfoLF, width=2)
            Initiative.insert(0, random.randint(1,20))
            Initiative.grid(column=2, row=0)
            
            MiscEntry = Entry(InfoLF)
            MiscEntry.grid(column=1, row=0)

            Initiative = Entry(InfoLF, width=2)
            Initiative.insert(0, random.randint(1,20))
            Initiative.grid(column=2, row=0)


            ChaDetails = Label(InfoLF, text=mondescript) 
            ChaDetails.grid(column=0, row=2, columnspan=2)
            InfoLF.pack()

            padframe = Frame(Frame0, height=5)
            padframe.pack()
            
            #AC STUFF------------------------
            Frame1 = Frame(Frame0)
            Frame1.pack()

            ACLabel = Label(Frame1, text="AC", bd=3, relief=SUNKEN)
            ACLabel.grid(column=0, row=0)

            AC = Spinbox(Frame1, from_=ACLOW, to=ACHIGH, width=2) 
            AC.insert(0, ACHIGH)
            AC.grid(column=1, row=0)
            #Separator Label------
            Separator = Label(Frame1, text="")
            Separator.grid(column=2, row=0, padx=10)

            #HP STUFF--------------------------


            HPLabel = Label(Frame1, text="HP", bd=3, relief=SUNKEN)
            HPLabel.grid(column=3, row=0)#(column=0, row=1)

            HP = Spinbox(Frame1, from_=0, to=HPMAX, width=HPDIGITS) 
            HP.insert(0, HPMAX)
            HP.grid(column=4, row=0)#(column=1, row=1)

            #Separator Label------------------------
            Separator = Label(Frame1, text="")
            Separator.grid(column=5, row=0, padx=10)
            #Movement-------------------------------
            MoveLabel = Label(Frame1, text="Spd: "+ MONSPD +"ft") 
            MoveLabel.grid(column=6, row=0)
            
            #STATS
            Statframe = Frame(Frame0, bd=1, relief=SOLID)
            Statframe.pack()

            #STR
            STRFrame = Frame(Statframe, bd=1, relief=SOLID)
            STRFrame.pack(side=LEFT)

            STRLabelframe = LabelFrame(STRFrame)
            STRBUTTON = Button(STRLabelframe, text="STR", command=lambda:roll("Str"))
            STRBUTTON.pack()
            STRLabel = Label(STRLabelframe, text=STRSTAT) #STRSTAT
            STRLabel.pack()
            STREntry = Entry(STRLabelframe, width=2)
            STREntry.pack()
            STRLabelframe.pack()

            #DEX
            DEXFrame = Frame(Statframe, bd=1, relief=SOLID)
            DEXFrame.pack(side=LEFT)

            DEXLabelframe = LabelFrame(DEXFrame)
            DEXBUTTON = Button(DEXLabelframe, text="DEX", command=lambda:roll("Dex"))
            DEXBUTTON.pack() 
            DEXLabel = Label(DEXLabelframe, text=DEXSTAT) 
            DEXLabel.pack()
            DEXEntry = Entry(DEXLabelframe, width=2)
            DEXEntry.pack()
            DEXLabelframe.pack()

            #CON
            CONFrame = Frame(Statframe, bd=1, relief=SOLID)
            CONFrame.pack(side=LEFT)

            CONLabelframe = LabelFrame(CONFrame)
            CONBUTTON = Button(CONLabelframe, text="CON", command=lambda:roll("Con"))
            CONBUTTON.pack()
            CONLabel = Label(CONLabelframe, text=CONSTAT) #CONSTAT
            CONLabel.pack()
            CONEntry = Entry(CONLabelframe, width=2)
            CONEntry.pack()
            CONLabelframe.pack()

            #INT
            INTFrame = Frame(Statframe, bd=1, relief=SOLID)
            INTFrame.pack(side=LEFT)

            INTLabelframe = LabelFrame(INTFrame)
            INTBUTTON = Button(INTLabelframe, text="INT", command=lambda:roll("Int"))
            INTBUTTON.pack()
            INTLabel = Label(INTLabelframe, text=INTSTAT) #INTSTAT
            INTLabel.pack()
            INTEntry = Entry(INTLabelframe, width=2)
            INTEntry.pack()
            INTLabelframe.pack()


            #WIS
            WISFrame = Frame(Statframe, bd=1, relief=SOLID)
            WISFrame.pack(side=LEFT)

            WISLabelframe = LabelFrame(WISFrame)
            WISBUTTON = Button(WISLabelframe, text="WIS", command=lambda:roll("Wis"))
            WISBUTTON.pack()
            WISLabel = Label(WISLabelframe, text=WISSTAT) #WISSTAT
            WISLabel.pack()
            WISEntry = Entry(WISLabelframe, width=2)
            WISEntry.pack()
            WISLabelframe.pack()

            #CHA
            CHAFrame = Frame(Statframe, bd=1, relief=SOLID)
            CHAFrame.pack()

            CHALabelframe = LabelFrame(CHAFrame)
            CHABUTTON = Button(CHALabelframe, text="CHA", command=lambda:roll("Cha"))
            CHABUTTON.pack()
            CHALabel = Label(CHALabelframe, text=CHASTAT) #CHASTAT
            CHALabel.pack()
            CHAEntry = Entry(CHALabelframe, width=2)
            CHAEntry.pack()
            CHALabelframe.pack()
            
            #DETAILS
            SecondaryFrame= Frame(Frame0, bd=2, relief=SOLID)
            SecondaryFrame.pack(fill=X)
            
            Blahblah = Label(SecondaryFrame, text=SSSL).pack() 
            
            #FEATURES
            FeatureFrame = Frame(Frame0, bd=2, relief=SOLID)
            FeatLabel = Label(FeatureFrame, text=FEATS) #FEATS --Can be left blank when not applicable!
            FeatLabel.pack()
            FeatureFrame.pack()     
            
            #ACTIONS
            ACTSFrame = Frame(Frame0, bd=2, relief=SOLID)
            ACTSLabel=Label(ACTSFrame, text="ACTIONS")
            ACTSLabel.pack()
            ACTION1 = Button(ACTSFrame, text=ATTACK1, command=lambda:roll("atk1"))
            ACTION1.pack()
            ACTION2 = Button(ACTSFrame, text=ATTACK2, command=lambda:roll("atk2"))
            ACTION2.pack()
            
            ACTSFrame.pack()


            MasterActionFrame = Frame(Frame0)
            MasterActionFrame.pack()

            ActionFrame = Frame(MasterActionFrame)
            ActionFrame.pack(side=LEFT)   




