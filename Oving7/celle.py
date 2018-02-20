class Celle:
	#Constructor
	def __init__(self):
		self._status = "doed"
	
	##Metode som setter status til doed
	def setDoed(self):
		self._status = "doed"
	
	##Metode som setter status til levende
	def setLevende(self):
		self._status = "levende"
	
	##Metode som returnerer finner ut om en celle er levende eller ikke
	# @return True hvis den er levende, False hvis den er doed
	def erLevende(self):
		if self._status == "levende":
			return True
		elif self._status == "doed":
			return False
		else:
			print("Celle er hverken doed eller levende....")
	
	##Metode som returnerer et char tegn, som indikerer om den er doed eller levende.
	# @ return 
	def skrivTegn(self):
		if self._status == "levende":
			tegn = "O"
		elif self._status == "doed":
			tegn = "."
		return tegn
		