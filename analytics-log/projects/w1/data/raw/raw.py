import datadotworld as dw
import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://data.world/cmack624/us-food-insecurity-1995-2019'

food_insecurity_dataset = dw.load_dataset(data_url)

# print(food_insecurity_dataset.describe())
# {'name': 'cmack624_us-food-insecurity-1995-2019', 'title': 'U.S. Food Insecurity 1995-2019', 'description': 'Food Security Status of U.S. Households 1995-2019 (source: USDA ERS)', 'homepage': 'https://data.world/cmack624/us-food-insecurity-1995-2019', 'license': 'Public Domain', 'resources': [{'name': 'trends', 'path': 'data/trends.csv', 'format': 'csv', 'profile': 'data-resource'}, {'name': 'original/Food Insecurity - 1995 to 2019.xlsx', 'path': 'original/Food Insecurity - 1995 to 2019.xlsx', 'format': 'xlsx', 'mediatype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'bytes': 11913, 'profile': 'data-resource'}], 'profile': 'data-package'}

# print(food_insecurity_dataset.keys())
# AttributeError: 'LocalDataset' object has no attribute 'keys'

trends_df = food_insecurity_dataset.dataframes['trends']
# print(trends_df.head())
# print(trends_df.describe())
# print(trends_df.info())
# print(trends_df.columns) # Index(['year', 'food_insecurity_includes_low_and_very_low_food_security', 'very_low_food_security'], dtype='object')
# print(trends_df.shape) # (30, 3)
# print(trends_df.head(10))
trends_df_numeric = trends_df.iloc[3:]

cols = ['food_insecurity_includes_low_and_very_low_food_security', 'very_low_food_security']

for c in cols:
    trends_df_numeric[c] = trends_df_numeric[c].astype(str).str.replace(r'[,%\s]', '', regex=True).pipe(pd.to_numeric, errors='coerce')

trends_df_numeric['year'] = pd.to_datetime(trends_df_numeric['year'].astype(str).str.strip(), format='%Y', errors='coerce')
trends_df_numeric = trends_df_numeric.set_index('year').sort_index()

# trends_df_numeric[cols].plot()
# plt.ylabel('% of households')
# plt.title('Food Insecurity Trends')
# plt.show()

trends_df_numeric['pct_change'] = (trends_df_numeric[cols[0]] - trends_df_numeric[cols[1]]) / trends_df_numeric[cols[1]] * 100

trends_df_numeric['pct_change'].plot()
plt.ylabel('% change of households')
plt.title('Food Insecurity Trends')
plt.show()