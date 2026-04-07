class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def translate(self, x ,y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
     
    def __mul__(self, other):
        if type(other) == int:
            return Point(self.x * other, self.y * other)
        elif type(other) == Point:
            return ((self.x * other.x) + (self.y * other.y))  
        pass



p1 = Point(2,3)


p2 = Point(4,5)

print(p1)
print(p2)
print (f"i mieipunti sono: {p1} e {p2}")

print ( p1 + p2 ) #chiama implicitamente il metodo __add__ di p1 

print ("prodotto scalare", p1 * p2)



