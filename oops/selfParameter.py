from random import randint
class train:

    def __init__(slf,trainNo): #at place of slf we can use any string
        slf.trainNo=trainNo
        
    def book(slf,fro,to):
        print(f"train is booked in train no : {slf.trainNo} from {fro} to {to}")
    
    def getStatus(slf):
        print(f"Train no : {slf.trainNo} is running on time")

    def getFare(slf,fro,to):
        print(f" ticket fare in train no : {slf.trainNo} from {fro} to {to} is {randint(2222,5555)}")

t=train(1230)
t.book("dhuri","Rajpura")
t.getStatus()
t.getFare("dhuri","Rajpura")
