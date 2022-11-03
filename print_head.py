import pandas as pd
from IPython.display import display
from pprint import pprint

def print_head(data, rows=5):
    
    # DataFrame
    if type(data) in [pd.core.frame.DataFrame, pd.core.series.Series]:
        
        pd.set_option("display.max_rows", rows)
        display(data)
        pd.reset_option("display.max_rows")
        
    # Dict
    if type(data) is dict:
        
        pprint( dict(zip(list(data.keys())[:rows], list(data.values())[:rows]))  )
        print("length:", len(data))
        
    # List
    if type(data) is list:
        
        pprint( data[:rows] )
        print("length:", len(data))