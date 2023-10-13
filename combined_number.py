"""Write a function accepting a list of non negative integers, and returning 
their largest possible combined number as a string. For example

given [50, 2, 1, 9]  it returns "95021"    (9 + 50 + 2 + 1)
given [5, 50, 56]    it returns "56550"    (56 + 5 + 50)
given [420, 42, 423] it returns "42423420" (42 + 423 + 420)"""

# This only works for single digit solutions, updated solution to be done soon
# %%
# Import initial list
separated_list = [2, 6, 4, 9]

# %%
# Sort the list into descending order
separated_list.sort(reverse= True)
print(separated_list)

# %%
# Create a blank string, append each item converted to string to blank string
blank_string = ""
for i in separated_list:
    blank_string += str(i)

print(blank_string)
# %%
