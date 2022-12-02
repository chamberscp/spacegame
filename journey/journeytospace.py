import sys
import time

AP = 'Alpha_Proxima'    
EE = 'Epsillon_Eridani' 
HR = 'HR3259'           
LP = 'LP 890-9'         

a = 0.2
b = 0.2
c = 0.08
light = 299792458
mph = 0
v = 0
var1 = 1
WF = 1

days = 0
dayage = 7300
age = dayage/365

credits = 0
fuel = 0
warpSpeed = 0 #tbd



#=============================================  Game paths and loops ====================================



#================================== PLANET 1 SECTION 1: Intro to starter planet ========================
def P1_Sec1():
    print()
    print("(## DEEP SPACE III but in text! ###)")
    print("###  You must find your to way back to Earth, thinking carefully about your choices, aisde from worldy hazards, manage your resrouces to ensure survival ###")
    print("###  The game will end if you run out of fuel, make poor choices, or if your charater's age goes above 65 years, Good luck out there!                    ###")
    time.sleep(a)
    print()
    print()
    print("You feel as if your body was tossed about like a ragdoll, you stuggle to bring even your basic senses into focus")
    time.sleep(a)
    print("For a fraction of a second you feel an intense heat, and a flash blinds and disorents you even more then you were at first, and then like that, it passes...")
    time.sleep(a)
    print("After a few moments of shaking yourself and stuggling to stand, things slowly clear as you regain your bearing")
    time.sleep(a)
    print("your AI Apollo displays a message on your hud it reads APOLLO: NO BREATHABLE ATMOSPHERE DETECTED, NO SIGNS OF LIFE, EMERGENCY BEACON NON FUNCTIONAL")
    time.sleep(a)
    print("You look around you, seemingly nothing but barren wastes....but wait")
    time.sleep(a)
    print("you see something, a cave....")
    time.sleep(a)
    print("you head inside, as there is nothing else for miles....")
    time.sleep(a)
    print("Your helmet light cuts through the darkness...")
    time.sleep(a)
    print()
    question = '"I Have a bad feeling about this.. (you think to yourself)"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(b)
    print()
    print()
    print("As you venture inside you see the cave splits off into several tunnels....")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Go down the Left path, *you see what looks to be claw marks on the walls*....")
    time.sleep(a)
    print("Path #2: Go down the Center path, *you think to yourself you heard faint humming coming from this direction*....")
    time.sleep(a)
    print("Path #3: Go down the right path *you sense it's warmer down this path, and yet your body goes cold when you look at it*...")
    time.sleep(a)
    print()
    while True:
        Path_Planet1_path1 = input("Which path will you choose? (1/2/3): ")
        if Path_Planet1_path1 == '1':
            print()
            path1()
            break           
        elif Path_Planet1_path1 == '2':
            print()
            path2()
            break    
        elif Path_Planet1_path1 == '3':
            print()
            path3()
            break
        else:
            print("Invalid Input.")


#===============Planet one path 1: give player starting credits  ============
def path1():
    global credits
    print("As you go down the path you begin to see dried blood and old bones, human bones....")
    time.sleep(a)
    print("you can tell this tragedy happened a while ago, so you calm yourself and explore the room..")
    time.sleep(a)
    print("After the grizzly job of searching the bodies, you've collected 5000 Credits..maybe you'll find some use for these later....")
    time.sleep(a)
    credits = credits + 5000
    print()
    displayStats()
    print()
    time.sleep(a)
    print("nothing of value remains, you head back to where the cave splits....")
    time.sleep(a)
    print("you find the other paths are no longer there, the stone seemingly smoothed over, only the exit remains....")
    time.sleep(a)
    print("As you exit the cave your scanner starts beeping....")
    time.sleep(a)
    P1_Sec2()
    #some how in this path we need to add credits to the varriable posted at the top of the code

    

