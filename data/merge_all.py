import pandas as pd

und_ndgain_file = "data/cleaned_UND_NDGAIN.csv"
merged_file = "data/merged_country_year_events_fatalities.csv"

und_ndgain_data = pd.read_csv(und_ndgain_file)
merged_data = pd.read_csv(merged_file, sep=';')

filtered_data = und_ndgain_data[und_ndgain_data['Country'].isin(merged_data['Country'])]

final_data = pd.merge(filtered_data, merged_data[['Country', 'Year', 'Events', 'Fatalities']], on=['Country', 'Year'], how='inner')

output_file = "data/final.csv"
final_data.to_csv(output_file, index=False)