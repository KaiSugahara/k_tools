from tqdm import tqdm
from multiprocessing import Pool

def map_with_mp_and_tqdm(func, data, processes=8):

    pool = Pool(processes=processes)

    with tqdm(total=len(data)) as t:

        for _ in pool.imap_unordered(func, data):
            t.update(1)