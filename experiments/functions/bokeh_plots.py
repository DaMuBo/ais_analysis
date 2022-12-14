"""
This module holds functions and classes for nice and interactive visualisations to be used.
"""
from bokeh.plotting import figure
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
from bokeh.palettes import Category10

from sklearn.preprocessing import MinMaxScaler

def visualize_top_regions(data, columns={'lat':'lat_merc_x','lon':'lon_merc_x','size':'mmsi_nunique'}, titel="Most Busy Regions in Norway"):
    """
    This function creates a plot which visualises the top regions in norway
    """
    tile_provider = get_provider(CARTODBPOSITRON)

    min_max = MinMaxScaler(feature_range=(1,40))
    train = data[columns['size']].to_numpy().reshape(-1,1)
    data[columns['size']] = min_max.fit_transform(train)
    plotter = figure(title=titel, plot_width=800, plot_height=700,
           x_range=(1500000, 1700000), y_range=(7000000, 12000000),
           x_axis_type="mercator", y_axis_type="mercator")
    plotter.add_tile(tile_provider)
    plotter.circle(x=data[columns['lat']], y=data[columns['lon']], size=data[columns['size']], color="red", fill_alpha=1)
    return plotter

def  bar_chart(data, columns={'x':'dow','values':'mmsi_nunique'},titel="Most Busy Days"):
    """
    A Short function to create a bar plot which is showing the data
    """
    if columns['x'] == 'dow':
        replacer = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
        data.replace({columns['x']:replacer},inplace=True)
        print(data)
    plotter = figure(x_range=data[columns['x']],plot_width=800, plot_height=700,title=titel )
    plotter.vbar(x=data[columns['x']],top=data[columns['values']],color=Category10[7])
    plotter.xgrid.grid_line_color = None
    plotter.y_range.start = 0

    return plotter
