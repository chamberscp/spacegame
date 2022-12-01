from fractions import Fraction
import math

light = 299792458
mph = 0
v = 0
var1 = 1
WF = 1

a = 'Alpha_Proxima'    # 4.29c   # Has 3 known planets
b = 'Epsillon_Eridani' # 10.50c  # Has 1 known planet
c = 'HR3259'           # 41.04c  # Has 3 known planets
d = 'LP 890-9'         # 105c    # Has 2 known planets



#Calculate velocity in m/s

def getVelocity():
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
    
        
def getTime():
    global v
    global mph
    m = input('Where would you like to go? ')
    print(m)
    if m == '1':
        dist = 2.5219*(10**13)
        print(f'{a} is 4.29 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24
        print(f'It will take {days} days to get to {a}')
    
    elif m == '2':
        dist = 6.1726*(10**13)
        print(f'{b} is 10.50 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24
        print(f'It will take {days} days to get to {b}')
    
    elif m == '3':
        dist = 241259000000000
        print(f'{c} is 41.04 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24      
        print(f'It will take {days} days to get to {c}') 
     
    elif m == '4':
        dist = 617300000000000
        print(f'{d} is 105 light years away.')
        getVelocity()
        time = dist / mph
        days = time/24      
        print(f'It will take {days} days to get to {d}')  
        
        
def fuelUsage():
    normal = 1
    fueltank = 100
    if WF > 0 and WF <= 2:
        usage = normal * 1.5
    elif WF > 2 and WF <= 5:
        usage = normal * 2.5 
    elif WF > 5 and WF <= 8:
        usage = normal * 5
    elif WF > 8:
        usage = normal * 10 
        
    
    
        
getTime()