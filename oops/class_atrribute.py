class demo:
    a=4
o=demo()
print(o.a)  # prints the class attribute because instance attribute is not present
o.a=12      # instance attribute is set
print(o.a) # prints the instance attribute because instance attribrute is present
print(demo.a) #prints the class attribute