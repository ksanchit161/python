def repair_logs(entries):
    result=[]
    valid=[]
    for i in entries:
        word=""
        for j in i:
            if j.isalpha():
                word+=j.lower()
        valid.append(word)
    for i in valid:
        if len(i)>=1 and len(i)<4:
            result.append(i)
        if len(i)>=1 and len(i)>=4:
            result.append(i[::-1])
    return(result)

words=["p3alantir", "va!lin0or", "num3enor"]
print(repair_logs(words))


        