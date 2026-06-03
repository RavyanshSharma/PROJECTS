import pandas as pd

movies= pd.read_csv(r"movies.csv")

#print(movies.head())
#print(movies.shape)
#print(movies.describe())
#print(movies.info())

movies.isnull().sum()             
movies.dropna(subset=['rating'])    
movies.drop_duplicates()         
movies['genre'] = movies['genre'].str.strip().str.title() 


top10 = movies.sort_values('rating', ascending=False).head(10)

action = movies[(movies['genre'] == 'Action') & (movies['rating'] > 7.5)]

most_voted = movies.sort_values('votes', ascending=False).head(5)

genre_summary = movies.groupby('genre').agg(
    avg_rating = ('rating', 'mean'),
    total_votes = ('votes', 'sum'),
    movie_count = ('title', 'count')
).sort_values('avg_rating', ascending=False).round(2)

print(genre_summary)
