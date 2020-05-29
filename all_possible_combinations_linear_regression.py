import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from itertools import combinations
from clean_data import tennis_data

# Predicting a single feature using all possible combinations from all features available. Just did it for fun (obviously, not practical)!
columns = tennis_data.columns.tolist()[1:] #exclude player column
num_of_columns = len(columns)

for i in range(num_of_columns):
    print('----------------------------------------------------------------')
    print('Predicting: ' + columns[i])
    features_to_choose_from = columns[:i] + columns[i + 1:] # all features but feature that is being predicted
    all_combos = []

    for t in range(1, len(features_to_choose_from) + 1):
        combos = [list(x) for x in combinations(features_to_choose_from, t)]
        all_combos.extend(combos)

    print('Number of Combinations: ', len(all_combos))

    for combo in all_combos:
        features = tennis_data[combo]
        outcomes = tennis_data[[columns[i]]]

        features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size = 0.8)

        scalar = StandardScaler()
        features_train = scalar.fit_transform(features_train)
        features_test = scalar.transform(features_test)

        linear_regressor = LinearRegression()
        linear_regressor.fit(features_train, outcome_train)
        print(linear_regressor.score(features_test, outcome_test))