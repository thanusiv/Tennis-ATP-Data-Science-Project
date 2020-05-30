# Tennis ATP Data Project

## Overview

This project uses the tennis player dataset provided by the Association of Tennis Professionals (ATP) to predict specific game statistics of a player based on their career's statistics from previous years. In this project, I used linear and multiple linear regression to predict the number of return and service games won by a player based on their respective service and return game statistics. I also used a Random Forest to try to predict a specific player based on all their statistics from a particular year and showcase why it did not work the way it was intended.

## Explanation of Dataset

The following information describes each column in the `tennis_stats.csv` file.

### Identifying Data

- `Player` : name of the tennis player
- `Year` : year the statistics for the player were collected

### Service Game Statistics

- `Aces` : number of serves by the player where the receiver does not touch the ball
- `DoubleFaults` : number of times player missed both first and second serve attempts
- `FirstServe` : % of first serve attempts made
- `FirstServePointsWon` : % of first-serve points won by the player
- `SecondServePointsWon` : % of second-serve points won by the player
- `BreakPointsFaced` : number of times where the receiver could have won service game of the player
- `BreakPointsSaved` : % of the time the player was able to stop the receiver from winning service game when they had the chance
- `ServiceGamesPlayed` : total number of games where the player served
- `ServiceGamesWon` : percentage of games where the player served and won
- `TotalServicePointsWon` : % of points in games where the player served that they won

### Return Game Statistics

- `FirstServeReturnPointsWon` : % of opponents first-serve points the player was able to win
- `SecondServeReturnPointsWon` : % of opponents second-serve points the player was able to win
- `BreakPointsOpportunities` : number of times where the player could have won the service game of the opponent
- `BreakPointsConverted` : % of the time the player was able to win their opponent’s service game when they had the chance
- `ReturnGamesPlayed` : total number of games where the player’s opponent served
- `ReturnGamesWon` : total number of games where the player’s opponent served and the player won
- `ReturnPointsWon` : total number of points where the player’s opponent served and the player won

### Outcome Statistics

- `TotalPointsWon` : % of points won by the player
- `Wins` : number of matches won in a year
- `Losses` : number of matches lost in a year
- `Winnings` : total winnings in USD($) in a year
- `Ranking` : ranking at the end of year

## Files

The `tennis_stats.csv` is the CSV file that holds the dataset.

The `clean_data.py` file is used for exploratory analysis. The dataset was already more or less cleaned since each variable is a separate column and each observation is a separate row. The types for each column are appropriate as well.

The `visualization.py` file was used to graph columns against each other and see if there are any correlations between game statistics.

The `predicting_return_games_linear_regression.py` and `predicting_service_games_linear_regression.py` files use linear and multiple linear regression to predict the number of return and service games won by a player. They print put the top 10 set of features that provided the highest accuracy for the test dataset. A graph has also been made for the top performing model's predictions against the test label.

The `random_forest.py` was an attempt to predict a specific player based off their game statistics but has performed quite poorly. This makes sense since the data for a particular player is quite limited and more data is required to even have a reasonable model.

## Technologies Used

- [Python](https://www.python.org/) : Programming language used
- [Pandas](https://pandas.pydata.org/) : Data analysis and manipulation library
- [Matplotlib](https://matplotlib.org/) : Plotting/graphing library
- [Scikit-learn](https://scikit-learn.org/stable/) : Machine learning library

## Acknowledgements

- Thanks to the [Association of Tennis Professionals (ATP)](https://www.atptour.com/) for providing the dataset
- Thanks to [Codecademy Pro](https://www.codecademy.com/catalog/subject/all) for providing the initial guidlines for the project
