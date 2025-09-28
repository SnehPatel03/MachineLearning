# generator Func with yield
# give a even numbers with specific Limit
def even_numbers(limit):
    for i in range(2,limit  +1,2):   #(start,end,step)
        yield i #return keyword give only one value and end the loop
    
for num in even_numbers(10): #with return we cant do this one
    print(num)    