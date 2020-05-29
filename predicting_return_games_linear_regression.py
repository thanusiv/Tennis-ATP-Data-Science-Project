import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from itertools import combinations
from clean_data import tennis_data

columns = tennis_data.columns.tolist()[1:] #exclude player column
num_of_columns = len(columns)

# Predicting percentage of return games won in a year based off the Return Game Columns
return_game_feature_columns = ['FirstServeReturnPointsWon', 'SecondServeReturnPointsWon', 'BreakPointsOpportunities', 'BreakPointsConverted', 'ReturnGamesPlayed', 'ReturnPointsWon']
return_game_target_column = ['ReturnGamesWon']

all_combos = []
features_scores = {}

for t in range(1, len(return_game_feature_columns) + 1):
    combos_of_particular_size = [list(x) for x in combinations(return_game_feature_columns, t)]
    all_combos.extend(combos_of_particular_size)

for combo in all_combos:
    features = tennis_data[combo]
    target = tennis_data[return_game_target_column]

    train_features, test_features, train_target, test_target = train_test_split(features, target, train_size = 0.8)

    scalar = StandardScaler()
    train_features = scalar.fit_transform(train_features)
    test_features = scalar.transform(test_features)

    linear_regressor = LinearRegression()
    linear_regressor.fit(train_features, train_target)

    score = linear_regressor.score(test_features, test_target)
    features_scores[score] = combo

features_scores = {k: v for k, v in sorted(features_scores.items(), key=lambda item: item[0])}

print('Features that predicted the number of return games won by a player in a year')
for score in list(reversed(list(features_scores)))[:10]:
    print('Features: ', features_scores[score], ' Score: ', score)

# Plot predictions vs target of current best set of features (changes based on seed for training and test data)
best_set_of_features = list(features_scores.values())[-1]
features = tennis_data[best_set_of_features]
target = tennis_data[return_game_target_column]

train_features, test_features, train_target, test_target = train_test_split(features, target, train_size = 0.8)

scalar = StandardScaler()
train_features = scalar.fit_transform(train_features)
test_features = scalar.transform(test_features)

linear_regressor = LinearRegression()
linear_regressor.fit(train_features, train_target)
predictions = linear_regressor.predict(test_features)

percentages_nums = [x/10 for x in range(11)]
percentages_strings = [str(x * 100) + '%' for x in percentages_nums]

ax = plt.subplot(1,1,1)
plt.scatter(test_target, predictions, alpha = 0.4)
plt.title('Actual Labels vs Model Predictions for Percentage of Return Games Won')
plt.xlabel('Percentage of Return Games Won (Labels)')
plt.ylabel('Percentage of Return Games Won (Model Predictions)')
ax.set_xticks(percentages_nums)
ax.set_xticklabels(percentages_strings)
ax.set_yticks(percentages_nums)
ax.set_yticklabels(percentages_strings)
plt.show()