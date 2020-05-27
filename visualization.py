import matplotlib.pyplot as plt
from clean_data import tennis_data

percentages_nums = [x/10 for x in range(11)]
percentages_strings = [str(x * 100) + '%' for x in percentages_nums]

plt.figure(figsize=(12,25))
ax = plt.subplot(2,2,1)
ax.set_title('Aces vs Winnings In a Year')
ax.set_xlabel('Aces')
ax.set_ylabel('Winnings')
plt.scatter(tennis_data['Aces'], tennis_data['Winnings'])

ax = plt.subplot(2,2,2)
ax.set_title('First Serves Made vs First Serve Points Won In a Year')
ax.set_xlabel('First Serves')
ax.set_ylabel('First Serve Points')
ax.set_xticks(percentages_nums)
ax.set_xticklabels(percentages_strings)
ax.set_yticks(percentages_nums)
ax.set_yticklabels(percentages_strings)
plt.scatter(tennis_data['FirstServe'], tennis_data['FirstServePointsWon'])

ax = plt.subplot(2,2,3)
ax.set_title('Total Points Won vs Number of Wins In a Year')
ax.set_xlabel('Total Points Won')
ax.set_ylabel('Number of Wins')
ax.set_xticks(percentages_nums)
ax.set_xticklabels(percentages_strings)
plt.scatter(tennis_data['TotalPointsWon'], tennis_data['Wins'])

ax = plt.subplot(2,2,4)
ax.set_title('Doube Faults vs Number of Wins In a Year')
ax.set_xlabel('Number of Double Faults')
ax.set_ylabel('Number of Wins')
plt.scatter(tennis_data['DoubleFaults'], tennis_data['Wins'])

plt.show()