inventory=[{'A':10,'B':20},{'A':'10'}]
result={}
for dict_ in inventory:
    for key in dict_.keys():
        if isinstance(dict_[key],int):
            if key in result.keys():
                temp=result[key]
                result[key]=temp+dict_[key]
            else:
                result[key]=dict_[key]
        else:
            print("Non-integer quantity skipped")
print(result)
