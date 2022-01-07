from itertools import repeat
from multiprocessing import Pool
from multiprocessing import Process, current_process
import time

def f(numbers):
    result= [4 * num for num in numbers]
    name=current_process().name
    print(name[5:], " output:", result)
    time.sleep(0.1)
    return result

if __name__=='__main__':
    WORKERS = 10
    p = Pool(processes=WORKERS)
    numbers = [0, 1, 2, 3, 4, 5]
    print("Input list:" ,numbers)
    print("Output in random order:")
    result = p.map(f, repeat(numbers, WORKERS))