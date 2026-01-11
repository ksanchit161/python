sentence=input()
count=0
for i in range(len(sentence)):
    if i!=((len(sentence))-1) and sentence[i].islower() and sentence[i+1].isupper():
        count+=1
print(count)
  
  
  # can also use concept of AscII values as 
  # values of uppercase is higher as compared to lowercase
  # minus their value and check positive or negative