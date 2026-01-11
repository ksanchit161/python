delivery=[45, 60, 10, 5, -1]
ontime=0
delay=0
for i in delivery:
    if (i)==-1:
        break
    if (i)<=40:
        ontime+=1
    else:
        delay+=1
result=(ontime,delay)
print(result)
