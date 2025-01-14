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

chat gpt
import pandas as pd

# ND-GAIN Indicator Economy data
nd_gain_data = {
    "Economy ISO3": ["AFG", "AFG", "AFG", "AFG"],
    "Economy Name": ["Afghanistan", "Afghanistan", "Afghanistan", "Afghanistan"],
    "Indicator ID": [
        "UND.NDGAIN.capacity", 
        "UND.NDGAIN.economic", 
        "UND.NDGAIN.ecosystems", 
        "UND.NDGAIN.exposure"
    ],
    "Indicator": [
        "ND-GAIN Index: Adaptive Capacity",
        "ND-GAIN Index: Economic Readiness",
        "ND-GAIN Index: Ecosystem Services Vulnerability",
        "ND-GAIN Index: Exposure Vulnerability"
    ],
    "Attribute 1": ["-", "-", "-", "-"],
    "Attribute 2": ["-", "-", "-", "-"],
    "Attribute 3": ["-", "-", "-", "-"],
    "Partner": ["-", "-", "-", "-"],
    "1995": [None, None, None, None],
    "1996": [None, None, None, None],
    "1997": [None, None, None, None],
    "1998": [None, None, None, None],
    "1999": [0.9, 0.5, 0.52, 0.48],
    "2000": [0.9, 0.5, 0.52, 0.48],
    "2001": [0.9, 0.5, 0.52, 0.48],
    # More data truncated for brevity
    "2010": [0.79, 0.34, 0.52, 0.48],
    "2011": [0.78, 0.25, 0.52, 0.48],
    "2012": [0.78, 0.24, 0.52, 0.48],
    "2013": [0.75, 0.23, 0.52, 0.48],
    "2014": [0.76, 0.22, 0.51, 0.48],
    "2015": [0.73, 0.21, 0.51, 0.48],
}

# Convert ND-GAIN data to DataFrame
nd_gain_df = pd.DataFrame(nd_gain_data)

# Melt the ND-GAIN data to create a long format DataFrame
nd_gain_long = pd.melt(
    nd_gain_df,
    id_vars=["Economy ISO3", "Economy Name", "Indicator ID", "Indicator", "Attribute 1", "Attribute 2", "Attribute 3", "Partner"],
    var_name="Year",
    value_name="ND-GAIN Value"
)

# Event Fatalities data
event_data = {
    "Country": ["Algeria", "Algeria", "Algeria", "Algeria", "Algeria", "Algeria"],
    "Year": [2010, 2011, 2012, 2013, 2014, 2015],
    "Events": [107.0, 158.0, 125.0, 138.0, 126.0, 78.0],
    "Fatalities": [246, 306, 245, 341, 227, 154]
}

# Convert event data to DataFrame
event_df = pd.DataFrame(event_data)

# Merge the two DataFrames on Year and Country/Economy Name
merged_df = pd.merge(
    nd_gain_long,
    event_df,
    left_on=["Year", "Economy Name"],
    right_on=["Year", "Country"],
    how="inner"
)

# Display the merged DataFrame
print(merged_df)
#
