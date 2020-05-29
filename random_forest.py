import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from clean_data import tennis_data

# Predicting player based off several columns from the dataset. Model performs quite poor using a random forest. Need to tweak the feature column set more and determine specific 
# correlations between players to get a more accurate model

feature_columns = ['Aces', 'DoubleFaults', 'FirstServe', 'BreakPointsSaved', 'TotalServicePointsWon', 'Wins', 'Losses', 'Ranking', 'Year' ,'Winnings']
target_column = ['Player']

features = tennis_data[feature_columns]
target = tennis_data[target_column[0]]
train_features, test_features, train_target, test_target = train_test_split(features, target, train_size = 0.8)

classifier = RandomForestClassifier(n_estimators= 200)
classifier.fit(train_features, train_target)
print(classifier.score(test_features, test_target))