# Find First Duplicate and print it and breack the loop
items = ["apple", "banana" , "mango" ,"apple" ,"cherry"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate Found",item)
        break
    else:
         unique_item.add(item)
        