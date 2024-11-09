import pandas as pd

df = pd.read_csv('Squirrel_Census.csv')

color = df.groupby(['Primary Fur Color']).count()

color_series = color['X']

new_df = pd.DataFrame({'count': color_series})
print(new_df)

new_df.to_csv('numberOfSquirell.csv')
