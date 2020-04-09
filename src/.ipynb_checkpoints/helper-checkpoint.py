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


def plotter(df, x, columns, title=None):
    """ Simple plotter
    
    Inputs:
    pandas dataframe
    x axis : string
    columns: list of column names
    title: string
    
    Returns:
    None
    """    
    
    num_plots = len(columns)
    rows = math.ceil(num_plots/2)
    
    if num_plots>2:
        fig, axes = plt.subplots(rows, 2, figsize=(24,12))
    else:
        fig, axes = plt.subplots(rows, num_plots, figsize=(10,4))
    
    for i, ax in enumerate(axes.flatten()):
        
        if i < num_plots:         
            ax.plot(df[x], df[columns[i]])
            ax.set_title(columns[i], fontsize=12)
            ax.set_xlabel(x)
            ax.set_ylabel(columns[i], fontsize=12)
        else:
            break
        
    fig.suptitle(title, x=0.5, y=1.05,fontsize=18)    
    fig.tight_layout()
        
    return None


def plotter_onegraph(df, x, columns):
    
    fig, ax = plt.subplots()
    for col in columns:
        ax.plot(df[x], df[col], label=col)
  
    plt.legend()
    plt.xlabel(x)
    fig.tight_layout()
    
    return None