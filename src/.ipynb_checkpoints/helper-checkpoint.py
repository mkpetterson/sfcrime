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
    
    # Make fig depending on # of subplots
    if num_plots>2:
        fig, axes = plt.subplots(rows, 2, figsize=(24,12))
    else:
        fig, axes = plt.subplots(rows, num_plots, figsize=(10,4))
    
    # Plot
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
#        ax.set_yscale('log')
        ax.set_xlabel('Year')
        ax.legend(loc='upper left', bbox_to_anchor=(0.00, 0.84))
        
#    ax.set_ylabel('Counts')

    if columnsax2:
        ax2 = ax.twinx()
        
        color='green'
        ax2.plot(df[x], df[columnsax2], 'g--')
        ax2.set_ylabel('Fraction')
        ax2.tick_params(axis='y', color=color)
        ax2.legend(loc='upper left', bbox_to_anchor=(0.00, 0.84))
        ax2.set_ylim(0.05, 0.25)
        
    plt.legend()
    plt.xlabel(x)
    fig.tight_layout()
    
    return None


def violence(crime):
    """ Returns data frame of violent crime and non-violent crime """
    
    violent = crime[((crime['Category'] == 'ASSAULT') | 
                 (crime['Category'] == 'ROBBERY') | 
                 (crime['Category'] == 'KIDNAPPING') | 
                 (crime['Category'] == 'ARSON') | 
                 (crime['Category'] == 'SEX OFFENCES, FORCIBLE'))]

    nonviolent = crime[((crime['Category'] != 'ASSAULT') & 
                 (crime['Category'] != 'ROBBERY') & 
                 (crime['Category'] != 'KIDNAPPING') & 
                 (crime['Category'] != 'ARSON') & 
                 (crime['Category'] != 'SEX OFFENCES, FORCIBLE'))]

    return violent, nonviolent


def resolution(df):
    """ Returns fraction of crimes in dataframe that were resolved """
    
    n_crimes = len(df.index)
    resolved = df[df['Resolution'] != 'NONE']
    frac_resolved = len(resolved.index)/n_crimes

    return frac_resolved


def vresolution(df):
    """ Returns fraction of violent vs non-violent crime
    
    Inputs
    pandas dataframe
    
    Returns
    fraction of violence and non-violence, both floats
    """
    
    v, n = violence(df)    
    vfrac = round(resolution(v), 5)
    nvfrac = round(resolution(n), 5)
    
    return vfrac, nvfrac

    