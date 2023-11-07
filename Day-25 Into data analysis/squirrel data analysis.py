import pandas as pd

df = pd.read_csv('2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

# grey = (df['Primary Fur Color'] == 'Gray').value_counts()
# total_gray = len(df[df['Primary Fur Color'] == 'Gray'])

gray = df['Primary Fur Color'].value_counts()['Gray']
# print(gray)
red = df['Primary Fur Color'].value_counts()['Cinnamon']
# print(red)
black = df['Primary Fur Color'].value_counts()['Black']
# print(black)

data_file = {
    "squirrels": ['gray', 'red', 'black'],
    "total": [gray, red, black]
}
new_df = pd.DataFrame(data_file)
new_df.to_csv("total_squirrel_by_color.csv")
