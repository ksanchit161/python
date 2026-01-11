late=int(input())
if late>=1 and late<=5:
    print(int(0.5*late))
elif  late>=6 and late<=10:
    print(late)
elif  late>=11 and late<=30:
    print(late*5)
else:
    print("Your Membership would be Cancelled")