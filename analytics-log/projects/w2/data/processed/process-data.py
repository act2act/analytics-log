import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

raw_data_path = "projects/w2/data/raw/Onyx Data -DataDNA Dataset Challenge - Udemy Courses - January 2024.xlsx"

# Read the actual data sheet (second sheet) not the data dictionary
excel_data = pd.read_excel(raw_data_path, sheet_name=1, engine="openpyxl")
df = pd.DataFrame(excel_data)

# Basic EDA
## Summary statistics

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(df.head())
#     print(df.describe())

# print(df.shape) # (3678, 12)
# print(df.columns) # ['course_id', 'course_title', 'url', 'is_paid', 'price', 'num_subscribers', 'num_reviews', 'num_lectures', 'level', 'content_duration', 'published_timestamp', 'subject']
# print(df.info()) # int64 = ['course_id', 'num_subscribers', 'num_reviews', 'num_lectures'], float64 = ['content_duration'], object = ['course_title', 'url', 'level', 'published_timestamp', 'subject'], bool = ['is_paid']

"""
   course_id                                       course_title  \
0    1070968                 Ultimate Investment Banking Course   
1    1113822  Complete GST Course & Certification - Grow You...   
2    1006314  Financial Modeling for Business Analysts and C...   
3    1210588  Beginner to Pro - Financial Analysis in Excel ...   
4    1011058       How To Maximize Your Profits Trading Options   

                                                 url  is_paid  price  \
0  https://www.udemy.com/ultimate-investment-bank...     True    200   
1      https://www.udemy.com/goods-and-services-tax/     True     75   
2  https://www.udemy.com/financial-modeling-for-b...     True     45   
3  https://www.udemy.com/complete-excel-finance-c...     True     95   
4  https://www.udemy.com/how-to-maximize-your-pro...     True    200   

   num_subscribers  num_reviews  num_lectures               level  \
0             2147           23            51          All Levels   
1             2792          923           274          All Levels   
2             2174           74            51  Intermediate Level   
3             2451           11            36          All Levels   
4             1276           45            26  Intermediate Level   

   content_duration   published_timestamp           subject  
0               1.5  2017-01-18T20:58:58Z  Business Finance  
1              39.0  2017-03-09T16:34:20Z  Business Finance  
2               2.5  2016-12-19T19:26:30Z  Business Finance  
3               3.0  2017-05-30T20:07:24Z  Business Finance  
4               2.0  2016-12-13T14:57:18Z  Business Finance  

              price  num_subscribers   num_reviews  num_lectures
count   3678.000000      3678.000000   3678.000000   3678.000000   
mean      66.049483      3197.150625    156.259108     40.108755   
std       61.005755      9504.117010    935.452044     50.383346   
min        0.000000         0.000000      0.000000      0.000000   
25%       20.000000       111.000000      4.000000     15.000000   
50%       45.000000       911.500000     18.000000     25.000000   
75%       95.000000      2546.000000     67.000000     45.750000   
max      200.000000    268923.000000  27445.000000    779.000000   

       content_duration  
count       3678.000000  
mean           4.094517  
std            6.053840  
min            0.000000  
25%            1.000000  
50%            2.000000  
75%            4.500000  
max           78.500000  
"""

## Distributions
num_cols = ['price', 'num_subscribers', 'num_reviews', 'num_lectures', 'content_duration']
# for col in num_cols:
#     # df[col].plot(kind='hist', bins=20)
#     sns.histplot(df[col], bins=20)
#     plt.title(f'{col} Distribution')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.show()

## Categorical splits
categorical_cols = ['is_paid', 'level', 'subject']
# for col in categorical_cols:
#     # df[col].value_counts().plot(kind='bar')
#     ax = sns.countplot(x=col, data=df)
#     ax.grid(axis='y', linestyle='--', alpha=0.5)
#     ax.set_axisbelow(True)
#     plt.title(f'{col} Distribution')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.xticks(rotation=45)
#     plt.show()

## Time series
df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
df['published_year'] = df['published_timestamp'].dt.year
# counts = df.groupby('published_year').size()
# ax = counts.plot(kind='bar')
# ax.grid(axis='y', linestyle='--', alpha=0.5)
# ax.set_axisbelow(True)
# plt.title('Number of courses published per year')
# plt.ylabel('Number of courses')
# plt.xticks(rotation=45)
# plt.show()

# q = df.groupby('published_year')[num_cols].quantile([0.25, 0.5, 0.75]).unstack()
# for col in num_cols:
#     # df.groupby('published_year')[col].mean().plot(kind='line')
#     # ax = df.groupby('published_year')[col].median().plot(kind='line')
#     # ax.grid(axis='y', linestyle='--', alpha=0.5)
#     # ax.set_axisbelow(True)
#     # plt.title(f'{col} over time')
#     q[col][0.5].plot(label='median')
#     plt.fill_between(q.index, q[col][0.25], q[col][0.75], alpha=0.2, label='IQR')
#     plt.title(f'{col} over time (median with IQR)')
#     plt.legend()
#     plt.show()

# Diagnostic/correlation analysis
## Correlation
# print(df[num_cols].corr())

"""
                     price  num_subscribers  num_reviews  num_lectures  content_duration
price             1.000000         0.050769     0.113696      0.330160          0.293450
num_subscribers   0.050769         1.000000     0.649946      0.157746          0.161839
num_reviews       0.113696         0.649946     1.000000      0.243029          0.228889
num_lectures      0.330160         0.157746     0.243029      1.000000          0.801647
content_duration  0.293450         0.161839     0.228889      0.801647          1.000000
"""

## Log-scale relationships for heavy-tailed variables
skewed_cols = num_cols[1:]
# for col in skewed_cols:
#     df[col] = np.log(df[col])
#     sns.histplot(df[col], bins=20)
#     plt.title(f'{col} Distribution')
#     plt.xlabel(col)
#     plt.ylabel('Frequency')
#     plt.show()

# Visualizations
## Scatter plot
# sns.scatterplot(x='price', y='num_subscribers', data=df, hue='level', size='num_reviews')
# plt.title('Price vs Number of Subscribers')
# plt.xlabel('Price')
# plt.ylabel('Number of Subscribers')
# plt.show()

## Heatmap
# sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation between numeric columns')
# plt.xticks(rotation=45)
# plt.show()

## Boxplot
# sns.boxplot(x='level', y='price', data=df)
# plt.title('Price vs Level')
# plt.xlabel('Level')
# plt.ylabel('Price')
# plt.show()

## Time series
# df['published_month'] = df['published_timestamp'].dt.month
# sns.lineplot(x='published_month', y=df.groupby('published_month')['price'].median(), data=df)
# plt.title('Median Price per Month')
# plt.ylabel('Price')
# plt.savefig('projects/w2/output/figures/median_price_per_month.png')
# plt.show()