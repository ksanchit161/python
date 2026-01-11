numbers=[0, 200, 400]
result=[]
for i in numbers:
    if i%1000==0:
        result.append(i//1000)
    else:
        result.append((i//1000)+1)
print(sum(result))