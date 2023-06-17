import pandas as pd
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
    def wygeneruj_raport(self):
        print("Składka emerytalna: "+str(round((0.0976*self.pensja),2))+"\n" + 
              "Składka rentowa: "+str(round((0.065*self.pensja),2))+"\n" + 
              "Składka na wypadkowe: "+str(round((0.0167*self.pensja),2))+"\n" + 
              "Fundusz pracy: "+str(round((0.0245*self.pensja),2))+"\n" + 
              "FGŚP: "+str(round((0.0010*self.pensja),2)))
    
    pracownik_wojtek=Pracownik("Wojtek","Marszalek",3500)
    print(pracownik_wojtek.oblicz_netto(250))
    print(pracownik_wojtek.oblicz_koszty_pracodawcy())
    print(pracownik_wojtek.wygeneruj_raport())

df=pd.read_csv('/Users/wojtekmarszalek/Desktop/pracownicy.csv')

for index, data in df[:4].iterrows():
    pracownik=Pracownik(data["imię"], data["nazwisko"], data['pensja'])
    print(str(pracownik))
    print("Wynagrodzenie netto: "+str(pracownik.oblicz_netto(250)))
    print("Koszty pracodawcy: "+str(pracownik.oblicz_koszty_pracodawcy()))
    print(pracownik.wygeneruj_raport())
          
