# class complex:
#     def __init__(self,i,r):
#         self.i=i
#         self.r=r

#     def __add__(self,c2):
#         return (self.i + c2.i ,self.r +c2.r)
    
#     def __multiply_(self,c2)
#         return 
    
# a=complex(1,2)
# b=complex(3,4)
# print(a+b)
class Complex:
    def __init__(self, r, i):
        self.r = r  # real part
        self.i = i  # imaginary part

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        return Complex(self.r * c2.r - self.i * c2.i, 
                       self.r * c2.i + self.i * c2.r)

    def __repr__(self):
        return f"{self.r} + {self.i}i"

a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)  # Output: 4 + 6i
print(a * b)  # Output: -5 + 10i
