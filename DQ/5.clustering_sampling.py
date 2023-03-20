import pandas as pd
import matplotlib.pyplot as plt
wnba = pd.read_csv('WNBA Stats.csv')

# print(wnba.shape)
# print(wnba['MIN'].value_counts().sort_index())
print(wnba['MIN'].value_counts(bins=3))
print(wnba['MIN'].value_counts(bins=3, normalize=True))

pts = []
for i in range(100):
    stratum_1 = wnba[wnba['MIN'] <= 340].sample(4, random_state=i)
    stratum_2 = wnba[(wnba['MIN'] > 340) & (wnba['MIN'] <= 680)].sample(4, random_state=i)
    stratum_3 = wnba[wnba['MIN'] > 680].sample(4, random_state=i)
    sample = pd.concat([stratum_1, stratum_2, stratum_3])
    sample_mean = sample['PTS'].mean()
    pts.append(sample_mean)

plt.scatter(range(1, 101), pts)
plt.axhline(wnba['PTS'].mean())
plt.yticks(ticks=list(range(100, 400, 50)))
plt.show()
