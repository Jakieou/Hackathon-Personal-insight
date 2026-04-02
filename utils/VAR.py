import pandas as pd
from statsmodels.tsa.stattools import adfuller
import os

def ADF_test(df):
    df = pd.read_csv(os.path.join("output", df + ".csv"))
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df.set_index('date')
    for col in df.columns:
        pvalue = adfuller(df[col].dropna())[1]
        print(col, "p-value:", pvalue)

def diff_data(df, columns, file_name):
    df = pd.read_csv(os.path.join("output", df + ".csv"))
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df.set_index('date')

    df_new = df.copy()
    df_new[columns] = df_new[columns].diff()
    df_new = df_new.dropna()
    df_new.columns = [col.replace("_Raw", "_Diff") for col in df_new.columns]
    df_new.to_csv(os.path.join("output", file_name + ".csv"))
    return df_new