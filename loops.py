clr = ["blue","green","red","yellow"]

print(":::::For Loop:::::")
for x in clr:
    print(x)

print(":::::While Loop:::::")
x= 0
while(x < len(clr)):
    print(clr[x].capitalize())
    x+=1
    