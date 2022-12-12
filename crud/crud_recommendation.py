
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm 


def f_recommend(book_id, n_rec, owner_id):
    df = pd.read_csv(r'd:\naomy\LIA-FastAPI-MySQL\data\data.csv')
    df_copy = df.copy()
    df.rename(columns={'id':'book_id'},inplace=True)
    df['pages_norm'] = normalize(df['pages'].values)
    df['book_rating_norm'] = normalize(df['classification'].values)
    df = ohe(df = df, enc_col = 'genre')
    df = ohe(df = df, enc_col = 'author')
    cols = ['pages', 'genre', 'description', 'title', 'author']
    df.drop(columns = cols, inplace = True)
    df.set_index('book_id', inplace = True)

    df_recommendations = recommend(df.index[book_id], n_rec, owner_id, df)
    df_seila= df_copy.loc[df_copy['id'].isin(df_recommendations.index.values), ['title']]
    return df_seila

def normalize(data):
    '''
    Normalize input data to be between 0 and 1
    
    params:
        data: values you want to normalize
    
    returns:
        The input data normalized between 0 and 1
    '''
    min_val = min(data)
    if min_val < 0:
        data = [x + abs(min_val) for x in data]
    max_val = max(data)
    return [x/max_val for x in data]

def ohe(df, enc_col):
    '''
    This function will one hot encode the specified column and add it back
    onto the input dataframe
    
    params:
        df (DataFrame) : The dataframe you wish for the results to be appended to
        enc_col (String) : The column you want to OHE
    
    returns:
        The OHE columns added onto the input dataframe
    '''
    
    ohe_df = pd.get_dummies(df[enc_col])
    ohe_df.reset_index(drop = True, inplace = True)
    return pd.concat([df, ohe_df], axis = 1)

def cosine_sim(v1,v2):
    '''
    This function will calculate the cosine similarity between two vectors
    '''
    return dot(v1,v2)/(norm(v1)*norm(v2))

def recommend(book_id, n_rec, owner_id, df):
    """
    df (dataframe): The dataframe
    song_id (string): Representing the song name
    n_rec (int): amount of rec user wants
    """

    
    # calculate similarity of input book_id vector and all other vectors
    inputVec = df.loc[book_id].values
    df['sim']= df.apply(lambda x: cosine_sim(inputVec,x.values), axis=1)
    
    df_rec = df.nlargest(columns='sim',n=n_rec)
    df_final = df_rec.loc[df['owner_id'] != owner_id]
    # returns top n user specified books that the user didnt listed already
    return df_final