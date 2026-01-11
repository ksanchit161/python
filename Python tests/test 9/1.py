text=input()
count=0
max=0
for i in text:
    if i=="H":
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)