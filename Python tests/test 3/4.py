# N,M=map(int,input().split())
# ans=[]
# for i in range(N):
#     number=list(map(int,input().split()))
#     ans.append(number)
# result=[]
# for i in range(N):
#     for j in range(M):
#         if i==0 or j==0 or i==N-1 or j==M-1:
#             result.append(ans[i][j])
# print(sum(result))


N,M=map(int,input().split())
ans=[]
for i in range(N):
    number=list(map(int,input().split()))
    ans.append(number)
result=[]
total=0
total=total+(sum(ans[0]))
total=total+(sum(ans[N-1]))
for i in range(1,N-1):
    total=total+ans[i][0]
    total=total+ans[i][M-1]
print(total)