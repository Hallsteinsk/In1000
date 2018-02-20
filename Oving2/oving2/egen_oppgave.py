#Classes################################################################
class Player:
	playerName = None
	playerScore = None
	
	#Constructor
	def __init__(self, playerName, initialScore):
		self.playerName = playerName
		self.playerScore = int(initialScore)
	
	#Getters
	def getName(self):
		return self.playerName
	
	def getScore(self):
		return self.playerScore
	
	#Other fucntions
	def increaseScore(self): #Increases the score by one
		self.playerScore += 1
	
	def resetScore(self): #Resets the score if the player wants another run
		self.playerScore = 0
	
class Question:
	question = None
	alternativeA = None
	alternativeB = None
	alternativeC = None
	alternativeD = None
	correctAnswer = None
	
	#Constructor
	def __init__(self, question, alternativeA, alternativeB, alternativeC, alternativeD, correctAnswer):
		self.question = question
		self.alternativeA = alternativeA
		self.alternativeB = alternativeB
		self.alternativeC = alternativeC
		self.alternativeD = alternativeD
		self.correctAnswer = correctAnswer
	
	#Getters
	def getCorrectAnswer(self):
		return self.correctAnswer
	
	#Other functions
	def printQuestion(self): #Prints out the question and all the alternatives
		print(self.question)
		print(self.alternativeA)
		print(self.alternativeB)
		print(self.alternativeC)
		print(self.alternativeD)

#Functions##############################################################		
def makePlayer(): #Function that returns a player object with the users name and 0 in initial score
	return Player(input("Welcome to the QUIZ new player!\nPlease enter your name:\n"), 0)
	
def createQuestions(): #Function that generates the questions in the task specifications
		questions = [] #Empty list, that will be filled with question objects by using the append-fucntion
		questions.append(Question("1. Grand Central Terminal, Park Avenue, New York is the world's",
		"A. largest railway station",
		"B. highest railway station",
		"C. longest railway station",
		"D. None of the above",
		"a"))
		
		questions.append(Question("2. Entomology is the science that studies",
		"A. Behavior of human beings",
		"B. Insects",
		"C. The origin and history of technical and scientific terms",
		"D. The formation of rocks",
		"b"))
		
		questions.append(Question("3. Eritrea, which became the 182nd member of the UN in 1993, is in the continent of",
		"A. Asia",
		"B. Africa",
		"C. Europe",
		"D. Australia",
		"b"))

		questions.append(Question("4. Garampani sanctuary is located at",
		"A. Junagarh, Gujarat",
		"B. Diphu, Assam",
		"C. Kohima, Nagaland",
		"D. Gangtok, Sikkim",
		"b"))		

		questions.append(Question("5. For which of the following disciplines is Nobel Prize awarded?",
		"A. Physics and Chemistry",
		"B. Physiology or Medicine",
		"C. Literature, Peace and Economics",
		"D. All of the above",
		"d"))

		questions.append(Question("6. Hitler party which came into power in 1933 is known as",
		"A. Labour Party",
		"B. Nazi Party",
		"C. Ku-Klux-Klan",
		"D. Democratic Party",
		"b"))		
		
		return questions #Return a list filled with questions

#Main program##########################################################	

#Initialization	
player = makePlayer()
print("\n") #Line shift for a more orderly presentation to the player
questions = createQuestions()

#Game loop
while(True): #Infitie loop that runs until break

	for i in questions: #For loop that iterates trough the question list
		print("Answer the following question with one letter:")
		i.printQuestion()
		userAnswer = input("Your answer:\n")
		if userAnswer.lower() == i.getCorrectAnswer(): #If check to see if the answer given by player is the correct one
			print("\nCorrect!\n") #User message
			player.increaseScore() #Increase score by 1
		else:
			print("\nWrong answer...\n") #User message, does not increase score

	print("Quiz is done " + player.getName() + ". Your score:", player.getScore()) #Present the score to the player
	
	playAgain = input("Play again? Press \"y\" or \"n\"") #Ask if the player want to try again
	if playAgain == "y": #If yes the score is reset and the game loop begins again
		player.resetScore()
	elif playAgain == "n":
		break	#Exits the loop if player writes "n"
	else:
		print("You did not type \"y\" or \"n\" so the game ends now!") #Give message to user that the input is wrong and ends the program
		break

#Main program ended#####################################################