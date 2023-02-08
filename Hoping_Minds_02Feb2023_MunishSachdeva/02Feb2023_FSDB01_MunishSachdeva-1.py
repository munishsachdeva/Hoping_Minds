class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def semi_perimeter(self):
        s = float((self.a + self.b + self.c) / 2)
        return s
    
    def area_1(self):
        s = self.semi_perimeter()
        area = float((s * (s - self.a) * (s - self.b) * (s - self.c))**0.5)
        return area
    
    def area_height(self):
        height = ((self.c**2) - ((self.b**2) / (4)))**0.5
        return height
    
    def area_2(self):
        s = self.area_height()
        area = (self.b * s) * 0.5
        return area

a = int(input())
b = int(input())
c = int(input())

triangle = Triangle(a, b, c)

print(f'Area 1: {triangle.area_1()}')
print(f'Height: {triangle.area_height()}')
print(f'Area 2: {triangle.area_2()}')
