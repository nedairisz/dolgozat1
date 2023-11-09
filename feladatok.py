import math
import random

# Kérj be 1 páros számot a felhasználótól. (1 pont)
# Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)	
def feladat1():
    print("1. feladat")
    szam:int = int(input("Adj meg egy páros számot!: "))
    while not(szam%2==0):
        print("Nem jó!")
        szam:int = int(input("Adj meg egy páros számot!: "))
    else:
        print("OK!")

# Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. 
# Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”
def feladat2():
    print("2. feladat")
    i:int=0
    gyujto = 0
    while i<13:
        szam:int = math.floor(random.random()*141+10)
        print(szam, end=" ") 
        if szam%3==0:
            gyujto += 1
        i+=1
    print(f"\nA számok között {gyujto} db 3-mal osztható van!")
        
'''Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! 
pl: feladat3(„Ez az én dumám”,4)
a 4. karakter „z”, 
nagybetűvé alakítva: Z -  ezt írjuk ki 3-szor
A kiírás formátuma: A szöveg 4. karaktere z -  ZZZ'''
def feladat3(txt:str, n:int):
    print("3. feladat")
    if len(txt)<n:
        print(f"Nincs {n} karakter!")
    elif len(txt)>n:  
        print(f"A szöveg {n}. karaktere {txt[n]} - {txt[n].capitalize()*3}")

# Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja. Hány nevet adott meg a felhasználó? 
# A kiírás formája: „A felhasználó 12 nevet adott meg.”
def feladat4():
    print("4. feladat")
    szamlalo = 0
    nev:str = str(input("Adj meg egy nevet!:" ))
    while not(nev=="@"):
        nev: str = str(input("Adj meg egy nevet!:"))
        szamlalo += 1
    print(f"A felhasználó {szamlalo} nevet adott meg!")

'''Szimuláljuk a kő-papír-olló játékot. 
Írj eljárást, amiben: 
A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban. 
Ezután a gép generál egy egész számot [1,3] között.  1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban
Ezután írd ki, hogy ki nyert!
	Ha a két szó ugyanaz, írja ki, hogy Döntetlen. 
	Egyéb esetben azt írja ki, aki győzött!
++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!'''
def feladat5():
    print("5. feladat")
    miatipp:str = str(input("Tippelj! (kő/papír/olló): "))
    while not(miatipp== "kő" or miatipp=="papír" or miatipp=="olló"):
        miatipp:str = str(input("Tippelj! (kő/papír/olló): "))
        felhasznalo_tippje= miatipp.lower
        
    i:int=0
    while i<3:
        gep_tippje:int = math.floor(random.random()*3+1)
        print(gep_tippje, end=" ")
        i += 1
        