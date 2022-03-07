# Dataframe of temperatures
# 01/23/2022
# CSC221 M1Lab – DataFrame
# Alina Florestal

#import pandas for dataframe
import pandas as pd

#dictionary
temp_dict = {'Maxine': [87, 70, 55], 'James': [33, 44, 90], 'Amanda': [21, 32, 87]}

#dataframe changes a to j(b)
temperatures = pd.DataFrame(temp_dict, index=['Morning', 'Afternoon', 'Evening'])
print("a&b:Temperature Dataframe")
print(temperatures)
print("c:Select column for Maxine")
print(temperatures['Maxine'])
print("d:Select row for Morning readings")
print(temperatures.loc['Morning'])
print("e:Select row for Morning and Evening Readings")
print(temperatures.loc[['Morning','Evening']])
