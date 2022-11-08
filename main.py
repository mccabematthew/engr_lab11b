import csv

# open csv as generic var.
with open('WeatherDataWindows.csv', mode='r') as file:

    # reading csv data as dicts and creating lists for later purpose
    datafile = csv.DictReader(file)
    max_temps = []
    min_temps = []
    avg_temps = []
    precip = []
    months = []
    hum = []
    bad_day = []
    ovr_95 = []
    undr_50 = []


    # for loop to loop through each line in weather data file
    for lines in datafile:
        # transforming weather data to approp. data type, and adding to list
        max_temps.append(int(lines['Temp High']))
        min_temps.append(int(lines['Temp Low']))
        precip.append(float(lines['Precipitation (in.)']))
        months.append(lines['Date'])
        hum.append(int(lines['Humidity Avg']))

    for i in hum:
        if i > 95:
            bad_day.append(i)

    # sorting temp lists to get highest and lowest temp on 3 yr period and assigning
    max_temps.sort()
    min_temps.sort()
    sent_max = max_temps[-1]
    sent_min = min_temps[0]

    for i in max_temps:
        if i > 95:
            ovr_95.append(i)
    for i in min_temps:
        if i < 50:
            undr_50.append(i)

    # precipitation calc.
    avg_precip = sum(precip) / len(precip)
    bad_days = len(bad_day)
    sum_ovr_95 = len(ovr_95)
    sum_undr_50 = len(undr_50)

    # formatted p statements for readability
    print(f'\n\tThe max. and min. temp over the 3 year period was {sent_max} deg. f, and {sent_min} deg. f respectively')
    print(f'\tThe average daily precipitation across three years was {avg_precip:.2f} in.')
    # interesting analysis statements
    print('\n\t\t\t\t-----------------Hmmmm... Interesting-----------------')
    print(f'\tOver the 3 year period, there were {bad_days} days where the avg humidity was above 95')
    print(f'\tFurthermore, the amount of days where the temp was below 50 is {sum_undr_50}, hope you brought a parka!')
    print(f'\tFinally, the amount of days where the temp was above 95 is {sum_ovr_95}, WOW toasty!')

