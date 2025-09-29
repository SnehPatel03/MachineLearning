import time

def cachePut(func):
    cache_value ={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result     
        return result
    return wrapper

@cachePut
def long_run_func(a, b):
    time.sleep(4)
    return a+b

print(long_run_func(2,3))
print(long_run_func(2,3))







