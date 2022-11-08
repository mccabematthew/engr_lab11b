import csv

# open csv as generic var.
with open('WeatherDataWindows.csv', mode='r') as file:

    # reading csv data as dicts and creating lists for later purpose
    datafile = csv.DictReader(file)
    max_temps = []
    min_temps = []
    precip = []

    # for loop to loop through each line in weather data file
    for lines in datafile:
        # transforming weather data to approp. data type, and adding to list
        max_temps.append(int(lines['Temp High']))
        min_temps.append(int(lines['Temp Low']))
        precip.append(float(lines['Precipitation (in.)']))

    # sorting temp lists to get highest and lowest temp on 3 yr period and assigning
    max_temps.sort()
    min_temps.sort()
    sent_max = max_temps[-1]
    sent_min = min_temps[0]

    # precipitation calc.
    avg_precip = sum(precip) / len(precip)

    # formatted p statements for readability
    print(f'The max. and min. temp over the 3 year period was {sent_max}, and {sent_min} respectively')
    print(f'The average daily precipitation across three years was {avg_precip:.2f} in.')

