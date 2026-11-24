# 24.11.26 Kevin

#Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
#Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
#Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
#Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.


import random
valik = input("kull või kiri")
suv = random.randint(0,1)
if suv == 1:
    avalik = "kiri"
else:
    avalik = "kull"
    
if valik == avalik:
    print("Palju õnne!")
else:
    print("Kaotus!")
        

       
       
#Ilmaennustuse rakendus (and)
#Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
#Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid. Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
#Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.


temp = int(input("Sisesta temp: "))
if temp < 0:
    print("Talveriided")
elif temp >= 0 and temp <= 15:
    print("Sügisriided")
else:
    print("Suveriided")