number=int(input())
max=0
while number>0:
    last=number%10
    if last>max:
        max=last
    number=number//10
print(max)