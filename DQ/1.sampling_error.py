import pandas as pd
wnba = pd.read_csv('wnba.csv')

# Explore the dataset
print(wnba.head())
print(wnba.tail())
print(wnba.shape)

# Find maximum number of games played (parameter) for all player in 2016-2017 season
parameter = wnba['Games Played'].max()
print(parameter)

# Find maximum number of games (static) by random sampling 30 players
# Set argument random_state = 1 to make results reproducible
sample = wnba.sample(30, replace=False, weights=None, random_state=1)
statistic = sample['Games Played'].max()
print(statistic)

#Calculate sampling error
sampling_error = parameter - statistic
print(sampling_error)
