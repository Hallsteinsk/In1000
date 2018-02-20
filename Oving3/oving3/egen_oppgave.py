#Oppgave 5
#Egen oppgave. Lage polygon.
#Skriv et program som tar imot et tall fra bruker som bestemmmer hvor mange kanter et poligon skal ha.
#Deretter skal koordinater leses inn og poligonet tegnes basert paa dette med EzGraphics.

#(Skriver kommentarer paa engelse saa jeg slipper aa tenke paa bokstaver som ikke er det emgelske alfabet).
#Link to code I used in for EzGraphics: 
#- http://www.ezgraphics.org/UserGuide/GettingStarted
#- http://www.ezgraphics.org/UserGuide/Polygons

#My solution:


#Present the task for the user:
print("You are going to create a polygon.\nYou decide the number of edges and the location of the corners.\n")

#Read input from user to decide how many edges the polygon will have. Catches illegal inputs:
while(True):
	try:
		numberOfEdges = int(input("How manye edges will your polygon have? Choose a number from 3 to 8:"))
		while(True):
			if numberOfEdges < 3 or numberOfEdges > 8:
				numberOfEdges = int(input("You chose a wrong value for number of edges. Please try again.\nChoose a number from 3 to 8:"))
			else:
				break
		break
	except ValueError:
		print("You did not input a valid number. Pleas try again.")
		
#Decleares an empty list that fills with the coordinates frm the user. 
#Input-code catches non integer inputs. If the user sets a value outside 0 or 400, it will automaticly be set to minimum
#or maximum value: below 0 will be set to 0. Above 400 will be set to 400.
coordinateList = []
print("You have to input %.i x and y coordinates for your polygon.\nThe input values has to be between 0 and 400" % numberOfEdges)
for i in range(1, (numberOfEdges * 2) + 1):
	while(True):
		try:
			if i%2 == 1:
				x = int(input("Type inn x-ccordinate number %.i " % int((i/2) + 0.5)))
				if x < 0:
					coordinateList.append(0)
				elif x > 400:
					coordinateList.append(400)
				else:
					coordinateList.append(x)
			if i%2 == 0:
				y = int(input("Type inn y-ccordinate number %.i " % (i/2)))
				if y < 0:
					coordinateList.append(0)
				elif y > 400:
					coordinateList.append(400)
				else:
					coordinateList.append(y)
			break
		except ValueError:
			print("You did not input av valid number blease try again:")


#Import EzGraphics and create window and canvas
#The window is by default 400 X 400 pixels large.
from ezgraphics import GraphicsWindow
win = GraphicsWindow()
win.setTitle("Oppgave 5, egen_oppgave.py")
canvas = win.canvas()

#Draws the polygon onto the canvas:
if numberOfEdges == 3:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5])
elif numberOfEdges == 4:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5], 
	coordinateList[6], coordinateList[7])
elif numberOfEdges == 5:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5], 
	coordinateList[6], coordinateList[7],
	coordinateList[8], coordinateList[9])
elif numberOfEdges == 6:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5], 
	coordinateList[6], coordinateList[7],
	coordinateList[8], coordinateList[9],
	coordinateList[10], coordinateList[11])
elif numberOfEdges == 7:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5], 
	coordinateList[6], coordinateList[7],
	coordinateList[8], coordinateList[9],
	coordinateList[10], coordinateList[11],
	coordinateList[12], coordinateList[13])
elif numberOfEdges == 8:
	canvas.drawPolygon(
	coordinateList[0], coordinateList[1], 
	coordinateList[2], coordinateList[3], 
	coordinateList[4], coordinateList[5], 
	coordinateList[6], coordinateList[7],
	coordinateList[8], coordinateList[9],
	coordinateList[10], coordinateList[11],
	coordinateList[12], coordinateList[13],
	coordinateList[14], coordinateList[15])

#Wait for user to close the window
win.wait()