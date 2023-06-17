class Pracownik:
    def __init__(self, imie_pracownika, nazwisko_pracownika, pensja_brutto):
        self.imie = imie_pracownika
        self.nazwisko = nazwisko_pracownika
        self.pensja = pensja_brutto


    def __str__(self):
        return self.imie +" "+self.nazwisko +" "+str(self.pensja)
    def oblicz_netto(self, kup):
        skladki_zus=(0.0976*self.pensja)+(0.0245*self.pensja)+(0.015*self.pensja)
        podstawa_zdrowotna=self.pensja-skladki_zus
        skladka_zdrowotna=podstawa_zdrowotna*0.09
        podstawa_podatek=round(self.pensja-skladki_zus-kup)
        podatek=(0.12*podstawa_podatek)-300
        wynagrodzenie_netto=round(self.pensja-skladki_zus-skladka_zdrowotna-podatek,2)
        return self.pensja, skladki_zus, podstawa_zdrowotna, skladka_zdrowotna, podstawa_podatek, podatek, wynagrodzenie_netto
    
    pracownik_wojtek=Pracownik("Wojtek","Marszalek",3500)
    print(pracownik_wojtek.oblicz_netto(250))