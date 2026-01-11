weight=[30, 20, 15, 10]
i=0
while i<=len(weight)-3:
    if weight[i]+weight[i+1]+weight[i+2]>60:
        weight.pop(i+1)
    else:
        i+=1
print(weight)
