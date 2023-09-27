"""Given a list of integers find the closest to zero.
If there is a tie, choose the positive value."""

# %%
#Input list of numbers
list_numbers = [11, -3, 2, -5, 235, -93, 8]


# %%
# Calculate the difference between number and zero with absolute values
# Code for line 12 came from an example provided by "Thefourtheye" in
# https://stackoverflow.com/questions/20832769/how-to-obtain-the-absolute-value-of-numbers

abs_distance = [abs(number) for number in list_numbers]
print(abs_distance)

# %%
# Identify which value is closest to zero based on absolute distance
smallest_distance = min(abs_distance)
print(smallest_distance)

# %%
# Identify where in the index the integer closest to zero is
smallest_distance_index = abs_distance.index(smallest_distance)
# Set  this index position as variable
print(smallest_distance_index)

# %%
# Find the corresponding index position in the original list of numbers
closest_to_zero = list_numbers[smallest_distance_index]

# Print value closest to zero
print(f"The closest number to zero is {closest_to_zero}")

# %%
