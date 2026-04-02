import pandas as pd
import numpy as np
import os
import glob


def process_sort(file, date_col, value_col, new_name,file_name, date_format=None, country_col=None, country_name=None):
    df = pd.read_csv(os.path.join(r"/workspaces/Hackathon-Personal-insight/input", file),
                      encoding='utf-8', encoding_errors='ignore')
    df = df.copy()

    if date_format is not None:
        df[date_col] = pd.to_datetime(df[date_col], format=date_format)
    df[date_col] = df[date_col].dt.floor('D') # 将日期向下取整到天
    df = df.dropna(subset=[date_col])

    if country_col is not None and country_name is not None:
        df = df[df[country_col] == country_name]
    
    df = df[[date_col, value_col]]
    df = df.rename(columns={date_col: 'date', value_col: new_name})
    df = df.sort_values('date')
    

    output_folder = r"/workspaces/Hackathon-Personal-insight/output"
    output_path = os.path.join(output_folder, f"{file_name}.csv")
    df.to_csv(output_path, index=False)
    return df

def convert_text_to_score(df, text_col):
    mapping = {
        "No confidence at all": 0,
        "Not very much confidence": 1,
        "A fair amount of confidence": 2,
        "A lot of confidence": 3,
        "Don't know": np.nan
    }
    df['trust_num'] = df[text_col].map(mapping)
    df = df.dropna(subset=['trust_num'])
    mean = df['trust_num'].mean()
    std = df['trust_num'].std()

    df['Trust_Score'] = (df['trust_num'] - mean) / std
    df_daily = df.groupby('date')['Trust_Score'].mean().reset_index()
    df_daily.to_csv("output/Trust_converted.csv", index=False)

    return df_daily

def merge_datasets(file_list):
    """
    file_list: [(file_path, value_column_name), ...]
    output_path: 输出csv路径
    """

    dfs = []

    for file, value_name in file_list:
        df = file.copy()

        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        df = df[['date', value_name]]

        dfs.append(df)

    processed_data = dfs[0]
    for df in dfs[1:]:
        processed_data = processed_data.merge(df, on='date', how='inner')
    processed_data = processed_data.sort_values('date')

    output_path = r"/workspaces/Hackathon-Personal-insight/output/processed_data.csv"
    processed_data.to_csv(output_path, index=False)
    return processed_data
