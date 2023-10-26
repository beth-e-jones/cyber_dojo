"""Write a function accepting a list of non negative integers, and returning 
their largest possible combined number as a string. For example

given [50, 2, 1, 9]  it returns "95021"    (9 + 50 + 2 + 1)
given [5, 50, 56]    it returns "56550"    (56 + 5 + 50)
given [420, 42, 423] it returns "42423420" (42 + 423 + 420)"""

import itertools

def largest_combined_number(separated_list=[1,6]):
    number_length = len(separated_list)
    # Generate all possible permutations of numbers
    for item in separated_list:
        possible_combinations = list(
            itertools.permutations(
                separated_list, # Use separated list as input
                r=number_length # number of items in each permutation
            )
        )
    # print all possible combinations 
    print(possible_combinations)

    # create blank list for concatenated string for each permutation
    combined_combinations = []
    # for each combination, join the string of the numbers 
    for combination in possible_combinations:
        combined_values = "".join(
            [str(value) for value in combination]
        )
        # appending as an integer into empty list
        combined_combinations.append(int(combined_values)) 

    print(combined_combinations)
    print(type(combined_combinations))

    combined_combinations.sort(reverse=True)
    print(combined_combinations)

    # Print largest combination based on max value in combined list
    print(f"The largest possible combination is",(combined_combinations[0]))

    return(None)


largest_combined_number()
