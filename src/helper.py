import numpy as np
import pandas as pd
import math
import scipy.stats as stats
import matplotlib.pyplot as plt

def calculate_diff(df, column, new_col_name='diff'):
    """ Returns a df with new column representing difference between rows
    
    Inputs
    dataframe: pandas df
    column we are calculating year over year difference for: string
    new column name: string
    
    Retuns
    new dataframe: pandas df
    
    """
    diff = [np.nan]
    rows = len(df.index.values)
    
    for i in range(1, rows):
        col_value = df.loc[i, column]
        prev_col_value = df.loc[i-1, column]        
        diff.append(col_value - prev_col_value)
    
    df[new_col_name] = pd.Series(diff)
    return df


def plotter(df, x, columns):
    """ Simple plotter
    
    Inputs:
    pandas dataframe
    x axis : string
    columns: list of column names
    
    Returns:
    Figure 
    """    
    
    num_plots = len(columns)
    rows = math.ceil(num_plots/3)
    
    if num_plots>3:
        fig, axes = plt.subplots(rows, 3, figsize=(24,12))
    else:
        fig, axes = plt.subplots(rows, num_plots, figsize=(10,4))
    
    for i, ax in enumerate(axes.flatten()):
        
        if i < num_plots:         
            ax.plot(df[x], df[columns[i]], 'bo')
            ax.set_title(columns[i])
            ax.set_xlabel(x)
            ax.set_ylabel(columns[i])
        else:
            break
        
    fig.tight_layout()
        
    return None
