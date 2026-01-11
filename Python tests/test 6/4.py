def robot(scores):
    result={}
    for i in scores.keys():
        total=sum(scores[i])
        average=round(total/len(scores[i]),2)
        if average>=75:
            Grade="A"
        elif average>=50 and average<75:
            Grade="B"
        elif average<50:
            Grade="C"
        result[i]=[total,average,Grade]
    return result
scores={'Ravi': [40, 45, 35], 'Tina': [60, 65, 70]}
print(robot(scores))
        
        
