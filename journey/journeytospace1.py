import sys
import time


AP = 'Alpha_Proxima'    
EE = 'Epsillon_Eridani' 
HR = 'HR3259'           
LP = 'LP 890-9'         

a = 2.6
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
gameover = False


#=============================================  Game paths and loops ====================================



#================================== PLANET 1 SECTION 1: Intro to starter planet ========================
def P1_Sec1():
    print()
    print("###                                               DEEP SPACE III but in text!                                                                            ###")
    print("###  You must find your to way back to Earth, thinking carefully about your choices, aisde from worldy hazards, manage your resrouces to ensure survival ###")
    print("###  The game will end if you run out of fuel, make poor choices, or if your charater's age goes above 65 years, Good luck out there!                    ###")
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
    print()
    print("---  Welcome to Bastion: last remaining city of Alpha Centari  ---")
    print("---                 SPACEPORT: 500m <==                        ---")
    print("---                 RUSTY'S SUPLLY: 200m ==>                   ---")
    print("---                 EMERGENCY SHELTER: 50m ^                   ---")
    print("---                 CITY POPULATION: ( 1 )                     ---")
    print()
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
    global fuel
    global credits
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
    print("Currently <ENTIRE_INVENTORY> Is out of stock and on back order, but our SAVE-ALOT barter system is still the best price in the sytem.. ")
    time.sleep(a)
    print("You look down at the near by barter terminal.. ")
    time.sleep(a)
    print("Dilithum crystals: 1 unit for 50 Galactic credits or 50 Galactic credits for each unit of refined Dilithum fuel, no hidden taxes or fees! equal trade value both ways!")
    time.sleep(a)
    print("minimum trade in values set 2500 credits for 50 units of fuel, or 50 units of fuel for 2500 credits, we even offer 10 unit of fuel and 500 credits on the house as a thank you for Trusting Rusty's supply")
    time.sleep(a)
    print()
    print("########################################################")
    print("Option #1: Convert 2500 credits to 50 refined Dilithum fuel units")
    time.sleep(a)
    print("Option #2: Convert 50 Dilithum crystals to 2500 Credits")
    time.sleep(a)
    print("#########################################################")
    print()
    print("Option #3: you think to yourself, you could always just leave and head to the starport now")
    time.sleep(a)
    while True:
        storeconvert = input("Which Option will you choose? (1/2/3): ")
        if storeconvert == '1' and credits >= 2500:
            credits = credits -2500
            fuel = fuel + 60
            print()
            print("Trade in accepted, processing")
            time.sleep(a)
            print()
            time.sleep(a)
            displayStats()
            print()
            time.sleep(a)
            print("You decide to take your new found wealth to the Starport, hopefully you can make good use of it there...")
            time.sleep(a)
            print()
            Sec2_path1()
            time.sleep(a) 
        elif storeconvert == '1' and credits <= 2500:
            print("Insufficient credits, please choose another option")           
        elif storeconvert == '2' and fuel >= 50:
            credits = credits +3000
            fuel = fuel -50
            print()
            print("Trade in accepted, processing")
            print()
            time.sleep(a)
            displayStats()
            time.sleep(a)
            print()
            print("You decide to take your newfound wealth to the Starport, hopefully you can make good use of it there...")
            time.sleep(a)
            print()
            Sec2_path1()
            time.sleep(a)
            break
        elif storeconvert == '2' and fuel < 50:
            print("Insufficient fuel, please choose another option")
            time.sleep(a)   
        elif storeconvert == '3':
            print()
            print("you decide to head to the startport instead, maybe you can find some better options there...")
            time.sleep(a)
            print()
            print()
            Sec2_path1()
            time.sleep(a)
            break
        else:
            print("Invalid Input.")






