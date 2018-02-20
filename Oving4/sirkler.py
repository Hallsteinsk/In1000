#Oppgave 3
#I denne oppgaven har jeg laget et program som lager 9 sirkler etter hverandre som gradvis oeker i stoerrelse.
#Hver nye sirkel er skiftet 30 piksler langs x-aksen, mens diameteren oeker med 5 piksler. 

#Deloppgave 1: Lager et grafikkvindu og canvas.
from ezgraphics import GraphicsWindow
win = GraphicsWindow()
win.setTitle("Oppgave 3, sirkler.py")
can = win.canvas()

#Deloppgave 2
teller = 0
x_pos = 10
stoerrelse = 50 #Deloppgave 4


#Deloppgave 3
while teller < 9:
	can.drawOval(x_pos, 100, stoerrelse, stoerrelse)
	x_pos += 30
	stoerrelse += 5 #Deloppgave 4
	teller += 1

win.wait()
