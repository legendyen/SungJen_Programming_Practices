import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

#As we increase the sample size, the sample means vary less around the population mean,
#and the chances of getting an unrepresentative sample decrease.
#The more representative a sample is, the smaller the sampling error.
sample_means = []
for i in range(100):
    sample = wnba['PTS'].sample(100, random_state=i)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)

parameter = wnba['PTS'].mean()

# We can see how sample means tend to vary less around the population mean as we increase the sample size.
plt.scatter(range(1, 101), sample_means)
plt.axhline(parameter, label='Parameter mean')
plt.yticks(ticks=list(range(125, 325, 25)))
plt.legend()
plt.show()

# Conclusions:
# Simple random sampling isn't a reliable sampling method when the sample size is small.
# When we do simple random sampling, we should try to get a sample that is as large as possible.
