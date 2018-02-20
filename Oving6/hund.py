class Hund:

	##Constructor
	def __init__(self, alder, vekt):
		self._alder = alder
		self._vekt = vekt
		self._metthet = 10
	
	##Metode som returnerer vekt
	# @return vekt
	def hentVekt(self):
		return self._vekt
	
	##Metode som returnerer alder
	# @return alder
	def hentAlder(self):
		return self._alder
	
		
	##Metode hvor hunden springer. Dette foerer til at metthet minsker og vekt reduseres ogsaa dersom hunden er mindre mett enn 5
	def spring(self):
		self._metthet -= 1
		if self._metthet < 5:
			self._vekt -= 1
			
	##Metode hvor hunden spiser. Metoden tar metthetoeknin som argument, og oeker vekten til hunden dersom den er mer mett enn 7.
	# @param mat er tallet mettheten oeker med.
	def spis(self, mat):
		self._metthet += mat
		if self._metthet > 7:
			self._vekt += 1