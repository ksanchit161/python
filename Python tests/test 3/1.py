salary=int(input())
gender=input()
if gender=="M":
    print((salary)+(0.10*salary))
   
elif(gender=="F"):
    print((salary)+(0.15*salary))
else:
    print("Wrong Input")
