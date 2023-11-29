# №1

# my_car.go()

# №2

# class Book:
#     def init(self, title, author, publisher):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#
#     def get_title(self):
#         return self.title
#
#     def set_title(self, new_title):
#         self.title = new_title
#
#     def get_author(self):
#         return self.author
#
#     def set_author(self, new_author):
#         self.author = new_author
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_publisher(self, new_publisher):
#         self.publisher = new_publisher
#
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}"

# №3

# class Pet:
#     def init(self, name, animal_type, age):
#         self.name = name
#         self.animal_type = animal_type
#         self.age = age
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_animal_type(self, animal_type):
#         self.animal_type = animal_type
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_animal_type(self):
#
#         return self.animal_type
#
#     def get_age(self):
#         return self.age
#
# pet_1 = Pet("Fido", "dog", 5)
# print("Pet 1’s name:", pet_1.get_name())
# print("Pet 1’s type:", pet_1.get_animal_type())
# print("Pet 1’s age:", pet_1.get_age())
#
# user_input_name = input("Enter the name of your pet: ")

# №4

# class Car:
#     def init(self, year_model, make):
#         self._year_model = year_model
#         self.make = make
#         self._speed = 0
#
#     def accelerate(self):
#         self._speed += 5
#
#     def brake(self):
#         if self._speed > 0:
#             self._speed -= 5
#         else:
#             print("Speed is already 0 or below.")
#
#     def get_speed(self):
#         return self._speed
#     car = Car(“2021”, “BMW”)
#     for _ in range(5):
#     car.accelerate()
#     current_speed = car.get_speed()
#     print(f"Current speed: {current_speed}")

# №5

# class Information:
#
#     def __init__(self, first_name, last_name, address, age, phone_number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.age = age
#         self.phone_number = phone_number
#
#     def get_first_name(self):
#         return self.first_name
#
#     def get_last_name(self):
#         return self.last_name
#
#     def get_address(self):
#         return self.address
#
#     def get_age(self):
#         return self.age
#
#     def get_phone_number(self):
#         return self.phone_number
#
#     def change_age(self, value):
#         self.age += value
#
# information_1 = Information("John", "Doe", "Some street, 123", 29, "123456789")
# information_2 = Information("Jane", "Smith", "Another street, 234", 30, "234567890")
# information_3 = Information("Bob", "Marley", "Main street, 345", 31, "345678910")
#
# print(information_1.get_first_name(), information_1.get_last_name(),
# information_1.get_address(), information_1.get_age(),
# information_1.get_phone_number())
# print(information_2.get_first_name(), information_2.get_last_name(),
# information_2.get_address(), information_2.get_age(),
# information_2.get_phone_number())
# print(information_3.get_first_name(), information_3.get_last_name(),
# information_3.get_address(), information_3.get_age(),
# information_3.get_phone_number())



