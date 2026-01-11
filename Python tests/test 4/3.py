subject1=int(input())
subject2=int(input())
subject3=int(input())
subject4=int(input())
subject5=int(input())
total=subject1+subject2+subject3+subject4+subject5
average=total//5
if average>=75:
    grade="A"
elif average>=60:
    grade="B"
elif average>=55:
    grade="C"
elif average>=50:
    grade="D"
elif average<50:
    grade="E"
print(total)
print(average)
print(grade)