#================ Planet 1: Shelter section (kills the player) ============================
def Sec2_path3():
    print("You Decide the SHELTER is your best bet, you follow the signs..")
    time.sleep(a)
    print("You begin walking down the street.  It looks like people left in a hurry and in a panic.  There is trash and abandoned vehicles everywhere. ")
    time.sleep(a)
    print("As you arrive a the shelter, you notice that it was once barricaded.  Now however, is an open hole coverd by a sheet, and it looks like the roof caved in at some point..")
    time.sleep(a)
    print("You make your way inside and find it empty.")
    time.sleep(a)
    print("It once must have housed a thousand people,  There are countless metal bunk beds strown about.")
    time.sleep(a)
    print("It looks like someone brought in some barrels to use as warming fires at some point.")
    time.sleep(a)
    print("You can't seem to find anything useful as you look around.  You make your way towards the back of the shelter.  Surely they must have had supplies in the back.")
    time.sleep(a)
    print("As you enter the back room, your eyes struggle to adjust to the darkness of this room.  You reach out to try and find a light switch even though you can tell there hasn't been power here for a long time.  You tell yourself that old habits are...")
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
    print("Suddenly youy hear a voice behind you.")
    time.sleep(a)
    print()
    question = "Hello.  What a fine day for a visiter.  It has been forever since someone showed up here.  Fortune has smiled upon me."
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(a)
    print()
    question = '"You start to feel a sense of relief.  You can probably just get the man to let you go once you prove you are no threat.'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(a)
    print()
    question = '"You are a welcome treat the man says as he clasps his hands with a smile. I have survived of nutri-packs for far too long, You will make a a fine meal..."'
    for character in question: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(a)
    print()
    print("Just as you are about to protest, the owner of the voice comes into view, what at first seemed like a man, is in fact a hideous amalgamation of man and machine..")  
    time.sleep(a)
    print("Gleeming red eyes pierce your skull, a dark metal body only partially hidden by strips of dried and leathery skin, dried dark red blood splatters cover the cloth it drapes itself in,..")  
    time.sleep(a)
    print("some sort of pale imitation of a human being, pretending in its own cursed way to walk and act like at least a once human figure..")
    time.sleep(a)
    print("He reveals a hand with with a dozen small blades in place of fingers..")
    time.sleep(a)
    question = '"Let this final thought comfort you mortal, your death will be swift...."'
    for character in question: 
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(a)
    print("With a utterly efficient and swift strike, the monsters bladed hand is plunged right into your heart... ")
    time.sleep(a)
    print("Your mind races as everything begins to fade to black.")
    print()
    print()
    print("##--- GAME OVER- Cause: exploration hazard ---##")
    time.sleep(a)
    print("##--- PLEASE RESET THE GAME TO TRY AGAIN   ---##")
    time.sleep(a)
    sys.exit 
        
     
#================== Planet 1: Starport section best option, utilizes fuel or credits and leaves planet, go to travel section ==========================       

def Sec2_path1():
    global fuel
    global credits
    print("You make your way to the SPACEPORT, you follow the signs as the scilence gnaws at you..")
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
    print("the Port AI goes on: It seems your ship is lacking fuel, please ensure sufficient <MIN 50 STANDARD FUEL UNITS> dilithium has been placed in fuel storage cells....")
    time.sleep(a)
    print("Port AI: for a one time fee of <[2500]> Galactic Credits (all taxes and fees included) Bastion Port systems will automaticly refuel your ship and ensure you are flight <SYSTEM_CHECK_GREEN>!..")
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
        if Planet1_path3 == '1' and credits >= 2500:
            credits = credits - 2500
            fuel = fuel + 50
            print()
            Sec2_path1_1()
            time.sleep(a)
            break
        elif Planet1_path3 == '1' and credits <= 2500:
            print("Insufficient credits, please choose another option")
            time.sleep(a)
        elif Planet1_path3 == "2" and fuel >= 50:
            fuel = fuel - 50
            print()
            Sec2_path1_2()
            break
        elif Planet1_path3 == "2" and fuel <= 50:
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
    print("After taking a deep breath, you command your AI Zeus to launch the ship, 'Zeus take us up' *the ship engages Vtol mode, angles its accent, and fires the engines, you quickly accend to high orbit .....")
    time.sleep(a)
    print("You take one last scan of the planet with the ships sensors, no signs of life, no settlements besides ruins and rubble....")
    time.sleep(a)
    print("Stories of devastated worlds in the outer colonies, had reached you before, but those were supposed to be only rumors.....")
    time.sleep(a)
    print("you look at the display....")
    time.sleep(a)
    print()
    question = '"You Sense as if a Important moment is upon you, as if this choice will determine your very fate"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(b)
    print()
    print()
    print()
    pick_Planet()
    time.sleep(b)
    print()


