import pandas as pd
from urllib.request import urlretrieve

urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/countries.csv',
            'countries.csv')
urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/covid-countries-data.csv',
            'covid-countries-data.csv')
countries_df = pd.read_csv('countries.csv')
covid_data_df = pd.read_csv('covid-countries-data.csv')

combined_df = countries_df.merge(covid_data_df, on="location")
min_gdp = combined_df[combined_df.population > 10000000].sort_values('gdp_per_capita').head(20)
min_hospital = combined_df[combined_df.population > 10000000].sort_values('hospital_beds_per_thousand').head(20)
print(min_gdp.merge(min_hospital))
