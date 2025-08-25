class employee:
    company="ITC"
    salary=1000
    def show(self):
        print(f"the name of the company is {self.company}and the salary is {self.salary}")

class coder:
    language="python"
    def printLanguages(self):
        print(f"out of all languages here is your language : {self.language}")

class programmer(employee,coder):
   company="ITC Infotech"
   def showlanguage(self):
       print(f"the name of the company is {self.company} and he is good with {self.language} language")

a=employee()
b=programmer()

b.show()
b.printLanguages()
b.showlanguage()


print(a.company,b.company)

    
