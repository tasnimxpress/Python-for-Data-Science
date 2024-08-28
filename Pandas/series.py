# series
import pandas as pd

# list to series - pd.Series

# string data type: object
students = ['a', 'b', 'c']
print(type(students))
print(pd.Series(students))


# integer data type: int64
ages = [25, 26, 28]
age = pd.Series(ages)
print(age)


# float data type: float64
heights = [13.5, 16.4, 18.9]
height = pd.Series(heights)
print(height)


# different data type: object
mixed = ['a', 12, 18.2, 'hello', {'test': 'dictionary'}]
mixed_series = pd.Series(mixed)
print(mixed_series)
