#100 doors in a row are all initially closed. You make 100 passes by the doors. The first time through, you visit every door and toggle the door (if the door is closed, you open it; if it is open, you close it).
#The second time you only visit every 2nd door (door #2, #4, #6, ...).
#The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.
#Question: What state are the doors in after the last pass? Which are open, which are closed?

#Make 100 booleans for the doors
import pandas as pd

number_of_doors = 100
#This sets doors as initially one way (in this circumstance, false = closed), tells python that all doors are closed
doorstate = [False] * number_of_doors


#F strings again! Mixes printed text with automated bits! This page asks us to print the number of doors, which is largely to check that
#python got it right.
print(f"number of doors: {number_of_doors}")
#Ok, a loop here. For every run in the number of runs (deifned as from 1 to the number of doors + 1 because python counts from 
# 0and I got confused)
for run in range(1, number_of_doors + 1):
    #for every door in each run
    for door_number in range(1, number_of_doors + 1):
       #If the modulo of the door number divided by the run is equal to zero (i.e., if there is no remainder)
        if door_number % run == 0:
            #So if the modular is 0 (or more) that means it's in the run that matches the door number like run 4 and door 12, 
            # the door state should change. here, i've written that if the door state is false,it should become true.
            #the door number - 1 accounts for python's weird zero indexing
            if doorstate[door_number-1] == False:
                doorstate[door_number-1] = True
                
                #Elif here caught me out writing this - initially it was an if, and so both things happened in the same run
                # e.g., it went from false to true, then back to false every run. This says that if the modulo is zero but 
                # the door is already open, then close the door
                
            #no instructions given for if the modulo is not zero
            elif doorstate[door_number-1] == True:
                doorstate[door_number-1] = False

#This line prints every individual door state of True(open) or False(closed) after N number of runs, as set in the first line
#It's an F string again
print(f"final door state: {doorstate}")

#This one is a little for loop to just print the number of doors that are open at the end. We can run it for every range
#because the loop above will iterate all the way to the end before it moves on to anything else. The same will happen here. 
for door_number in range(1, number_of_doors + 1):
    #If the doorstate is open, print the door number!
    if doorstate[door_number-1] == True:
        print(door_number)

