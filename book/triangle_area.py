a=int(input("enter first side of triangle : "))
b=int(input("enter second side of triangle : "))
c=int(input("enter third side of triangle : "))
if((a+b)>c and (b+c)>a and (a+c)>b):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(f"the area of triangle is {area}")
else:
    print("triangle is not possible")