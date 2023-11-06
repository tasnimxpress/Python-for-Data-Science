import csv

with open('weather-data.csv') as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        temp = row[1]
        temperature.append(temp)
        for i in range(1, len(temperature)):
            temperature[i] = int(temperature[i])
    print(temperature[1:])

    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