#===============Planet one path 2: give the player starting Fuel  ============
def path2():
    global fuel
    print("you walk the path until you come up to what looks like a large room")
    time.sleep(a)
    print("The humming getting stronger as you get close, you ready yourself for whatever danger may lurk inside...")
    time.sleep(a)
    print("upon closer inspection the room is filled with humming light blue crystals, 'dilithium!' you exclaim.")
    time.sleep(a)
    print("you carefuly extract every viable dilithium crystal from the deposits *you find enough for 100 standard galactic units of fuel")
    time.sleep(a)
    fuel = fuel + 100
    print()
    displayStats()
    print()
    print("nothing of value remains, you head back to where the cave splits....")
    time.sleep(a)
    print("you find the other paths are no longer there, the stone seemingly smoothed over, only the exit remains....")
    time.sleep(a)
    print("As you exit the cave your scanner starts beeping....")
    P1_Sec2()



#===============Planet one path 3: kill the player        ============
def path3():
    print("You walk down the path, you see a bright green glow that seems just around the bend, but you can't quite catch it...")
    time.sleep(a)
    print("You feel Darkness suddenly begin to envolpe you, your head swirls and you feel like the world itself is spinning around you....")
    time.sleep(a)
    print("As you feel your eyes close for what you know is the last time, you see the display on your arm from your suits AI Athena blares a warning but all too late.....")
    time.sleep(a)
    print("### ATHENA: INTENSE GAMMA RADIATION BURST DETECTED ###..")
    time.sleep(a)
    print("The light fades as last, at least you don't have to worry about finding your way home anymore.......")
    time.sleep(a)
    print("##--- GAME OVER- Cause: exploration hazard ---##")
    time.sleep(a)
    print("##--- PLEASE RESET THE GAME TO TRY AGAIN   ---##")
    time.sleep(a)
    sys.exit



###==================== PLANET 1 SECTION 2: Bastion city and starport ============== ###

def P1_Sec2():
    print("you look down at your scanner...")
    time.sleep(a)
    print("you see on your map a settlement has been detected 5km away....with water and O2 reserves running low, you decide to head there, what have you got to lose?")
    time.sleep(a)
    print("after slogging through the wastes for what feels like hours, but your chono tells you was barely an 45 minutes, you arrive at the edge of the settlement, must just be your mind playing tricks...")
    time.sleep(a)
    print("you see a street sign in galatic basic that reads...")
    time.sleep(a)
    print("---Welcome to Bastion: last remaining city of Alpha Centari---")
    print("---               SPACEPORT: 500m <==                      ---")
    print("---               RUSTY'S SUPLLY: 200m ==>                 ---")
    print("---               EMERGENCY SHELTER: 50m ^                 ---")
    print("---               CITY POPULATION: ( 1 )                   ---")
    time.sleep(a)
    print("you think to yourself Alpha Centari is a Star not a planet, rather odd.......")
    time.sleep(a)
    print()
    print("Path #1: Head to the SPACEPORT, Maybe if you are lucky there is a ship to escape this wasteland......")
    time.sleep(a)
    print("Path #2: Head to the supply store, maybe you can find supplies..")
    time.sleep(a)
    print("Path #3: Head to the emergency shelter, maybe you can find some food and water and more importantly some o2 tanks to fill your reserves....")
    time.sleep(a)
    print()
    
    while True:
        Planet1_path2 = input("Which path will you choose? (1/2/3): ")
        if Planet1_path2 == '1':
            print()
            Sec2_path1()
            break
        elif Planet1_path2 == '2':
            print()
            Sec2_path2()
            break
        elif Planet1_path2 == '3':
            print()
            Sec2_path3()
            break
        else:
            print("Invalid Input.")
 
#================= Planet 1: Supply store section (alows the player to convert fuel to credits or vise versa) ======================