#==============P1 Starport Fuel accepted path =======================
def Sec2_path1_2():   
    print("Using a large portion of the crystals you have, you fill the fuel cells,")
    time.sleep(a)
    print("After your finish fueling you notice several containers of ermgency water rations and food stuffs, you begin to scarf them down greedily..")
    time.sleep(a)
    print("After eating in the Sealed safty of the ship while the station prepared the ship, you take a moment to check the NAV computer and see only one destination point, a relay point in high orbit....")
    time.sleep(a)
    print("Worst case you think to yourself, you can try and scan again from orbit, you double check flight preperations.....")
    time.sleep(a)
    print("You take one last scan of the planet with the ships sensors, no signs of life, no settlements besides ruins and rubble....")
    time.sleep(a)
    print("Stories of devastated worlds in the outer colonies, had reached you before, but those were supposed to be only rumors.....")
    time.sleep(a)
    print("you look at the display....")
    time.sleep(a)
    pick_Planet()




#============= Planet choice / warp travel section ================================ 

def pick_Planet():
    print()
    print("Ship Sensors pick up several operational gates in system, but you don't recognize any of the names... ")
    time.sleep(a)
    print("The Nav computer does not have the data saved either, the realization hits your, you'll have to gamble your fuel and your life to make a jump to a random system that holds who knows what in store for you ....")
    time.sleep(a) 
    print("you closely examine the list beacons your AI Ares displays for you... ")
    time.sleep(a)
    print("########################################################################################")
    print("Ares: (1)  'Alpha Proxima'    #   4.2c Light years away      # 2 planets detected       ")
    print("Ares: (2)  'Epsillon_Eridani' # 10.50c Light years away      # 1 planet detected        ")
    print("Ares: (3)  'HR3259'           # 41.04c Light years away      # 3 planets detected       ")
    print("Ares: (4)  'LP 890-9'         #   105c Light years away      # 1 planet detected        ")
    print("########################################################################################")
    print()
    print("You remind yourself any choice you make have dire consaquences, as travel between systems is not a simple matter, you must finely balance your fuel to warp speed ratio...")
    time.sleep(a)
    print("as you must put yourself in cryo for the journey but even cryo-sleep does not stop your body from aging...")
    time.sleep(a)
    print("These are anywhere from days to years of your life you will be commiting to, but you must also think about how even IF you will be able to find more fuel...")
    time.sleep(a)
    print()
    displayStats()
    print()
    getTime()
    print()

    
    
