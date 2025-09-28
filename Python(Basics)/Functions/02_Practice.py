import math    
def circleState(rad):
    area = math.pi*rad*rad
    cir = math.pi*2*rad
    return cir , area

c,a =circleState(3)


print("Circ" ,round(c,2),"area",round(a,2))