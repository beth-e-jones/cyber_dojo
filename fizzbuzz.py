"""Write a program that prints the numbers from 1 to 100. But for multiples of 
three print "Fizz"  instead of the number and for the multiples of five 
print "Buzz". For numbers  which are multiples of both three and five print 
"FizzBuzz".
"""

for fizzbuzz in range (1,100):
    # Create empty string for each iteration to print fizzbuzz
    empty_string = ""
    if fizzbuzz % 3 == 0:
        # Update empty string to add fizz if conditions met
        empty_string = empty_string + "fizz"
        
    if fizzbuzz % 5 == 0:
        # Update empty string to add buzz if conditions met
        empty_string = empty_string + "buzz"
    
    # If something is in the string (e.g., fizz or buzz, print that)
    if empty_string != "":
        print(empty_string)
        
# If neither fizz or buzz conditions apply, print the number
        
    if fizzbuzz % 3 != 0 and fizzbuzz % 5 != 0:
        print(fizzbuzz)
    
#Original error had the print outside the loop so it wasn't printing the number. 
# For future, make sure else is in the loop

