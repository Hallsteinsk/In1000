class Motorsykkel:
	
	#Constructor
	# @param merke er motorsyklens merke. String
	# @param registreringsnummer er registreringsnummeret til motorsyklen. Strin
	# @param kilometerstand er den kilometerstanden motorsyklen starter med. Float
	def __init__(self, merke, registreringsnummer, kilometerstand):
		self._merke = merke
		self._registreringsnummer = registreringsnummer
		self._kilometerstand = float(kilometerstand)
	
	##Metode som oeker kilometerstanden
	# @param km er antall kilomter som standen skal oekse med. Float
	def kjor(self, km):
		self._kilometerstand += float(km)
	
	##Metode som returnerer kilometerstandend.
	# @return kilometersrtanden til motorsyklen
	def hentKilometerstand(self):
		return self._kilometerstand
	
	##Metode som skriver ut motorsyklens merke, registreringsnummer og kilometersrtanden
	def skrivUt(self):
		print("Merke: %s" %self._merke)
		print("Registreringsnummer: %s" %self._registreringsnummer)
		print("Kilometerstand: %.1f" %self._kilometerstand)
		print()