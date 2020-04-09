# Data Manipulation
import pandas as pd
# Calculations and Numerical Operations
import numpy as np
# Data Visualization
import plotly
from plotly import tools
import plotly.offline as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from plotly.tools import make_subplots

#Geographic Data Visualization
import geopandas as gpd
from shapely.geometry import Point, Polygon, shape
import matplotlib.pyplot as plt


def binning(df):
    xvals = list(df['X'])
    yvals = list(df['Y'])
    
    # Make bins
    bins = 100
    x_bins = np.linspace(-122.55, -122.36, bins)
    y_bins = np.linspace(37.82, 37.7, bins)
    array = np.zeros((bins, bins))
    
    # Loop through GPS coordinates and figure out what pixel to add count to
    for x, y in zip(xvals, yvals):
        x_pix = np.where(np.abs(x_bins-x) == min(np.abs(x_bins-x)))[0][0]
        y_pix = np.where(np.abs(y_bins-y) == min(np.abs(y_bins-y)))[0][0]          
        
        array[y_pix, x_pix] += 1  
        
    lat = []
    long = []
    mag = []
    for i,row in enumerate(array):
        for j, col in enumerate(row):
            lat.append(y_bins[i])
            long.append(x_bins[j])
            mag.append(col)           
    
    return array, lat, long, mag


def plot_scatter(df, year):

    # Bin the data and get crime counts for GPS coordinates
    array, lat, long, mag = binning(df)
    
    # Create dataframe and replace 0 counts with nan (better for plotting)
    crime_map = pd.DataFrame({'Lat': pd.Series(lat),
                              'Long': pd.Series(long),
                              'Count': pd.Series(mag)})
    crime_map.replace(to_replace=0.0, value=np.nan, inplace=True)
    
    # Plot
    fig, ax = plt.subplots()
    im = ax.scatter(crime_map['Long'], crime_map['Lat'], c=crime_map['Count'], 
                    vmin=50, vmax=300, alpha=.8, s=5)
    ax.set_xlim(-122.55, -122.34)
    ax.set_ylim(37.7, 37.83)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f"Crime Reports in San Francisco in {year}")
    fig.colorbar(im, ax=ax)
    
    plt.savefig(year+'.png', dpi=350)
    
    return None


def plot_secondary(df, cols_ax1, cols_ax2):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
    
    return None
