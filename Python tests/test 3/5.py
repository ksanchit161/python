# row=int(input())
# column=int(input())
# matrix=[]
# for i in range(row):
#     number=list(map(int,input().split()))
#     number.sort(reverse=True)
#     matrix.append(number)
# result=[]
# for i in range(row):
#     result.append(matrix[i][0])
# print(result)


row=int(input())
column=int(input())
matrix=[]
for i in range(row):
    number=list(map(int,input().split()))
    matrix.append(number)
result=[]
for i in range(row):
    result.append(max(matrix[i]))
print(result)