def cube_calculations(a):
    pole=6*(a**2)
    objetosc=a**3
    return pole, objetosc

print(cube_calculations(4)) 

assert cube_calculations(7) == (294, 343)
assert cube_calculations(4) == (96, 64)

def objetosc_kuli(r):
    objetosc = 4/3 * 3.14 * r**3
    return round(objetosc,2)

print("Objetosc kuli wynosi " + str(objetosc_kuli(5)))

assert objetosc_kuli(5)==523.33
assert objetosc_kuli(8)==2143.57

#ostroslup
import math
def ostroslup_trojkatny(a,h,H):
    pole=round((math.pow(a,2)*math.sqrt(3))/4+(3*a*h)/2,2)
    objetosc=round((math.pow(a,2)*math.sqrt(3)*H)/12,2)

    return pole, objetosc

print(ostroslup_trojkatny(3,4,5))

assert ostroslup_trojkatny(5,6,7)==(55.83,25.26)
assert ostroslup_trojkatny(7,9,10)==(115.72,70.73)
