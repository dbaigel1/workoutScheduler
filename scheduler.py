# Gym Scheduler 
# Created by Daniel Baigel
# September 17, 2019
# 
# further applications:
# 	add workout feature, adds a workout to the database headers (e.g. cardio)
#   add a date for each muscle group so that you can see when the last time you
#   worked out that muscle group was, for data science you can then see longest intervals
#   b/w given workouts for a muscle group.

import csv
from datetime import date


#global variables
workouts = [] # names of muscles
workoutValues = [] # num of workouts for each muscle 
today = date.today()
lastDate = ""

#function declarations
def updateDataBase(inp, muscle):
	workoutValues[inp] += 1
	with open('workouts.csv', 'w', newline='') as csvfile:
		fieldnames = ['date', 'back', 'legs', 'chest', 'shoulders']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3]})
		
		print("Added entry to back. You have now worked out your %s %d times." %(muscle, workoutValues[inp]))
		print("The last time you worked out was %s." %(lastDate))
		print("For reference, today is %s." %(today))

#create database
def readData():
	with open('workouts.csv', mode='r') as csv_file:
	    csv_reader = csv.DictReader(csv_file)
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	            #print(f'Column names are {", ".join(row)}')
	            for item in row:
	            	if item == "date":
	            		global lastDate 
	            		lastDate = row[item]
	            	if item and item != "date":
	            		workouts.append(item)
	            line_count += 1
	        workoutValues.append(int(row["back"]))
	        workoutValues.append(int(row["legs"]))
	        workoutValues.append(int(row["chest"]))
	        workoutValues.append(int(row["shoulders"]))
	        line_count += 1
	        if line_count >= 2: #only one line of data so break after first loop
	        	break

#determine which muscle group for next workout
def nextMuscle(minMuscle, minValue, maxMuscle, maxValue):
#compute the minimum and maximum workout values
	for i in range(0, len(workouts)):
		if minValue > workoutValues[i]:
			minValue = workoutValues[i]
			minMuscle = workouts[i]

		if maxValue < workoutValues[i]:
			maxValue = workoutValues[i]
			maxMuscle = workouts[i]
	if minMuscle == "":
		print("All your muscles are equally worked out! \nTake a rest day, or start with back. \nYou've worked out everything %d times. Congrats!" %(maxValue))
	
	else:
		print("""The next muscle you should work out is: %s.\nIt has been worked out %d time(s). \nThat's %d fewer time(s) than %s.
		      """ %(minMuscle, minValue, (maxValue-minValue), maxMuscle))

#glossary for commands
def printCommands():
	print("The following are all possible commands:")
	print("\033[1m'next'\033[0m: prints what muscle group to workout next")
	print("\033[1m'back'\033[0m: adds a back & biceps workout to the database")
	print("\033[1m'legs'\033[0m: adds a leg workout to the database")
	print("\033[1m'chest'\033[0m: adds a chest & tricep workout to the database")
	print("\033[1m'shoulders'\033[0m: adds a shoulder workout to the database")
	print("\033[1m'stats'\033[0m: print current workout statistics")
	print("\033[1m'help'\033[0m: prints list of all possible commands")
	print("\033[1m'exit'\033[0m: exit the program")


#print current workout statistics
def printCurrentStats():
	print("Current workout statistics: ")
	for i in range(0, len(workouts)):
		print("Total workouts for %s: %d" %(workouts[i],workoutValues[i]))

#################### main program ##############################################

readData()
printCommands()

#create user interface
while True:
	print("Please enter a command:")
	userInput = str(input())

	if userInput == "back" or userInput == "biceps":

		updateDataBase(0, "back")

	elif userInput == "legs":
		#increment number of workouts in legs entry
		updateDataBase(1, "legs")

	elif userInput == "chest" or userInput == "triceps":
		#increment number of workouts in chest entry
		updateDataBase(2, "chest")
		
	elif userInput == "shoulders":
		#increment number of workouts in shoulders entry
		updateDataBase(3, "shoulders")

	elif userInput == "next":
		#print what muscle group the user should use next
		#i.e. the smallest integer in the arry
		minValue = 0
		for i in range(0, len(workoutValues)):
			minValue += workoutValues[i]
		nextMuscle("", minValue, "", 0)
		
	elif userInput == "help":
		printCommands()
	
	elif userInput == "exit":
		break

	elif userInput == "stats":
		printCurrentStats()

	else:
		print("Please enter a correct command")
		print("Types of commands include: 'back' or 'next'")

