def puzzle(num):
    number=num
    sum=0
    while number>4:
      sum=sum+15
      number=number-4
    if number==1:
       sum+=1
    if number==2:
       sum+=3
    if number==3:
       sum+=7
    if number==4:
       sum+=15
    return sum
number=int(input())
print(puzzle(number))

      

