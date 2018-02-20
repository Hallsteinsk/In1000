#Oppgave 3

#I denne oppgaven benytter jeg ezgraphicsmodulen og benytter funksjoner derifra for aa tegne 
#en roed sirkel. Prosedyre for aa tegne har jeg tatt fra EzGraphics.org sin "User guide". 
#Link: http://www.ezgraphics.org/UserGuide/GettingStarted
#Link: http://www.ezgraphics.org/UserGuide/OvalsAndCircles


#Deloppgave 4:
#Importerer ezgraphics
from ezgraphics import GraphicsWindow

#Lager vindu
win = GraphicsWindow()
win.setTitle("Oppgave 3: sirkel.py")

#Lager nytt canvas-objekt
canvas = win.canvas()

#Tegner en roed sirkel:
canvas.setColor("red")
canvas.drawOval(50,50,300,300)

#Venter til bruker lukker program
win.wait()