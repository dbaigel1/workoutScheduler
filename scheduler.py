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
from datetime import datetime


#global variables
workouts = [] # names of muscles
workoutValues = [] # num of workouts for each muscle 
today = date.today()
lastDate = "" #last time I worked out
muscleDates = [] #dates of last workout for each muscle

#function declarations
def updateDataBase(inp, muscle):
	workoutValues[inp] += 1
	lastTime = muscleDates[inp]
	muscleDates[inp] = today
	with open('workouts.csv', 'w', newline='') as csvfile:
		fieldnames = ['date', 'back','legs', 'chest', 'shoulders','backDate', 'legsDate', 'chestDate', 'shouldersDate']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3], 'backDate': muscleDates[0], 'legsDate': muscleDates[1], 'chestDate': muscleDates[2], 'shouldersDate': muscleDates[3]})
		
		print("Added entry to %s. You have now worked out your %s %d times." %(muscle, muscle, workoutValues[inp]))
		print("The last time you worked out was %s." %(lastDate))
		print("The last time you worked out your %s was %s." %(muscle, lastTime))
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
	            	if item and "Date" not in item and item != "date":
	            		workouts.append(item)
	            line_count += 1
	        #populate muscle values from data
	        workoutValues.append(int(row["back"]))
	        workoutValues.append(int(row["legs"]))
	        workoutValues.append(int(row["chest"]))
	        workoutValues.append(int(row["shoulders"]))
	        #populate most recent dates from data
	        muscleDates.append(row["backDate"])
	        muscleDates.append(row["legsDate"])
	        muscleDates.append(row["chestDate"])
	        muscleDates.append(row["shouldersDate"])

	        line_count += 1
	        if line_count >= 2: #only one line of data so break after first loop
	        	break

#determine which muscle group for next workout
def nextMuscle(minMuscle, minValue, maxMuscle, maxValue):
#compute the minimum and maximum workout values
	allEqual = True
	currMaxDate = today
	currMuscle = ""
	for i in range(0, len(workouts)):
		if minValue > workoutValues[i]:
			minValue = workoutValues[i]
			minMuscle = workouts[i]

		if maxValue < workoutValues[i]:
			maxValue = workoutValues[i]
			maxMuscle = workouts[i]

		
		if i < len(workouts) - 1:
			if workoutValues[i] != workoutValues[i+1]:
				allEqual = False

		#do 2 checks for least recent date & muscle worked out
		
		if type(muscleDates[i]) is str:
			temp = datetime.strptime(muscleDates[i], '%Y-%m-%d')
			temp = temp.date()
		else:
			temp = muscleDates[i]
		
		check = today - temp

		check2 = today - currMaxDate
		
		if check.days > check2.days:
			currMaxDate = (datetime.strptime(muscleDates[i], '%Y-%m-%d')).date()
			currMuscle = workouts[i]
		deltaDate = today - currMaxDate

	if allEqual:
		print("All your muscles are equally worked out!\nYou've worked out everything %d times. Congrats! \nTake a rest day, or start with %s. \nThe last time you worked out %s was %d days ago." %(maxValue, currMuscle, currMuscle, deltaDate.days))
	
	else:
		print("""The next muscle you should work out is: %s.\nIt has been worked out %d time(s). \nThat's %d fewer time(s) than %s. \nThe last time it was worked out was %s.\nThat's %d days ago. 
		      """ %(minMuscle, minValue, (maxValue-minValue), maxMuscle, currMaxDate, deltaDate.days))

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
	print("Most recent workout was on: %s" %(lastDate))
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
		#i.e. the smallest integer in the array
		#initialize minValue to be value larger than all items in array
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

