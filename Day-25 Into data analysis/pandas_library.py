import pandas as pd

data = pd.read_csv('weather-data.csv')
# print(data)
temp_series = data['temp']
# print(temp_series)
# average = round(sum(temp_series)/len(temp_series), 2)
# print(average)

# central tendency
avg = round(temp_series.mean(), 2)
print(f"Average temperature {avg}")
max_temp = temp_series.max()
print(f"Maximum temperature {max_temp}")
min_temp = temp_series.min()
print(f"Minimum temperature {min_temp}")
freq_temp = temp_series.mode()
print(f'Most frequent temperature {freq_temp}')
median_temp = temp_series.median()
print(median_temp)

# return a specific row
print(data[data.temp == max(data.temp)])

monday = data[data.day == 'Monday']
print(monday)
print(monday.condition)

#celcius to fahrenheit
# (0°C × 9/5)°C  + 32 = 32°F
celcius = monday.temp
fahrenheit = (monday.temp * 9/5) + 32
print(fahrenheit)

#create dataframe from scratch
data_dict = {
    "students": ['a', 'b', 'c'],
    "scores": [10, 20, 15]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("new_csv.csv")






