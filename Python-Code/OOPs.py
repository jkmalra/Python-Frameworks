
# class car():
#     def __init__ (self, brand: str, name: str, model: int):
#         self.brand = brand
#         self.name = name
#         self.model = model
#
# mycar = car('maruti', 'Zen',1992)
#
# print(mycar.brand, mycar.name, mycar.model)
# ----------------

class Stationary:
    def __init__(self, Brand, Name, Color):
        if not isinstance(Brand, str):
            raise TypeError('Brand must be a string')
        if not isinstance(Name, str):
            raise TypeError('Name must be a string')
        if not isinstance(Color, str):
            raise TypeError('Color must be a Black or Blue')
        self.Brand = Brand
        self.Name = Name
        self.Color = Color

mypen = Stationary('Renolds', 'Trimax', 123)
print(mypen.Brand, mypen.Name, mypen.Color)
