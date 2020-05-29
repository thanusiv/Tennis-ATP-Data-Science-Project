import pandas as pd
import matplotlib.pyplot as plt

# Almost all data is already cleaned where each variable is a separate column and each observation is a separate row

tennis_data = pd.read_csv(r'C:\Users\thanu\OneDrive\Documents\DataScienceProjects\TennisATPDataProject\tennis_stats.csv') # replace this with where you placed the csv file
#print(tennis_data.head())
#print(tennis_data.info())
#print(tennis_data.describe())
#print(tennis_data.columns)

duplicates = tennis_data[tennis_data.duplicated()]  # 2 duplicate rows
#print(duplicates)
tennis_data.drop_duplicates(inplace = True)

#print(tennis_data.isnull().sum()) # no null values in any column