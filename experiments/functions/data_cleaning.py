"""
some functions and methods for data cleaning of defined data
"""
import pickle
import pandas as pd
import numpy as np

class SimpleOutlierMask():
    """
    simple class for learning on training data a structure of the column and what are the outliers to be deleted
    """
    def __init__(self, column = pd.Series([0,0])):
        """
        initilization of the class
        """
        self.mean = column.mean()
        self.sstd = column.std() * 6 + self.mean

    def fit(self, column):
        """
        learning the structure of the given column
        """
        self.mean = column.mean()
        self.sstd = column.std() * 6 + self.mean

    def transform(self, column):
        """
        returning the corrected column where the outliers are deleted by the learned mean.
        """
        result = column.apply(lambda x: self.mean if x > self.sstd else x )
        return result

    def save(self,location):
        """
        saving the structure of the column to a file
        """
        output = {
            'mean': self.mean,
            'sstd': self.sstd
        }
        with open(location, 'wb') as file:
            pickle.dump(output, file)

    def load(self,location):
        """
        loading the strucutre of the column from a file in to the object
        """
        with open(location, 'rb') as file:
            data = pickle.load(file)
        self.mean = data['mean']
        self.sstd = data['sstd']

def x_coord(x,y):
    """
    This function is transforming the correct coordinates for visualising the data points on a 2D Plot
    """
    lat = float(x)
    lon = float(y)

    r_major = 6378137.000
    x = r_major * np.radians(lon)
    scale = x/lon
    y = 180.0/np.pi * np.log(np.tan(np.pi/4.0 +
        lat * (np.pi/180.0)/2.0)) * scale
    return (x, y)

def create_mercator(df,targetcolumns= {'x':'lat','y':'lon'}):
    """
    this function performs the mercator transformation on the target_columns
    """
    x_t = targetcolumns['x'] + '_merc'
    y_t = targetcolumns['y'] + '_merc'
    df[[x_t,y_t]] = df[[targetcolumns['x'],targetcolumns['y']]].apply(lambda x:x_coord(x[targetcolumns['x']],x[targetcolumns['y']]),axis = 1, result_type='expand')
    return df
