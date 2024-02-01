import threading
import time

from concurrent.futures import ThreadPoolExecutor
def fun(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

# time1 = time.perf_counter()
# #using normal code
# # fun(4)
# # fun(3)
# # fun(2)

# #using thread 
# # t1 = threading.Thread(target=fun,args=[4])
# # t2 = threading.Thread(target=fun,args=[3])
# # t3 = threading.Thread(target=fun,args=[2])
# # t1.start()
# # t2.start()
# # t3.start()
# # t1.join()
# # t2.join()
# # t3.join()
# time2 = time.perf_counter()
# print(time2-time1)


def poolingdemo():
    with ThreadPoolExecutor() as executor:
        l=[3,4,5]
        results = executor.map(fun,l)
        for result in results:
            print(result)

poolingdemo()
