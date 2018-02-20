#Oppgave 3.1
brukerSvar = input("Kan du tenke deg brus? (svar ja eller nei)\n")

#Oppgave 3.2 
if brukerSvar.lower() == "ja": #a) Bruker .lower() for at programmet skal godta både stor og små bokstaver (Case-insensitivt)
  print("Her har du en brus!")
elif brukerSvar.lower() == "nei": #b) bruker elif i stedet for "Nested if"
  print("Den er grei.")
else:								#c) bruker else for å fange alt annet enn ja og nei
  print("Det forst jeg ikke helt.")