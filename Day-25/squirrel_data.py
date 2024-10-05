import pandas as pd

df = pd.read_csv('Squirrel_Census.csv')

color = df.groupby(['Primary Fur Color']).count()
# print(color)
# print(type(color)) # dataframe

color_series = color['X']
# print(color_series)
# print(type(color_series)) # Series

new_df = pd.DataFrame({'count': color_series})
print(new_df)
new_df.to_csv('numberOfSquirell.csv')
