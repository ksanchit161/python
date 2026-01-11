str1=input()
str2=input()
if len(str1)<=1000 and len(str1)>=1 and  len(str2)<=1000 and len(str2)>=1:
    temp=(len(str1))//2
    rest=str1[temp:]
    str3=str1[0:temp]+str2 +rest
    print(str3)
