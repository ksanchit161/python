level=int(input())
basic_pay=int(input())
total= basic_pay + 0.25 * basic_pay 
match (level):
    case 1:
        total+=1500
    case 2:
        total+=950
    case 3:
        total+=600
    case 4:
        total+=250
print(total)


