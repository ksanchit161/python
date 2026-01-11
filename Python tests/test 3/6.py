row=int(input())
column=int(input())
matrix=[]
for i in range(row):
    number=list(map(int,input().split()))
    matrix.append(number)
result=[]
for j in range(column):
    max=matrix[0][j]
    for i in range(row):
        if matrix[i][j] > max:
            max=matrix[i][j]
    result.append(max)
print(result)