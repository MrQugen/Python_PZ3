import pandas as pd
from urllib.request import urlretrieve

urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/countries.csv',
            'countries.csv')
urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/covid-countries-data.csv',
            'covid-countries-data.csv')
countries_df = pd.read_csv('countries.csv')
covid_data_df = pd.read_csv('covid-countries-data.csv')

countries_df['gdp'] = countries_df.population*countries_df.gdp_per_capita
print(countries_df)