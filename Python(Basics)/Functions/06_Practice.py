#Factorial
def fact(n):
    if(n < 2):
        return 1
    else:
        return fact(n-1)*n
    
result = fact(5)
print(result)