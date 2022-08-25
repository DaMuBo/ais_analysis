"""
some functions for data loads of defined data
"""
import pandas as pd

def get_columns(engine,tablename='tbl_positionnew',ignore_columns = ['type','altitude']):
    """
    Get the columns from the database schema which are not to be ignored while loading data
    Inputs:
    -----------------
    engine: the database engine
        The database connection from where to load the data
    tablename: String
        The name of the table to get the column names of
    ignore_columns: List
        A List of column names which shouldn't be included in the final list
    Outputs:
    ---------------
    Return: List
        A List of column names which are included in the table
    """
    sqlstring = f"""
    SELECT DISTINCT column_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_schema = 'public' AND table_name = '{tablename}' AND column_name NOT IN ('{"','".join(ignore_columns)}')
    """
    df = pd.read_sql(sqlstring,con=engine)
    return df['column_name'].tolist()

def load_data(engine,tablename,columns, dates = []):
    """
    Loading the data in a dataframe from the database
    Inputs:
    -----------------
    engine: the database engine
        The database connection from where to load the data
    tablename: String
        The name of the table to get the data from
    columns: List
        A List of column names which should be included in the output
    dates: List
        A List with 2 values to select data between these two dates
    Outputs:
    -----------------
    return: DataFrame
        A Dataframe with the extracted data

    """
    sqlstring = f"""
    SELECT DISTINCT {','.join(columns)}
    FROM {tablename}

    """
    if len(dates) > 0:
        sqlstring = sqlstring + f" WHERE CAST(msgtime AS DATE) BETWEEN CAST('{dates[0]}' AS DATE) AND CAST('{dates[1]}' AS DATE)"
    df = pd.read_sql(sqlstring,con=engine)
    return df
