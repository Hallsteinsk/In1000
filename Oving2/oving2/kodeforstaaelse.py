#Deloppgave 1
#De tre foerste linjene i koden er lovlig. Den fjerde derimot proever aa legge sammen en int og en streng.
#Dette vil trolig gi en feilmelding om type, da pluss-operatoren kan kun brukes paa variabler av samme type. 

#Deloppgave 2
#Hvis bruker skriver inn et tall som er 10 eller stoerre vil aldri den "Ulovlige" linjen bli utfoer, og ingne feilmeldinger vil oppstaa.
#Skriver bruker inn et tall som er mindre enn 10 vil den "ulovlige" koden bli utfoert, og programmet vil stoppe og gi feilmelding.



a = input ( "Tast inn et heltall! " )
b = int ( a )
if b < 10 :
	print ( b + "Hei!" )
	
#Testet koden. Fikk TypeError paa linje 14 da jeg skrev inn verdien 1. Ingen feil oppsto da jeg skrev inn verdien 11.  