# Climate-Analysis: Make your own Climate Analysis

## Download weather data
1. Get API Key
   - create a free account with [Visual Crossing](https://www.visualcrossing.com/) (requires email)
   - press on the Button "Account" and copy your API-Key to clipboard
2. Specify the requested Data
   - open the config.txt file in an editor
   - replace "YourPersonalKey" with the API-Key
   - define requested data with parameters:
     - UNIT_GROUP: default *metric* ([Documentation](https://www.visualcrossing.com/resources/documentation/weather-api/unit-groups-and-measurement-units/))
     - LOCATION: place of the requested weather data
     - START_DATE [yyyy-mm-dd]: the first date of the requested data range
     - END_DATE [yyyy-mm-dd]: the last date of the requested data range
 3. Start Download
    - execute `python download.py` or `python3 download.py`
    - the new folder *data* contains the downloaded data
    - **Attention**: Only 1000 request(days) per day free.
      Repeat step 3 daily until the data is complete or pay for the data ([Pricing](https://www.visualcrossing.com/weather-data-editions))

      
## Example climate analysis: Dortmund from 1973 to 2022

### I. Progress of the *daily* mean temperature
![daily](figures/png/temp_timeline_1973-2022.png)
- 4 from 5 days with highest maximum daily temperature were after or in 2019
- all 5 days with the minimum daily temperature were before or in 1997
- mean temperature: 10.37 °C
- the linear model predicts a increase of 0.14 °C in ten years

### II. Timeline of the *yearly* minimum, maximum and average temperature
![yearly](figures/png/annual_temp_1973-2022.png)
- increase of annual max. Temperature in ten years: 0.75 °C
- increase of annual min. Temperature in ten years: 0.63 °C
- increase of annual avg. Temperature in ten years: 0.12 °C

## Export Jupyter Notebook
Requires [nbconvert](https://nbconvert.readthedocs.io/en/latest/install.html)

- HTML (dark theme)

  `jupyter nbconvert Report_Dortmund_2022.ipynb --to html --HTMLExporter.theme=dark`

- PDF (white, article)

  `jupyter nbconvert --to pdf Report_Dortmund_2022.ipynb`

## Todo
- [x] config file: metric, key, location, start and end data
- [ ] explore the frequency of extreme hot/cold days
- [ ] analyze windspeed
- [ ] analyze rain and snow

## Data Source
https://www.visualcrossing.com/

## Author

**Samuel Haefs**

- [Profile](https://github.com/SamGTex "Samuel Haefs")
- [Email](mailto:samuel.haefs@tu-dortmund.de "samuel.haefs@tu-dortmund.de")
