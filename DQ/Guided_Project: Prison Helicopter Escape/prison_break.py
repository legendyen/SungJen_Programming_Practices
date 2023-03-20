#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# "We begin by importing some helper functions"

# In[42]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[43]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# Let's print the first three rows

# In[44]:


for row in data[:3][:-1]:
    print(row)


# ## Removing the Details

# We initialize an index variable with the value of 0. The purpose of this variable is to help us track which row we're modifying.

# In[45]:


index= 0
for row in data:
    data[index] = row[:-1]
    index += 1


# In[46]:


print(data[:3])


# ## Extracting the Year

# In the code cell below, we iterate over data using the iterable variable row and: * With every occurrence of row[0], we refer to the first entry of row, i.e., the date. * Thus, with date = fetch_year(row[0]), we're extracting the year out of the date in row[0] and assiging it to the variable date. * We then replace the value of row[0] with the year that we just extracted.

# In[50]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[51]:


print(data[:3])


# ## Attempts per Year

# In[53]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# Before we move on, let's check what are the earliest and latest dates we have in our dataset.

# In[56]:


print(min_year)
print(max_year)


# Now we'll create a list of all the years ranging from min_year to max_year. Our goal is to then determine how many prison break attempts there were for each year. Since years in which there weren't any prison breaks aren't present in the dataset, this will make sure we capture them.

# In[57]:


years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# Let's take a look at years to see if it looks like we expected.

# In[58]:


print(years)


# Now we create a list where each element looks like [<'year>, 0].

# In[67]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# In[68]:


print(attempts_per_year)


# And finally we increment the second entry (the one on index 1 which starts out as being 0) by 1 each time a year appears in the data.

# In[69]:


for row in data:
    for year_attempt in attempts_per_year:
        if row[0] == year_attempt[0]:
            year_attempt[1] += 1

print(attempts_per_year)


# In[70]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# The years in which the most helicopter prison break attempts occurred were 1986, 2001, 2007 and 2009, with a total of three attempts each.

# ## Attempts by Country

# In[76]:


countries_frequency = df["Country"].value_counts()
# print(countries_frequency)
print_pretty_table(countries_frequency)


# In[ ]:




