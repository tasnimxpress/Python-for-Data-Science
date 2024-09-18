# read weather data

import pandas as pd

data = pd.read_csv('weather-data.csv')
# print(data)
# avg_temp = round(data['temp'].mean())
# max_temp = data['temp'].max()

# print(avg_temp, max_temp)

# get row
row = data.iloc[0, 0:]
print(row)

print(data[data['day'] == 'Monday'])
