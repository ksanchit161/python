p1= "make a lot of money"
p2="click this"
p3="buy now"
message=input("enter your comments  ")
if((p1 in message) or (p2 in message ) or (p3 in message)):
    print("this is a spam")
else:
  print("this is not a spam")