def cube_calculations(a):
    pole=6*(a**2)
    objetosc=a**3
    return pole, objetosc

print(cube_calculations(4)) 

assert cube_calculations(7) == (294, 343)
assert cube_calculations(4) == (96, 64)
