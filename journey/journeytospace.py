import sys
import time

a = 0.2
b = 0.2
c = 0.08

credits = 0
age = 20
fuel = 0
warpSpeed = 0 #tbd



#================================== Game paths and loops =========



#================================== PLANET 1 SECTION 1: Intro to starter planet ========================
def P1_Sec1():
    print()
    print("(## DEEP SPACE III but in text! ###)")
    time.sleep(a)
    print("You feel as if your body was tossed about like a ragdoll, you stuggle to bring even your basic senses into focus")
    time.sleep(a)
    print("For a fraction of a second you feel an intense heat, and a flash blinds and disorents you even more then you were at first, and then like that, it passes...")
    time.sleep(a)
    print("After a few moments of shaking yourself and stuggling to stand, things slowly clear as you regain your bearing")
    time.sleep(a)
    print("your display reads: NO BREATHABLE ATMOSPHERE DETECTED, NO SIGNS OF LIFE, EMERGENCY BEACON NON FUNCTIONAL")
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
    Path_Planet1_path1 = input("Which path will you choose? (1/2/3): ")
    if Path_Planet1_path1 == '1':
        print()
        path1()
    elif Path_Planet1_path1 == '2':
        print()
        path2()
    elif Path_Planet1_path1 == '3':
        print()
        path3()


#===============Planet one path 1: give player starting credits  ============
def path1():
    print("As you go down the path you begin to see dried blood and old bones, human bones....")
    time.sleep(a)
    print("you can tell this tragedy happened a while ago, so you calm yourself and explore the room..")
    time.sleep(a)
    print("After the grizzly job of searching the bodies, you've collected 5000 Credits..maybe you'll find some use for these later....")
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
    print("you walk the path until you come up to what looks like a large room")
    time.sleep(a)
    print("The humming getting stronger as you get close, you ready yourself for whatever danger may lurk inside...")
    time.sleep(a)
    print("upon closer inspection the room is filled with humming light blue crystals, 'dilithium!' you exclaim.")
    time.sleep(a)
    print("you carefuly extract every viable dilithium crystal from the deposits *you find enough for 100 standard galactic units of fuel")
    time.sleep(a)
    # and here we need to add 100 to the unit for fuel
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
    print("As you feel your eyes close for what you know is the last time, you see the display on your arm from your suits AI blares a warning but all too late.....")
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
    Planet1_path2 = input("Which path will you choose? (1/2/3): ")
    if Planet1_path2 == '1':
        print()
        Sec2_path1()
    elif Planet1_path2 == '2':
        print()
        Sec2_path2()
    elif Planet1_path2 == '3':
        print()
        Sec2_path3()

def Sec2_path2():
    pass

def Sec2_path3():
    pass

#================== Planet 1 Starport section ==========================       

def Sec2_path1():
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
    print("Path #1: Pay for the automated system to refuel the ship for you (requires 2500 credits minimum)....")
    time.sleep(a)
    print("Path #2: Attempt to reful the ship yourself (requires at least 50 standard units of fuel minimum)...")
    time.sleep(a)
    print()
    Planet1_path3 = input("Which path will you choose? (1/2): ")
    print()
    if Planet1_path3 == '1':
        print()
        Sec2_path1_1()
    elif Planet1_path3 == '2':
        print()
        print("aint ready yet")
    #elif print("insufficient Fuel, PLEASE CHOOSE ANOTHER OPTION")
    #elif Path_p1s == '2' #and credits is  > 2500  ============= need to add in the credit check and conversion  
    #     print()
    #     Sec2_path2.1() #tbd
    #elif Path_p1s1 == '3':
    #    print()
    #    Sec2_path3.1() #tbd

# this is where we will need either the fuel or the credit function checked and called
# either one allowing player progress

#===== P1 SP credits accepted path ====

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
    pick_Planet()
    print()

#============= Planet choice / warp travel section ================================ 

def pick_Planet():
    print()
    print("Ship Sensors pick up several operational gates in system, but you don't recognize any of the names... ")
    time.sleep(a)
    print("The Nav computer does not have the data saved either, the realization hits your, you'll have to gamble your fuel and your life to make a jump to a random system that you don't even know will work ....")
    time.sleep(a)    















#=================== Main Menu / Start Game Function =========

print()
print()
print("     ######################")
print("     |                    |")
print("     |   DEEP SPACE III   |")
print("     |                    |")
print("     ######################")
print()
print()
time.sleep(a)
print("##           -= DEEP SPACE III, but in TEXT!  =-                       ##")
time.sleep(a)
print("## You awake in a crashed escape pod on a desolate world               ##")
time.sleep(a)
print("## Before you lies the daunting task of finding your way back to Earth ##")
time.sleep(a)
print("## The journey will be hard, do you have what it takes?                ##")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    P1_Sec1()