class twoDvector:
    def  __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"{self.i}i + {self.j}j")

   

class threeDvector(twoDvector):
    def __init__(self,i,j,k):
     super().__init__(i,j)
     self.k=k
    
    def show(self):
        print(f"{self.i}i + {self.j} + {self.k}k")

a=twoDvector(1,4)
a.show()
b=threeDvector(2,4,5)
b.show()
