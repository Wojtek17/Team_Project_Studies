import math
def ostroslup_trojkatny(a,h,H):
    pole=round((math.pow(a,2)*math.sqrt(3))/4+(3*a*h)/2,2)
    objetosc=round((math.pow(a,2)*math.sqrt(3)*H)/12,2)

    return pole, objetosc

print(ostroslup_trojkatny(3,4,5))

assert ostroslup_trojkatny(5,6,7)==(55.83,25.26)
assert ostroslup_trojkatny(7,9,10)==(115.72,70.73)