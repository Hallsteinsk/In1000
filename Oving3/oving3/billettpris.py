#Oppgave 4
#I dnne oppgaven har jeg laget funksjonen finnBillettpris som spoer etter brukers alder
#og beregner billettpris basert paa instruksjonene i oppgaveteksten.
#Til slutt kalles funksjonen 4 ganger.

#Deloppgave 1
def finnBillettpris():
	alder = int(input("Skriv inn alder:\n"))
#Deloppgave 2
	billettpris = 0
#Deloppgave 3
#a
	if alder <= 17:
		billettpris = 30
#b
	elif alder > 17 and alder < 63:
		billettpris = 50
#c
	elif alder >= 63:
		billettpris = 35
#Deloppgave 4
	print("Bilettprisen er %.2f kroner\n" % float(billettpris))

#Deloppgave 5
for i in range (0,4):
	finnBillettpris()

#Deloppgave 6:
#Jeg er litt usikker paa denne... Jeg er usikker paa om jeg fulgte oppgaveteksten slavisk.
#Hadde jeg ikke lagt inn "and alder < 63:" i deloppgave 3b ville elif i 3c aldri blitt gjennomfoert.
#Er det dette denne deloppgaven skal svare paa? Jeg kan ikke finne noen andre problem med denne prosedyren.


