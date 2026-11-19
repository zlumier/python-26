# Kevin 19.11.26

# Ülesanne 3.6: Python Turtle
import turtle

kylje_pikkus = 200
nurk = 90
varv ="red"
edasi = kylje_pikkus * 1.5

#esimene
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
edasi = edasi * 1.5
turtle.goto(edasi,0)
turtle.down()

#teine
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
edasi = edasi * 1.5
turtle.goto(edasi,0)
turtle.down()

#kolmas
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
edasi = edasi * 1.5
turtle.goto(edasi,0)
turtle.down()
turtle.up()
turtle.goto(edasi,0)
    
turtle.done()

turtle.fd(100)
turtle.fd(90)
turtle.fd(100)
turtle.fd(90)
turtle.fd(100)
turtle.fd(90)
turtle.fd(100)
turtle.fd(90)

turtle.done()

# Ülesanne 3.4: Lemmikraamat

raamatu_pealkiri = "Suvi"
raamatu_autor = "Oskar Meri"
raamat = raamatu_pealkiri+" "+raamatu_autor
lk = 300
skoor = 10.0
print ("Minu lemmikraamat on "+raamat+", mis on "+str(lk)+" lehekülge pikk ja mille ma hindan "+str(skoor)+" punktiga ")




# Ülesanne 3.2: Ostunimekiri
toode = "juust"
kogus = 50
hind = 15.50

print ("Soovin "+str(toode)+" "+str(kogus)+", 3, mille tüki hind on "+str(hind)+" eurot.")