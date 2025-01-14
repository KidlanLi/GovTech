import pandas as pd

data_file = "data/UND-NDGAIN.csv"

data = pd.read_csv(data_file)

year_columns = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
columns_to_keep = ["Economy Name", "Indicator"] + year_columns
filtered_data = data[columns_to_keep]

long_data = pd.melt(
    filtered_data,
    id_vars=["Economy Name", "Indicator"],
    var_name="Year",
    value_name="Value"
)

pivot_data = long_data.pivot_table(
    index=["Economy Name", "Year"],
    columns="Indicator",
    values="Value"
).reset_index()

pivot_data.rename(columns={"Economy Name": "Country"}, inplace=True)

output_file = "data/cleaned_UND_NDGAIN.csv"
pivot_data.to_csv(output_file, index=False)