def Sec2_path2():
    print("you decide the Supply store would be the best place to start")
    time.sleep(a)
    print("As you make your way through the streets, the erie silence becomes ever more present in your mind, you wonder what happened to his world, or how off course you could have gotten")
    time.sleep(a)
    print("After all, there were not supposed to be any human settled worlds on the hyper route you were taking, not at least until the very end when you reached Pinnacle station")
    time.sleep(a)
    print("A few minutes later you arrived at the store, all signs point to it being throughly emptied quite a while ago")
    time.sleep(a)
    print("Knowing how Important it is that you find supplies quickly, you check the store thoroughly, at the back you find a service droid covered in dust.. ")
    time.sleep(a)
    print("You press the activation screen and it flickers to life..")
    time.sleep(a)
    print("<CUSTOMER_LOGIN> GGG...GGRRRR...GRRRREEE....GREETINGS <CUSTOMER_ID STRING NOT FOUND> and welcome to <INSERT_COUNTRY_STYLE_WELCOME_STRING> RUSTY'S Supply..")
    time.sleep(a)
    print("you decide the Supply store would be the best place to start")
    time.sleep(a)






#================ Planet 1: Shelter section (kills the player) ============================
def Sec2_path3():
    print("You Decide the SHELTER is your best bet, you follow the signs..")
    time.sleep(a)
    print("You begin walking down the street.  It looks like people left in a hurry and in a panic.  There is trash and abandoned vehicles everywhere. ")
    time.sleep(a)
    print("As you arrive a the shelter, you notice that it was once barricaded.  Now however, is an open hole coverd by a sheet, and it looks like the")
    print("roof caved in at some point..")
    time.sleep(a)
    print("You make your way inside and find it empty.")
    time.sleep(a)
    print("It once must have housed a thousand people.  There are countless metal bunk beds strown about.")
    time.sleep(a)
    print("It looks like someone brought in some barrells to use as warming fires at some point.")
    time.sleep(a)
    print("You can't seem to find anything useful as you look around.  You make your way towards the back of the shelter.  Surely they must have had supplies in the back.")
    time.sleep(a)
    print("As you enter the back room, your eyes struggle to adjust to the darkness of this room.  You reach out to try and find a light switch even though you can tell there hasn;t been power here for a long time.  You tell yourself that old habits are...")
    time.sleep(a)
    print("....")
    time.sleep(a)
    print("....")
    time.sleep(a)
    print("....")
    time.sleep(a)
    print("You slowly fade into conciousness realizing that your head hurts profusely and that the back of your head feels wet..")
    time.sleep(a)
    print("Your wits start to trickle back and you realize that you can't move.")
    time.sleep(a)
    print("Your hands and feet are bound.  You realize that someone must have been hiding in the dark and struck you when you entered the room..")    
    time.sleep(a)
    print("Suddenly you feel hear a voice behind you.")
    time.sleep(a)
    print()
    print("Hello.  What a fine day for a visiter.  It has been forever since someone showed up here.  Fortune has smiled upon me.")
    time.sleep(a)
    print()
    print("You start to feel a sense of relief.  You can probably just get the man to let you go once you prove you are no threat.")
    time.sleep(a)
    print()
    print("You are a welcome treat the man says as he clasps his hands with a smile. I had to raid the animal shelter weeks ago and I'm almost out of dog meat from the kennels.  You will make a tasty soup.")
    time.sleep(a)
    print()
    print("Just as you are about to protest, the man grabs a hammer from a table and strikes you in the front of the head.")  
    time.sleep(a)
    print("Your mind races as everything begins to fade to black.")
    print("##--- GAME OVER- Cause: exploration hazard ---##")
    time.sleep(a)
    print("##--- PLEASE RESET THE GAME TO TRY AGAIN   ---##")
    time.sleep(a)
    sys.exit 
        
     
#================== Planet 1: Starport section best option, utilizes fuel or credits and leaves planet, go to travel section ==========================       

