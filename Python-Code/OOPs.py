
# class car():
#     def __init__ (self, brand: str, name: str, model: int):
#         self.brand = brand
#         self.name = name
#         self.model = model
#
#     def full_name(self):
#         return f"Full Name of Car: {self.brand} {self.name} {self.model}"
#
#
# mycar = car('maruti', 'Zen',1992)
#
# print(mycar.brand, mycar.name, mycar.model)
# print(mycar.full_name())
# # ----------------

# class Stationary:
#     def __init__(self, Brand, Name, Color):
#         if not isinstance(Brand, str):
#             raise TypeError('Brand must be a string')
#         if not isinstance(Name, str):
#             raise TypeError('Name must be a string')
#         if not isinstance(Color, str):
#             raise TypeError('Color must be a Black or Blue')
#         self.Brand = Brand
#         self.Name = Name
#         self.Color = Color
#
# mypen = Stationary('Renolds', 'Trimax', 123)
# print(mypen.Brand, mypen.Name, mypen.Color)
# ------------------------

# INHERITANCE
class Car:
    def __init__(self, brand, model):
        self.Brand = brand
        self.Model = model

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.BatterSize = batterysize

Tesla = ElectricCar('tesla', 2025, '500 Volt')

print(Tesla.Model, Tesla.Brand, Tesla.BatterSize)
