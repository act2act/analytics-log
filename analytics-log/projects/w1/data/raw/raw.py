import datadotworld as dw
import pandas as pd
import matplotlib.pyplot as plt

data_url = 'https://data.world/cmack624/us-food-insecurity-1995-2019'

food_insecurity_dataset = dw.load_dataset(data_url)

print(food_insecurity_dataset.describe())
# {'name': 'cmack624_us-food-insecurity-1995-2019', 'title': 'U.S. Food Insecurity 1995-2019', 'description': 'Food Security Status of U.S. Households 1995-2019 (source: USDA ERS)', 'homepage': 'https://data.world/cmack624/us-food-insecurity-1995-2019', 'license': 'Public Domain', 'resources': [{'name': 'trends', 'path': 'data/trends.csv', 'format': 'csv', 'profile': 'data-resource'}, {'name': 'original/Food Insecurity - 1995 to 2019.xlsx', 'path': 'original/Food Insecurity - 1995 to 2019.xlsx', 'format': 'xlsx', 'mediatype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'bytes': 11913, 'profile': 'data-resource'}], 'profile': 'data-package'}