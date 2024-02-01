time1 = time.perf_counter()
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