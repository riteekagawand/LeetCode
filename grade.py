marks = int(input("Enter your Percentage: "))

if(marks >= 40):
    if(marks >= 85):
        print("First division")
    if(marks >= 60 ):
        if(marks < 85):
            print("Second division")
    if(marks >= 40):
        if(marks < 60):
         print("Third division")
else:
    print("Fail")