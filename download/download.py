from methods.get_data import getWeatherForecast
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

# user input: year
year = input('Download daily temperature data for the year: ')

# params
API_KEY="XFX3XC3N2BQDJ4PX78TAJSN9Q"
LOCATION="Dortmund"
UNIT_GROUP="metric"

dic = os.listdir('../data')
print(dic)
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