import random
import sys
pick = ['Attack', 'Parry', 'Force']
complement = ['Impressive...Most impressive...', 'The Force is with you, but you are not a Jedi yet!', "I see you're full of surprises!", "I've got a good feeling about this..."]
winquote = ['The Force is strong in my family...', 'Now *I* am the Master!', ]
insult = ["Your feelings betray you. Don't trust them.", "All too easy...", "So uncivilized...", "Control! Control! You must learn control!", "Try spinning. Thats a good trick!"] 
p_APS = [1,1,1]
e_APS = [1,1,1]
alignment = 0
You = 'Jedi'
clashy = random.randint(0,1)

#On a standard game, HP, eHP,  qi and e_qi are all set to 3
#p_APS = player "attack/parry/special" e_APS = ENEMY attack/parry/special
HP = random.randint(1,6)
eHP = random.randint(1,6)
qi = random.randint(1,6)
e_qi = random.randint(1,6)
e_boost = ['Anger','Fear', 'Confusion']

def game():
    global You
    global alignment
    global qi
    global e_qi
    global ans
    num = random.choice(pick)
    clashy = random.randint(0,1)
    print('[', You ,']', 'HP:',HP, '  Force:', qi,'           [Jargia] HP:', eHP, ' Force:', e_qi)
    ans = int(input('1) Attack  2) Parry 3) FORCE    4)QUIT '))
    print()
    if ans == 1:
        print('You swing your lightsaber as you take the offensive!')
        if num == pick[0]:
            print('[DRAW]')
            print('You exchange wild flurries of blows! You and your opponent both struggle to land a decisive hit!')
            print()
            print('As your blades lock in a deadly power struggle, the enemy taunts', random.choice(insult))
            print()
            clash()    
        if num == pick[1]:
            print('[LOSE]')
            print('Your enemy anticipated your attack and outmaneuvered you with a parry!')
            print('The enemy sneers', "'",random.choice(insult),"'")
            pointloss() 
        if num == pick[2]:
            if e_qi > 0:
                e_qi -= 1
                print('[WIN]')
                print('Your enemy was reaching out to the Force... But they left themselves open for your attack!')
                pointplus()
            if e_qi <= 0:
                e_qi = 0
                print('[WIN]')
                print('Your enemy was reaching out to the Force... But they left themselves open for your attack!')
                pointplus()
    if ans == 2:
        print('You take a defensive stance, ready for the enemy to attack!')
        if num == pick[0]:
            print('[WIN]')
            print("You feel the Force flowing through you, guiding you as your lightsaber deflects each volley of the enemy's onslaught.")
            print("With a combination of skill and trust in the Force, you succeed in finding a window of opportunity...")
            print()
            print('Your laser sword catches your enemy at an exposed opening!')
            print('Pained, your enemy seethes,', "'",random.choice(complement),"'")
            pointplus()    
        if num == pick[1]:
            print('[DRAW]')
            print("You both stare at one another through the Force, anticipating the other's next move...")
            print('Your opponent says, I sense the conflict in you...')
            clash() 
        if num == pick[2]:
            e_qi -= 1
            if e_qi > 0:
                print('[LOSE]')
                print('Your enemy attacks with the Force in a way your defenses could not have prepared you for!')
                pointloss()
            else:
                e_qi = 0
                print('[DRAW]')
                print('Your enemy raises their hand and draws from the Force....')
                print('But then realizes they lack the endurance to do that!')
                print()
                game()  
    if ans == 3:
        qi -= 1
        if qi < 0:
            qi = 0
        print('You focus, summon the Force, and prepare to use it as your ally...')
        if num == pick[0]:
            print('[LOSE]')
            print('Oh no! Your opponent rushes for the attack, catching you off guard!')
            pointloss()    
        if num == pick[1]:
            if qi > 0:
                print('[WIN]')
                print('Your technique surprises your enemy, throwing them for a loop!')
                pointplus()
            else:
                print('[DRAW]')
                print('The enemy falls for your bluff, momentarily losing the resolve to attack!')
                print()
                game()
        if num == pick[2]:
            e_qi -= 1
            print('[DRAW]')
            print('Darn! The enemy read your movements and saw your techniqe coming!')
            print()
            game()
    if ans == 4:
        print()
        print('Thank you for playing! Goodbye!')
        sys.exit()
    else:
        game()
            
            
