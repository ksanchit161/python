def titan(energy,hammer):
    count=len(energy)
    strike=0
    import math
    for i in energy:
        temp=i/hammer
        temp1=math.ceil(temp)
        strike=strike+temp1
        if i<=0:
            count-=1
    print(count)
    print(strike)

energy=[0, 10, 20]
hammer=10
titan(energy,hammer)