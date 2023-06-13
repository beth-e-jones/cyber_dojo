import numpy as np
import pandas as pd
from statistics import mean


number_sequence = [6, 9, 15, -2, 92, 11,232,-23]
meanval = mean(number_sequence)
length = len(number_sequence)
minval = min(number_sequence)
maxval = max(number_sequence)

print("Mean Value = ",meanval)
print("List length =",length)
print("Minimum value =",minval)
print("Maximum value =",maxval)