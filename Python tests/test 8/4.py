text=input()
word=""
def vowel(j):
    k=ord(j)+1
    new=chr(k)
    return new
def const(j):
    k=ord(j)-1
    new=chr(k)
    return new
for i in text:
    if i.lower() in "aeiou":
        word=word+vowel(i)
    elif i.lower() in "bfjpv":
        word=word+const(i)
    else:
        word=word+i
print(word)



