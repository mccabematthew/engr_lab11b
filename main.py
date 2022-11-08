import csv

with open('WeatherDataWindows.csv', mode='r') as file:

    weather_file = csv.reader(file)
    weather = file.readlines()
    next_line = file.readline()

    #print(extreme_high)

    while next_line != '':
        file.readline()
        weather.split()
        print(next_line, end='')

#def extreme_temps():
#   if