def pointplus():
    global alignment
    global eHP
    if ans == 1:
        eHP -= p_APS[0]
    if ans ==2:
        eHP -= p_APS[1]
    if ans ==3:
        eHP -= p_APS[2]
    if eHP == 0 or eHP <0:
        print()
        print('Jargia is beaten! Too proud to speak, his eyes plead for mercy.')
        print('The Jedi way abhors needless bloodshed. But you are not certain he will not take advantage of that whether now,')
        print('or some time in the future.  Beneath the glow of your lightsaber, his expression contorts in fear')
        print('and anticipation as you prepare to finalize your judgment...')
        print()
        mercy = int(input('Do you grant mercy to your enemy?    1)Y   2)N  '))
        if mercy == 1:
            alignment +=3
            print()
            print('Perhaps you may regret your lenience someday...')
            print('But for now, peace will prevail. You summon his lightsaber and clip it onto your belt.')
            print('Weakened from his wounds and anesthetised with relief, Jargia peacefully surrenders consciousness.')
            print()
            print('You load him onboard your ship. By the time he awakens, he will have to answer to the court of the Senate.')
            print()
            print('Congratulations. You win!  [Mercy Ending]')
            morality()
        if mercy == 2:
            alignment -=5
            print()
            print('Perhaps you may regret your harshness someday...')
            print('But for now, it is clear that imprisonment is too good for the likes of this bloodthirsty traitor.')
            print('The swift justice of your lightsaber proves to be most effective as Jargia topples to the ground in two pieces.')
            print('You board your ship knowing that you will have to answer for this someday.')
            print()
            print('But perhaps in time, the galaxy will thank you for this before that day comes...')
            print()
            print('Congratulations. You win!  [Wrath Ending]')
            morality()
        else:
            print()
            print('Congratulations. You win! [Undecided Ending]')
            sys.exit()
    else:
       print()
       game()
       
def pointloss():
    global HP
    HP = HP - 1
    if HP == 0:
        print()
        print("Jargia has beaten you.")
        print('His laugh sullies your dying thoughts. As your life fades, your lightsaber')
        print('leaps into his open hand. The last thing you see is')
        print("Jargia's grip crushing the hilt of your weapon, snuffing it out")
        print("ensuring that it joins you in your fate....")
        print()
        print('Game over! Thank you for playing!  [Bad Ending]')
        sys.exit()
    else:
       print()
       game()

def dialogue():
    global alignment
    global qi
    global HP
    global p_APS
    print()
    print('In response, you yield yourself to the Force, giving yourself particularly to...')
    response = int(input('1)Anger  2)Tranquility  3)Nothingness '))
    print()
    if response == 1:
            alignment -=1
            p_APS[0] += 1
            HP += random.randint(1,3)
            print()
            print('A surge of energy you sense to be the dark side of the Force begins to flow through you.')
            print('From deep within you, a guttural roar bellows: You will turn from your ways...or PERISH!!')
            print()
            game()
    if response == 2:
            alignment +=1
            p_APS[1] += 1
            HP += random.randint(1,3)
            print()
            print('A calm warmth you sense to be the light side of the Force begins to flow through you.')
            print('From deep within you, a gentle assurance whispers: The Force will be with you...always')
            print()
            game()
    if response == 3:
            p_APS[2] += 2
            qi += random.randint(1,3)
            print()
            print('A subtle chill you sense to be the Force begins to flow through you.')
            print('From deep within you, a temperant knowing echoes: In victory or defeat, I serve the will of the Force...')
            print()
            game()
        
def morality():
    if alignment <= -5:
        print()
        print('The Dark Side has noticeably begun to grip you.')
        print('Perhaps meditation and council from your fellow Jedi will')
        print('help you make peace with your trials before it is too late.')
        print('Yet somehow, you can already sense that there is far too much')
        print("they simply wouldn't understand....")
        print()
        print('[End--Dark Side]                                   Score:', alignment)
        sys.exit()
    if alignment >= 5:
        print()
        print('You leave the planet Sullust with a bond closer to the Light.')
        print('Perhaps this was a trial granted to you not by the Jedi Council,')
        print('but rather by the will of the Force itself.')
        print('As your hyperdrive catapults you toward Coruscant, you can only wonder')
        print('what more the Force has in store for your bright destiny.')
        print()
        print('[End--Light Side]                                    Score:', alignment)
        sys.exit()
    if alignment >= -4 and alignment <4:
        print()
        print('As Sullust becomes more distant, you feel the Force call to you...')
        print('It tells you NOT to return to Coruscant?...That there is a different')
        print('purpose in store for you...')
        print('Before you can rationalize, your hands are already busy at work setting')
        print("a course for a system you've never even heard of...Dagobah?")
        print("You engage your hyperdrive and wonder what the Force is asking you to trust now...")
        print()
        print('[End--Gray Side]                                     Score:', alignment)
        sys.exit()
    
