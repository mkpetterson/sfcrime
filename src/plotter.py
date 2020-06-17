# Data Manipulation
import pandas as pd
import numpy as np


#Geographic Data Visualization
import geopandas as gpd
from shapely.geometry import Point, Polygon, shape
import matplotlib.pyplot as plt
import shapefile as shp 


def binning(df):
    """ Create bins for crimes based on GPS data
    
    Inputs
    pandas dataframe 
    
    Returns
    2d array with crime counts in each bin
    lists with latitute, longitude, and count (flattened array)    
    
    """
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
    """ Creates scatter plot of crime data
    
    Inputs
    pandas dataframe
    year: string
       
    Returns
    None
    """

    # Bin the data and get crime counts for GPS coordinates
    array, lat, long, mag = binning(df)
    
    # Create dataframe and replace 0 counts with nan (better for plotting)
    crime_map = pd.DataFrame({'Lat': pd.Series(lat),
                              'Long': pd.Series(long),
                              'Count': pd.Series(mag)})
    crime_map.replace(to_replace=0.0, value=np.nan, inplace=True)
    
    # Plot
    fig, ax = plt.subplots()
    
    # Requires the pyshp package
    file = "AnalysisNeighborhoods/geo_export_56962ed9-324d-4175-9698-21ee69259dea.shp"
    sf = shp.Reader(file)

    # Plot the data and the shapefile
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x,y, color='gray', linewidth=0.7)
    
    
    im = ax.scatter(crime_map['Long'], crime_map['Lat'], c=crime_map['Count'], 
                    cmap='bwr',vmin=0, vmax=300, alpha=.4, s=5)
    ax.set_xlim(-122.55, -122.34)
    ax.set_ylim(37.7, 37.83)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(f"Crime Reports in San Francisco in {year}")
    fig.colorbar(im, ax=ax)
    
    plt.savefig(year+'.png', dpi=350)
    
    return None

