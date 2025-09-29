import time 
def debug(func):
    def wrapper(*args,**kwargs):
        argsValue = " ,".join(str(arg) for arg in args)
        kwargsValue = " ,".join(f"{k} ={v}" for k,v in kwargs.items())
        print(f"{func.__name__} Calling : args - {argsValue} , keywordArgs - {kwargsValue}")
        return func(*args,**kwargs)
    return wrapper 
    
@debug    
def greet(name, greeting="Hello"):
    print(f"{greeting},{name}")
   
greet("Sneh",greeting="Helloji")    