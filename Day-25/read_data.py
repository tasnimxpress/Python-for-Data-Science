# read weather data

import pandas as pd

data = pd.read_csv('weather-data.csv')
# print(data)
print(data.loc[0, 'day'])
print(data.at[0, 'day'])
