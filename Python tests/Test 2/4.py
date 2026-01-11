reels=list(map(int,input().split()))
count=0
for i in reels:
    if i%1000==0:
        count=count+(i/1000)
    else:
        count=count+(i//1000)+1
print(int(count))

