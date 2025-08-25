def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
a=int(input("enter number : "))
b=sum(a)
print(b)
 