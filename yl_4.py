# 24.11.26 Kevin

# Ringi pindala ja Turtle

# Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
# Programm küsib kasutajalt ringi raadiuse.
# Kasuta ** operaatorit raadiuse ruudu arvutamiseks ja π väärtusena 3.14.
# Lisa veakontroll, et kontrollida kasutaja sisestatud raadiuse korrektsust.
# Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta
# Näide:
# Kasutaja sisestab: 5
# Programm väljastab konsoolis: Ringi pindala on 78.5 ja ümbermõõt on 31.4
# Turtle graafika joonistab vastava ringi

import turtle
try:
    r = int(input("r="))
    s = 3.12 * (r**2)
    p = 2 * (3.14**2)
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r)
except:
    print("Urror")

#     Kingituste pakkimine
#     Sa töötad kingipoes ja sinu ülesanne on pakkida kingitusi.
#     Igasse kinkekarpi mahub täpselt 5 kingitust.
#     Sinu ülesandeks on arvutada, mitu täis kinkekasti saad teha ja mitu kingitust jääb üle, kui need kõik ei mahu karpidesse.
#     Loo programm, mis küsib kasutajalt, mitu kingitust on vaja pakkida.
#     Programm peaks seejärel arvutama, mitu täis kinkekasti saab teha ja mitu kingitust jääb üle. Kasuta täisarvulist jagamist (//) kinkekarpide arvu leidmiseks ja jäägi (%) operaatorit ülejäävate kingituste arvu leidmiseks.
#     Kasuta veakontrolli ja vastuse vormindamist
#     Näide:
#     Kasutaja sisestab: 23
#     Programm väljastab: Saad teha 4 täis kinkekasti. Üle jääb 3 kingitust.
try:
    komplekt = 5
    kingituste_arv = int(input("Kingituste arv: "))
    kastid = kingituste_arv // komplekt
    yle = kingituste_arv % komplekt

    print(f"Saad teha {kastid} täis kinkekasti. Üle jääb {yle} kingitust.")
except:
    print ("Urror")
print ("-"*20)

# # Raamatupoes on 30% soodusmüük.
# #Kirjuta programm, mis küsib kasutajalt soovitud raamatute arvu ja arvutab nende kogumaksumuse, kui iga raamatu tavahind on 12,53€.
# Väljasta lause, kasutades f-string vormindamist ja ümardamist 2 komakohta

ale = 0.3
hind = 12.53

try:
    raamat = int(input ("Sisesta raamatu kogus: "))
    summa = (hind-hind*ale)* raamat
    print(f"Vastus: {summa:0.2f}")



except:
    print("kasutaja sisestuses on viga")


turtle.done()