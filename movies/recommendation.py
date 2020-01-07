import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('movies/movie_dataset.csv', low_memory=False)
features = ['keywords', 'cast', 'genres', 'director']

def combine_features(row):
    return str(row['keywords'])+" "+str(row['cast'])+" "+str(row["genres"])+" "+str(row["director"])

for feature in features:
    df[feature] = df[feature].fillna('') #fill nan with blank string
    df['combined_features'] = df.apply(combine_features, axis=1) #applying combined_features() on every and store the result on combined_features column


def get_title_from_index(index):
    return df[df.index == index]['title'].values[0]

def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]

def get_similar_movies(movie_title):
    cv = CountVectorizer() #creating new CountVectrizer op
    count_matrix = cv.fit_transform(df["combined_features"]) #feeding the combined features to the cv op
    cos_sim = cosine_similarity(count_matrix)
    movie_user_likes = movie_title
    sim_movies = []
    movie_index = get_index_from_title(movie_user_likes)

    similar_movies = list(enumerate(cos_sim[int(movie_index)])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
    sorted_sim_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:]

    i=0
    for element in sorted_sim_movies:
        sim_movies.append(get_title_from_index(element[0]))
        i=i+1
        if i>5:
            break
    
    return sim_movies
    