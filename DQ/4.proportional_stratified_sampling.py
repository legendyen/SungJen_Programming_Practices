import pandas as pd
import matplotlib.pyplot as plt
wnba = pd.read_csv('WNBA Stats.csv')

# print(wnba.shape)
# print(wnba['Games Played'].value_counts().sort_index())
print(wnba['Games Played'].value_counts(bins=3))
print(wnba['Games Played'].value_counts(bins=3, normalize=True))

pts = []
for i in range(100):
    stratum_1 = wnba[wnba['Games Played'] <= 12].sample(1, random_state=i)
    stratum_2 = wnba[(wnba['Games Played'] > 12) & (wnba['Games Played'] <= 22)].sample(2, random_state=i)
    stratum_3 = wnba[wnba['Games Played'] > 22].sample(7, random_state=i)
    sample = pd.concat([stratum_1, stratum_2, stratum_3])
    sample_mean = sample['PTS'].mean()
    pts.append(sample_mean)

plt.scatter(range(1, 101), pts)
plt.axhline(wnba['PTS'].mean())
plt.yticks(ticks=list(range(100, 400, 50)))
plt.show()
