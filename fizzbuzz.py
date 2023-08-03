#Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and
# for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range (1,100): 
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        
    elif fizzbuzz % 3 == 0:
        print("fizz")
    
    elif fizzbuzz % 5 == 0:
        print("buzz")
    
    else:
        print(fizzbuzz)
    
#Original error had the print outside the loop so it wasn't printing the number. For future, make sure else is in the loop