def getTime():
    global v
    global mph
    global days
    while True:
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
            break
        elif m == '2':
            dist = 6.1726*(10**13)
            print(f'{EE} is 10.50 light years away.')
            getVelocity()
            time = dist / mph
            days = time/24
            print(f'It will take {days} days to get to {EE}')
            print(f'It will take 6 units of fuel to get to {EE}.  You currently have {fuel} units.')
            go_to_Epsillon_Eridani()
            break
        elif m == '3':
            dist = 241259000000000
            print(f'{HR} is 41.04 light years away.')
            getVelocity()
            time = dist / mph
            days = time/24      
            print(f'It will take {days} days to get to {HR}')
            print(f'It will take 6 units of fuel to get to {HR}.  You currently have {fuel} units.')
            go_to_HR3259()
            break
        elif m == '4':
            dist = 617300000000000
            print(f'{LP} is 105 light years away.')
            getVelocity()
            time = dist / mph
            days = time/24      
            print(f'It will take {days} days to get to {LP}')
            print(f'It will take 6 units of fuel to get to {LP}.  You currently have {fuel} units.')
            go_to_LP890()
            break
        else:
            print("Improper input")

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
    global fuel 
    ageCalc()
    time.sleep(a)
    print()
    print()
    fuel = fuel - 6
    print("After much thought, you lock in your choice, and prepare for warp jump and cryo-sleep.. ")
    time.sleep(a)
    print("Your AI Poseidon goes over final checks: all preperations complete, ready for jump on your command.. ")
    time.sleep(a)
    print("After a deep breath you punch the command into the console and lay down in your pod, as  you close your eyes you quell the racing thoughts.. ")
    time.sleep(a)
    print("Darkness decends and you dift into the sweet silence of sleep..... ")
    time.sleep(a)
    print()
    print("You arrive at Alpha Proxima.")
    time.sleep(a)
    print()
    displayStats()
    time.sleep(a)
    print()
    print()
    print()
    print("This is the end of the product demo, Future plans include up to 5 explorable planets, a planet map system allowing player movement (system almost ready) and mini games for resource gathering")
    time.sleep(a)
    print("As well as greater narrative complexity with each planet, hidden endings tied to a morality system based off player choices")
    time.sleep(a)
    print()
    print()
    endstate = input("Please come back next time so we can share more of the fun features our team has planned! Press Y to restart and N to exit the game.")
    if endstate == "y" or endstate == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
    if endstate == "n" or endstate == "N":
        print()
        print("Thank you for Playing DEEP SPACE 3: by Brandon Sample and Chris Chambers!")
        time.sleep(3)
        
    

def go_to_wolf359():
    global fuel 
    ageCalc()
    time.sleep(a)
    print()
    print()
    fuel = fuel - 6
    print("After much thought, you lock in your choice, and prepare for warp jump and cryo-sleep.. ")
    time.sleep(a)
    print("Your AI Poseidon goes over final checks: all preperations complete, ready for jump on your command.. ")
    time.sleep(a)
    print("After a deep breath you punch the command into the console and lay down in your pod, as  you close your eyes you quell the racing thoughts.. ")
    time.sleep(a)
    print("Darkness decends and you dift into the sweet silence of sleep..... ")
    time.sleep(a)
    print()
    print("You arrive at Wolf-359.")
    print()
    displayStats()
    time.sleep(a)
    print()
    print()
    print()
    print("This is the end of the product demo, Future plans include up to 5 explorable planets, a planet map system allowing player movement (system almost ready) and mini games for resource gathering")
    time.sleep(a)
    print("As well as greater narrative complexity with each planet, hidden endings tied to a morality system based off player choices")
    time.sleep(a)
    print()
    print()
    endstate = input(" This is the end of the product demo, please come back next time so we can share more of the fun features our team has planned! Press Y to restart and N to exit the game.")
    if endstate == "y" or endstate == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
    elif endstate == "n" or endstate == "N":
        print()
        print("Thank you for Playing DEEP SPACE 3: by Brandon Sample and Chris Chambers!")
        time.sleep(3)

def go_to_Epsillon_Eridani():
    global fuel 
    ageCalc()
    time.sleep(a)
    print()
    print()
    fuel = fuel - 6
    print("After much thought, you lock in your choice, and prepare for warp jump and cryo-sleep.. ")
    time.sleep(a)
    print("Your AI Poseidon goes over final checks: all preperations complete, ready for jump on your command.. ")
    time.sleep(a)
    print("After a deep breath you punch the command into the console and lay down in your pod, as  you close your eyes you quell the racing thoughts.. ")
    time.sleep(a)
    print("Darkness decends and you dift into the sweet silence of sleep..... ")
    time.sleep(a)
    print()
    print("You arrive at Epsillon Eridani.")
    print()
    displayStats()
    time.sleep(a)
    print()
    print()
    print()
    print("This is the end of the product demo, Future plans include up to 5 explorable planets, a planet map system allowing player movement (system almost ready) and mini games for resource gathering")
    time.sleep(a)
    print("As well as greater narrative complexity with each planet, hidden endings tied to a morality system based off player choices")
    time.sleep(a)
    print()
    print()
    endstate = input(" This is the end of the product demo, please come back next time so we can share more of the fun features our team has planned! Press Y to restart and N to exit the game.")
    if endstate == "y" or endstate == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
    elif endstate == "n" or endstate == "N":
        print()
        print("Thank you for Playing DEEP SPACE 3: by Brandon Sample and Chris Chambers!")
        time.sleep(3)

