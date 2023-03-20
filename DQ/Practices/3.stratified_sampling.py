import pandas as pd
import matplotlib.pyplot as plt
wnba = pd.read_csv('WNBA Stats.csv')

pos = wnba['Pos'].unique()
wnba['PPG'] = wnba['PTS'] / wnba['Games Played']

#Group players by position to stratify later
stratum = wnba.groupby('Pos')

#Store mean along with its corresponding position
dic = {}
for p in pos:
    sampling = stratum.get_group(p).sample(10, random_state=0)
    sample_mean = sampling['PPG'].mean()
    dic[p] = sample_mean

print(dic)

#Loop through dictionary to find position that scores highest number
lst = []
for k, v in dic.items():
    lst.append((v, k))
    lst.sort(reverse=True)

for v, k in lst[:1]:
    position_most_points = (k, v)

print(position_most_points)
