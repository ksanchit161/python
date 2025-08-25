import random
computer=random.choice([-1,0,1])
you=input("enter s for snake , w for water and g for gun ")
dict={"s": 1,
      "w": 0,
      "g": -1}
a=dict[f"{you}"]
if(a == computer):
    print("draw")
elif(a==1 and computer==0):
    print("you won")
elif(a==1 and computer==-1):
    print("computer wins")

elif(a==0 and computer==1):
    print("computer won")
elif(a==0 and computer==-1):
    print("you won")

elif(a==-1 and computer==0):
    print("computer won")
elif(a==-1 and computer==1):
    print("you won")
