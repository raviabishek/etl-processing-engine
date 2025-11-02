import pandas as pd

def transform(df):
    '''
    It will output quantity greater than 1
    :param df: dataframe (raw data)
    :return: dataframe quantity greater than 1
    '''
    transform_df = df[df['quantity'] > 2]
    return transform_df