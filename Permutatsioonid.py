__author__ = 'Diana'
#Permutatsioonid.py Diana Algma 24.09.2014

import os.path      #isfile() kasutamiseks

def sõnadeks(sõne):         #teeb sõnest (lausest/tekstireast) sõnade järjendi
    L=[]
    s2=sõne.lower().split(' ')      #lahutab sõne tühikute kohalt ja muudab suurtähed väikesteks
    for sõna in s2:
        sõnake=sõna.strip('.!?",\n<>:;#%&/()=@£${[]}*_')     #eemaldab mittevajalikud jutumärgid
        if sõnake != '':
            L.append(sõnake)            #lisab saadud sõna järjendisse, kui sõna pole tühi
    return L

def permutatsioonid(järjestamata, järjestatud=''):     #järjestamata: järjend sõnadest, järjestatud: sõne
    if len(järjestamata)==0:                    #baas: kõik on järjestatud, väljastan sõne
        print(järjestatud[1:])                          #alates teisest elemendist, sest esimene on mittevajalik tühik
    else:                                       #samm:
        for i in range(len(järjestamata)):
            tehtud=järjestatud+" "+järjestamata[i]      #tehtud sõnad on seni järjestatud sõnad, tühik ja i-ndas sõna
            tegemata=järjestamata[0:i]+järjestamata[i+1:]   #tegemata sõnade järjendis on seni järjestamata sõnad ilma
                                                        #i-nda sõnata
            permutatsioonid(tegemata, tehtud)           #järjestab järgmised sõnad

tekst=input("Sisesta tekst või tekstifaili nimi: ")

if os.path.isfile(tekst):       #kui sisestati tekstifail:
    f=open(tekst)
    print("Avati fail")
    sõnad=[]                    #teeb sõnade jaoks järjendi
    for rida in f:              #iga rida tehakse sõnadeks ja lisatakse sõnade järjendisse
        sõnad=sõnad+sõnadeks(rida)
else:                           #kui sisestati tekst:
    print("Sisestati tekst")
    sõnad=sõnadeks(tekst)       #tekst tehakse sõnade järjendiks

print("Sõnu:", len(sõnad))
if len(sõnad)> 900:
    print("Sõnu on liiga palju.") #Python ei saaks rekursiooniga hakkama
elif len(sõnad) > 9:
    vastus=input("Sõnu on väga palju, kas soovid jätkata? ")    #Permutatsioonide väljastamine võib võtta väga kaua aega
    if vastus == "jah" or vastus == "Jah":      #Kui vastatakse midagi muud, siis programm lõpetab töö
        print("Permutatsioonid:")
        permutatsioonid(sõnad)          #väljastatakse kõik permutatsioonid
else:
    print("Permutatsioonid:")
    permutatsioonid(sõnad)          #väljastatakse kõik permutatsioonid
