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
