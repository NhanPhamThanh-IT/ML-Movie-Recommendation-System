# %% [markdown]
# ### __Importing the dependencies__

# %%
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# %% [markdown]
# ### __Data Collection__

# %%
# Loading the dataset
movies_data = pd.read_csv('./data/movies.csv')

# %%
# Printing the first 5 rows of the dataframe
movies_data.head(5)

# %%
# Number of rows and columns in the dataframe
movies_data.shape

# %% [markdown]
# ### __Data Preprocessing__

# %%
# Selecting the relevant features, which will be used for content-based filtering
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# %%
# Replacing the null values with null string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# %%
# Combining all the 5 selected features
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# %%
print(combined_features)

# %%
# Converting the text data to future vectors
vectorizer = TfidfVectorizer()

# %%
# Creating the feature vectors
feature_vectors = vectorizer.fit_transform(combined_features)

# %%
# Printing the feature vectors
print(feature_vectors)

# %% [markdown]
# ### __Cosine Similarity__

# %%
# Getting the similarity scores using cosine similarity
similarity = cosine_similarity(feature_vectors)

# %%
# Printing the similarity scores
print(similarity)

# %%
# Printing the shape of the similarity matrix
print(similarity.shape)

# %% [markdown]
# ### __Getting the movie name from the user__

# %%
# Creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()

# %%
# Printing the list of all movie titles
print(list_of_all_titles)

# %%
# Getting the movie name from the user
movie_name = input('Enter your favourite movie name: ')

# %%
# Finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

# %%
# Printing the list of all close matches
print(find_close_match)

# %%
# Finding the most close match for the movie name given by the user
close_match = find_close_match[0]

# %%
# Printing the most close match
print(close_match)

# %%
# Finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# %%
# Printing the index of the movie with title
print(index_of_the_movie)

# %%
# Getting a list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# %%
# Printing the similarity score
print(similarity_score)

# %%
# Printing the number of similar movies
print(len(similarity_score))

# %%
# Sorting the movies based on their similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

# %%
# Printing the most similar movies
print(sorted_similar_movies)

# %%
# Printing the name of similar movies based on the index
print('Movies suggested for you\n')

for i, movie in enumerate(sorted_similar_movies):
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i+1, '.',title_from_index)

# %% [markdown]
# ### __Movie Recommendation System__

# %%
# User input for movie name
movie_name = input('Enter your favourite movie name: ')

# %%
list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

# %%
print('Movies suggested for you\n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1


