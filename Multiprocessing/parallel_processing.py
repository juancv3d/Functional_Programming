import collections
import multiprocessing
import time
from pprint import pprint
import os
import concurrent.futures


Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel'
])


def transform(x):
    print(f'Process {os.getpid()} working record {x.name}')
    time.sleep(1)
    result = {'name': x.name, 'age': 2017 - x.born}
    print(f'Process {os.getpid()} done processing {x.name}')
    return result


if __name__ == '__main__':
    scientists = (
        Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
        Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
        Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
        Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
        Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
        Scientist(name='Vera Rubin', field='astronomy',
                  born=1928, nobel=False),
        Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
    )
    pprint(scientists)
    print()

    #! This is how normally you would do it
    t_start = time.time()
    print('Before parallel processing...\n')
    result = tuple(transform(x) for x in scientists)
    t_end = time.time()

    pprint(result)
    print(
        f'\nTime taken by normal processing: {t_end - t_start:.2f} seconds\n')

    #! With multiprocessing, we can create a pool of workers and have them work in parallel.
    #! optimazing the code to use multiple cores and using less time.
    print('Starting parallel processing...\n')
    start = time.time()
    with multiprocessing.Pool(processes=len(scientists)) as pool:
        result = pool.map(transform, scientists)
    end = time.time()

    pprint(result)
    print(
        f'\nTime to complete with multiprocessing: {end - start:.2f} seconds\n')

    #! With concurrent.futures we can use threads and processes to work in parallel.
    #! This is a more advanced technique and is less optimized than multiprocessing.
    #! But it is more flexible and easier to use.
    print('Starting concurrent processing...\n')
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(scientists)) as executor:
        result = executor.map(transform, scientists)
    end = time.time()

    pprint(tuple(result))
    print(
        f'\nTime to complete with concurrent processing: {end - start:.2f} seconds\n')

    #! Other way to work in parallel. is by using threads
    #! with concurrent.futures.ThreadPoolExecutor we can use threads instead of processes.
    print('Starting threading pool...\n')
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(scientists)) as executor:
        result = executor.map(transform, scientists)
    end = time.time()
    pprint(tuple(result))
    print(
        f'\nTime to complete with concurrent threading: {end - start:.2f} seconds\n')

    #! The ThreadPoolExecutor is more flexible than ProcessPoolExecutor.
    #! but it is less efficient than ProcessPoolExecutor.
