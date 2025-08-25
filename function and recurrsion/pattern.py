def stars(n):
 if(n==1):
    print("*")
    return
 else:
   print("*" * n)
   return stars(n-1)

a=int(input("enter nuber :  "))
stars(a)