def Sec2_path1():
    global fuel
    global credits
    print("You Decide the SPACEPORT is your best bet, you follow the signs..")
    time.sleep(a)
    print("after some time you come to the SPACEPORT, no signs of life, its erie and quiet, your AI reports even no microorganisms....")
    time.sleep(a)
    print("You walk through the seemingly countless empty docks, until at the very end you find a single ship, covered in dust but otherwise intact.. ..")
    time.sleep(a)
    print("as you board the vessle it seems funtional, main power even still works, the terminal is still linked to the ports automated system....")
    time.sleep(a)
    print("you press the flashing button on the panel to activate the AI..")
    time.sleep(a)
    print("<CUSTOMER_LOGIN> GGG...GGRRRR...GRRRREEE....GREETINGS <CUSTOMER_ID STRING NOT FOUND> and welcome to Bastion Port, it looks like your ship is <READY> to fly!..")
    time.sleep(a)
    print("the AI goes on: It seems your ship is lacking fuel, please ensure sufficient <MIN 50 STANDARD FUEL UNITS> dilithium has been placed in fuel storage cells....")
    time.sleep(a)
    print("AI: for a one time fee of <[2500]> Galactic Credits (all taxes and fees included) Bastion Port systems will automaticly refuel your ship and ensure you are flight <SYSTEM_CHECK_GREEN>!..")
    time.sleep(a)
    print("you look at the display, feeling as this choice will have a lasting impact on you....")
    time.sleep(a)
    print()
    print("Path #1: Pay for the automated system to refuel the ship for you (requires 2500 credits, in exchange for 50 units of fuel)....")
    time.sleep(a)
    print("Path #2: Attempt to reful the ship yourself (requires at least 50 standard units of fuel minimum)...")
    time.sleep(a)
    print()
   
    while True:
        Planet1_path3 = input("Which path will you choose? (1/2): ")
        print()
        if Planet1_path3 == '1' and credits > 2500:
            credits = credits - 2500
            fuel = fuel + 50
            print()
            Sec2_path1_1()
            break
        elif Planet1_path3 == '1' and credits < 2500:
            print("Insufficient credits, please choose another option")
            time.sleep(a)
        elif Planet1_path3 == "2" and fuel > 50:
            fuel = fuel - 50
            print()
            Sec2_path1_2
            break
        elif Planet1_path3 == "2" and fuel < 50:
            print("Insufficient fuel, please choose another option")
            time.sleep(a)
        else:
            print("Invalid Input.")



#================================= P1 STarport credits accepted path =========================

def Sec2_path1_1():
    print("<PAYMENT RECIVED> TTHH--- THHHAA--- THANK YOU! payment accepted, Please enjoy some complimentary refreshments, courtesy of Bastion port! ")
    time.sleep(a)
    print("A nearby terminal opens a panel, sealed packages containing emergency water rations and food stuffs of questionable quality are presented, you take them greedily.")
    time.sleep(a)
    print("After eating in the Sealed safty of the ship while the station refuled and prepared the ship, you take a moment to check the NAV computer and see only one destination point, a relay point in high orbit....")
    time.sleep(a)
    print("Worst case you think to yourself, you can try and scan again from orbit, you double check flight preperations.....")
    time.sleep(a)
    print("You take one last scan of the planet with the ships sensors, no signs of life, no settlements besides ruins and rubble....")
    time.sleep(a)
    print("Stories of devastated worlds in the outer colonies, had reached you before, but those were supposed to be only rumors.....")
    time.sleep(a)
    print("you look at the display....")
    time.sleep(a)
    print()
    question = '"You Sense as if a Important moment is upon you, almost as if a chapter of your life is about to unfold )"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(b)
    print()
    displayStats()
    print()
    print()
    pick_Planet()
    print()


#==============P1 Starport Fuel accepted path =======================
def Sec2_path1_2():
    global fuel   
    print("Using a large portion of the crystals you have, you fill the fuel cells, ")
    time.sleep(a)





#============= Planet choice / warp travel section ================================ 

