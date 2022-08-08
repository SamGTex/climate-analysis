import os
import pandas as pd
from methods.get_data import getWeatherForecast

# get parameters from config file
with open("config.txt") as f:
    lines = f.readlines()

params = []
for line in lines:
    line = line.replace(' ','')
    line = line.replace('\n','')

    name, value = line.split('=')
    locals()[name] = value
    params.append(value)
 
API_KEY = str(params[0])
LOCATION = str(params[1])
UNIT_GROUP = str(params[2])
YEAR_INIT = int(params[3])
YEAR_FINIT = int(params[4])

# list of all file names (name contains year of the data)
file_names = os.listdir('data/')
file_names = " ".join(file_names) # one long list
years_left = []

for year in range(YEAR_INIT, YEAR_FINIT):
    if not str(year) in file_names:
        years_left.append(year)

years_left.sort(reverse=True) # download nearest years first
print(f'Years open to download: {years_left}\n')


for year in years_left:
    print(f'Start download from {year}, {LOCATION}.')
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'

    csv_file = getWeatherForecast(API_KEY, LOCATION, UNIT_GROUP, start_date, end_date)

    liste = []
    for ind,Row in enumerate(csv_file):
        if ind==0:
            columns=Row
        else:
            liste.append(Row)


    df = pd.DataFrame(liste, columns=columns)
    df.to_csv(f'../data/Dortmund {start_date} to {end_date}.csv')