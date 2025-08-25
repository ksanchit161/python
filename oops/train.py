from random import randint
class train:

    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):
        print(f"train is booked in train no : {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f" ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(2222,5555)}")

t=train(1230)
t.book("dhuri","Rajpura")
t.getStatus()
t.getFare("dhuri","Rajpura")
