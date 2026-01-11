baskets=[40, 25, 10]
i=0
while i<(len(baskets)-2):
    if (baskets[i] + baskets[i+1] +baskets[i+2])>60:
        baskets.pop(i+1)
    else:
        i+=1
print(baskets)