def objetosc_stozka(r, h):
    objetosc = 1/3 * 3.14 * r**2 * h
    return objetosc

print(objetosc_stozka(3, 100))

assert objetosc_stozka(3, 100) == 942