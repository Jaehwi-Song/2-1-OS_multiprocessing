import multiprocessing
import timeit
import random

sortlist=[]

def sorting(l):
    l.acquire()
    try:
        start = timeit.default_timer()
        name = multiprocessing.current_process().name
        
        print("##### Process #" + name[8:] + " started...")

        for i in range(20):
            sortlist.append(random.randint(0,50))
        
        sortlist.sort()
        end = timeit.default_timer()

        print("[" + name[8:] + "]--> "+ str(sortlist))
        print("Execution time: " +  str(end-start) + " sec")
        print("##### Process #" + name[8:] + " ended...")
        
    finally:
        l.release()

if __name__ == '__main__' :
    lock = multiprocessing.Lock()
    for i in range(5):
        p = multiprocessing.Process(target=sorting, args=(lock,))
        p.start()