def enemyboost():
    global e_qi
    global eHP
    global e_APS
    pwr_up = random.choice(e_boost)
    if pwr_up == e_boost[0]:  #Anger/Attack
        e_APS[0] +=1
        eHP += random.randint(1,3)
        print()
        print("Jargia savagely claws into your mind with the Force...")
        print("Only your ANGER can defeat me,", You,"!  Your Jedi ways are holding you back!")
        print()
        game()
    if pwr_up == e_boost[1]:  #Fear/Parry
        e_APS[1] +=1
        eHP += random.randint(1,3)
        print()
        print("Jargia reaches into your mind, wielding more strength in the Force than you initially would have presumed...")
        print("He looks deeply into your eyes. 'I sense a great fear in you,", You,"Give in to it. Accept your destiny!'")
        print()
        game()
    if pwr_up == e_boost[2]:  #Confusion/Force
        e_APS[2] +=1
        eHP += random.randint(1,3)
        print()
        print("Jargia laces his words with the subtlety of the Dark Side...")
        print( You, "...The Jedi withhold the true secrets of the power the Force can offer those who are open to its riches!")
        print("Join me, and I can show you true power!")
        print()
        game()

def clash():
    clashy = random.randint(0,1)
    if clashy == 0:
        dialogue()
    if clashy == 1:
        enemyboost()

        
     
        
def startgame():
    print()
    global You
    You = input("What is your name, young Jedi?  ")
    print()
    print("At long last you've found Jargia Fauluum!")
    print("The Republic traitor and secret Sith apprentice had been in hiding on the mining system of Sullust.")
    print("You,",You,", a newly appointed Jedi Knight, have been tasked with bringing him to justice for his crimes against the Jedi and the Republic.")
    print("The Council requests you bring him back alive if at all possible.")
    print("The time for negotiation has passed. He ignites his lightsaber, its crimson red tinting your surroundings with its sinister hue.")
    print("In turn yours livens with a hauntingly familiar snap-hiss. Your sabers hum in bitter anticipation for the inevitable...")
    print()
    game()




def title():
    print("Star Wars: Jedi Battle   [v0.98]")
    tut = int(input("[1] Start Game   [2] Tutorial  [3] Quit "))
    if tut == 1:
        startgame()
    if tut == 2:
        tutorial()
    if tut == 3:
        sys.exit()
        
def tutorial():
    print()
    print("                          [Combat Basics]            ")
    print("Combat is comprised of three basic actions: ATTACK, PARRY, and FORCE")
    print("ATTACK -- Charge at the enemy with your lightsaber.")
    print("       *Overwhelms the concentration of one trying to use the FORCE.")
    print("       *Backfires against one who is ready to PARRY.")
    print("       *Draws with ATTACKS resulting in a  'Clash' (more on that later)")
    print()
    print("PARRY -- A defensive stance, vigilant for an opportunity to retaliate.")
    print("       *Counters ATTACK")
    print("       *Two PARRYs may result in a dialogue, similar to a 'Clash'")
    print("       *PARRY is overpowered by use of the FORCE")
    print()
    print("FORCE -- Use the Force for a chance at gaining an advantage in combat.")
    print(" NOTE: Each use of the Force consumes 'Force'. Even when depleted, the Force")
    print("       can still be called upon as a feint, resulting in no damage against your foe")
    print()
    print("       *Use of the Force requires concentration, leaving one open to ATTACK")
    print("       *One who PARRYs is not prepared for the power of the FORCE...")
    print("       *When two skilled FORCE users call upon this power at the same time")
    print("        the result ends in a stalemate. However, both users are exerted.")
    print()
    print("                             [Clashes]    ")
    print(" Your choices in combat will have an influence on your Jedi path. There will be opportunities")
    print("to call upon the Force in combat to augment your abilities. Know that your enemy can do the same.")
    print("Should the chance present itself, try many avenues to victory.")
    print("Will you stay the Jedi path? Or will the Dark Side command your destiny....")
    print()
    print("                 Good luck! And May the Force Be With You!")
    print('\n' *4)
    title()
    
title()
    
    


