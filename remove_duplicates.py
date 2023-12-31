"""Define a function RemoveDuplicate(nlist) to remove duplicate elements 
from list. Here are some examples:

[] -> []

[1,2] -> [1,2]

[1,1,2,2,3,3] -> [1,2,3]

Author: Ramya V, KGISL
""" 

# Define function and set original number list
def duplicate_removal(number_list = [2, 2, 3, 5, 7, 7, 8]):
    # create empty list to append into
    empty_list=[]
    # loop to append every number from original list not already in new list
    for i in number_list:
        if i not in empty_list:
            empty_list.append(i)
            
    print(empty_list)

# Now function defined, running it will return the newly populated empty list  
duplicate_removal()