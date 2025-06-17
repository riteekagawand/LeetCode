list=["red","blue","green"]
color =str(input("Enter a Color: "))
for x in list:
    if(color==x or color==x.capitalize() or color==x.upper()):
        print(color,"is Present in the List at index")
    else:
        continue
    
        