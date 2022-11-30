from fractions import Fraction

c = 670616629
mph = 0



a = 'Alpha_Centari'     
Aplha_Centari = 4.29        # Has 3 known planets
b = 'Epsillon_Eridani'
Epsillon_Eridanio = 10.50     # Has 1 known planet
c = 'Wolf1061' 
Wolf_1061 = 13.8             # 3 planets, 1 in habitable zone
d= 'HR3259'
HR3259 = 41.04               # Has 3 known planets

v = 0

#Calculate velocity in m/s

def getVelocity():
    global v
    global mph
    var1 = input('Please enter the warp speed (0-10) that you would like to go (and keep in mind that the faster you will go you will burn more fuel, but age less): ')
    var1 = Fraction(var1)
    expo = Fraction(10/3)
    result = var1**expo
    if v == 0:
        v = result * 299792458
        print(f'Velocity is equal to {v} m/s')
        mph = v*2.237
        print(f'{mph} mph')
        print('time in hours = distance in miles / vel ')


def getTime():
    global v
    global mph
    m = input('Where would you like to go? ')
    print(m)
    if m == '1':
        dist = 2.54*(10**13)
        print(f'{a} is {dist} light years away.')
        getVelocity()
        time = dist / mph
        days = time/24
        print(f'It will take {days} days to get to {a}')
      
    '''elif m == '2':
        x = Epsillon_Eridani
        dist = 10.00
        print(f'{x} is {dist} light years away.')
        getVelocity()
        time = dist / v
        print(f'It will take {time} hours to get to {x}')'''
    
       

getTime()
      
      
       
     




        












#calculate age in days
#calculate days to years
#calcualate time to travel in days
    #calculate time to travel in hours
    

