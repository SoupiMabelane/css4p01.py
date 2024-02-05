# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:44:49 2024

@author: mabel
"""

import pandas as pd  # this line imports the python library, pandas. 

df = pd.read_csv("movie_dataset.csv", index_col=['Rank']) #this line drops the index column
print(df)

                      
# 1. The highest rated movie in the dataset
print(df["Title"][df['Rating'] == df['Rating'].max()])

# 2. Average revenue of all movies in the dataset
x = df["Revenue (Millions)"].mean() 
print(x)

# 3. Average revenue of movies from 2015 to 2017
yr = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
print(yr["Revenue (Millions)"].mean())

# 4. Number of movies released in the year 2016
print(len(df[(df['Year'] == 2016)]))

# 5. Movies directed by Christopher Nolan
print(len(df[(df['Director']== "Christopher Nolan")]))
 

# 6. Movies in the dataset with a rating of atleast 8.0
print(len(df["Title"][df['Rating'] >= 8.0]))

# 7. Median rating of movies directed by Christopher Nolan
print(df['Rating'][(df['Director']== "Christopher Nolan")].median())


#Correlation

Correlation = df.corr()
print(Correlation)

# 8. Year with the highest average rating
ar = df.groupby(['Year']).mean()
Max = ar['Rating'].max()
print(ar.idxmax())

# 9. The percentage increase in number of movies made between 2006 and 2016
Len_2016 = len(df[(df['Year'] == 2016)])
Len_2006 = len(df[(df['Year'] == 2006)]) 
print('2006 to 2016 percetage increase', ((Len_2016-Len_2006)/Len_2006)*100)

# 10. Most common actor in all the movies
actors = df['Actors']
list_actors = []
for i in actors:
    subs = i.split(',')
    list_actors.append(subs)
print(list_actors)
df = pd.DataFrame(list_actors)
print(df.stack().value_counts())



# 11. Number of genres in the dataset
genre = df['Genre']
list_genre = []
for n in genre:
    subs = n.split(',')
    list_genre.append(subs)
print(list_genre)
print(len(list_genre.append(subs)))


