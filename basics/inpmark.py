marks=[]
for i in range(5):
    m=int(input("Enter marks for student {}: ".format(i+1)))
    marks.append(m)
marks.sort()
print("Marks list:", marks)
