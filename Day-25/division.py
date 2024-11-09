import pandas as pd

df = pd.read_csv("E:/GitHub/100DaysOfPython/Day-25/division.csv")
# print(df)


def division(name):
    corrdinate = df[df['division'] == name]
    X = corrdinate['x'].iloc[0]
    Y = corrdinate['y'].iloc[0]
    return (X, Y)


print(division('Rajshahi'))
print(len(df))
