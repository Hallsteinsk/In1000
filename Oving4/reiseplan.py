#Oppgave 4
#Denne oppgaven leser inn reisemaal, klesplagg og avreisedato fra bruker. Disse verdiene legges i en noestet liste.
#Deretter skrives alle listene ut, og bruker skal deretter velge 2 indekser for aa skrive ut et spesifikt element fra lista.

#Deloppgave 1
steder = []

for i in range(0, 5):
	steder.append(input("Skriv inn et reisemaal: "))

#Deloppgave 2
klesplagg = []
avreisedatoer = []

for i in range(0, 5):
	klesplagg.append(input("Skriv inn et klesplagg: "))
	
for i in range(0, 5):
	avreisedatoer.append(input("Skriv inn en avreisedato: "))

#Deloppgave 3
reiseplan = [steder, klesplagg, avreisedatoer]

#Deloppgave 4
for reise in reiseplan:
	print(reise)
	
#Deloppgave 5
print("Du skal naa skrive inn to indekser som gir en gyldig plassering i lista \"Reiseplan\"")
i1 = int(input("Skriv inn den foreste indeksen. Den skal vere mellom 1 og 3: ")) - 1
i2 = int(input("Skriv inn den andre indeksen. Den skal vere mellom 1 og 5: ")) - 1

if i1 >= 0 and i1 < 3 and i2 >= 0 and i2 < 5:
	print(reiseplan[i1][i2])
else:
	print("Ugylig input!")