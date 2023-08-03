#Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and
# for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range (1,100): #for some reason, the last printed thing is always the second number in this range minus one. fix!
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print ("fizzbuzz")
        
    elif fizzbuzz % 3 == 0:
        print ("fizz")
    
    elif fizzbuzz % 5 == 0:
        print ("buzz")
    
#need to find way of printing the other numbers as at the moment i've just told it to print if these conditions apply
# i don't know how to get it to give me everything else too      

print(fizzbuzz)