#100 doors in a row are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it).
#The second time you only visit every 2nd door (door #2, #4, #6, ...).
#The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.
#Question: What state are the doors in after the last pass? Which are open, which are closed?

#Make 100 booleans for the doors
import pandas as pd

number_of_doors = 100
doorstate = [False] * number_of_doors


print(f"number of doors: {number_of_doors}")
for run in range(1, number_of_doors + 1):
    for door_number in range(1, number_of_doors + 1):
        if door_number % run == 0:
            if doorstate[door_number-1] == False:
                doorstate[door_number-1] = True
            elif doorstate[door_number-1] == True:
                doorstate[door_number-1] = False

print(f"final door state: {doorstate}")

for door_number in range(1, number_of_doors + 1):
    if doorstate[door_number-1] == True:
        print(door_number)

