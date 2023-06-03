def objetosc_kuli(r):
    objetosc = 4/3 * 3.14 * r**3
    return round(objetosc,2)

print("Objetosc kuli wynosi " + str(objetosc_kuli(5)))

assert objetosc_kuli(5)==523.33
assert objetosc_kuli(8)==2143.57