#Deloppgave 1
tempFahrenheit = 100 #Setter temperaturen til 100 her. Dette var bare for deloppgave 1, den blir overskrevet i oppgave 5

#Deloppgave 5
#Her vil jeg forsikre meg om at bruker skriver inn et tall. Derfor setter jeg opp en evig loop som man kun kan komme ut av dersom man skriver inn et tall.
while(True):
	tempFahrenheit = input("Skriv inn temperaturen i farenheit:\n") #Henter verdi fra bruker

	try: #Proever aa omforme brukerinput til flyttall
		tempFahrenheit = float(tempFahrenheit)
		break #Gaar ut av loopen her dersom omformin er suksesfull
	except ValueError: #Fanger opp her dersom brukerinput ikke er tall
		print("Du skrev inn en feil verdi. Proev igjen") #Ber bruker om aa proeve igjen

#Deloppgave 2 
print("Temperaturen i fahrenheit er:", round(tempFahrenheit, 2)) #benytter round() for aa begrense tallet til maks 2 desimaltall

#Deloppgave 3
tempCelcius = (tempFahrenheit - 32) * (5/9) #Regner ut tempe i celcius med formel gitt i oppgavetekst

#Deloppgave 4
print("Temperaturen er i celcius:", round(tempCelcius, 2)) #Skriver ut temperaturen i celcius. Round brukes for aa begrense antall desimaltall