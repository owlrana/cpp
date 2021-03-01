class fraction:
    
    def __init__ (self, top, bottom):

        self.num = top
        self.den = bottom

    def __repr__ (self):

        return str(self.num) + '/' + str(self.den)

f1 = fraction(4,5)

print(f1.num)
print(f1.den)
print(f1)