def go_to_HR3259():
    global fuel 
    ageCalc()
    time.sleep(a)
    print()
    print()
    fuel = fuel - 6
    print("After much thought, you lock in your choice, and prepare for warp jump and cryo-sleep.. ")
    time.sleep(a)
    print("Your AI Poseidon goes over final checks: all preperations complete, ready for jump on your command.. ")
    time.sleep(a)
    print("After a deep breath you punch the command into the console and lay down in your pod, as  you close your eyes you quell the racing thoughts.. ")
    time.sleep(a)
    print("Darkness decends and you dift into the sweet silence of sleep..... ")
    time.sleep(a)
    print()
    print("You arrive at HR3259.")
    print()
    displayStats()
    time.sleep(a)
    print()
    print()
    print()
    print("This is the end of the product demo, Future plans include up to 5 explorable planets, a planet map system allowing player movement (system almost ready) and mini games for resource gathering")
    time.sleep(a)
    print("As well as greater narrative complexity with each planet, hidden endings tied to a morality system based off player choices")
    time.sleep(a)
    print()
    print()
    endstate = input(" This is the end of the product demo, please come back next time so we can share more of the fun features our team has planned! Press Y to restart and N to exit the game.")
    if endstate == "y" or endstate == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
    elif endstate == "n" or endstate == "N":
        print()
        print("Thank you for Playing DEEP SPACE 3: by Brandon Sample and Chris Chambers!")
        time.sleep(3)

def go_to_LP890():
    global fuel 
    ageCalc()
    time.sleep(a)
    print()
    print()
    fuel = fuel - 6
    print("After much thought, you lock in your choice, and prepare for warp jump and cryo-sleep.. ")
    time.sleep(a)
    print("Your AI Poseidon goes over final checks: all preperations complete, ready for jump on your command.. ")
    time.sleep(a)
    print("After a deep breath you punch the command into the console and lay down in your pod, as  you close your eyes you quell the racing thoughts.. ")
    time.sleep(a)
    print("Darkness decends and you dift into the sweet silence of sleep..... ")
    time.sleep(a)
    print()
    print("You arrive at LP890.")
    print()
    displayStats()
    time.sleep(a)
    print()
    print()
    print()
    print("This is the end of the product demo, Future plans include up to 5 explorable planets, a planet map system allowing player movement (system almost ready) and mini games for resource gathering")
    time.sleep(a)
    print("As well as greater narrative complexity with each planet, hidden endings tied to a morality system based off player choices")
    time.sleep(a)
    print()
    print()
    endstate = input(" This is the end of the product demo, please come back next time so we can share more of the fun features our team has planned! Press Y to restart and N to exit the game.")
    if endstate == "y" or endstate == "Y":
        print()
        displayStats()
        print
        P1_Sec1()
    elif endstate == "n" or endstate == "N":
        print()
        print("Thank you for Playing DEEP SPACE 3: by Brandon Sample and Chris Chambers!")
        time.sleep(3)
    

#============= Player calculations ================================ 
def displayStats():
    print(f"///// Fuel = {fuel} units ///// Current Age = {age} ///// Credits = {credits} /////")


def ageCalc():
  global age
  global dayage
  global days
  x = dayage + days
  age = round(x/365,2)
  return age
         

 

#=================== Main Menu / Start Game Function =========

print()
print()
print("                  #############################                                  ")
print("                  |                           |                                  ")
print("                  |   Journey To Space  III   |                                  ")
print("                  |                           |                                  ")
print("                  |                           |                                  ")
print("                  #############################                                  ")
print("              By: Chris Chambers and Brandon Sample!                             ")                    
print()
print("##           -=  Journey To Space III  but in TEXT!  =-                            ##")
print("##       You awake in a crashed escape pod on a desolate world                     ##")
print("##       Before you lies the daunting task of finding your way back to Earth       ##")
print("##       The journey will be hard, do you have what it takes?                      ##")
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