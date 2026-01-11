def decode(code):
    result=""
    for i in code:
        word=""
        for j in i:
            if j.isalpha():
                word+=j
        if len(word)>1:
            if len(word)%2==0:
                result+=word[-1]
            else:
                result+=word[0]
    return result.upper()

code=["zen", "yogi", "mono", "plane", "rt", "$$"]
print(decode(code))            
