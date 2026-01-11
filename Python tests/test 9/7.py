credits=[('A','S',5),('B','S',5)]
result={}
for i in credits:
    name=i[0]
    marks=i[2]
    if not isinstance(marks,int):
        print("Skipping")
        continue
    if  name in result.keys():
        result[name]=marks + result[name]
    else:
        result[name]=marks
print(result)


