import pandas as pd
wnba = pd.read_csv('wnba.csv')

age_proportion = wnba['Age'].value_counts(normalize=True).sort_index()
print(age_proportion)
age_percentage = (wnba['Age'].value_counts(normalize=True) * 100).sort_index()
print(age_percentage)

proportion_25 = age_proportion.loc[25]
percentage_30 = age_percentage.loc[30]

percentage_over_30 = age_percentage.loc[30:].sum()
percentage_below_23 = age_percentage.loc[:23].sum()
