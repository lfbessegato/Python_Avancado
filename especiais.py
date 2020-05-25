class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __repr__(self):
        return '({0}, {1}i)'.format(self.r, self.i)
    
    def __add__(self, outher):
        return Complex(self.r + outher.r, self.i + outher.i)

	
c1 = Complex(3,2)
c2 = Complex(2,4)
c3 = c1 + c2
print(c3)