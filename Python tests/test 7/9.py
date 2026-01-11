def detective_average_marks(records):
    sum=0
    count=0
    if not isinstance(records,dict):
        return ("Invalid Data")
    for i in records.keys():
        if isinstance(i,str) and isinstance(records[i],int):
            sum+=records[i]
            count+=1
    try:
        average=sum/count
    except:
        return ("No Valid Records")
    sentence=f"Average:{average:.2f}" # dont use round function
    
    return sentence
dictionary={"Sirius": "A+", "Remus": 85, "Peter": 75}
print(detective_average_marks(dictionary))
