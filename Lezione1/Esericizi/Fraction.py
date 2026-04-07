class Fraction:
   
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
        self.__simplify__()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other):
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)
    
    def __simplify__(self):
        a = self.numerator
        b = self.denominator

        s = +1 if (a * b) > 0 else -1
        a = a if a > 0 else -a
        b = b if b > 0 else -b

        for MCD in range(a,0,-1):
            if (a % MCD == 0) and (b % MCD == 0):
                break
        
        self.numerator = s * (a // MCD)
        self.denominator = b // MCD

    def __eq__(self, other):
        return (self.numerator == other.self.numerator) and (self.denominator == other.denominator)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    
    

    