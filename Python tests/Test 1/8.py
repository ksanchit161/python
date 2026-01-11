cost=int(input())
sell=int(input())
if cost==sell:
    print("No profit no loss")
elif(cost>sell):
    print("loss")
else:
    print("profit")