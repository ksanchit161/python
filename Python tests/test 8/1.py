prices=[100, 200, 300, 400, 500]
result=[]
for i in prices:
    if i<100:
        update=round(i+(0.1*i))
        result.append(update)
    elif i>500:
        update=round(i-(0.05*i))
        result.append(update)
    else:
        result.append(i)

print(result)