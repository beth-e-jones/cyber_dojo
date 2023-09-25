#Given a list of integers find the closest to zero.
#If there is a tie, choose the positive value.

# %%
""" Route one option - just finds min and prints it"""
list_numbers = [11, -3, 5, 235, 8]

# %%
smallest_number = min(list_numbers)

# %%
print(f"The closest number to zero is {smallest_number}")



# %%
""" This previous solution doesn't account for minus numbers. 
I'll need a solution to identify minus numbers """