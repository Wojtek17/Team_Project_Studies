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
        podatek=round((0.12*podstawa_podatek)-300,2)
        wynagrodzenie_netto=round(self.pensja-skladki_zus-skladka_zdrowotna-podatek,2)
        return wynagrodzenie_netto
    
    def oblicz_koszty_pracodawcy(self):
        skladki_pracodawcy=(0.0976*self.pensja)+(0.065*self.pensja)+(0.0167*self.pensja)+(0.0245*self.pensja)+(0.0010*self.pensja)
        koszt_pracodawcy=round(self.pensja+skladki_pracodawcy,2)
        return koszt_pracodawcy
    
    pracownik_wojtek=Pracownik("Wojtek","Marszalek",3500)
    print(pracownik_wojtek.oblicz_netto(250))
    print(pracownik_wojtek.oblicz_koszty_pracodawcy())