class G19:
    salary=12000
    group=19
    branch="CSE"

    def __init__(self,name,salarry):# dunder method which is automatically called when any object is formed.
        self.name=name
        self.salary=salarry
        print("I am creating an object ")

sanchit=G19("harry",12000)
print(sanchit.name,sanchit.salary)