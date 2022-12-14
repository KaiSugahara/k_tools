import pandas as pd
from scipy.sparse import csr_matrix, coo_matrix

def product_sparse_matrix(a, b):

    A, B = a.copy(), b.copy()
    A.columns, B.columns = ['INDEX', 'COLUMNS', 'VALUE'], ['INDEX', 'COLUMNS', 'VALUE']
    A, B = A.sort_values(['COLUMNS', 'INDEX']), B.sort_values(['INDEX', 'COLUMNS'])
    A_ROW, A_COL, A_VAL = A['INDEX'], A['COLUMNS'], A['VALUE'].values
    B_ROW, B_COL, B_VAL = B['INDEX'], B['COLUMNS'], B['VALUE'].values
    
    # Check
    if list(A_COL) != list(B_ROW):
        Exception('ラベルが一致しません．')
    
    A_ROW_MAP = A_ROW.unique()
    A_ROW_MAP = {A_ROW_MAP[i]: i for i in range(len(A_ROW_MAP))}
    B_COL_MAP = B_COL.unique()
    B_COL_MAP = {B_COL_MAP[i]: i for i in range(len(B_COL_MAP))}
    LABEL_MAP = A_COL.unique()
    LABEL_MAP = {LABEL_MAP[i]: i for i in range(len(LABEL_MAP))}
    
    A_ROW = A_ROW.map(A_ROW_MAP).values
    B_COL = B_COL.map(B_COL_MAP).values
    A_COL, B_ROW = A_COL.map(LABEL_MAP).values, B_ROW.map(LABEL_MAP).values

    # Scipy(CSR)に変換
    A = csr_matrix((A_VAL, (A_ROW, A_COL)))
    B = csr_matrix((B_VAL, (B_ROW, B_COL)))
    
    # DataFrameに復元
    OUTPUT = (A * B).tocoo()
    OUTPUT = pd.DataFrame([OUTPUT.row, OUTPUT.col, OUTPUT.data], index=['ROW', 'COL', 'DATA']).T
    OUTPUT['ROW'] = OUTPUT['ROW'].map({val: idx for idx, val in A_ROW_MAP.items()})
    OUTPUT['COL'] = OUTPUT['COL'].map({val: idx for idx, val in B_COL_MAP.items()})

    return OUTPUT