import os
import pandas as pd
import matplotlib.pyplot as plt
import time

src = 'projects/w3/data/raw/Onyx Data DataDNA Dataset Challenge - Hotel Bookings - July 2023.xlsx'
cache = 'projects/w3/data/processed/hotel_bookings.parquet'

# t0 = time.perf_counter()
# df = pd.read_excel(src, sheet_name=1, engine='openpyxl')
# print(df.head())
# elapsed = time.perf_counter() - t0
# print(f"Time taken: {elapsed:.2f} seconds") 
# Time taken: 29.72 seconds


def load_data():
    # Parquet caching for faster loading
    if not os.path.exists(cache) or os.path.getmtime(cache) < os.path.getmtime(src):
        df = pd.read_excel(src, sheet_name=1, engine='openpyxl')
        df.to_parquet(cache, engine='pyarrow', index=False)
    return pd.read_parquet(cache, engine='pyarrow')

# t0 = time.perf_counter()
# df = load_data()
# print(df.head())
# elapsed = time.perf_counter() - t0
# print(f"Time taken: {elapsed:.2f} seconds")
# 1st run: Time taken: 31.55 seconds
# 2nd run: Time taken: 0.12 seconds

df = load_data()

# Basic EDA--------------------------------

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    # print(df.head())
    # print(df.describe())
# print(df.shape) # (119390, 32)
# print(df.columns)
# print(df.info())
"""
df.head()
          hotel  is_canceled  lead_time  arrival_date_year arrival_date_month  \
0  Resort Hotel            0        342               2015               July   
1  Resort Hotel            0        737               2015               July   
2  Resort Hotel            0          7               2015               July   
3  Resort Hotel            0         13               2015               July   
4  Resort Hotel            0         14               2015               July   

   arrival_date_week_number  arrival_date_day_of_month  \
0                        27                          1   
1                        27                          1   
2                        27                          1   
3                        27                          1   
4                        27                          1   

   stays_in_weekend_nights  stays_in_week_nights  adults  children  babies  \
0                        0                     0       2       0.0       0   
1                        0                     0       2       0.0       0   
2                        0                     1       1       0.0       0   
3                        0                     1       1       0.0       0   
4                        0                     2       2       0.0       0   

  meal country market_segment distribution_channel  is_repeated_guest  \
0   BB     PRT         Direct               Direct                  0   
1   BB     PRT         Direct               Direct                  0   
2   BB     GBR         Direct               Direct                  0   
3   BB     GBR      Corporate            Corporate                  0   
4   BB     GBR      Online TA                TA/TO                  0   

   previous_cancellations  previous_bookings_not_canceled reserved_room_type  \
0                       0                               0                  C   
1                       0                               0                  C   
2                       0                               0                  A   
3                       0                               0                  A   
4                       0                               0                  A   

  assigned_room_type  booking_changes deposit_type  agent  company  \
0                  C                3   No Deposit    NaN      NaN   
1                  C                4   No Deposit    NaN      NaN   
2                  C                0   No Deposit    NaN      NaN   
3                  A                0   No Deposit  304.0      NaN   
4                  A                0   No Deposit  240.0      NaN   

   days_in_waiting_list customer_type   adr  required_car_parking_spaces  \
0                     0     Transient   0.0                            0   
1                     0     Transient   0.0                            0   
2                     0     Transient  75.0                            0   
3                     0     Transient  75.0                            0   
4                     0     Transient  98.0                            0   

   total_of_special_requests reservation_status reservation_status_date  
0                          0          Check-Out              2015-07-01  
1                          0          Check-Out              2015-07-01  
2                          0          Check-Out              2015-07-02  
3                          0          Check-Out              2015-07-02  
4                          1          Check-Out              2015-07-03  
"""

