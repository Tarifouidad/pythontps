from typing import Any


class Point:
    def __init__(self,x,y) :
       self.x=x
       self.y=y
     
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x=x
    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
class Rectangle(Point):
    def __init__(self,x,y,largeur,longueur):
        super().__init__(x,y)
        self.largeur=largeur
        self.longueur=longueur
    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, Longueur={self.longueur}, Largeur={self.largeur})"
class Parallelepipede(Rectangle):
    def __init__(self, x, y, longueur, largeur, hauteur):
        super().__init__(x, y, longueur, largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def aire(self):
        base_area = super().aire()
        lateral_area = 2 * (self.longueur * self.hauteur + self.largeur * self.hauteur)
        return 2 * base_area + lateral_area

    def volume(self):
        return super().aire() * self.hauteur

    def __str__(self):
        return f"Parallelepipede({self.x}, {self.y}, Longueur={self.longueur}, Largeur={self.largeur}, Hauteur={self.hauteur})"

# Test des classes
point = Point(1, 2)
print(point)

rectangle = Rectangle(3, 4, 5, 6)
print(rectangle)
print(f"Aire du rectangle : {rectangle.aire()}")

parallelepiped = Parallelepipede(7, 8, 9, 10, 11)
print(parallelepiped)
print(f"Aire du parallelepiped : {parallelepiped.aire()}")
print(f"Volume du parallelepiped : {parallelepiped.volume()}")
