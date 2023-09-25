#Given a list of integers find the closest to zero.
#If there is a tie, choose the positive value.

# %%
""" Route one option - just finds min and prints it. 
Need function solution later"""
list_numbers = [11, -4, 3, 5, 235, 8]

# %%
# define smallest number as the minimum
smallest_number = min(list_numbers)

# %%
""" This doesn't prioritise positive numbers over negative. Needs fix"""

# %%
for int in list_numbers:
    if smallest_number < 0:
        smallest_number = (smallest_number * -1)

print(smallest_number)

# %%
# print result
print(f"The closest number to zero is {smallest_number}")
# %%
