# read weather data

import pandas as pd

data = pd.read_csv('weather-data.csv')
print(data['temp'])
