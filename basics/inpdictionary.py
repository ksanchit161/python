a={}
n = int(input("Enter the number of entries: "))
for _ in range(n):
    key = input("Enter name: ")
    value = input("Enter language: ")
    a[key] = value
print(a)
