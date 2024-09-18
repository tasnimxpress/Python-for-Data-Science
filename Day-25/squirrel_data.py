import pandas as pd

df = pd.read_csv('Squirrel_Census.csv')

color = df.groupby(['Primary Fur Color']).count()
# print(type(color)) # dataframe

color_series = color['X']
print(color_series)

# print(type(color_series))
new_df = pd.DataFrame(
    ['color_series', index = 'Primary Fur Color', columns = 'X']).squeeze()
print(new_df)
