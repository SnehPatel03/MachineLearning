x= 100

def parent():
    x = 50
    def inner():
        print("x is", x)
    return inner

result = parent()
result()
    
# parent passes not noly the function but also the references of the Inner fucntions data members.

#  So the closure of the functions are transfer in form of BAG that contains not only inner fucntion but also the references of data members.