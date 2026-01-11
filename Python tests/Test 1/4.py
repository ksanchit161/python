Flag=True
try:
    age=int(input())
    credit=int(input())
except:
    print("Invalid Input")
    Flag=False
if(Flag):
    if age<=0 or credit<=0:
        print("Invalid Input")
    elif(age<21 or credit<=700):
        print("Loan rejected")
    elif(age>=21 or credit>700):
        print("Loan Aprroved")
