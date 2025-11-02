import pandas as pd

def extract(path='C:/Users/black/PycharmProjects/etl-processing-engine/data/Coffee_sales/sales.csv'):
    return pd.read_csv(path)