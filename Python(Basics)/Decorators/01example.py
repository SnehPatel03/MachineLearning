# To find exicutuion time of fucntions

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result=func(*args)
        end = time.time()
        print("Time to excute : ", end - start,"s")
        return result
    return wrapper 


@timer
def ex1(n):
    time.sleep(n)   
    
    
ex1(3)