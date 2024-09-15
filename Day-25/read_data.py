# read weather data

with open('weather-data.csv') as file:
    for _ in file:
        data = file.readlines()
        print(data)
