class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is {self.n * self.n}")

    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n ** 0.5}")

num=int(input("enter number : "))
a=calculator(num)
a.square()
a.squareroot()
a.cube()