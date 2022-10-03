import csv

def add_array2csv(arr, filepath="./log.csv", is_culumns=False):
    
    mode = "w" if is_culumns else "a"
    
    with open(filepath, mode) as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(arr)