number=int(input())
sum=0
if number<0:
    number=number*(-1)
while number>0:
    last=number%10
    sum=sum+last
    number=number//10
print(sum)