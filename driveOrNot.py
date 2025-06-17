name = str(input("Enter your Name: "))
age = int(input("Enter your age"))

if(age >= 18):
    if(age >= 50):
        print(name,"You are not allowed to drive")
    else:
     print(name,"You can Drive")
else:
    print(name,"You are a minor")