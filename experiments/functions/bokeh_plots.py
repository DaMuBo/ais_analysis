"""
This module holds functions and classes for nice and interactive visualisations to be used.
"""

import os
import sys

import pandas as pd

from bokeh.plotting import figure,save, output_file, show
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from bokeh.models import ColumnDataSource
from bokeh.palettes import Category10

from sklearn.preprocessing import MinMaxScaler

def visualize_top_regions(data,columns={'lat':'lat_merc_x','lon':'lon_merc_x','size':'mmsi_nunique'}, titel="Most Busy Regions in Norway"):
    """
    This function creates a plot which visualises the top regions in norway
    """
    tile_provider = get_provider(CARTODBPOSITRON)

    MinMax = MinMaxScaler(feature_range=(1,40))
    train = data[columns['size']].to_numpy().reshape(-1,1)
    data[columns['size']] = MinMax.fit_transform(train)
    p = figure(title=titel, plot_width=800, plot_height=700,
           x_range=(1500000, 1700000), y_range=(7000000, 12000000),
           x_axis_type="mercator", y_axis_type="mercator")
    p.add_tile(tile_provider)
    p.circle(x=data[columns['lat']], y=data[columns['lon']], size=data[columns['size']], color="red", fill_alpha=1)
    return p

def  bar_chart(data, columns={'x':'dow','values':'mmsi_nunique'},titel="Most Busy Days"):
    """
    A Short function to create a bar plot which is showing the data
    """
    if columns['x'] == 'dow':
        replacer = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
        data.replace({columns['x']:replacer},inplace=True)
        print(data)
    p = figure(x_range=data[columns['x']],plot_width=800, plot_height=700,title=titel )
    p.vbar(x=data[columns['x']],top=data[columns['values']],color=Category10[7])
    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p
