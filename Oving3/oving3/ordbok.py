#Oppgave 2

#I denne oppgaven har jeg laget en ordliste som inneholder dagligvarer. 
#Varenavn er brukt som noekkel og prisen som "value". Siden jeg skal skrive ut ordboken 2 ganger
#valgte jeg aa lage en funksjon som gjoer dette. Funksjonen skriver ut paa en enkel maate, og 
#paa en "fancy" maate.

#Deloppgave 1
def skrivOrdbok(ordbok):
	#Enkel utskrift....
	print("Enkel utskrift:")
	print(ordbok)
	print() 

	#Fancy utskrift:
	print("Fancy utskrift:")
	for i in ordbok:
		print(i + " - kr %.2f" % ordbok[i])
	print()

vareOrdbok = {"melk":14.90, "broed":24.90, "yoghurt":12.90, "pizza":39.90}

print("Her er ordboken i deloppgave 1:")
skrivOrdbok(vareOrdbok)


#Deloppgave 2:
print("Legg til to nye varer i ordboken:")
for i in range(0,2):
	vare = input("Skriv inn varenavn ")
	pris = input("Skriv inn pris ")
	vareOrdbok[vare] = float(pris)

print()
print("Her er ordboken i deloppgave 2:")
skrivOrdbok(vareOrdbok)
