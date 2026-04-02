import pandas as pd
import os
import statsmodels.api as sm
def construction_gap(file):
    df = pd.read_csv(os.path.join(r"/workspaces/Hackathon-Personal-insight/output", file),
                      encoding='utf-8', encoding_errors='ignore')
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.set_index('date', inplace=True)
    df['Stringency_z'] = (df['Stringency_Raw'] - df['Stringency_Raw'].mean()) / df['Stringency_Raw'].std()
    # Calculate the gap between Stringency_z and Trust_Score
    df['Gap_signed'] = df['Stringency_z'] - df['Trust_Score']
    df['Gap_abs'] = df['Gap_signed'].abs()

    return df[['Gap_signed', 'Gap_abs']]

def gap_var(file,lags=25):
    df = pd.read_csv(os.path.join(r"/workspaces/Hackathon-Personal-insight/output", file),
                      encoding='utf-8', encoding_errors='ignore')
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df.set_index('date', inplace=True)
    df['Stringency_z'] = (df['Stringency_Raw'] - df['Stringency_Raw'].mean()) / df['Stringency_Raw'].std()
    df['Stringency_lag' + str(lags)] = df['Stringency_z'].shift(lags)
    return df[['Stringency_lag' + str(lags), 'Trust_Score', 'Stringency_z']]


def build_reg_df(file, gap_df,stringency_lag=25, trust_lag=1, cases_lag=7, death_lag=7, policy_change_lag=25):
    df = pd.read_csv(os.path.join(r"/workspaces/Hackathon-Personal-insight/output", file))
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df = df.set_index('date')
    
    df['Stringency_z'] = (df['Stringency_Raw'] - df['Stringency_Raw'].mean()) / df['Stringency_Raw'].std()
    df['Newcase_z'] = (df['Newcase_Raw'] - df['Newcase_Raw'].mean()) / df['Newcase_Raw'].std()
    df['Death_z'] = (df['Death_Raw'] - df['Death_Raw'].mean()) / df['Death_Raw'].std()

    # lag / change
    df['Stringency_lag'] = df['Stringency_z'].shift(stringency_lag)
    df['Trust_lag'] = df['Trust_Score'].shift(trust_lag)
    df['Cases_lag'] = df['Newcase_z'].shift(cases_lag)
    df['Death_lag'] = df['Death_z'].shift(death_lag)

    df['Policy_change'] = df['Stringency_z'] - df['Stringency_z'].shift(policy_change_lag)
    
    reg_df = df.join(gap_df[['Gap_signed', 'Gap_abs']], how='left')
    
    reg_df = reg_df[[
        'Trust_Score',
        'Stringency_z',
        'Newcase_z',
        'Death_z',
        'Stringency_lag',
        'Trust_lag',
        'Cases_lag',
        'Death_lag',
        'Policy_change',
        'Gap_signed',
        'Gap_abs'
    ]]
    reg_df = reg_df.dropna()
    reg_df.to_csv(os.path.join(r"/workspaces/Hackathon-Personal-insight/output", "regression_data.csv"))
    return reg_df

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate(y_true, y_pred, name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    
    print(f"{name} RMSE:", rmse)
    print(f"{name} R2:", r2)
    print("------")
