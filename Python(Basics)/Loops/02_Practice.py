# even Digit SUM 
n= int(input("Enter the Number "))
sum = 0

for num in range(1,n+1):
    if(num % 2 == 0):
       sum  = sum + num

print("Sum of even numbers are :" , sum)
