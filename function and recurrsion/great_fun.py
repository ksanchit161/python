def greatest(a,b,c):
    if(a>b and a>c):
        print("a is greatest")
    if(b>a and b>c):
        print("b is greatest")
    if(c>b and c>a):
        print("c is greatest")

first=int(input("enter number : "))
second=int(input("enter number : "))
third=int(input("enter number : "))
greatest(first,second,third)