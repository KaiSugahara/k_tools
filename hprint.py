import pandas as pd
import polars as pl
from IPython.display import display
from pprint import pprint

def hprint(data, rows=5):
    
    # Pandas DataFrame
    if type(data) in [pd.core.frame.DataFrame, pd.core.series.Series]:
        
        pd.set_option("display.max_rows", rows)
        display(data)
        pd.reset_option("display.max_rows")

    # Polars DataFrame
    elif type(data) in [pl.dataframe.frame.DataFrame, pl.series.series.Series]:

        pl.Config.set_tbl_rows(rows)
        display(data)
        
    # Dict
    elif type(data) is dict:
        
        pprint( dict(zip(list(data.keys())[:rows], list(data.values())[:rows]))  )
        print("length:", len(data))
        
    # List
    elif type(data) is list:
        
        pprint( data[:rows] )
        print("length:", len(data))

    # Otherwise
    else:
        
        print( data )