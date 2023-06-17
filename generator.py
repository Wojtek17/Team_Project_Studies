import csv
import pandas as pd
import random

names=[]
surnames=[]
salaries=[]
for i in range (0,100):
    name=random.choice([
  "Alicja",
  "Bartosz",
  "Celina",
  "Damian",
  "Eliza",
  "Franciszek",
  "Gabriela",
  "Hubert",
  "Iwona",
  "Janusz",
  "Karolina",
  "Łukasz",
  "Magdalena",
  "Natalia",
  "Oskar",
  "Patrycja",
  "Rafał",
  "Sylwia",
  "Tomasz",
  "Zuzanna"
])
    names.append(name)
    surname=random.choice([
  "Kowalski",
  "Nowak",
  "Wiśniewski",
  "Wójcik",
  "Kowalczyk",
  "Kamiński",
  "Lewandowski",
  "Zieliński",
  "Szymański",
  "Woźniak",
  "Dąbrowski",
  "Kozłowski",
  "Jankowski",
  "Mazur",
  "Wojciechowski",
  "Kwiatkowski",
  "Kaczmarek",
  "Piotrowski",
  "Grabowski",
  "Zając"
])
    surnames.append(surname)

    salary=random.choice(range(1000,10000,200))
    salaries.append(salary)
    
#    print(name,surname,salary)
df=pd.DataFrame(names)
df["nazwisko"]=surnames
df["pensja"]=salaries
df.rename({0:"imię"},axis=1, inplace=True)
df