import pandas as pd
import numpy as np

# Read the csv-file as strings, set day-column to be numbers
def read_tabular(path):
  df = pd.read_csv(path, dtype=object)
  df['Day'] = pd.to_numeric(df['Day'])
  return df

# Compare guessed results to real results with a two-place function of choice
def apply_function_on_results(_df, f):
  df = _df.copy()
  for i in range(0,len(df)):
    for x in df.columns[2:]:
      df.at[i,x] = f(df.iloc[i][x], df.iloc[i]['Result'])
  df = df.drop('Result',axis=1)
  return df

# Aggregate the results on a day-by-day basis
def group_by_day(_df, aggr='mean'):
  df = _df.copy()
  if aggr == 'mean':
    df = df.groupby(['Day']).mean()
  elif aggr == 'sum':
    df = df.groupby(['Day']).sum()
  else:
    raise ValueError("Choose either 'sum' or 'mean' as aggregate!")
  df.loc[0] = 0
  df.sort_index(inplace=True)
  return df

def cumulative_sum(df):
  return cumulative(df, pd.Series(np.ones(len(df)), copy=False))

def cumulative_ratio(df):
  return cumulative(df, pd.Series(np.array(list(range(1,len(df)+1))), copy=False))

# Compute the cumulative value for each index in a column
def cumulative(_df, seq):
  df = _df.copy()
  for x in df.columns:
    df[x] = df[x].cumsum() / seq
  return df