"""
df.describe()
         is_canceled      lead_time  arrival_date_year  \
count  119390.000000  119390.000000      119390.000000   
mean        0.370416     104.011416        2016.156554   
min         0.000000       0.000000        2015.000000   
25%         0.000000      18.000000        2016.000000   
50%         0.000000      69.000000        2016.000000   
75%         1.000000     160.000000        2017.000000   
max         1.000000     737.000000        2017.000000   
std         0.482918     106.863097           0.707476   

       arrival_date_week_number  arrival_date_day_of_month  \
count             119390.000000              119390.000000   
mean                  27.165173                  15.798241   
min                    1.000000                   1.000000   
25%                   16.000000                   8.000000   
50%                   28.000000                  16.000000   
75%                   38.000000                  23.000000   
max                   53.000000                  31.000000   
std                   13.605138                   8.780829   

       stays_in_weekend_nights  stays_in_week_nights         adults  \
count            119390.000000         119390.000000  119390.000000   
mean                  0.927599              2.500302       1.856403   
min                   0.000000              0.000000       0.000000   
25%                   0.000000              1.000000       2.000000   
50%                   1.000000              2.000000       2.000000   
75%                   2.000000              3.000000       2.000000   
max                  19.000000             50.000000      55.000000   
std                   0.998613              1.908286       0.579261   

            children         babies  is_repeated_guest  \
count  119386.000000  119390.000000      119390.000000   
mean        0.103890       0.007949           0.031912   
min         0.000000       0.000000           0.000000   
25%         0.000000       0.000000           0.000000   
50%         0.000000       0.000000           0.000000   
75%         0.000000       0.000000           0.000000   
max        10.000000      10.000000           1.000000   
std         0.398561       0.097436           0.175767   

       previous_cancellations  previous_bookings_not_canceled  \
count           119390.000000                   119390.000000   
mean                 0.087118                        0.137097   
min                  0.000000                        0.000000   
25%                  0.000000                        0.000000   
50%                  0.000000                        0.000000   
75%                  0.000000                        0.000000   
max                 26.000000                       72.000000   
std                  0.844336                        1.497437   

       booking_changes          agent      company  days_in_waiting_list  \
count    119390.000000  103050.000000  6797.000000         119390.000000   
mean          0.221124      86.693382   189.266735              2.321149   
min           0.000000       1.000000     6.000000              0.000000   
25%           0.000000       9.000000    62.000000              0.000000   
50%           0.000000      14.000000   179.000000              0.000000   
75%           0.000000     229.000000   270.000000              0.000000   
max          21.000000     535.000000   543.000000            391.000000   
std           0.652306     110.774548   131.655015             17.594721   

                 adr  required_car_parking_spaces  total_of_special_requests  \
count  119390.000000                119390.000000              119390.000000   
mean      101.831122                     0.062518                   0.571363   
min        -6.380000                     0.000000                   0.000000   
25%        69.290000                     0.000000                   0.000000   
50%        94.575000                     0.000000                   0.000000   
75%       126.000000                     0.000000                   1.000000   
max      5400.000000                     8.000000                   5.000000   
std        50.535790                     0.245291                   0.792798   

             reservation_status_date  
count                         119390  
mean   2016-07-30 00:24:47.883407104  
min              2014-10-17 00:00:00  
25%              2016-02-01 00:00:00  
50%              2016-08-07 00:00:00  
75%              2017-02-08 00:00:00  
max              2017-09-14 00:00:00  
std                              NaN 
"""

"""
df.info()
Index(['hotel', 'is_canceled', 'lead_time', 'arrival_date_year',
       'arrival_date_month', 'arrival_date_week_number',
       'arrival_date_day_of_month', 'stays_in_weekend_nights',
       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal',
       'country', 'market_segment', 'distribution_channel',
       'is_repeated_guest', 'previous_cancellations',
       'previous_bookings_not_canceled', 'reserved_room_type',
       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',
       'company', 'days_in_waiting_list', 'customer_type', 'adr',
       'required_car_parking_spaces', 'total_of_special_requests',
       'reservation_status', 'reservation_status_date'],
      dtype='object')
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119390 entries, 0 to 119389
Data columns (total 32 columns):
 #   Column                          Non-Null Count   Dtype         
---  ------                          --------------   -----         
 0   hotel                           119390 non-null  object        
 1   is_canceled                     119390 non-null  int64         
 2   lead_time                       119390 non-null  int64         
 3   arrival_date_year               119390 non-null  int64         
 4   arrival_date_month              119390 non-null  object        
 5   arrival_date_week_number        119390 non-null  int64         
 6   arrival_date_day_of_month       119390 non-null  int64         
 7   stays_in_weekend_nights         119390 non-null  int64         
 8   stays_in_week_nights            119390 non-null  int64         
 9   adults                          119390 non-null  int64         
 10  children                        119386 non-null  float64       
 11  babies                          119390 non-null  int64         
 12  meal                            119390 non-null  object        
 13  country                         118902 non-null  object        
 14  market_segment                  119390 non-null  object        
 15  distribution_channel            119390 non-null  object        
 16  is_repeated_guest               119390 non-null  int64         
 17  previous_cancellations          119390 non-null  int64         
 18  previous_bookings_not_canceled  119390 non-null  int64         
 19  reserved_room_type              119390 non-null  object        
 20  assigned_room_type              119390 non-null  object        
 21  booking_changes                 119390 non-null  int64         
 22  deposit_type                    119390 non-null  object        
 23  agent                           103050 non-null  float64       
 24  company                         6797 non-null    float64       
 25  days_in_waiting_list            119390 non-null  int64         
 26  customer_type                   119390 non-null  object        
 27  adr                             119390 non-null  float64       
 28  required_car_parking_spaces     119390 non-null  int64         
 29  total_of_special_requests       119390 non-null  int64         
 30  reservation_status              119390 non-null  object        
 31  reservation_status_date         119390 non-null  datetime64[ns]
dtypes: datetime64[ns](1), float64(4), int64(16), object(11)
memory usage: 29.1+ MB
"""
## Data cleaning
df['children'] = df['children'].fillna(0, inplace=True)
df['children'] = df['children'].astype('Int64')
print(df['children'].dtype)

# Distributions--------------------------------
ax = df['market_segment'].value_counts()
ax.plot(kind='bar')
plt.title('Market Segment Distribution')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('projects/w3/output/figures/00_market_segment_distribution.png')
plt.show()