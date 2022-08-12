import os
import pandas as pd
from methods.get_data import getWeatherForecast

#----------BEGIN FUNCTIONS-------------------------------------------------------------

# get parameters from config.txt: 
# api_key, location, unit_group, start_date, end_date
def get_params(path):
    with open("config.txt") as f:
        lines = f.readlines()

        params = []
        for line in lines:
            line = line.replace(' ','')
            line = line.replace('\n','')

            name, value = line.split('=')
            locals()[name] = value
            params.append(value)

        api_key = str(params[0])
        location = str(params[1])
        unit_group = str(params[2])
        start_date = params[3]
        end_date = params[4]
    return api_key, location, unit_group, start_date, end_date

# check if data already downloaded
def check_exist(file_names, start_date, end_date):
    _file_exa = f'Dortmund {start_date} to {end_date}.csv'
    return _file_exa in file_names

# download data
def download(api_key, location, unit_group, start_date, end_date, file_names, save_path):
    # check if file already exist, than skip
    if check_exist(file_names, start_date, end_date):
        print(f'Already downloaded: {start_date} to {end_date}')
        return

    # request data from visualcrossing
    data = getWeatherForecast(api_key, location, unit_group, start_date, end_date)
    
    data_csv = []
    for ind,Row in enumerate(data):
        if ind==0:
            columns=Row
        else:
            data_csv.append(Row)

    df = pd.DataFrame(data_csv, columns=columns)
    df.to_csv(f'{save_path}/Dortmund {start_date} to {end_date}.csv')
    return
#----------END FUNCTIONS---------------------------------------------------------------

def main():
    # get parameters
    API_KEY, LOCATION, UNIT_GROUP, START_DATE, END_DATE = get_params('config.txt')

    if len(API_KEY) != 25:
        print('Please enter a valid API Key to config.txt!')
        print('Check your account details to get you personal Key: https://www.visualcrossing.com/account')
        return

    # get initial/finit day, month and year as Integer
    year_i, month_i, day_i = map(int, START_DATE.split('-')) # start date
    year_f, month_f, day_f = map(int, END_DATE.split('-')) # end data

    # console output
    print(f'---- Requested weather data: {START_DATE} to {END_DATE} ----')
    print('You can change the period any time in the config file.')
    print('Please take care of the date format: yyyy-mm-dd\n')

    # create folder to save the requested data
    save_path = f'data/{LOCATION}_{START_DATE}_{END_DATE}'
    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    # get existing file names currently saved in the target save folder
    file_names = os.listdir(save_path)

    # download data yearly
    if year_i == year_f: #request contains maximum one year
        start_date = f'{year_i}-{month_i}-{day_i}'
        end_date = f'{year_i}-12-31'
        download(API_KEY, LOCATION, UNIT_GROUP, START_DATE, END_DATE, file_names, save_path)

    else: #request contains several years
        # first year
        start_date = f'{year_i}-{month_i}-{day_i}'
        end_date = f'{year_i}-12-31'
        download(API_KEY, LOCATION, UNIT_GROUP, start_date, end_date, file_names, save_path)

        # full years exluding first and last year
        for year in range(year_i+1, year_f):
            start_date = f'{year}-01-01'
            end_date = f'{year}-12-31'
            download(API_KEY, LOCATION, UNIT_GROUP, start_date, end_date, file_names, save_path)
        
        # last year
        start_date = f'{year_f}-01-01'
        end_date = f'{year_f}-{month_f}-{day_f}'
        download(API_KEY, LOCATION, UNIT_GROUP, start_date, end_date, file_names, save_path)


if __name__=='__main__':
    main()