def pick_Planet():
    print()
    print("Ship Sensors pick up several operational gates in system, but you don't recognize any of the names... ")
    time.sleep(a)
    print("The Nav computer does not have the data saved either, the realization hits your, you'll have to gamble your fuel and your life to make a jump to a random system that you don't even know will work ....")
    time.sleep(a)    
    print("you closely examine the list beacons your AI Ares displays for you... ")
    time.sleep(a)
    print("########################################################################################")
    print("Ares: (1)  'Alpha Proxima'    #   4.2c Light years away      # Has 2 known planets      ")
    print("Ares: (2)  'Epsillon_Eridani' # 10.50c Light years away      # Has 1 known planet       ")
    print("Ares: (3)  'HR3259'           # 41.04c Light years away      # Has 3 known planets      ")
    print("Ares: (4)  'LP 890-9'         #   105c Light years away      # Has 1 known planet       ")
    print("########################################################################################")
    print()
    displayStats()
    print()
    getTime()
    
    
def getTime():
    global v
    global mph
    global days
   
    m = input('Where would you like to go? ')
    print(m)
    if m == '1':
        dist = 2.5219*(10**13)
        print(f'{AP} is 4.29 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24
        print(f'It will take {days} days to get to {AP}')
        print(f'It will take 6 units of fuel to get to {AP}.  You currently have {fuel} units.')
        go_to_Alpha_Proxima()
    
    elif m == '2':
        dist = 6.1726*(10**13)
        print(f'{EE} is 10.50 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24
        print(f'It will take {days} days to get to {EE}')
    
    elif m == '3':
        dist = 241259000000000
        print(f'{HR} is 41.04 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24      
        print(f'It will take {days} days to get to {HR}') 
     
    elif m == '4':
        dist = 617300000000000
        print(f'{LP} is 105 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24      
        print(f'It will take {days} days to get to {LP}')

def getVelocity(): # Get V in m/s
    global v
    global mph
    global WF
    WF =input('Please enter the warp speed (0-10) that you would like to go (and keep in mind that the faster you will go you will burn more fuel, but age less): ')
    
    if WF == '1':
        v = light * 1
    elif WF == '2':
        v = light * 8
    elif WF == '3':
        v = light * 27
    elif WF == '4':
        v = light * 50 #64
    elif WF == '5':
        v = light * 125
    elif WF == '6':
        v = light * 216
    elif WF == '7':
        v = light * 343
    elif WF == '8':
        v = light * 512
    elif WF == '9':
        v = light * 729
    elif WF == '10':
        v = light * 1000
    else:
        print('Improper Warp Factor')          
    
    mph = v * 2.237
    print(f'Velocity is equal to {mph} mph')
    
              

def go_to_Alpha_Proxima():
    ageCalc()
    print(f'{age}')
    print("SETUP ALPHA PROXIMA STORY")

def go_to_wolf359():
    print('SETUP WOLF359 STORY')

def go_to_Epsillon_Eridani():
    print('')

def go_to_HR3259():
    print('')

def go_to_LP890():
    print('')
    

#============= Player calculations ================================ 
def displayStats():
    print(f"///// Fuel = {fuel} units ///// Current Age = {age} ///// Credits = {credits} /////")


def ageCalc():
    global dayage 
    global age
    global days
    dayage = (age*365) + days
         

    
#=================== Main Menu / Start Game Function =========

print()
print()
print("     #############################")
print("     |                           |")
print("     |   Journey To Space  III   |")
print("     |                           |")
print("     |                           |")
print("     #############################")
print()
print()
time.sleep(a)
print("##           -= Journey To Space III, but in TEXT!  =-                       ##")
time.sleep(a)
print("## You awake in a crashed escape pod on a desolate world                     ##")
time.sleep(a)
print("## Before you lies the daunting task of finding your way back to Earth       ##")
time.sleep(a)
print("## The journey will be hard, do you have what it takes?                      ##")
time.sleep(a)
print()

while True:
    startGame = input("Would you like to start the game? (Y/N): ")
    if startGame == "n" or startGame == "N":
        print("Maybe next time")
        time.sleep(3)
        break
    elif startGame == "y" or startGame == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
        break
    else:
        print("Would you like to start the game? (Y/N): ")