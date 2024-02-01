from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*12


print(fx(5))
print("done")
print(fx(15))
print("done")
print(fx(25))
print("done")
print(fx(35))
print("done")
print(fx(45))
print("done")



print(fx(15))
print("done")
print(fx(25))
print("done")
print(fx(35))
print("done")
print(fx(45))
print("done")
print(fx(55))
print("done")