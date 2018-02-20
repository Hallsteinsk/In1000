#Oppgave 2

#Deloppgave 1 og 2
#Ikke spesifisert i oppgaven, men jeg bestemmer at tall fra bruker kan vaere floats
#Hvis bruker skriver inn 0 blir ikke 0en lagt til i listen. 
#Inkluderer exception handling i tilfelle bruker ikke skriver inn et tall.

tallListe = []
print("Lag en liste med flyttall.\n(Skriv inn 0 naar du har skrevet inn alle tallene dine.):")
while(True):
	try:
		inputTall = float(input("Skriv inn et tall: "))
		if inputTall == 0:
			break
		else:
			tallListe.append(inputTall)
	except ValueError:
		print("Du skrev ikke inn et gyldig tall. Proev igjen.")

#Deloppgave 3
print("\nUtskrift av tallene i lista:")
for tall in tallListe:
	print(tall)

#Deloppgave 4
minSum = 0
for tall in tallListe:
	minSum += tall

print("\nSummen av tallene i lista er: %.1f" % minSum)

#Deloppgave 5
minTall = maxTall = tallListe[0]
for tall in tallListe:
	if tall < minTall:
		minTall = tall

for tall in tallListe:
	if tall > maxTall:
		maxTall = tall

print("Det minste tallet er: %.1f" % minTall)
print("Det stoerste tallet er: %.1f" % maxTall)
