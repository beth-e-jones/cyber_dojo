def fizzbuzz(iterable_range=range(1,6),number_1=3, number_2=5, empty_string=""):
    for fizzbuzz in iterable_range:
        #empty_string = ""
        if fizzbuzz % (number_1) == 0:
            empty_string = empty_string + "fizz"
            
        if fizzbuzz % (number_2) == 0:
            empty_string = empty_string + "buzz"
                    
        if empty_string != "":
            print(empty_string)      
                
        if fizzbuzz % (number_1) != 0 and fizzbuzz % (number_2) != 0:
            print(fizzbuzz)       
        
   
fizzbuzz()
        

    