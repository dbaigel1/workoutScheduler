# Gym Scheduler 
# Created by Daniel Baigel
# September 17, 2019

# program will do 2 different things based on input
# 1. Add entry to workout database
#		if input is a string, increment data entry on that string by 1
# 
# further applications:
# 	add workout feature, adds a workout to the database headers (e.g. cardio)
# Data will be stored in a csv file, and then stored in the program as a dictionary
# Key will be string ("Back", "Chest", etc.) and Value will be number of entries.

#create database
import csv
from datetime import date


#create arrays
workouts = []
workoutValues = []
today = date.today()
lastDate = ""

with open('workouts.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            for item in row:
            	if item == "date":
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
    print(f'Processed {line_count} lines.')

#print current workout statistics
print("Current workout statistics: ")
for i in range(0, len(workouts)):
	print("Total workouts for %s is: %d" %(workouts[i],workoutValues[i]))


#input from user
processed = False


#create user interface
while not processed:
	
	print("Please enter a command:")
	userInput = str(input())

	if userInput == "back" or userInput == "biceps":
		#increment number of workouts in back entry
		#print total number of workouts in that category
		#write back to csv file with new value
		workoutValues[0] += 1
		with open('workouts.csv', 'w', newline='') as csvfile:

			fieldnames = ['date', 'back', 'legs', 'chest', 'shoulders']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3]})
		processed = True
		print("Added entry to back. You have now worked out your back %d times." %(workoutValues[0]))
		print("The last time you worked out was %s." %(lastDate))
		print("For reference, today is %s." %(today))

	elif userInput == "legs":
		#increment number of workouts in legs entry
		workoutValues[1] += 1
		with open('workouts.csv', 'w', newline='') as csvfile:

			fieldnames = ['date', 'back', 'legs', 'chest', 'shoulders']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3]})
		processed = True
		print("Added entry to legs. You have now worked out your legs %d times." %(workoutValues[1]))
		print("The last time you worked out was %s." %(lastDate))
		print("For reference, today is %s." %(today))

	elif userInput == "chest" or userInput == "triceps":
		#increment number of workouts in chest entry
		workoutValues[2] += 1
		with open('workouts.csv', 'w', newline='') as csvfile:

			fieldnames = ['date', 'back', 'legs', 'chest', 'shoulders']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3]})
		processed = True
		print("Added entry to chest. You have now worked out your chest %d times." %(workoutValues[2]))
		print("The last time you worked out was %s." %(lastDate))
		print("For reference, today is %s." %(today))
		
	elif userInput == "shoulders":
		#increment number of workouts in shoulders entry
		workoutValues[3] += 1
		with open('workouts.csv', 'w', newline='') as csvfile:

			fieldnames = ['date', 'back', 'legs', 'chest', 'shoulders']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerow({'date': today, 'back': workoutValues[0], 'legs': workoutValues[1], 'chest': workoutValues[2], 'shoulders': workoutValues[3]})
		processed = True
		print("Added entry to shoulders. You have now worked out your shoulders %d times." %(workoutValues[3]))
		print("The last time you worked out was %s." %(lastDate))
		print("For reference, today is %s." %(today))

	elif userInput == "next":
		#print what muscle group the user should use next
		#i.e. the smallest integer in the arry
		processed = True
		minMuscle = ""
		minValue = workoutValues[0]
		maxValue = 0
		maxMuscle = ""

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
			print("""The next muscle you should workout is: %s. \n 
			     	 It has been workedout %d times. \n
			     	 That's %d fewer times than %s.
			      """ %(minMuscle, minValue, maxValue, maxMuscle))

	elif userInput == "help":
		print("The following are all possible commands:") #glossary for commands
		print("\033[1m'next'\033[0m: prints what muscle group to workout next")
		print("\033[1m'back'\033[0m: adds a back & biceps workout to the database")
		print("\033[1m'legs'\033[0m: adds a leg workout to the database")
		print("\033[1m'chest'\033[0m: adds a chest & tricep workout to the database")
		print("\033[1m'shoulders'\033[0m: adds a shoulder workout to the database")
		print("\033[1m'help'\033[0m: prints list of all possible commands")
	
	elif userInput == "exit":
		break

	else:
		print("Please enter a correct command")
		print("Types of commands include: 'back' or 'next'")

