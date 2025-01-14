import pandas as pd

events_file = "data/number_of_political_violence_events_by_country-year_as-of-13Dec2024.csv"
fatalities_file = "data/number_of_reported_fatalities_by_country-year_as-of-13Dec2024.csv"

events_data = pd.read_csv(events_file, sep=';')
fatalities_data = pd.read_csv(fatalities_file, sep=';')

merged_data = pd.merge(events_data, fatalities_data, on=['Country', 'Year'], how='outer')
merged_data = merged_data[(merged_data['Year'] >= 2010) & (merged_data['Year'] <= 2021)]

complete_countries = merged_data.groupby('Country').filter(lambda x: len(x['Year'].unique()) == 12)

output_file = "data/merged_country_year_events_fatalities.csv"
complete_countries.to_csv(output_file, sep=';', index=False)