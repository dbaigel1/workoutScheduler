# Gym Scheduler 
# Created by Daniel Baigel
# September 17, 2019

# program will do 2 different things based on input
# 1. Add entry to workout database
#		if input is a string, increment data entry on that string by 1
# 2. Return what muscle to workout next 
#		if input is "workout" return the muscle group with least entries
#		further application could tell you how much less you have worked 
#		out this muscle than other entries.
#
# Data will be stored in a csv file, and then stored in the program as a dictionary
# Key will be string ("Back", "Chest", etc.) and Value will be number of entries.

#create database
import csv

#create arrays
workouts = []
workoutValues = []

with open('workouts.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            for item in row:
            	if item:
            		workouts.append(item)
            line_count += 1
        print(f'\t back workouts: {row["back"]} \n leg workouts: {row["legs"]} \n chest workouts: {row["chest"]} \n shoulder workouts: {row["shoulders"]}')
        workoutValues.append(int(row["back"]))
        workoutValues.append(int(row["legs"]))
        workoutValues.append(int(row["chest"]))
        workoutValues.append(int(row["shoulders"]))
        line_count += 1
        if line_count >= 2: #only one line of data so break after first loop
        	break
    print(f'Processed {line_count} lines.')


print(workouts)
print(workoutValues)



#input from user
processed = False

while not processed:
	
	print("Please enter a command:")
	userInput = str(input())

	if userInput == "back" or userInput == "biceps":
		#increment number of workouts in back entry
		#print total number of workouts in that category
		processed = True
	elif userInput == "legs":
		#increment number of workouts in legs entry
		processed = True
	elif userInput == "chest" or userInput == "triceps":
		#increment number of workouts in chest entry
		processed = True
	elif userInput == "shoulders":
		#increment number of workouts in shoulders entry
		processed = True
	elif userInput == "next":
		#print what muscle group the user should use next
		#i.e. the smallest integer in the dictionary
		processed = True
	else:
		print("Please enter a correct command")
		print("Types of commands include: 'back' or 'next'")

#create user interface

#write back to csv file with new value
#with open('workouts.csv', 'w', newline='') as csvfile:
#    fieldnames = ['back', 'legs', 'chest', 'shoulders']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
