
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm 
from fastapi import HTTPException, status


def f_recommend(book_id, owner_id):
    '''
    Gets the csv file, converts to pandas dataframe, normalizes and one hot encodes columns, 
    adjusts dataframe to recommend books using cosine similarity as metric, then returns dict of the books recommended
    '''
    df = pd.read_csv(r'd:\naomy\LIA-FastAPI-MySQL\data\data.csv')
    df_copy = df.copy()
    df.rename(columns={'id':'book_id'},inplace=True)
    df['pages_norm'] = normalize(df['pages'].values)
    df['book_rating_norm'] = normalize(df['classification'].values)
    df = ohe(df = df, enc_col = 'genre')
    df = ohe(df = df, enc_col = 'author')
    cols = ['pages', 'genre', 'description', 'title', 'author','classification']
    df.drop(columns = cols, inplace = True)
    df.set_index('book_id', inplace = True)

    df_recommendations = recommend(df.index[book_id], owner_id, df)
    df_seila= df_copy.loc[df_copy['id'].isin(df_recommendations.index.values), ['title']]#returns dataframe with the titles associated to the book ids
    df_seila.drop_duplicates(inplace=True)
    list_books = df_seila.to_dict(orient='list')
    return list_books
    
def normalize(data):
    '''
    Gets dataframe and normalizes input data to be between 0 and 1
    '''
    min_val = min(data)
    if min_val < 0:
        data = [x + abs(min_val) for x in data]
    max_val = max(data)
    return [x/max_val for x in data]

def ohe(df, enc_col):
    '''
    One hot encodes specified columns and adds them back
    onto the input dataframe
    '''
    
    ohe_df = pd.get_dummies(df[enc_col])
    ohe_df.reset_index(drop = True, inplace = True)
    return pd.concat([df, ohe_df], axis = 1)

def cosine_sim(v1,v2):
    '''
    Calculates the cosine similarity between two vectors
    '''
    return dot(v1,v2)/(norm(v1)*norm(v2))

def recommend(book_id, owner_id, df):
    """
    Content based recommendations.
    Calls the cosine similarity function to calculate similarities and returns the
    most similar books, excluding the ones listed by the user
    """
    book_id = book_id - 1 #because it starts from zero, while the ids in the database start from 1
    # calculate similarity of input book_id vector and all other vectors
    inputVec = df.loc[book_id].values
    df['sim']= df.apply(lambda x: cosine_sim(inputVec,x.values), axis=1)
    
    df_rec = df.nlargest(10, columns='sim')
    df_final = df_rec.loc[df['owner_id'] != owner_id]#excludes books already listed by the user
    # returns top 10 similar books that the user didnt list already
    return df_final