flag=True
sentence=input()
for i in sentence:
    if i in "*@/#$":
        print("Invalid symbol")
        flag=False
        break
if flag:
    ans=sentence.split()
    result=[]
    for i in ans:
        result.append(i[::-1])
    print(" ".join(result))

 
    
    
