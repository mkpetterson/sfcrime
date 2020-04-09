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


def plotter_onegraph(df, x, columns, columnsax2=None):
    """ Plots several columns from dataframe all on one plot. 
    If desired, can plot additional data on secondary axis. 
    
    Inputs
    
    
    Returns
    
    
    """
    
    fig, ax = plt.subplots()
    for col in columns:
        ax.plot(df[x], df[col], label=col)
        ax.set_yscale('log')
        ax.set_xlabel(x)
        ax.legend(loc='upper left', bbox_to_anchor=(0.00, 0.84))

#    plt.legend()    
    ax.set_ylabel('Counts')

    if columnsax2:
        ax2 = ax.twinx()
        
        color='green'
        ax2.plot(df[x], df[columnsax2], 'g--')
        ax2.set_ylabel('Fraction')
        ax2.tick_params(axis='y', color=color)
        ax2.legend(loc='upper left', bbox_to_anchor=(0.00, 0.84))
        ax2.set_ylim(0.1, 0.2)
        
    plt.legend()
    plt.xlabel(x)
    fig.tight_layout()
    
    return None