# Keep asking the User to Input if entered num is not b/w 1 to 10
while(True):
    number = int(input("enter a Number b/w 1 to 10: "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("Enter a valid number")    