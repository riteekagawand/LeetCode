a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

if(a>b and a>c):
    print("A is the greatest",a)
elif(b>a and b>c):
    print("B is the greatest",b)
else:
    print("C is the greatest",c)