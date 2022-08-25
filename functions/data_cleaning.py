"""
some functions and methods for data cleaning of defined data
"""
import pickle

class simple_outlier_mask():
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
        pickle.dump(output, open(location, 'wb'))

    def load(self,location):
        """
        loading the strucutre of the column from a file in to the object
        """
        data = pickle.load(open(location, 'rb'))
        self.mean = data['mean']
        self.sstd = data['sstd']
