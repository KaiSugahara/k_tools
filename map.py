from tqdm import tqdm
from multiprocessing import Pool

def map(func, data, processes=8):

    results = []
    pool = Pool(processes=processes)

    with tqdm(total=len(data)) as t:
        for result in pool.imap(func, data):
            results.append(result)
            t.update(1)

    return results