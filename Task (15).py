import pandas as pd
from urllib.request import urlretrieve

urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/countries.csv',
            'countries.csv')
urlretrieve('https://raw.githubusercontent.com/ChornaOlga/PLfDA/main/LAB_3/covid-countries-data.csv',
            'covid-countries-data.csv')
countries_df = pd.read_csv('countries.csv')
covid_data_df = pd.read_csv('covid-countries-data.csv')

combined_df = countries_df.merge(covid_data_df, on="location")
combined_df['tests_per_million'] = combined_df['total_tests'] * 1e6 / combined_df['population']
combined_df['cases_per_million'] = combined_df['total_cases'] * 1e6 / combined_df['population']
combined_df['deaths_per_million'] = combined_df['total_deaths'] * 1e6 / combined_df['population']
print(combined_df.sort_values('deaths_per_million', ascending=False).head(10))
