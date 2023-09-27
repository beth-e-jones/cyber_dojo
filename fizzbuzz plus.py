"""Write a program that prints the numbers from 1 to 100, but...

#numbers that are exact multiples of 3, or that contain 3, must print a string 
# containing "Fizz" #For example 9 -> "...Fizz..." 
# #For example 31 -> "...Fizz..."

#numbers that are exact multiples of 5, or that contain 5, must print a string 
# containing "Buzz"  #For example 10 -> "...Buzz..."
  #For example 52 -> "...Buzz..."
  """
  
  # This code is unfinished, I can't get the  containing 3 and containing 5 to work

for fizzbuzz in range (1,100): 
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        
    elif fizzbuzz % 3 == 0:
        print("fizz")
    
    elif fizzbuzz % 5 == 0:
        print("buzz")
    
    else:
        print(fizzbuzz)
    

     