# class Example:
#   def __new__(cls, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     return object.__new__(cls)
#
#   def __init__(self, first, second, third):
#     print(first)
#     print(second)
#     print(third)

class House:

    houses_history = []
    #__instance = None

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]

    def __del__(self):
        print(self.name, "снесён, но останется в истории.")
        return self

#     def go_to(self, new_floor):
#         if new_floor > self.number_of_floors or new_floor < 1:
#             print('Такого этажа не существует')
#         else:
#             for i in range(1, new_floor + 1):
#                 print(i)
#
#     def __len__(self):
#         return self.number_of_floors
#
# #    def __str__(self):
# #        return f'{self.name}, {self.number_of_floors}'
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors == other
#         elif isinstance(other, House):
#             return self.number_of_floors == other.number_of_floors
#         else:
#             return f'object "Other" in __eq__ is not INT or Class "House" type'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors < other
#         elif isinstance(other, House):
#             return self.number_of_floors < other.number_of_floors
#         else:
#             return f'object "Other" in __lt__ is not INT or Class "House" type'
#
#     def __le__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors <= other
#         elif isinstance(other, House):
#             return self.number_of_floors <= other.number_of_floors
#         else:
#             return f'object "Other" in __le__ is not INT or Class "House" type'
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors > other
#         elif isinstance(other, House):
#             return self.number_of_floors > other.number_of_floors
#         else:
#             return f'object "Other" in __gt__ is not INT or Class "House" type'
#
#     def __ge__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors >= other
#         elif isinstance(other, House):
#             return self.number_of_floors >= other.number_of_floors
#         else:
#             return f'object "Other" in __ge__ is not INT or Class "House" type'
#
#     def __ne__(self, other):
#         if isinstance(other, int):
#             return self.number_of_floors != other
#         elif isinstance(other, House):
#             return self.number_of_floors != other.number_of_floors
#         else:
#             return f'object "Other" in __ne__ is not INT or Class "House" type'
#
#     def __add__(self, value):
#         if isinstance(value, int):
#             self.number_of_floors += value
#             return self
#         else:
#             return f'object "Value" in __add__ is not INTor Class "House" type'
#
#     def __radd__(self, value: int):
#         if isinstance(value, int):
#             self.number_of_floors += value
#             return self
#         else:
#             return f'object "Value" in __radd__ is not INT or Class "House" type'
#
#     def __iadd__(self, other: int):
#         if isinstance(other, int):
#             self.number_of_floors += other
#             return self
#         else:
#             return f'object "Value" in __iadd__ is not INT or Class "House" type'




# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# h3 = House('ЖК Матрёшки', 20)
####
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
#print(House.__mro__)
#print(h1.__dict__)

# Удаление объектов
del h2
del h3

print(House.houses_history)
#
# print(h1 == h2) # __eq__
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
#
# print(h1 < 15.3) # __lt__


# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
#h2.go_to(10)

# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# # __str__
# print(h1)
# print(h2)
#
# # __len__
# print(len(h1))
# print(len(h2))
