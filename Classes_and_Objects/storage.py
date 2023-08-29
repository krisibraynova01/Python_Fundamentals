# class Storage:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#     def get_products(self):
#         return self.storage
#
# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())

class Weapon:

    def __init__(self, bullets=0):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon()
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)

