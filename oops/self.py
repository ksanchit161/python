
class G19:
    salary=12000
    group=19
    branch="CSE"
    def salarry(self):
        print(f"salary is {self.salary}")
    @staticmethod
    def greet():
     print("hello user")    

sanchit=G19()
print(sanchit.salary,sanchit.branch,sanchit.group)
sanchit.salarry()
sanchit.greet()
    