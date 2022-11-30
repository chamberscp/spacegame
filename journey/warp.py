from fractions import Fraction

c = 299792458

c_per_day = float(2.348336594911937)
c_per_hour = float(0.0978473581213071)
lightyear_hours = float(10.22)
days_per_year = 365
hours_per_day = float(24.00)
hours_per_year = 8760


a = 'Alpha_Centari'     
Aplha_Centari = 4.29        # Has 3 known planets
b = 'Epsillon_Eridani'
Epsillon_Eridanio = 10.50     # Has 1 known planet
c = 'Wolf1061' 
Wolf_1061 = 13.8             # 3 planmets, 1 in habitable zone
d= 'HR3259'
HR3259 = 41.04               # Has 3 known planets

time = 0
warp = 0
v = 0

#Calculate velocity in m/s

def getVelocity():
    global warp
    global v
    var1 = input('Please enter the warp speed (0-10) that you would like to go (and keep in mind that the faster you will go you will burn more fuel, but age less): ')
    var1 = Fraction(var1)
    expo = Fraction('10/3')
    result = var1**expo
    print(result)
    if v == 0:
        v = result * 299792458
        print(v)
        print(f'Velocity is equal to {v} m/s')


def getTime():
    m = input('Where would you like to go? ')
    print(m)
    global v
    if m == '1':
        dist = .102
        #print(f'{a} is {dist} light years away.')
        #getVelocity()
        time = dist * v
        #print(f'It will take {time} days to get to {a}')
      
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
    

